# v0.1.0-alpha.1 — Validación inicial del hardware ESP32 IR

**Tipo:** Pre-release (alfa, no estable)

## Incluye

- Firmware de laboratorio ESPHome para ESP32 clásico con framework Arduino.
- GPIO del módulo IR: alimentación GPIO21, transmisión GPIO4 y recepción GPIO14 invertida, basados en una revisión conocida (a validar físicamente).
- Recepción infrarroja registrada en logs, transmisión de trama NEC de prueba bajo acción manual.
- Wi-Fi, Home Assistant API cifrada, recuperación por AP, OTA nativa y portal web autenticado.
- Sensores de diagnóstico, instrucciones de instalación, tests estáticos y workflow de GitHub Actions.

## No incluye

- Control de aires acondicionados, entidad `climate` o selección multimarca.
- Biblioteca IRremoteESP8266 integrada (se analizará después de validar el hardware).
- Firmware `.bin` listo para instalar: cada instalación debe compilar sus secretos privados.
- Validación de funcionamiento en hardware real; es un pre-release inicial.

## Precauciones

- El pinout puede ser distinto en otras revisiones.
- El USB-C puede ser exclusivamente de alimentación.
- Nunca publicar credenciales de Wi-Fi/API/OTA/web ni binarios compilados con ellas.
- El paquete NO garantiza que el firmware original acepte el formato OTA.

## Próximo hito

Compilar, instalar y completar `docs/PRUEBAS.md`. Solo después de registrar resultados publicar `v0.1.0` estable o emitir una revisión alfa corregida.
