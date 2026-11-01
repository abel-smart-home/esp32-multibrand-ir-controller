# Hardware y pinout (provisional)

## Tarjeta objetivo

La foto de la tarjeta comprada muestra un módulo **ESP32-WROOM-32E N4**, LED emisor IR transparente, receptor IR oscuro, USB-C y seis pads rotulados `GND`, `5V`, `RX`, `TX`, `IO0`/`100` y `GND` (lectura de la fotografía). La variante exacta del PCB no está verificada físicamente.

En una revisión similar documentada el 10-abr-2026 en Home Assistant Community:

| Función | GPIO sugerido | Riesgo/estado |
| --- | --- | --- |
| Emisor IR | GPIO4 | Requiere prueba real |
| Receptor IR | GPIO14 invertido | Otros pinouts publicados usan GPIO5; verificar |
| Habilitar alimentación del circuito IR | GPIO21 (HIGH) | Necesario en la revisión documentada |
| Alimentación | USB-C 5 V | No presuponer conectividad serial por USB-C |

Referencia técnica: https://community.home-assistant.io/t/solution-esp32-infrared-wifi-module-esp32e-n4-infrared-transmitter-receiver-correct-pinout-for-esphome/1003067

Enlace de compra aportado para el proyecto: https://es.aliexpress.com/item/1005013022459185

## Precauciones

- Solo alimentar la tarjeta con 5 V mediante el puerto diseñado para ello. No conectar 5 V directamente a GPIO.
- Si hace falta programación serial, usar adaptador USB-UART con señales lógicas **3.3 V** y masa común; nunca poner 5 V en RX/TX/IO0. No usar dos fuentes de alimentación simultáneamente sin revisar el cableado.
- No suponer que las etiquetas serigrafiadas coinciden con la revisión documentada sin probar.
- Para la primera prueba, retirar otros equipos sensibles a señales IR de la línea de visión.
- IR no mide temperatura ambiente ni confirma si el aire recibió una orden. Eso requeriría otra fuente de datos.

## Pendientes de verificación

- Confirmar GPIO TX/RX y estado eléctrico GPIO21.
- Verificar que el emisor pueda alcanzar la unidad interna desde la ubicación real.
- Medir alcance/ángulo, interrupciones y ecos del receptor.
- Probar el procedimiento de carga del firmware de fábrica sin perder acceso de recuperación.
