"""Pruebas básicas sin necesidad de conectar el ESP32."""
from pathlib import Path
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
FIRMWARE = ROOT / "firmware" / "ir_multimarca_lab.yaml"

class ESPHomeSecretLoader(yaml.SafeLoader):
    pass

ESPHomeSecretLoader.add_constructor("!secret", lambda loader, node: "!secret " + loader.construct_scalar(node))

class RepositoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = FIRMWARE.read_text(encoding="utf-8")
        cls.doc = yaml.load(cls.raw, Loader=ESPHomeSecretLoader)

    def test_esp32_and_arduino(self):
        self.assertEqual(self.doc["esp32"]["board"], "esp32dev")
        self.assertEqual(self.doc["esp32"]["framework"]["type"], "arduino")

    def test_ir_pinout(self):
        self.assertEqual(self.doc["switch"][0]["pin"], "GPIO21")
        self.assertEqual(self.doc["switch"][0]["restore_mode"], "ALWAYS_ON")
        self.assertEqual(self.doc["remote_transmitter"]["pin"], "GPIO4")
        self.assertEqual(self.doc["remote_receiver"]["pin"]["number"], "GPIO14")
        self.assertIs(self.doc["remote_receiver"]["pin"]["inverted"], True)

    def test_no_climate_or_custom_components_pretended(self):
        self.assertNotIn("climate", self.doc)
        self.assertNotIn("external_components", self.doc)

    def test_api_and_web_security(self):
        self.assertTrue(self.doc["api"]["encryption"]["key"].startswith("!secret "))
        self.assertTrue(self.doc["web_server"]["auth"]["password"].startswith("!secret "))
        self.assertTrue(any(p["platform"] == "web_server" for p in self.doc["ota"]))
        self.assertTrue(any(p["platform"] == "esphome" for p in self.doc["ota"]))

    def test_no_real_credentials_stored(self):
        self.assertIn("**/secrets.yaml", (ROOT / ".gitignore").read_text(encoding="utf-8"))
        self.assertIn("Pendiente", (ROOT / "docs" / "PRUEBAS.md").read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()
