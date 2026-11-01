#!/usr/bin/env python3
"""Crea firmware/secrets.yaml, sin sobrescribirlo, con contraseñas aleatorias.

Uso: python tools/generar_secrets.py
Los datos de Wi-Fi se deben editar localmente. Nunca subir secrets.yaml ni firmware .bin.
"""
from pathlib import Path
import base64
import secrets

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "firmware" / "secrets.yaml"

def quoted(text: str) -> str:
    # yaml entre comillas dobles: escapa caracteres que alteran el valor
    return '"' + text.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n') + '"'

def main():
    if DEST.exists():
        raise SystemExit(f"Ya existe {DEST}; no se sobrescribe para proteger tus claves.")
    api_key = base64.b64encode(secrets.token_bytes(32)).decode("ascii")
    data = {
        "wifi_ssid": "EDITAR_RED_WIFI_2_4_GHZ",
        "wifi_password": "EDITAR_CONTRASENA_WIFI",
        "api_encryption_key": api_key,
        "ota_password": secrets.token_urlsafe(30),
        "fallback_ap_password": secrets.token_urlsafe(18),
        "web_username": "admin",
        "web_password": secrets.token_urlsafe(24),
    }
    DEST.write_text("# Archivo privado: NO subir a GitHub.\n" + "".join(f"{k}: {quoted(v)}\n" for k, v in data.items()), encoding="utf-8")
    print(f"Creado {DEST}. Edita wifi_ssid y wifi_password. No compartas sus valores.")

if __name__ == "__main__":
    main()
