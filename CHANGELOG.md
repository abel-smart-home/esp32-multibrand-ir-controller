# Historial de cambios

## [0.3.0-alpha.1] — Candidato (no publicado)

### Añadido
- `firmware/ir_multimarca_v03.yaml`: `climate.template` visible + `select.template` persistente.
- Enrutamiento en tiempo de ejecución a Midea, Coolix, Gree genérico, LG genérico, Daikin genérico y Mitsubishi genérico.
- 7 opciones seleccionables: Mirage Magnum 22/Midea, Midea genérico y 5 protocolos alternativos.
- Selector sin transmisión IR, restauración de selección y arranque con modo OFF sin reenvíos.
- Prueba deliberada COOL 24 °C, plan de pruebas, notas de pre-release y validación CI V0.3.

### Alcance y pendientes
- `COOL/OFF`, consigna 17–30 °C; perfiles alternativos no validados físicamente.
- La compatibilidad sobre Mirage en esta versión y la compilación CI se deben verificar ANTES de publicar.
- No incluye biblioteca IRremoteESP8266, aprendizaje ni receptor que sincronice el estado público.

## [0.2.0-alpha.1] — Pre-release publicado

### Añadido
- `firmware/ir_mirage_magnum22_v02.yaml`: `midea_ir` + `climate` en Home Assistant.
- OTA nativa cifrada por clave API y recepción simplificada para Midea/Coolix.
- Pruebas CI para ambos firmwares V0.1/V0.2.

### Pruebas en hardware
- Encendido, ajuste ascendente/descendente de consigna y apagado confirmados en Mirage Inverter Magnum 22.
- Pendientes: recepción del mando original, modos avanzados y pruebas prolongadas.

## [0.1.0-alpha.1] — 2026-10-31

### Añadido
- ESPHome de laboratorio para ESP32 IR, GPIO21/4/14, recepción con registros y trama NEC de prueba.
- API cifrada, OTA, web autenticada, AP de rescate, diagnósticos, generación local de secretos y CI inicial.
