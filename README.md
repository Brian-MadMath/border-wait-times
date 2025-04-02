Claro, aquí tienes la versión en inglés de tu README traducida y adaptada correctamente:

---

# 🚦 Border Wait Times Scraper

This project collects and processes wait times for the main ports of entry in **Tijuana, Mexicali, and Tecate**, fetching data every 10 minutes using **GitHub Actions** from Bordify and displaying them dynamically with **JavaScript**.

## 📌 Description

The system uses **Python scrapers** to extract wait times from each crossing, detect traffic status by **color** (red, yellow, green), and classify lanes as **vehicular or pedestrian**. All data is saved in JSON format and updated automatically every 10 minutes.

A **JavaScript script** consumes this data to display it dynamically on a website.

## 🚀 Features

- Fetches data every **10 minutes** from Bordify.
- Detects **wait times** for different lane types (**General, Sentri, ReadyLane**).
- Detects traffic status using **colors** (red, yellow, green).
- Classifies each crossing as **vehicular or pedestrian**.
- Extracts the appropriate **icon** (car or pedestrian).
- Stores the information in **JSON** files.
- **Displays the data dynamically using JavaScript.**

## 🛠 Installation & Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your_username/border-wait-times.git
   cd border-wait-times
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the scrapers manually:**
   ```sh
   python3 scraper-tijuana.py
   python3 scraper-mexicali.py
   python3 scraper-tecate.py
   ```

4. **Run the JavaScript script locally:**
   ```sh
   node scraper.js
   ```

5. **View the generated JSON output:**
   ```sh
   cat wait-times-tijuana.json
   ```

## 🖮 Example JSON Output

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

## 🌐 JavaScript Script Functionality

The `scraper.js` file reads the JSON data and renders it on a website.  
If used with **Webflow**, you can embed the `webflow script.js` file.

Manual execution:
```sh
node scraper.js
```

## 🔄 GitHub Actions Automation

The `scraper.yml` workflow runs every **10 minutes** and updates the JSON files automatically.

```yaml
on:
  schedule:
    - cron: '*/10 * * * *'  # Runs every 10 minutes
  workflow_dispatch: {}     # Allows manual execution
```

## 🔍 Tech Stack

- **Python** 🐍  
- **JavaScript (Node.js)** 📝  
- **Selenium** 🌐  
- **Puppeteer** 🤖  
- **WebDriver Manager** 🚗  
- **YAML** 📝  
- **JSON** 📊  
- **GitHub Actions** 🔄  

## 🛠 Troubleshooting

If you run into errors, check the following:
- **Bordify is online** and its HTML structure hasn't changed.
- **WebDriver is up to date:**
  ```sh
  pip install -U webdriver-manager
  ```
- **All dependencies are properly installed.**
- **Node.js is installed for the JavaScript script:**
  ```sh
  node -v
  ```

## 📩 Contact

For questions or suggestions, contact us at [brian@madandmath.com](mailto:brian@madandmath.com).

📌 **Developed by:** _[MadMath Creative Studio](https://www.madandmath.com/) 🚀_

---

¿Quieres que lo suba directo al `README.md` del repo?
