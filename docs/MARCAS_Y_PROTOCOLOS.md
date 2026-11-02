# Marcas, perfiles y protocolos — V0.3.0-alpha.2

**Importante:** una **marca comercial** no es necesariamente un **protocolo infrarrojo**. Un mismo fabricante puede utilizar varios mandos/protocolos según la línea o modelo.

| Opción en Home Assistant | Motor | Evidencia |
| --- | --- | --- |
| Midea | ESPHome `midea_ir` | **Validado** encendido, temperatura y apagado en Mirage Inverter Magnum 22 |
| Coolix | `coolix` | Experimental |
| Gree genérico | `gree` | Experimental |
| LG genérico | `climate_ir_lg` | Experimental |
| Daikin genérico | `daikin` | Experimental |
| Mitsubishi genérico | `mitsubishi` | Experimental |
| AUX - aux | `heatpumpir/aux` | Experimental; sin prueba física |
| Carrier - MCA | `heatpumpir/carrier_mca` | Experimental; otras variantes Carrier posibles |
| Hisense - AUD | `heatpumpir/hisense_aud` | Experimental; otras variantes Hisense posibles |
| Samsung - AQV | `heatpumpir/samsung_aqv` | Experimental; otras variantes Samsung posibles |
| Mabe | **Ninguno** | Aparece en lista para identificar; seleccionarlo no habilita TX |
| Duventus | **Ninguno** | Aparece en lista para identificar; seleccionarlo no habilita TX |
| General Electric | **Ninguno** | Aparece en lista para identificar; seleccionarlo no habilita TX |
| York | **Ninguno** | Aparece en lista para identificar; seleccionarlo no habilita TX; IRremoteESP8266 sí documenta un protocolo York que aún no incorporamos |

## Cambio del selector

Se eliminó el duplicado de Mirage Magnum 22: solo queda **Midea**. Como en la alfa anterior el selector persistía el **índice** de la opción, quitar un elemento podría reinterpretar una preferencia antigua. Para prevenir que se active accidentalmente otro protocolo, el selector cambia su nombre e identificador de entidad a **Perfil IR multimarca** y toma **Midea** como valor inicial en la primera instalación de esta alfa. Después de seleccionar un perfil, se vuelve a guardar de manera persistente en reinicios.

Es posible que Home Assistant muestre temporalmente la entidad anterior `select.perfil_infrarrojo` como no disponible. No la borres hasta confirmar que la nueva funciona y revisar tus automatizaciones.

## Seguridad

- Elegir un perfil no transmite ni enciende/apaga físicamente el aire.
- Sin motor configurado, las órdenes de climatización son rechazadas y no se publica falsamente un estado encendido.
- El estado transmitido es **solicitado**, no confirmado por el equipo.
- Nunca se envían señales IR al reiniciar el ESP32.
- Antes de probar un perfil experimental, orienta el LED al aparato deseado, comprueba compatibilidad en el mando original y ejecuta una orden deliberada.
- Las nuevas marcas requerirán modelos o señales originales para confirmar compatibilidad.

## Fuentes del protocolo

- ESPHome IR Remote Climate: https://esphome.io/components/climate/climate_ir/
- ESPHome HeatpumpIR: https://esphome.io/components/climate/heatpumpir/
- IRremoteESP8266, protocolos soportados: https://github.com/crankyoldgit/IRremoteESP8266/blob/master/SupportedProtocols.md
