from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # Importar WebDriver Manager
import time
import json

# Configurar Selenium con WebDriver Manager
service = Service(ChromeDriverManager().install())  # Descarga e instala automáticamente el driver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=service, options=options)

# URL de Bordify (Página con todas las garitas de Tijuana)
URL = "https://bordify.com/?city=tijuana"
driver.get(URL)

# Esperar que la página cargue completamente
time.sleep(5)

# Diccionario para guardar los tiempos de espera organizados por garita
datos_garitas = {}
errores = []  # Lista para almacenar los errores

# Buscar todas las secciones de garitas en la página
secciones_garitas = driver.find_elements(By.CLASS_NAME, "bg-white.shadow.rounded")

for seccion in secciones_garitas:
    try:
        # Extraer nombre de la garita y limpiar espacios innecesarios
        nombre_garita = seccion.find_element(By.CLASS_NAME, "text-base.md\\:text-lg.leading-6.font-medium.text-gray-900").text.replace("Desde", "").strip()
        datos_garitas[nombre_garita] = []

        # Buscar los bloques de cruce dentro de la garita
        bloques_cruce = seccion.find_elements(By.CLASS_NAME, "focus\\:outline-none")

        for cruce in bloques_cruce:
            try:
                tipo = cruce.find_element(By.CLASS_NAME, "text-sm.text-gray-900.truncate").text.strip()
            except Exception as e:
                tipo = "No disponible"
                errores.append(f"Error obteniendo tipo en {nombre_garita}: {e}")

            try:
                tiempo = cruce.find_element(By.CLASS_NAME, "text-lg.font-medium.text-gray-900.leading-6").text.strip()
            except Exception as e:
                tiempo = "No disponible"
                errores.append(f"Error obteniendo tiempo en {nombre_garita}: {e}")

            try:
                lineas = cruce.find_element(By.CLASS_NAME, "text-sm.text-gray-500.truncate").text.strip()
            except Exception as e:
                lineas = "No disponible"
                errores.append(f"Error obteniendo líneas abiertas en {nombre_garita}: {e}")

            datos_garitas[nombre_garita].append({
                "tipo": tipo,
                "tiempo": tiempo,
                "líneas_abiertas": lineas
            })
    except Exception as e:
        errores.append(f"Error al extraer datos de {nombre_garita}: {e}")

# Cerrar Selenium
driver.quit()

# Agregar timestamp al JSON
from datetime import datetime
import pytz

# Definir la zona horaria de Tijuana
zona_horaria_tijuana = pytz.timezone("America/Tijuana")

# Obtener la hora actual en la zona horaria correcta
fecha_actualizacion = datetime.now(zona_horaria_tijuana).strftime("%Y-%m-%d %H:%M:%S")


# Imprimir los datos guardados en la terminal de manera legible
print("\n📊 Datos de tiempos de espera:")
print(json.dumps(datos_garitas, indent=4, ensure_ascii=False))


# Guardar datos en JSON

datos_garitas["Ultima_actualizacion"] = fecha_actualizacion
with open("wait-times-tijuana.json", "w", encoding="utf-8") as file:
    json.dump(datos_garitas, file, indent=4, ensure_ascii=False)

print(f"\n📂 Datos guardados en 'wait-times-tijuana.json'")
print(f"🕒 Última actualización: {fecha_actualizacion}")
print(f"✅ Script finalizado sin errores." if not errores else f"❌ Errores encontrados:\n" + "\n".join(errores))
