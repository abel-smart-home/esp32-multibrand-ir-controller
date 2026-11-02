# Instalación de v0.3.0-alpha.2

1. Subir los archivos modificados al repositorio GitHub (`firmware/ir_multimarca_v03.yaml`, `tests/test_v03.py`, `docs/`).
2. Ejecutar GitHub Actions; revisar **Validar V0.3 multimarca** y **Compilar V0.3 multimarca**; **no instalar antes de aprobar la compilación**.
3. En ESPHome Device Builder, guardar copia del YAML de la V0.3 actual y pegar el firmware nuevo conservando secretos.
4. Ejecutar **Validate → Install → Wirelessly** sobre el dispositivo ya existente.
5. La nueva entidad del selector se llama `Perfil IR multimarca`; elegir `Midea` y comprobar frío 24 °C y OFF con el Mirage Magnum 22.
6. Probar reinicio: el perfil elegido debe persistir. No debe transmitirse ninguna orden durante el reinicio.
7. Elegir `Mabe (sin protocolo confirmado)` y tratar de enviar frío: el controlador debe registrar una advertencia y **no emitir IR**; regresar a Midea.
8. Si la compilación falla por recursos/flash o problemas con HeatpumpIR, mantener el firmware V0.3 anterior y compartir los errores; no forzar OTA ni publicar release.

**Advertencia de migración:** el antiguo selector `Perfil infrarrojo` puede quedar obsoleto en Home Assistant. El nuevo selector usa un identificador diferente para evitar índices persistidos incompatibles, comenzando en Midea.
