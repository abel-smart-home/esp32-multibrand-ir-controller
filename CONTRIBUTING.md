# Colaboración

1. Abre un Issue describiendo la revisión exacta de hardware, marca/modelo de aire y logs redactados.
2. Crea una rama `feature/nombre` o `fix/nombre` desde `main`.
3. Cambia firmware, pruebas y documentación en el mismo PR cuando corresponda.
4. Verifica `python -m unittest discover -s tests -v` y `esphome config firmware/ir_multimarca_lab.yaml` con secretos locales.
5. No publiques claves, logs sensibles, firmware con credenciales, ni afirmes compatibilidad con modelos no probados.
6. Conserva una nota de licencia antes de incorporar bibliotecas de terceros.

Las primeras contribuciones deben centrarse en V0.1: compilación, pinout y pruebas de RX/TX reales.
