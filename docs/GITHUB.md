# Publicar el proyecto en GitHub (Windows/PowerShell)

Repositorio sugerido: `abel-smart-home/esp32-multibrand-ir-controller`. Este documento no presupone que el repositorio ya existe.

## 1. Crear repositorio vacío

1. Abre https://github.com/new e inicia sesión.
2. Owner: tu cuenta `abel-smart-home` (si ese es el nombre que aparece en tu cuenta; si es organización, selecciónala).
3. Repository name: `esp32-multibrand-ir-controller`.
4. Description: `Controlador IR multimarca ESP32 + Home Assistant (fase de validación de hardware)`.
5. Público o privado, como prefieras.
6. **No marques** añadir README, `.gitignore` o licencia: ya vienen en el ZIP.
7. Create repository.

## 2. Preparar archivos

- Extrae el ZIP. Abre PowerShell dentro de la carpeta raíz que contiene `README.md`.
- No cargues el ZIP como un único archivo: GitHub debe mostrar `README.md`, `firmware/`, `docs/` y `.github/` como archivos/carpetas.
- **NO ejecutes el generador de secretos antes de subir archivos**; aunque `secrets.yaml` está en `.gitignore`, evita cualquier riesgo de arrastre manual.

## 3. Realizar tres commits organizados

Instala Git para Windows si aún no está disponible, luego ejecuta:

```powershell
git init -b main
git config user.name "Tu nombre o alias"
git config user.email "tu-correo-de-commits@ejemplo.com"

git add README.md CHANGELOG.md CONTRIBUTING.md LICENSE .gitignore docs/
git commit -m "docs: iniciar proyecto y documentar la validacion IR"

git add firmware/ tools/
git commit -m "feat: agregar firmware ESPHome de laboratorio IR v0.1"

git add tests/ .github/
git commit -m "ci: agregar pruebas y validacion automatica ESPHome"

git remote add origin https://github.com/abel-smart-home/esp32-multibrand-ir-controller.git
git push -u origin main
```

**Nota:** remplaza nombre, correo de Git y `abel-smart-home` si tu propietario real es otro. El correo puede ser el privado `noreply` de GitHub. Iniciar sesión para `git push` puede pedir autenticación mediante navegador o gestor de credenciales, no la contraseña normal de GitHub.

## 4. Verificar que Actions termine correctamente

1. Abre la pestaña `Actions` > `Verificar firmware y repositorio`.
2. Revisa los tres pasos: Python, pruebas de estructura y validación ESPHome.
3. Si hay un fallo de compatibilidad o sintaxis, **no publiques una versión estable**; corrige, haz otro commit y repite. Las pruebas del repositorio no sustituyen las pruebas en hardware.

## 5. Crear la etiqueta de la versión alfa

Solo después de que el commit y la validación de GitHub Actions estén correctos:

```powershell
git tag -a v0.1.0-alpha.1 -m "Primera alpha: pruebas de hardware IR"
git push origin v0.1.0-alpha.1
```

## 6. Publicar pre-release

1. Abre `Releases` > `Draft a new release` (o https://github.com/abel-smart-home/esp32-multibrand-ir-controller/releases/new).
2. `Choose a tag`: `v0.1.0-alpha.1` (el tag ya se publicó).
3. Release title: `v0.1.0-alpha.1 — Validación inicial del ESP32 IR`.
4. Copia el texto de `docs/RELEASE_NOTES_v0.1.0-alpha.1.md` en Description.
5. Marca **Set as a pre-release**.
6. No adjuntes `.bin` compilados que contienen credenciales ni `secrets.yaml`. GitHub genera automáticamente archivos fuente ZIP/TAR.
7. Pulsa `Publish release`.

### ¿Cuándo se crea `v0.1.0` estable?

Cuando compruebes en tu unidad física Wi-Fi, recepción IR, emisión IR y OTA y anotes los resultados en `docs/PRUEBAS.md`. Haz commits de los cambios probados, etiqueta `v0.1.0` en ese commit y publica un **release normal** sin marcar prerelease. Si fallan pruebas, sigue con `v0.1.0-alpha.2`.

## Alternativa: solo navegador

Si no quieres usar Git, puedes subir las carpetas y archivos desde `Add file` > `Upload files` en el repositorio vacío. Confirma que incluya `.github/workflows/validate.yml` y que respete directorios. GitHub hará un commit inicial de la carga y entonces puedes crear tag y pre-release desde Releases con `Create new tag`. La ruta por Git es preferible si deseas **tres commits separados** desde el inicio.

Documentación oficial: https://docs.github.com/es/repositories/creating-and-managing-repositories/creating-a-new-repository y https://docs.github.com/es/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
