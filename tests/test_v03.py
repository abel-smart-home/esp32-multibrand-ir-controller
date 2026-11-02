"""Pruebas estáticas V0.3: verifican contrato, no reemplazan esphome compile ni la placa real."""
from pathlib import Path
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / "firmware" / "ir_multimarca_v03.yaml"

class SecretLoader(yaml.SafeLoader):
    pass

SecretLoader.add_constructor("!secret", lambda loader, node: f"!secret {loader.construct_scalar(node)}")

class MultibrandV03Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = FILE.read_text(encoding="utf-8")
        cls.doc = yaml.load(cls.raw, Loader=SecretLoader)

    def test_device_and_encryption(self):
        cfg = self.doc
        self.assertEqual(cfg['esp32']['board'], 'esp32dev')
        self.assertEqual(cfg['esp32']['framework']['type'], 'arduino')
        self.assertEqual(cfg['esphome']['name'], '${device_name}')
        self.assertEqual(cfg['api']['encryption']['key'], '!secret api_encryption_key')
        self.assertIn('encryption', cfg['ota'][0])
        self.assertNotIn('password', cfg['ota'][0])

    def test_pinout(self):
        cfg = self.doc
        self.assertEqual(cfg['switch'][0]['pin'], 'GPIO21')
        self.assertEqual(cfg['remote_transmitter']['pin'], 'GPIO4')
        self.assertEqual(cfg['remote_receiver']['pin']['number'], 'GPIO14')
        self.assertIs(cfg['remote_receiver']['pin']['inverted'], True)

    def test_profile_persistence(self):
        select = self.doc['select'][0]
        self.assertIs(select['optimistic'], True)
        self.assertIs(select['restore_value'], True)
        self.assertEqual(select['initial_option'], 'Mirage Magnum 22 - Midea')
        self.assertEqual(len(select['options']), 7)
        self.assertIn('climate.template.publish', select['on_value'][0])
        self.assertNotIn('remote_transmitter', str(select['on_value']))

    def test_one_public_climate(self):
        climates = self.doc['climate']
        public = [c for c in climates if not c.get('internal', False)]
        self.assertEqual(len(climates), 7)
        self.assertEqual(len(public), 1)
        self.assertEqual(public[0]['platform'], 'template')
        self.assertEqual(public[0]['restore_mode'], 'NO_RESTORE')
        self.assertEqual(public[0]['initial_state']['mode'], 'OFF')
        self.assertEqual(public[0]['supported_modes'], ['OFF', 'COOL'])

    def test_profile_routes_match_options(self):
        select = self.doc['select'][0]
        router = self.doc['climate'][-1]['on_control'][0]['lambda']
        for option in select['options']:
            self.assertIn(f'"{option}"', router)
        for backend in self.doc['climate'][:-1]:
            self.assertIn(f"id({backend['id']})", router)
            self.assertTrue(backend['internal'])
            self.assertEqual(backend['transmitter_id'], 'ir_tx')
            self.assertFalse(backend.get('supports_heat', True))
            self.assertNotIn('receiver_id', backend)

    def test_safety_on_restart_and_selection(self):
        raw = self.raw
        self.assertIn('mode == climate::CLIMATE_MODE_OFF && !x.get_mode().has_value()', raw)
        self.assertIn('if (backend == nullptr)', raw)
        self.assertIn('command.perform()', raw)
        self.assertIn('Probar perfil: frío 24 °C', raw)
        self.assertNotIn('external_components:', raw)

    def test_backend_pointer_assignments_cpp(self):
        # ESPHome id(climate) ya devuelve un puntero Climate*; &id produce Climate**.
        router = self.doc['climate'][-1]['on_control'][0]['lambda']
        self.assertNotIn('backend = &id(', router)
        for backend in self.doc['climate'][:-1]:
            self.assertIn(f"backend = id({backend['id']});", router)

    def test_secret_files_stay_excluded(self):
        self.assertIn('**/secrets.yaml', (ROOT/'.gitignore').read_text(encoding='utf-8'))

if __name__ == '__main__':
    unittest.main()
