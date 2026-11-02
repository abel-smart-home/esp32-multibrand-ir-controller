# Arquitectura V0.3: router de perfiles nativo ESPHome

## Decisión

Para **esta alpha** usamos componentes *incluidos en ESPHome 2026.10.1*, en vez de incorporar IRremoteESP8266 todavía. `template climate` proporciona una entidad pública. Los motores `midea_ir`, `coolix`, `gree`, `climate_ir_lg`, `daikin` y `mitsubishi` existen como `climate` internos. El selector `template select` persiste su índice en flash. Una automatización `on_control` decide qué motor recibirá la orden.

Esto prueba el requisito de selección **sin recompilar** entre perfiles ya incluidos. Más adelante podremos pasar a un motor único en C++ si el consumo de flash, velocidad o variantes de protocolo lo exigen.

```text
HOME ASSISTANT
 ├── climate.Aire acondicionado IR Multimarca (única entidad pública)
 └── select.Perfil infrarrojo (persistido)
             │ API cifrada
             ▼
 ESPHome 2026.10.1 · ESP32
 ├── Control template: OFF / COOL, consigna 17–30 °C
 ├── Router `on_control`: selección → motor interno
 │    ├── Midea (Mirage Magnum 22 VALIDADO)
 │    ├── Coolix EXPERIMENTAL
 │    ├── Gree generic EXPERIMENTAL
 │    ├── LG generic EXPERIMENTAL
 │    ├── Daikin generic EXPERIMENTAL
 │    └── Mitsubishi generic EXPERIMENTAL
 └── GPIO4 TX / GPIO14 RX / GPIO21 energía IR
```

## Invariantes

1. Cambiar perfil desde HA o recuperarlo de memoria **no envía IR**.
2. Reiniciar el ESP32 no envía encendido/apagado. El control público comienza `OFF` tras el reinicio; muestra estado solicitado, no confirmado.
3. Cambiar perfil restablece el control público a OFF, pero **no apaga** al aire anterior. Debe apagarse previamente.
4. Modo COOL y OFF, temperaturas 17–30°C. Calor, ventilador, oscilación y captura de mando original quedan pendientes de comprobación y ampliación.
5. Solo un `climate` público; no agregar `receiver_id` a los motores internos en esta alpha para evitar estados incorrectos desde controles ajenos.
6. No requiere IRremoteESP8266 ni un custom component para esta prueba. El cambio a un motor C++ queda sujeto a evaluación; no es una función implementada.
7. Los perfiles representan protocolos o variantes, no compatibilidad universal por marca.

## Limitación técnica

Los motores internos se compilan todos. El router selecciona uno en tiempo de ejecución. Añadir un protocolo nuevo **sí exige** actualizar el firmware; cambiar entre los incluidos no.

Al usar acciones nativas de Home Assistant, la temperatura y el modo mostrados son órdenes estimadas; el A/C no confirma recepción. Un perfil distinto puede necesitar otra variante o rango de temperatura.
