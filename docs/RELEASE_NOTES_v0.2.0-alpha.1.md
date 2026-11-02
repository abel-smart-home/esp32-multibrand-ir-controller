# v0.2.0-alpha.1 — Primer control de aire acondicionado (Mirage Magnum 22)

**Tipo:** Pre-release experimental. **Estado:** funciones básicas confirmadas por el usuario en hardware real; pruebas adicionales pendientes.

## Cambios
- Se incorpora `firmware/ir_mirage_magnum22_v02.yaml` sin eliminar el YAML de laboratorio V0.1.
- Nueva entidad `climate` ESPHome con `midea_ir` para el Mirage Magnum 22 probado.
- Transmisor GPIO4, receptor GPIO14 invertido, alimentación IR GPIO21, según esta placa verificada mediante pruebas.
- Se reduce `dump: all` a `[midea, coolix]` para limitar el procesamiento y ruido de registros.
- Se configura OTA nativa cifrada mediante la clave API ya existente (`ota: encryption:`), sin contraseña OTA antigua.
- Se conserva el método OTA web con autenticación como alternativa local de recuperación. **Este canal usa HTTP, no está cifrado; no exponerlo a Internet.**
- Documentación y pruebas automáticas adicionales de configuración e instalación.

## Evidencia física aportada por el usuario
- El dispositivo ejecuta ESPHome y ya está integrado con Home Assistant.
- El protocolo Midea **encendió** el Mirage Magnum 22 desde Home Assistant.
- Los cambios de temperatura **suben y bajan** la consigna del minisplit.
- La orden **apagar** apagó el equipo.
- Pruebas pendientes: recepción y sincronización con mando original, modo calor (si aplica), ventilador, reinicio sin órdenes accidentales, estabilidad y OTA cifrada después de aplicar este cambio.

## Alcance y limitaciones
- Esta versión **no** es un controlador universal ni permite seleccionar marcas/modelos sin recompilar: eso está previsto en V0.3.
- `climate` muestra órdenes solicitadas e inferidas, no confirma el estado real de una unidad sin retorno.
- No contiene temperatura ambiental medida por sensor.
- No se incluye firmware `.bin` con credenciales privadas.
- Las compilaciones de CI utilizan exclusivamente claves de ejemplo.

## Antes de publicar
1. Subir los archivos a GitHub y revisar que las pruebas y compilaciones de **V0.1 y V0.2** finalicen correctamente.
2. Instalar por OTA cifrada la configuración actualizada de V0.2 y verificar reconexión.
3. Crear el tag `v0.2.0-alpha.1` sobre el commit aprobado y publicarlo como pre-release.
