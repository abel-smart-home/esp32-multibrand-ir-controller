# Pruebas V0.2 — Mirage Inverter Magnum 22

Se registran las observaciones reportadas por el usuario después de instalar la V0.2 en la placa real. Los ensayos no observados **no** se consideran aprobados.

| ID | Prueba | Estado |
|---|---|---|
| AC-01 | El YAML V0.2 valida y compila localmente | **Reportado funcionando** en ESPHome Device Builder; falta validar el commit en CI |
| AC-02 | OTA V0.2 instalado y el ESP32 reconecta | **Reportado funcionando**; falta comprobar la migración a OTA cifrada |
| AC-03 | Aparece entidad `climate` en Home Assistant | **Confirmado por uso** del control |
| AC-04 | El receptor decodifica una trama del mando original con V0.2 | Pendiente de comprobar |
| AC-05 | Encender desde Home Assistant | **Confirmado** por el usuario |
| AC-06 | Subir y bajar consigna desde Home Assistant | **Confirmado** por el usuario |
| AC-07 | Apagar desde Home Assistant | **Confirmado** por el usuario |
| AC-08 | Control original actualiza estado mostrado en HA | Pendiente de comprobar |
| AC-09 | Reiniciar sin transmitir órdenes IR involuntarias | Pendiente de comprobar |
| AC-10 | Estabilidad sin avisos recurrentes / desconexiones | Pendiente de comprobar |
| AC-11 | OTA nativa cifrada con clave API | Pendiente de comprobar después de actualizar |

## Validación de seguridad OTA

ESPHome 2026.9+ permite exigir OTA cifrada con la clave que ya utiliza `api.encryption`. La imagen actualizada usa:

```yaml
ota:
  - platform: esphome
    encryption:
  - platform: web_server
```

Antes de probar, conservar la clave API actual y un respaldo del YAML anterior. Tras instalar con **Install → Wirelessly**, confirmar en logs `Encryption: required`. No sustituir la clave API en medio de la migración. El portal web sigue permitiendo OTA por HTTP con autenticación y se mantiene **solo** para recuperación en la LAN.

## Próximos pasos de protocolo

Validar `fan_mode`, swing, modos de calor (según variante) y sincronización del control remoto. Anotar nombres y respuestas reales en el mismo plan de pruebas.
