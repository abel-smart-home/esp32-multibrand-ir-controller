# Mirage Magnum 22: selección del primer protocolo infrarrojo

**Estado:** Midea validado físicamente para encender, cambiar temperatura y apagar; el resto de funciones siguen bajo prueba. Firmware de pruebas: `firmware/ir_mirage_magnum22_v02.yaml`.

## Evidencia y límites

- El modelo Mirage Magnum 22 tiene varias variantes comerciales (solo frío y frío/calor).
- Comercios documentan control remoto original `RG10A(D2S)-GEF` para Magnum 22; el código exacto del control instalado debe confirmarse visualmente.
- Captura de ESPHome aportada durante el desarrollo: `0xB24DBF40C03F`. Interpretación como bytes complementarios `B2 4D | BF 40 | C0 3F`, compatible con trama Midea IR de 48 bits. Fue un indicio de compatibilidad, confirmado después por pruebas de encendido, cambios de temperatura y apagado mediante `midea_ir`; otras funciones no están confirmadas.
- `dump: all` generó coincidencias simultáneas en varios decodificadores y avisos de ejecución larga; V0.2 limita el registro a `[midea, coolix]`.
- Protocolo UART/Midea del puerto de la unidad **no equivale** a compatibilidad garantizada del protocolo IR.

## Cambios de V0.2

- `climate: platform: midea_ir` con IDs explícitos de emisor y receptor.
- `dump: [midea, coolix]` para reducir decodificadores y registros.
- `supports_heat: false` y `supports_heat_cool: false` hasta verificar variante con calefacción. No cambiarlo sin comprobarlo.
- Sin sensor de temperatura ambiente: Home Assistant sólo conoce la consigna, no la temperatura real.
- Se mantiene el mismo `device_name` que V0.1 para OTA e identidad del dispositivo.

## Referencias

- https://mirage.mx/productos/todo/aire-acondicionado/minisplit/inverter/magnum-22-inverter/
- https://www.climahorro.com.mx/productos/control-remoto-minisplit-mirage-magnum-22-mod-rg10ad2s-gef/
- https://esphome.io/components/climate/climate_ir/
- https://esphome.io/components/remote_receiver/
- https://components.espressif.com/components/embedblocks/aircon-ir/versions/0.1.0/readme

## Próxima etapa

Confirmadas las funciones básicas de `midea_ir`, verificar ventilador, swing, recepción del control original y reinicios. Si no, capturar secuencias etiquetadas y estudiar el perfil Midea (incluidas variantes RG10A) antes de introducir IRremoteESP8266 o códigos raw.
