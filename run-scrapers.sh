#!/bin/bash
set -e

echo "🚀 Iniciando ejecución local del workflow..."

# 1. Instalar Google Chrome manualmente si no existe
if ! command -v google-chrome &> /dev/null; then
  echo "🔧 Instalando Google Chrome..."
  wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  sudo apt update
  sudo apt install -y ./google-chrome-stable_current_amd64.deb
fi

# 2. Instalar dependencias de Python
echo "🐍 Instalando dependencias de Python..."
pip install --upgrade pip
pip install -r requirements.txt
pip install selenium webdriver-manager

# 3. Ejecutar scrapers
echo "📡 Ejecutando scrapers..."
python scraper-tijuana.py
python scraper-tecate.py
python scraper-mexicali.py

# 4. Hacer commit y push si hay cambios
echo "💾 Haciendo commit y push..."
git config --global user.name "github-actions"
git config --global user.email "actions@github.com"
git add wait-times-*.json
git commit --allow-empty -m "🔄 Actualización automática local: $(date +'%Y-%m-%d %H:%M')" || echo "Sin cambios"
git push

echo "✅ Workflow local completado correctamente."
