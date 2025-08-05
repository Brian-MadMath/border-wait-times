from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
from datetime import datetime
import pytz

# Configurar Selenium con WebDriver Manager
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")  # más compatible en Chrome reciente
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = "/usr/bin/google-chrome"  # 👈 ESTA ES LA LÍNEA NUEVA
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                      (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")


driver = webdriver.Chrome(service=service, options=options)

# URL de Bordify (Página con todas las garitas de Tijuana)
URL = "https://bordify.com/?city=tijuana"
driver.get(URL)

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bg-white.shadow.rounded"))
    )
    secciones_garitas = driver.find_elements(By.CLASS_NAME, "bg-white.shadow.rounded")

except Exception as e:
    print("❌ No se pudo cargar el contenido esperado.")
    driver.save_screenshot("screenshot.png")
    driver.quit()
    raise e



# Diccionario para guardar los tiempos de espera organizados por garita
datos_garitas = {}
errores = []

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bg-white.shadow.rounded"))
    )
except Exception as e:
    print("⚠️ ERROR: No se encontró el elemento esperado.")
    driver.save_screenshot("screenshot.png")
    print("📸 Screenshot guardado como screenshot.png")
    driver.quit()
    raise e  # relanza el error para que el workflow falle


for seccion in secciones_garitas:
    try:
        nombre_garita = seccion.find_element(By.CLASS_NAME, "text-base.md\\:text-lg.leading-6.font-medium.text-gray-900").text.replace("Desde", "").strip()
        datos_garitas[nombre_garita] = []

        # 🔹 Buscar los bloques de cruce en la sección (donde están juntos color, icono y datos)
        bloques_cruce = seccion.find_elements(By.CLASS_NAME, "flex.py-4.px-2.sm\\:px-4.items-center.space-x-3")

        for bloque in bloques_cruce:
            try:
                color = "gray"  # Default
                icono = "desconocido"  # Default

                # 🔹 Extraer el color desde el div correspondiente  
                try:
                    icon_div = bloque.find_element(By.CSS_SELECTOR, "div.inline-block.relative div.h-14.w-14.rounded-full")
                    class_list = icon_div.get_attribute("class")

                    print(f"🔍 Clases encontradas en {nombre_garita}: {class_list}")

                    if "bg-red-500" in class_list or "bg-red-400" in class_list:
                        color = "red"
                    elif "bg-yellow-500" in class_list or "bg-yellow-400" in class_list:
                        color = "yellow"
                    elif "bg-emerald-500" in class_list or "bg-green-500" in class_list or "bg-green-400" in class_list:
                        color = "green"

                except Exception as e:
                    errores.append(f"Error obteniendo color en {nombre_garita}: {e}")

           
                # 🔹 Extraer el icono (vehicular o peatonal)
                try:
                    # Primero encontrar el contenedor padre
                    icon_parent = bloque.find_element(By.CLASS_NAME, "inline-block.relative")
    
                    # Luego buscar dentro del contenedor el div del icono
                    icon_div = icon_parent.find_element(By.CLASS_NAME, "rounded-full")
    
                    # Verificar el título del div para determinar el tipo de icono
                    title_text = icon_div.get_attribute("title").lower()  # Obtener el atributo "title"

                    if "peatonal" in title_text:
                        icono = "peatonal"
                    elif "vehicular" in title_text:
                        icono = "vehicular"
                    else:
                        icono = "desconocido"

                except Exception as e:
                    errores.append(f"Error obteniendo icono en {nombre_garita}: {e}")



                # 🔹 Extraer datos del cruce desde el div correspondiente
                try:
                    info_div = bloque.find_element(By.CLASS_NAME, "flex-1.min-w-0")
                    tipo = info_div.find_element(By.CLASS_NAME, "text-sm.text-gray-900.truncate").text.strip()
                    tiempo = info_div.find_element(By.CLASS_NAME, "text-lg.font-medium.text-gray-900.leading-6").text.strip()
                    lineas = info_div.find_element(By.CLASS_NAME, "text-sm.text-gray-500.truncate").text.strip()
                except:
                    tipo, tiempo, lineas = "No disponible", "No disponible", "No disponible"

                # Guardar los datos estructurados
                datos_garitas[nombre_garita].append({
                    "tipo": tipo,
                    "tiempo": tiempo,
                    "líneas_abiertas": lineas,
                    "color": color,
                    "icono": icono
                })

            except Exception as e:
                errores.append(f"Error al procesar cruce en {nombre_garita}: {e}")

    except Exception as e:
        errores.append(f"Error al extraer datos de {nombre_garita}: {e}")

# Cerrar Selenium
driver.quit()

# Agregar timestamp al JSON
zona_horaria_tijuana = pytz.timezone("America/Tijuana")
fecha_actualizacion = datetime.now(zona_horaria_tijuana).strftime("%Y-%m-%d %H:%M")

datos_garitas["Ultima_actualizacion"] = fecha_actualizacion
with open("wait-times-tijuana.json", "w", encoding="utf-8") as file:
    json.dump(datos_garitas, file, indent=4, ensure_ascii=False)

print("\n📊 Datos de tiempos de espera:")
print(json.dumps(datos_garitas, indent=4, ensure_ascii=False))
print(f"\n📂 Datos guardados en 'wait-times-tijuana.json'")
print(f"🕒 Última actualización: {fecha_actualizacion}")
print(f"✅ Script finalizado sin errores." if not errores else f"❌ Errores encontrados:\n" + "\n".join(errores))
