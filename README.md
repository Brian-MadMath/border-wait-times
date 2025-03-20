# 🚦 Border Wait Times Scraper

Este proyecto recopila y procesa los tiempos de espera en las principales garitas de Tijuana, Mexicali y Tecate, obteniendo información cada 10 minutos mediante **GitHub Actions** desde Bordify y mostrándolos en un sitio web con **JavaScript**.

## 📌 Descripción

Este sistema cuenta con scrapers en **Python** que extraen los tiempos de espera de cada garita, detectan el estado del tráfico mediante colores (rojo, amarillo, verde) y clasifican los cruces como **vehiculares o peatonales**. La información se almacena en archivos JSON y se actualiza cada 10 minutos automáticamente.

Un script en **JavaScript** consume estos datos para mostrarlos dinámicamente en un sitio web.

## 🚀 Funcionalidad

- Extrae datos cada **10 minutos** desde Bordify.
- Identifica **tiempos de espera** para diferentes tipos de carriles (**General, Sentri, ReadyLane**).
- Detecta el estado del tráfico mediante **colores** (rojo, amarillo, verde).
- Clasifica cada cruce como **vehicular o peatonal**.
- Extrae el **icono** correspondiente (auto o peatón).
- Guarda los datos en archivos **JSON**.
- **Publica la información en un sitio web dinámico usando JavaScript.**

## 📂 Estructura del Proyecto

```
📦 border-wait-times
├── 📝 scraper-tijuana.py        # Scraper de Tijuana
├── 📝 scraper-mexicali.py       # Scraper de Mexicali
├── 📝 scraper-tecate.py         # Scraper de Tecate
├── 📝 scraper.yml              # GitHub Actions para ejecución automática
├── 📝 scraper.js               # Script en JavaScript para mostrar los datos en la web
├── 📝 webflow script.js         # Código para incrustar datos en Webflow
├── 📝 requirements.txt          # Dependencias necesarias
├── 📝 config.yml                # Configuración del scraper
├── 📝 wait-times-tijuana.json   # Datos de Tijuana
├── 📝 wait-times-mexicali.json  # Datos de Mexicali
├── 📝 wait-times-tecate.json    # Datos de Tecate
├── 📝 README.md                 # Documentación del proyecto
```

## 🛠 Instalación y Configuración

1. **Clonar el repositorio:**
   ```sh
   git clone https://github.com/tu_usuario/border-wait-times.git
   cd border-wait-times
   ```

2. **Instalar dependencias:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Ejecutar los scrapers manualmente:**
   ```sh
   python3 scraper-tijuana.py
   python3 scraper-mexicali.py
   python3 scraper-tecate.py
   ```

4. **Ejecutar el script en JavaScript localmente:**
   ```sh
   node scraper.js
   ```

5. **Ver los datos generados en JSON:**
   ```sh
   cat wait-times-tijuana.json
   ```

## 🖮 Ejemplo de Salida JSON

```json
{
    "Garita Otay Mesa": [
        {
            "tipo": "General",
            "tiempo": "2:24 horas",
            "líneas_abiertas": "2 líneas abiertas",
            "color": "red",
            "icono": "vehicular"
        },
        {
            "tipo": "Sentri",
            "tiempo": "18 minutos",
            "líneas_abiertas": "3 líneas abiertas",
            "color": "green",
            "icono": "vehicular"
        }
    ],
    "Ultima_actualizacion": "2025-03-20 14:43"
}
```

## 🌐 Funcionamiento del Script en JavaScript

El script `scraper.js` obtiene los datos desde los archivos JSON y los muestra en un sitio web. 
Si se usa con **Webflow**, se puede incrustar el archivo `webflow script.js`.

Ejemplo de ejecución manual:
```sh
node scraper.js
```

## 🔄 Automatización con GitHub Actions

El script `scraper.yml` ejecuta los scrapers **cada 10 minutos** de forma automática y actualiza los archivos JSON en el repositorio.

```yaml
on:
  schedule:
    - cron: '*/10 * * * *'  # Ejecuta cada 10 minutos
  workflow_dispatch: {}  # Permite ejecución manual
```

## 🔍 Tecnologías Utilizadas

- **Python** 🐍
- **JavaScript (Node.js)** 📝
- **Selenium** 🌐
- **Puppeteer** 🤖
- **WebDriver Manager** 🚗
- **YAML** 📝
- **JSON** 📊
- **GitHub Actions** 🔄

## 🛠 Mantenimiento y Errores

Si encuentras errores, verifica lo siguiente:
- **El sitio Bordify está activo** y su estructura HTML no ha cambiado.
- **El WebDriver está actualizado:**
  ```sh
  pip install -U webdriver-manager
  ```
- **Las dependencias están instaladas correctamente.**
- **Para el script en JavaScript, asegúrate de tener Node.js instalado:**
  ```sh
  node -v
  ```

## 📩 Contacto

Si tienes preguntas o mejoras, contáctanos en [tu_email@example.com](mailto:tu_email@example.com).

📌 **Desarrollado por:** _MadMath Agency_ 🚀

