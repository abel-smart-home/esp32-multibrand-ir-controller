# Plan de pruebas V0.3 (selector dinámico)

**Estado:** candidato `v0.3.0-alpha.1`, NO verificado todavía en ESP32 real.

| ID | Prueba | Resultado |
| --- | --- | --- |
| V03-01 | `esphome config` correcto | Pendiente CI |
| V03-02 | `esphome compile` sin errores ni flash insuficiente | Pendiente CI |
| V03-03 | OTA sobre el mismo ESP32 V0.2 y reconexión con HA | Pendiente |
| V03-04 | Una sola entidad `climate` visible, seis motores ocultos | Pendiente |
| V03-05 | Selector inicia con Mirage/Midea si no tiene valor previo | Pendiente |
| V03-06 | En el perfil Mirage/Midea encender, 24→23→25 °C y apagar | Pendiente |
| V03-07 | Seleccionar otro perfil con aire apagado **no envía IR** | Pendiente |
| V03-08 | Reiniciar y confirmar que selector mantiene perfil | Pendiente |
| V03-09 | Reiniciar y confirmar que no transmite ninguna orden IR | Pendiente |
| V03-10 | Tras elegir perfil nuevo, frontend comienza en OFF (sin apagar físicamente otro A/C) | Pendiente |
| V03-11 | Botón «Probar perfil: frío 24 °C» transmite solo al presionarlo | Pendiente |
| V03-12 | Regresar a Mirage/Midea y comprobar control funcional | Pendiente |
| V03-13 | OTA nativa cifrada y portal local de recuperación | Pendiente |

## Recomendaciones de seguridad

- Mantener despejado el campo del IR mientras se prueban perfiles no verificados.
- Para cambiar entre aires reales, **apagar primero el aire anterior** desde su perfil correspondiente. Cambiar el selector NO envía OFF.
- Perfiles Gree, LG, Daikin, Mitsubishi y Coolix son propuestas genéricas y pueden no responder a algunos modelos. No declarar soporte verificado sin prueba.
- Si V0.3 no compila o el Mirage deja de funcionar, conservar y reinstalar `firmware/ir_mirage_magnum22_v02.yaml` desde Device Builder vía OTA.
- No compartir `secrets.yaml` ni binarios compilados con credenciales reales.

## Registro

- Modelo ESP32 / revisión:
- Versión ESPHome:
- Resultado CI (enlace):
- Wi-Fi y OTA:
- Versión V0.3 instalada:
- Pruebas sobre Mirage:
- Perfil restaurado tras apagar/encender:
- Ausencia de IR al reinicio y al cambiar perfil:
- Fallos y logs (sin credenciales):
