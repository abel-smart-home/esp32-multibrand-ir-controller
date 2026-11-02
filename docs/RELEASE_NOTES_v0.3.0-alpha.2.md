# v0.3.0-alpha.2 — Catálogo de protocolos ampliado

**Tipo:** pre-release de pruebas. **No publicar hasta validar y compilar en CI.**

- Se elimina la opción duplicada `Mirage Magnum 22 - Midea`: el perfil verificado se denomina `Midea`.
- Cuatro nuevos motores experimentales: AUX (`aux`), Carrier (`carrier_mca`), Hisense (`hisense_aud`), Samsung (`samsung_aqv`) a través de `heatpumpir`.
- Cuatro marcas sin protocolo confirmado visibles para identificación: Mabe, Duventus, General Electric y York. **No transmiten IR**.
- Solo una entidad `climate` expuesta en Home Assistant; el perfil es persistente y seleccionable sin recompilar.
- `climate.template` deja de ser optimista para no mostrar órdenes de perfiles inexistentes como completadas.
- Se renombra el selector a `Perfil IR multimarca` para evitar reusar índices persistidos de un catálogo anterior; el primer arranque usa Midea.
- Wi-Fi, API cifrada, OTA cifrada y GPIO originales sin cambios.

**Verificación:** pruebas Python locales solamente; compilación ESPHome en GitHub Actions y prueba física pendientes.

**Nota:** las marcas no garantizan compatibilidad con todos sus modelos. No hay aprendizaje universal en esta revisión.
