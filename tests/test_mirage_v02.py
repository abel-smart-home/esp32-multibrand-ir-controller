"""Pruebas estructurales de V0.2 (NO sustituyen hardware)."""
import unittest
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
FIRMWARE = ROOT / "firmware" / "ir_mirage_magnum22_v02.yaml"
OLD = ROOT / "firmware" / "ir_multimarca_lab.yaml"
class ESPHomeSecretLoader(yaml.SafeLoader):
    pass
ESPHomeSecretLoader.add_constructor("!secret", lambda loader, node: "!secret " + loader.construct_scalar(node))

class MirageV02Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc = yaml.load(FIRMWARE.read_text(encoding="utf-8"), Loader=ESPHomeSecretLoader)
        cls.old = yaml.load(OLD.read_text(encoding="utf-8"), Loader=ESPHomeSecretLoader)

    def test_same_device_identity_for_ota(self):
        self.assertEqual(self.doc["esphome"]["name"], self.old["esphome"]["name"])
        self.assertEqual(self.doc["esp32"]["board"], "esp32dev")

    def test_midea_climate_and_explicit_hardware(self):
        self.assertEqual(self.doc["climate"][0]["platform"], "midea_ir")
        self.assertEqual(self.doc["climate"][0]["transmitter_id"], "ir_tx")
        self.assertEqual(self.doc["climate"][0]["receiver_id"], "ir_rx")
        self.assertEqual(self.doc["remote_transmitter"]["pin"], "GPIO4")
        self.assertEqual(self.doc["remote_receiver"]["pin"]["number"], "GPIO14")
        self.assertEqual(self.doc["switch"][0]["pin"], "GPIO21")

    def test_encrypted_native_ota(self):
        self.assertTrue(self.doc["api"]["encryption"]["key"].startswith("!secret "))
        esphome_ota = next(x for x in self.doc["ota"] if x["platform"] == "esphome")
        self.assertIn("encryption", esphome_ota)
        self.assertNotIn("password", esphome_ota)
        self.assertTrue(any(x["platform"] == "web_server" for x in self.doc["ota"]))

    def test_limited_ir_logs_and_no_heat_assumption(self):
        self.assertEqual(self.doc["remote_receiver"]["dump"], ["midea", "coolix"])
        self.assertIs(self.doc["climate"][0]["supports_heat"], False)
        self.assertNotIn("sensor", self.doc["climate"][0])
        self.assertNotIn("external_components", self.doc)

if __name__ == "__main__":
    unittest.main()
