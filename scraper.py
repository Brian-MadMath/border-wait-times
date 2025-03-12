from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import json

# Especificar ruta de ChromeDriver
CHROMEDRIVER_PATH = "/usr/local/bin/chromedriver"

# Configurar Selenium con ChromeDriver
service = Service(CHROMEDRIVER_PATH)
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

# Mostrar resultados organizados en la terminal
print(json.dumps(datos_garitas, indent=4, ensure_ascii=False))

# Mostrar los errores al final, si los hay
if errores:
    print("\n❌ Errores encontrados durante la ejecución:")
    for error in errores:
        print("-", error)
else:
    print("\n✅ Script finalizado sin errores.")


from datetime import datetime

# Obtener la fecha y hora actual en formato legible
fecha_actualizacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Agregar la fecha de última actualización al JSON
datos_garitas["ultima_actualizacion"] = fecha_actualizacion

# Guardar el JSON con la información y la fecha de actualización
with open("wait-times.json", "w", encoding="utf-8") as file:
    json.dump(datos_garitas, file, indent=4, ensure_ascii=False)

print(f"\n📂 Datos guardados en 'wait-times.json'")
print(f"🕒 Última actualización: {fecha_actualizacion}")
print(f"\n")
