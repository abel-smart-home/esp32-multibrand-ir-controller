# Control IR Multimarca para ESP32 + Home Assistant

**Estado actual: `v0.1.0-alpha.1` · prueba de hardware (PRE-RELEASE).**

Proyecto para convertir un módulo ESP32 con emisor/receptor infrarrojo en un controlador de aire acondicionado **multimarca**, configurable desde Home Assistant, conservando el perfil seleccionado tras reinicios y sin recompilar para cambiar entre protocolos incluidos.

> **Importante:** la versión que contiene este repositorio **todavía NO controla aires acondicionados**, **NO crea una entidad `climate`** y **NO permite seleccionar marca/modelo**. Esta primera entrega permite comprobar la tarjeta ESP32, la comunicación Wi-Fi/HA, la recepción de IR y una trama NEC de laboratorio. No se ha probado aún sobre la unidad física del proyecto.

## Hardware inicial

- Módulo ESP32-WROOM-32E con USB-C y transmisor/receptor IR integrado.
- GPIO4: emisor IR; GPIO14 invertido: receptor IR; GPIO21: alimentación del circuito IR **según una revisión publicada por la comunidad**. Pueden cambiar en otras revisiones.
- USB-C podría ser únicamente alimentación; no asumir que sirve para flasheo serial.

![Estado](https://img.shields.io/badge/fase-validaci%C3%B3n%20de%20hardware-orange)

## Funciones de esta versión

- Firmware ESPHome `firmware/ir_multimarca_lab.yaml` (ESP32 clásico con framework Arduino).
- Conexión Wi-Fi, API nativa cifrada con Home Assistant y OTA de ESPHome.
- Portal web local con autenticación y OTA web (solo red local confiable).
- Acceso Wi-Fi de rescate si pierde red.
- Receptor IR con decodificación en registros (`dump: all`).
- Botón de Home Assistant para transmitir **una trama NEC de prueba**, no un comando de aire acondicionado.
- Diagnósticos de Wi-Fi, IP, tiempo encendido, ESPHome y estado en línea.
- Ejemplos de secretos privados y herramienta para generarlos.
- Pruebas de estructura y validación de configuración por GitHub Actions.

## Inicio rápido

1. Descomprime o clona el repositorio.
2. Instala Python 3 si vas a usar el generador y ejecuta `python tools/generar_secrets.py`; edita `firmware/secrets.yaml` con la red **Wi-Fi de 2.4 GHz** y su contraseña reales. Alternativamente, copia `firmware/secrets.example.yaml` y reemplaza todas las claves (API requiere 32 bytes codificados en base64).
3. En el complemento **ESPHome Device Builder**, crea un dispositivo basado en ESP32 `esp32dev` e introduce el contenido de `firmware/ir_multimarca_lab.yaml`. Asegúrate de que las claves `!secret` existan en el `secrets.yaml` del directorio donde compile ESPHome.
4. Valida y compila. La primera carga al firmware original depende de si su portal de actualizaciones acepta el `.bin` OTA generado; **no uses Factory Image en un portal OTA**. Consulta [Instalación y recuperación](docs/INSTALACION.md).
5. Agrega el dispositivo detectado a Home Assistant desde la integración ESPHome. Observa los logs con el control remoto original apuntando a la placa, luego prueba una transmisión NEC con otros aparatos IR alejados.
6. Registra los resultados en [Plan de pruebas](docs/PRUEBAS.md) antes de calificar la validación como completa.

**No se incluyen claves Wi-Fi ni archivos `.bin` compilados.** No publiques `secrets.yaml` ni un firmware compilado con tus credenciales. El repositorio no contiene ningún `external_components` ficticio; el componente propio comenzará tras validar la placa.

## Documentación

- [Arquitectura y versiones](docs/ARQUITECTURA.md)
- [Hardware y pinout](docs/HARDWARE.md)
- [Instalación, primer flasheo y recuperación](docs/INSTALACION.md)
- [Plan de pruebas](docs/PRUEBAS.md)
- [Guía para GitHub, commits y pre-release](docs/GITHUB.md)
- [Texto de publicación de la alpha](docs/RELEASE_NOTES_v0.1.0-alpha.1.md)
- [Changelog](CHANGELOG.md)

## Alcance futuro

- V0.2: entidad `climate` y protocolo de prueba validado con un aire acondicionado real.
- V0.3: catálogo/selector persistente de marcas y variantes desde Home Assistant; motor IR basado en IRremoteESP8266, sujeto a compatibilidad en compilación y pruebas.
- V1.0: estabilidad, recuperación de estados, diagnósticos y catálogo verificado.

Los comandos IR suelen ser unidireccionales: Home Assistant mostrará **estado solicitado o inferido**, no confirmación del A/C.

## Atribuciones y licencia

- Proyecto propio bajo licencia MIT (consulta `LICENSE`).
- **ESPHome** y **IRremoteESP8266** son proyectos de terceros; este paquete **no incluye** código de IRremoteESP8266. Antes de incorporarlo en una versión distribuible se revisarán y cumplirán sus licencias.
- Los pines y la ruta OTA del firmware de fábrica están basados en experiencias comunitarias, sin garantía de reproducirse exactamente en todas las placas.

Referencias:
- ESPHome RX: https://esphome.io/components/remote_receiver/
- ESPHome TX: https://esphome.io/components/remote_transmitter/
- ESPHome OTA web: https://esphome.io/components/ota/web_server/
- ESPHome framework: https://esphome.io/components/esp32/
- Comunidad, revisión de la placa: https://community.home-assistant.io/t/solution-esp32-infrared-wifi-module-esp32e-n4-infrared-transmitter-receiver-correct-pinout-for-esphome/1003067
- IRremoteESP8266: https://github.com/crankyoldgit/IRremoteESP8266
