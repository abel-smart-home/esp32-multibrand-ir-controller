# Control IR Multimarca para ESP32 + Home Assistant

**Versión publicada:** `v0.1.0-alpha.1`. **Nueva V0.2 candidata:** encendido, ajustes de temperatura y apagado confirmados físicamente en Mirage Magnum 22. Pendiente CI del nuevo commit y publicación como pre-release.

Proyecto para convertir un módulo ESP32 con emisor/receptor infrarrojo en un controlador de aire acondicionado **multimarca**, configurable desde Home Assistant, conservando el perfil seleccionado tras reinicios y sin recompilar para cambiar entre protocolos incluidos.

> **Importante:** `firmware/ir_multimarca_lab.yaml` sigue siendo la referencia V0.1. La V0.2 incorpora `climate` mediante `midea_ir` en `firmware/ir_mirage_magnum22_v02.yaml`; el usuario confirmó que funciona para encender, modificar la temperatura y apagar su Mirage Magnum 22. Aún faltan pruebas de recepción del mando, modos adicionales, reinicios y OTA cifrada. La selección de marca/modelo sin recompilar corresponde a una versión posterior.

## Hardware inicial

- Módulo ESP32-WROOM-32E con USB-C y transmisor/receptor IR integrado.
- GPIO4: emisor IR; GPIO14 invertido: receptor IR; GPIO21: alimentación del circuito IR **según una revisión publicada por la comunidad**. Pueden cambiar en otras revisiones.
- USB-C podría ser únicamente alimentación; no asumir que sirve para flasheo serial.

![Estado](https://img.shields.io/badge/fase-pruebas%20v0.2-orange)

## Funciones de V0.1 (base de laboratorio)

- Firmware ESPHome `firmware/ir_multimarca_lab.yaml` (ESP32 clásico con framework Arduino).
- Conexión Wi-Fi, API nativa cifrada con Home Assistant y OTA de ESPHome.
- Portal web local con autenticación y OTA web (solo red local confiable).
- Acceso Wi-Fi de rescate si pierde red.
- Receptor IR con decodificación en registros (`dump: all`).
- Botón de Home Assistant para transmitir **una trama NEC de prueba**, no un comando de aire acondicionado.
- Diagnósticos de Wi-Fi, IP, tiempo encendido, ESPHome y estado en línea.
- Ejemplos de secretos privados y herramienta para generarlos.
- Pruebas de estructura y validación de configuración por GitHub Actions.

## Instalación inicial V0.1 (conservada como referencia)

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

## Candidato V0.2 probado parcialmente en Mirage Magnum 22

- Archivo nuevo: [`firmware/ir_mirage_magnum22_v02.yaml`](firmware/ir_mirage_magnum22_v02.yaml).
- Protocolo: **Midea IR**, con encendido, cambio de temperatura y apagado confirmados por el usuario en hardware real.
- Actualizar el mismo dispositivo ESPHome por OTA, **sin crear otro dispositivo**. Esta revisión recomienda OTA nativa cifrada con la clave API que ya funciona; revisar `docs/PRUEBAS_V02.md` antes de hacer la transición.
- [`docs/MIRAGE_MAGNUM22.md`](docs/MIRAGE_MAGNUM22.md), [`docs/PRUEBAS_V02.md`](docs/PRUEBAS_V02.md) y [`docs/RELEASE_NOTES_v0.2.0-alpha.1.md`](docs/RELEASE_NOTES_v0.2.0-alpha.1.md).
- Mantener [`firmware/ir_multimarca_lab.yaml`](firmware/ir_multimarca_lab.yaml) como recuperación.

## Alcance futuro

- V0.2: entidad `climate` con encendido, temperatura y apagado confirmados para Mirage Magnum 22; pendiente completar pruebas para cerrar esta etapa.
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
