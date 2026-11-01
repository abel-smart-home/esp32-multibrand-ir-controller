# Instalación, primer flasheo y recuperación

> La primera carga del firmware todavía no está comprobada sobre la tarjeta concreta. No conectar señales de 5 V a GPIO.

## 1. Preparar secretos y firmware

En el PC, con el repositorio descomprimido:

```powershell
python tools/generar_secrets.py
```

Después edita `firmware/secrets.yaml`: reemplaza `wifi_ssid` y `wifi_password`. El generador ya crea claves aleatorias para la API, OTA, AP de rescate y portal web. El archivo está excluido de Git.

En Home Assistant > **ESPHome Device Builder**:

1. Crea un nuevo dispositivo ESP32 clásico (placa `esp32dev`).
2. Abre su editor YAML y pega el contenido de `firmware/ir_multimarca_lab.yaml`.
3. Abre el archivo `secrets.yaml` de **ese mismo Device Builder**, y añade allí las claves de tu archivo local `firmware/secrets.yaml` (o coloca ambos archivos en el mismo directorio si compilas con CLI). No publiques ninguna captura de las claves.
4. Valida la configuración (Validate / Check configuration). Compila (Install > Manual download / Download firmware binary) sin instalar todavía.

Por CLI en un equipo con ESPHome instalado, desde el repositorio:

```powershell
esphome config firmware/ir_multimarca_lab.yaml
esphome compile firmware/ir_multimarca_lab.yaml
```

La compilación necesita ESPHome 2026.10.1 o una versión posterior que mantenga compatibilidad con los componentes incluidos.

## 2. Primera programación: portal del fabricante, solo si aparece

Para algunas unidades publicadas de ESP32E-N4 se ha documentado:

1. Alimentar por USB-C (puede no ser interfaz de datos).
2. Buscar la red Wi-Fi original `IR_WIFI` o `IR-WIFI`.
3. **No introducir las credenciales del Wi-Fi doméstico en el firmware de fábrica antes de inspeccionar su método de actualización.** Un usuario describió pérdida del portal tras cambiar la red.
4. Si aparece el AP, conectarse y entrar a `http://192.168.4.1/`.
5. Buscar la sección `Update` del fabricante. Desde ESPHome Device Builder, descargar la variante **OTA Update**, no **Factory Image**; en esa revisión el portal de fábrica aceptó ese formato.
6. Subir `.bin` OTA y observar el reinicio. Si el portal rechaza la imagen, **detenerse**: no repetir archivos desconocidos ni forzar el proceso. Confirmar la variante de placa y el método de recovery antes de continuar.
7. Una vez en ESPHome, el equipo debe conectarse al Wi-Fi indicado y quedar disponible para integración en HA; anotar su IP.

Estas instrucciones provienen de la comunidad y **no garantizan** que tu firmware de fábrica tenga el mismo portal ni acepte el mismo formato.

Fuente: https://community.home-assistant.io/t/solution-esp32-infrared-wifi-module-esp32e-n4-infrared-transmitter-receiver-correct-pinout-for-esphome/1003067

## 3. Si el portal original no funciona

- No asumir que USB-C sirve para flashear: en revisiones similares es solo alimentación.
- Se puede requerir USB-UART de lógica 3.3 V conectado a RX/TX, GND e IO0/BOOT con un procedimiento de arranque serial específico. Antes de conectar, identificar físicamente el esquema/revisión. No improvisar puentes permanentes entre pines.
- Conservar acceso a la placa para una recuperación física. Evitar una instalación empotrada hasta completar las pruebas OTA.

## 4. Añadir a Home Assistant

En **Ajustes > Dispositivos y servicios**, integrar el equipo detectado por ESPHome (o añadirlo por IP). Si la integración solicita clave, usa `api_encryption_key` privada, sin publicarla.

Entidades esperadas: `Enviar IR de prueba (NEC)`, `Reiniciar controlador IR`, `Dispositivo en línea`, `Señal Wi-Fi`, `Tiempo encendido`, `Dirección IP`, `Versión ESPHome` (el prefijo del dispositivo y los IDs pueden variar).

## 5. Comprobar recepción y transmisión

1. Ve a los **LOGS** del dispositivo en ESPHome y acerca el control remoto original a 20-50 cm del receptor negro.
2. Presiona encendido o cambia la temperatura del control. Deben aparecer códigos reconocidos o tramas `raw` / de protocolo desconocido. Si no aparece nada, revisa GPIO14 y GPIO21.
3. Apunta el emisor transparente hacia un receptor IR de prueba o, como verificación orientativa, observa con una cámara que sea sensible al infrarrojo.
4. Desde Home Assistant pulsa deliberadamente **Enviar IR de prueba (NEC)**. Es un código genérico de laboratorio; **no apaga ni enciende intencionalmente el A/C**.
5. Comprueba el funcionamiento real del transmisor con equipo IR externo si está disponible: que el registro de envío aparezca no significa que la luz IR llegó a su destino.
6. Reinicia, comprueba reconexión y realiza una actualización OTA normal desde ESPHome o la página web local.

## 6. Seguridad de OTA

- La web usa autenticación HTTP básica. Opera solo en la LAN/VLAN de confianza; las claves pueden viajar en claro sobre HTTP. Evita exponer el puerto 80 a Internet.
- OTA nativa usa contraseña configurada; API de ESPHome, una clave de cifrado independiente.
- Para actualizaciones normales prefiere ESPHome Device Builder (OTA nativa); reserva la web para diagnóstico/local.
- Nunca subir `secrets.yaml`, volcados que contengan contraseñas o `.bin` con las credenciales personales al repositorio público ni al pre-release.

Referencias: https://esphome.io/components/ota/web_server/ y https://esphome.io/components/ota/esphome/
