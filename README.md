# ESP32 Multibrand IR Controller + Home Assistant

Controlador de aire acondicionado por infrarrojos con ESPHome, destinado a un ESP32-WROOM-32E con transmisor/receptor IR. **Fuente de la verdad:** https://github.com/abel-smart-home/esp32-multibrand-ir-controller

## Estado de versiones

- **v0.1.0-alpha.1:** validación del hardware IR, Wi-Fi, API/OTA y diagnósticos.
- **v0.2.0-alpha.1:** entidad `climate` Midea. Probados sobre **Mirage Inverter Magnum 22** encendido, cambio de temperatura y apagado. Documento de hardware: [`docs/MIRAGE_MAGNUM22.md`](docs/MIRAGE_MAGNUM22.md).
- **v0.3.0-alpha.1 (CANDIDATO, NO PUBLICADO):** router multimarca con selector persistente desde Home Assistant y motor IR seleccionado en tiempo de ejecución. **Faltan validación CI/compilación y pruebas físicas.**

## V0.3 experimental: sin recompilar para cambiar de perfil

Archivo nuevo: [`firmware/ir_multimarca_v03.yaml`](firmware/ir_multimarca_v03.yaml).

**Una entidad `climate` visible** (`Aire acondicionado IR Multimarca`) y un `select` (`Perfil infrarrojo`) visible en Home Assistant. En V0.3 se compilan varios motores ESPHome como entidades internas: `midea_ir`, `coolix`, `gree` (`generic`), `climate_ir_lg`, `daikin` y `mitsubishi`.

El selector presenta 7 perfiles/opciones: Mirage Magnum 22/Midea (probado en V0.2), Midea genérico, Coolix, Gree genérico, LG genérico, Daikin genérico y Mitsubishi genérico. **Los demás son EXPERIMENTALES y no garantizan compatibilidad con cualquier aire de esa marca.**

- Cambiar de perfil **no exige recompilar** entre los protocolos incluidos, y su elección se guarda en flash.
- Cambiar de perfil **no manda IR**. Para cambiar de un aire a otro, **apaga antes el aire anterior**.
- El `climate` comienza en OFF tras un reinicio, sin reenviar órdenes; el estado mostrado es solicitado/inferido, no confirmado.
- En esta alfa sólo se habilitan **COOL/OFF** y consigna 17–30 °C. Ventilador, calor, aletas y recepción/sincronización de mando quedan pendientes.
- No se ha integrado IRremoteESP8266: esta alpha usa únicamente protocolos **nativos de ESPHome**. El futuro motor C++ se evaluará después de comprobar la experiencia y el tamaño del firmware.


## Actualización V0.3.0-alpha.2 — más marcas y perfiles

La versión previa (`v0.3.0-alpha.1`) ya se publicó como pre-release. Esta revisión candidata elimina el perfil duplicado **Mirage Magnum 22 - Midea**: ahora se utiliza únicamente **Midea**, que se probó con el Mirage Magnum 22. El selector se llama **Perfil IR multimarca**; al migrar, inicia en Midea para evitar que los índices guardados de la versión anterior apunten por error a otro protocolo, y luego vuelve a persistir el perfil seleccionado.

Se incorporan perfiles experimentales **AUX / aux, Carrier / carrier_mca, Hisense / hisense_aud y Samsung / samsung_aqv** con el componente HeatpumpIR de ESPHome. También se muestran **Mabe, Duventus, General Electric y York** como **sin protocolo confirmado**: seleccionarlas no transmite ninguna señal infrarroja. Ninguna marca garantiza compatibilidad por sí sola con todos sus modelos.

La única entidad `climate` sigue siendo `Aire acondicionado IR Multimarca`, con estado solicitado y no confirmado por el minisplit. Ver [`docs/MARCAS_Y_PROTOCOLOS.md`](docs/MARCAS_Y_PROTOCOLOS.md) y [`docs/INSTALACION_V03_ALPHA2.md`](docs/INSTALACION_V03_ALPHA2.md). Validación y compilación en GitHub Actions **pendientes antes de instalar**.

## Instalación V0.3 (después de pasar CI)

1. Conserva una copia del YAML actual V0.2. No borres [`firmware/ir_mirage_magnum22_v02.yaml`](firmware/ir_mirage_magnum22_v02.yaml).
2. En ESPHome Device Builder abre tu dispositivo existente **Control IR Multimarca LAB** (el mismo nombre/host `control-ir-multimarca-lab`).
3. Sustituye el YAML de V0.2 por el de V0.3. **No cambies** tus secretos privados; se siguen usando `wifi_ssid`, `wifi_password`, `api_encryption_key`, `fallback_ap_password`, `web_username`, `web_password`.
4. Ejecuta `Validate` y luego `Install → Wirelessly`. Si falla, consulta el log completo: el YAML de V0.2 continúa disponible para recuperación OTA.
5. Abre Home Assistant y confirma que aparezcan `Aire acondicionado IR Multimarca` y `Perfil infrarrojo`. Puede permanecer la entidad histórica Mirage de V0.2 como huérfana; revisa la integración antes de eliminarla.
6. Mantén el perfil `Mirage Magnum 22 - Midea` y prueba COOL 24, bajar/subir temperatura y OFF con el aire real.
7. Cambia a otro perfil **sólo sin dirigir el IR a equipos en uso** y confirma que el selector no transmita al cambiar ni al reiniciar.
8. Apaga/enciende el ESP32 y confirma que la selección persista, sin órdenes IR automáticas.
9. Anota resultados en [`docs/PRUEBAS_V03.md`](docs/PRUEBAS_V03.md).

**No publiques** `secrets.yaml` ni archivos `.bin` compilados con claves privadas. La vía web OTA usa HTTP local y no debe exponerse a Internet.

## Hardware y compatibilidad

GPIO4: transmisor; GPIO14 invertido: receptor; GPIO21: alimentación del circuito IR. Confirmados funcionalmente para el prototipo del proyecto, aunque otras revisiones de la tarjeta pueden variar. USB-C puede ser sólo alimentación.

V0.3 **no es todavía un producto universal**. La selección cambia únicamente el protocolo, no aprende códigos desconocidos. Requiere línea de visión con el A/C y no dispone de retorno de estado confirmado.

## Documentación

- [`docs/ARQUITECTURA_V03.md`](docs/ARQUITECTURA_V03.md): arquitectura del router y sus límites.
- [`docs/PRUEBAS_V03.md`](docs/PRUEBAS_V03.md): checklist V0.3.
- [`docs/RELEASE_NOTES_v0.3.0-alpha.1.md`](docs/RELEASE_NOTES_v0.3.0-alpha.1.md): notas de pre-release candidatas.
- [`docs/PRUEBAS_V02.md`](docs/PRUEBAS_V02.md): pruebas Mirage V0.2.
- [`docs/INSTALACION.md`](docs/INSTALACION.md): primer flasheo y recuperación.
- [`CHANGELOG.md`](CHANGELOG.md): versiones.

## Licencia

Código propio: MIT (`LICENSE`). Se utilizan componentes incluidos en ESPHome, conforme a sus respectivas licencias. No se distribuye IRremoteESP8266 ni código derivado de esa biblioteca en la V0.3.

Referencias: [ESPHome Template Climate](https://esphome.io/components/climate/template/), [ESPHome Template Select](https://esphome.io/components/select/template/), [ESPHome IR Climate](https://esphome.io/components/climate/climate_ir/).
