# Plan de pruebas de V0.1

Marca cada caso después de ejecutarlo en **tu placa real**, nunca solo por compilar.

| ID | Prueba | Criterio de aceptación | Resultado |
| --- | --- | --- | --- |
| HW-01 | Arranque sin errores | Inicia y muestra logs | Pendiente |
| HW-02 | Wi-Fi 2.4 GHz | Se asocia y mantiene IP | Pendiente |
| HW-03 | Descubrimiento HA | Dispositivo y diagnósticos visibles | Pendiente |
| HW-04 | GPIO21 | Circuito IR recibe alimentación | Pendiente |
| HW-05 | Receptor | Logs cambian al pulsar mando original | Pendiente |
| HW-06 | Emisor | NEC de laboratorio sale físicamente por LED IR | Pendiente |
| HW-07 | Reinicio | Vuelve solo a Wi-Fi y Home Assistant | Pendiente |
| HW-08 | OTA | Actualización a otra compilación de prueba sin cable | Pendiente |
| HW-09 | Rescate Wi-Fi | AP disponible con red principal ausente | Pendiente |
| HW-10 | Seguridad | Se exigen credenciales API/web/OTA | Pendiente |

## Registro de prueba

- Fecha:
- Fotos de ambos lados de la PCB (sin datos privados):
- Revisión de la placa (si figura):
- Versión ESPHome:
- IP local (no compartir públicamente si no es necesario):
- Aire acondicionado de prueba: marca/modelo:
- Control remoto: marca/modelo:
- Logs relevantes (redactados):
- Fallas y recuperación:

## Criterio de salida

V0.1 no será versión estable hasta superar pruebas HW-01 a HW-08 en la placa real, y documentar cualquier limitación de HW-09/10. Incluso superadas, **no significa compatibilidad multimarca**.
