"""Contrato V0.3 alpha.2; la compilación de ESPHome en CI sigue siendo obligatoria."""
from pathlib import Path
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / "firmware" / "ir_multimarca_v03.yaml"

class Loader(yaml.SafeLoader):
    pass
Loader.add_constructor("!secret", lambda loader, node: "!secret " + loader.construct_scalar(node))

class V03Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc = yaml.load(FILE.read_text(encoding="utf-8"), Loader=Loader)
        cls.code = cls.doc['climate'][-1]['on_control'][0]['lambda']

    def test_hardware_and_api(self):
        x=self.doc
        self.assertEqual(x['esp32']['board'],'esp32dev')
        self.assertEqual(x['esp32']['framework']['type'],'arduino')
        self.assertEqual(x['remote_transmitter']['pin'],'GPIO4')
        self.assertEqual(x['remote_receiver']['pin']['number'],'GPIO14')
        self.assertEqual(x['switch'][0]['pin'],'GPIO21')
        self.assertEqual(x['api']['encryption']['key'],'!secret api_encryption_key')
        self.assertIn('encryption',x['ota'][0])

    def test_profiles_without_duplicate_mirage(self):
        p=self.doc['select'][0]
        self.assertEqual(p['initial_option'],'Midea')
        self.assertTrue(p['restore_value'])
        self.assertEqual(p['name'],'Perfil IR multimarca')
        self.assertEqual(p['options'].count('Midea'),1)
        self.assertFalse(any('Mirage Magnum' in s for s in p['options']))
        self.assertEqual(len(p['options']),14)

    def test_engines_and_routing(self):
        engines=self.doc['climate'][:-1]
        public=[x for x in self.doc['climate'] if not x.get('internal',False)]
        self.assertEqual(len(public),1)
        self.assertEqual(len(engines),10)
        self.assertEqual({x['protocol'] for x in engines if x['platform']=='heatpumpir'},
                         {'aux','carrier_mca','hisense_aud','samsung_aqv'})
        for x in engines:
            self.assertTrue(x['internal'])
            self.assertEqual(x['transmitter_id'],'ir_tx')
            self.assertIn(f'backend = id({x["id"]});', self.code)
            self.assertNotIn(f'backend = &id({x["id"]})',self.code)

    def test_unsupported_profiles_are_safe(self):
        opts=self.doc['select'][0]['options']
        for brand in ('Mabe','Duventus','General Electric','York'):
            self.assertIn(f'{brand} (sin protocolo confirmado)',opts)
            self.assertNotIn(f'profile == "{brand} (sin protocolo confirmado)"',self.code)
        self.assertIn('if (backend == nullptr)',self.code)
        self.assertIn('return;',self.code)
        self.assertFalse(self.doc['climate'][-1]['optimistic'])

    def test_no_auto_tx_and_persistence(self):
        x=self.doc
        self.assertEqual(x['climate'][-1]['restore_mode'],'NO_RESTORE')
        self.assertEqual(x['climate'][-1]['initial_state']['mode'],'OFF')
        self.assertIn('climate.template.publish',x['select'][0]['on_value'][0])
        self.assertNotIn('remote_transmitter',str(x['select'][0]['on_value']))
        self.assertIn('command.perform();',self.code)
        self.assertIn('id(ir_frontend).publish_state();',self.code)

    def test_no_embedded_private_secrets(self):
        self.assertIn('**/secrets.yaml',(ROOT/'.gitignore').read_text(encoding='utf-8'))

if __name__=='__main__': unittest.main()
