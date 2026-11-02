# Historial de cambios

## [0.2.0-alpha.1] - Pendiente de publicar

### Añadido
- Entidad `climate` con `midea_ir` para prueba del Mirage Magnum 22.
- Recepción limitada a Midea y Coolix para reducir logs excesivos.
- Cifrado obligatorio para OTA nativa usando la clave API existente.
- Plan de pruebas V0.2 y validación automatizada de ambos firmware.

### Validación en hardware
- Confirmados encendido, aumento/reducción de consigna y apagado desde Home Assistant.
- Pendientes sincronización con control original, recuperación tras reinicio y comprobación de OTA cifrada.

## [0.1.0-alpha.1] - 2026-10-31

### Añadido

- Configuración ESPHome de laboratorio para validar el módulo ESP32 IR.
- Pinout provisional GPIO21/4/14, logs de recepción y botón NEC de prueba.
- API cifrada, OTA, web autenticada, AP de rescate y diagnósticos.
- Generador local de claves y exclusión de secretos en Git.
- Documentación de instalación, arquitectura, plan de pruebas, commits y publicación.
- Validaciones automáticas de configuración y estructura mediante GitHub Actions.

### Pendiente

- Compilación y ensayos en el dispositivo real; aún no existe `climate` ni control multimarca.

## [0.2.0-alpha.1] - Candidato no publicado (2026-11-01)

### Agregado
- Nuevo firmware opcional de prueba Mirage Magnum 22 con `midea_ir` y entidad `climate`.
- Recepción optimizada para Midea y Coolix, y pruebas de climatización específicas.
- Ampliación de CI para validar y compilar ambas configuraciones, pendiente de ejecución en GitHub.

### Pendiente
- Validación física de encendido, apagado, cambio de temperatura y sincronización del control original.
- Selección multimarca persistente para V0.3.
