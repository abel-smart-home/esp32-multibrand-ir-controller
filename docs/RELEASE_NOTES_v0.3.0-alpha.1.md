# v0.3.0-alpha.1 — Selector IR multimarca persistente (experimental)

**Tipo:** Pre-release. **NO PUBLICAR todavía hasta que GitHub Actions valide/compile y se hagan las pruebas acordadas.**

## Incluye
- Primera selección de perfiles desde Home Assistant con `select` persistente en flash, sin recompilar entre perfiles incluidos.
- Una sola entidad `climate` visible que envía órdenes al motor IR seleccionado.
- 7 opciones para 6 motores: Mirage Magnum 22 / Midea validado para encendido, temperatura y apagado; Midea genérico, Coolix, Gree genérico, LG genérico, Daikin genérico y Mitsubishi genérico experimentales.
- Selector y reinicio sin comandos IR automáticos.
- Modo frío, apagado y temperatura objetivo como funciones iniciales.
- Diagnósticos, API cifrada, OTA y Wi-Fi existentes conservados.
- YAML V0.2 intacto como alternativa de recuperación.

## Verificaciones
- Pruebas estáticas locales: pendiente documentar resultado.
- GitHub Actions `config` y `compile` ESPHome: pendiente de ejecutar en `main`.
- Compatibilidad física con Mirage usando el nuevo router: pendiente de probar.
- Compatibilidad física de los demás motores: **no probada**.

## Restricciones
- No existe garantía multimarca universal.
- No se sincronizan automáticamente las órdenes del control remoto original con el clima público.
- No controla calefacción, velocidad ni oscilación todavía.
- Cambiar de perfil nunca envía `OFF` al equipo anterior. Apagar el equipo original **antes** de cambiar.
- El estado en HA es estimado, no confirmado.
- No se distribuyen claves privadas ni firmware binario personal.

## Siguiente paso
Subir la actualización a `main`, ejecutar GitHub Actions, actualizar el ESP32 por OTA y completar `docs/PRUEBAS_V03.md` antes de publicar el pre-release.
