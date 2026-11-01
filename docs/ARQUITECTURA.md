# Arquitectura objetivo y decisiones

## Lo que existe en V0.1

ESPHome (framework Arduino) <-> API nativa Home Assistant; Wi-Fi / portal web / OTA; GPIO21 (energía IR); GPIO14 (receptor) y GPIO4 (emisor de trama NEC de prueba). La entidad `climate`, el perfil activo y el motor IR multimarca **NO están implementados**.

## Objetivo V0.2 a V1.0

```text
HOME ASSISTANT
 climate + select(marca/protocolo) + diagnósticos
          ⇅ API ESPHome
ESP32 / plataforma personalizada `multibrand_ir`
 ├── Catálogo de perfiles soportados y capacidades (incluido en firmware)
 ├── Control de estado solicitado (no confirmado por A/C)
 ├── Motor de protocolos (IRremoteESP8266/IRac)
 ├── Recepción / decodificación cuando sea posible
 ├── Persistencia de identificador de perfil en flash
 └── Transmisor y receptor IR
          ↓ infrarrojos
        AIRE ACONDICIONADO
```

## Invariantes de diseño

1. Cambiar perfil entre aquellos **compilados en el dispositivo** NO debe exigir recompilar.
2. Soportar un protocolo **nuevo, ausente del firmware**, puede exigir actualizarlo.
3. La marca no basta: se utiliza `perfil_id`, incluyendo variante/modelo compatible.
4. Antes de guardar un perfil se ofrece una prueba manual deliberada; no enviar comandos IR durante selección o boot.
5. Al reiniciar se conserva configuración; **no se transmiten comandos IR automáticamente**.
6. El estado que recibe HA es 'solicitado/estimado'. Si no existe retorno real desde el A/C, no afirmar confirmación.
7. La recepción del mando original solo modifica estado cuando haya una decodificación fiable.
8. Evitar escrituras en flash por cada pulsación; persistir configuración con retraso/control de desgaste.
9. Manejar protocolo con variantes, temperaturas mínima/máxima y modos realmente soportados.
10. Recuperación sin Home Assistant: Wi-Fi y portal de diagnóstico no deben depender de la API disponible.

## Dependencias futuras

- `IRremoteESP8266` se incorporará en V0.2/0.3 solo después de validar su integración con la versión de ESPHome y el framework Arduino.
- El componente propio deberá administrar IR Tx/Rx directamente, evitando usar simultáneamente drivers incompatibles sobre el mismo pin/periférico.
- Primero se validará protocolo/modelo de un equipo real; después catálogo extenso.

## Versionado

- `v0.1.0-alpha.1`: primera validación sin pruebas físicas; se publica como pre-release.
- `v0.1.0`: solo tras pruebas de RX, TX, Wi-Fi y OTA en el hardware real.
- `v0.2.0-alpha.1`: primera implementación de climatización, con un protocolo validado.
- `v0.3.0-alpha.1`: selector multimarca persistente.
- `v1.0.0`: criterios de estabilidad documentados.
