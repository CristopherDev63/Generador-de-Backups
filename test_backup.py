import os
import shutil
from pathlib import Path
# Importamos tu función principal desde tu script main.py
from main import generar_backup

# Definimos la estructura limpia sugerida dentro de ./tests/
CARPETA_BASE = Path("./tests")
ORIGEN_PRUEBA = CARPETA_BASE / "test_origen"
DESTINO_PRUEBA = CARPETA_BASE / "test_destino"
ZIP_PRUEBA = DESTINO_PRUEBA / "test_wiki.zip"

def preparar_entorno_limpio():
    """Elimina la carpeta de pruebas base para asegurar que no arrastremos basura de ejecuciones pasadas."""
    if CARPETA_BASE.exists():
        shutil.rmtree(CARPETA_BASE)
    
    # Creamos las carpetas vacías desde cero
    ORIGEN_PRUEBA.mkdir(parents=True, exist_ok=True)
    DESTINO_PRUEBA.mkdir(parents=True, exist_ok=True)
    print("🧹 Entorno `./tests/` limpio y recreado desde cero.")

def poblar_origen_con_datos():
    """Genera una estructura de archivos simulando notas reales dentro de tu origen."""
    print("✍️ Generando notas y archivos de prueba en el origen...")
    
    # 1. Creamos subcarpetas simulando un Obsidian real
    (ORIGEN_PRUEBA / "Notas").mkdir(exist_ok=True)
    (ORIGEN_PRUEBA / "Plantillas").mkdir(exist_ok=True)
    
    # 2. Creamos archivos de texto (.md) con contenido falso
    (ORIGEN_PRUEBA / "index.md").write_text("# Mi Wiki de Pruebas\nEste es el index de mi Obsidian.")
    (ORIGEN_PRUEBA / "Notas" / "Ciberseguridad.md").write_text("# Notas de Cero a Pro\nConceptos clave de ciberseguridad defensiva.")
    (ORIGEN_PRUEBA / "Plantillas" / "Estructura_Nota.md").write_text("---\ntags: [plantilla]\n---\n# Título\nCuerpo.")
    
    print("✅ Origen poblado con éxito.")


if __name__ == "__main__":
    print("🚀 INICIANDO PRUEBA DE RESPALDO INTEGRAL")
    
    # 1. Limpiamos y recreamos las carpetas de prueba
    preparar_entorno_limpio()
    
    # 2. Creamos la estructura de notas dentro de test_origen
    poblar_origen_con_datos()
    
    # 3. Ejecutamos TU función real para empaquetar todo
    print("\n📦 Ejecutando 'generar_backup' de tu script principal...")
    # Le pasamos: ruta_origen, ruta_zip y el formato de compresión que usa tu script
    generar_backup(ORIGEN_PRUEBA, ZIP_PRUEBA, "zip")
    
    # 4. Verificación final: ¿El archivo zip se creó en el destino?
    print("\n🔍 Verificando resultado de la prueba...")
    if ZIP_PRUEBA.exists():
        # Obtenemos el tamaño del ZIP generado en kilobytes
        tamano_kb = ZIP_PRUEBA.stat().st_size / 1024
        print(f"🎉 ¡ÉXITO! El archivo de respaldo existe en: {ZIP_PRUEBA}")
        print(f"   Tamaño del backup: {tamano_kb:.2f} KB")
    else:
        print("❌ FALLO: El archivo ZIP no se encontró en la carpeta de destino.")
        print("   Revisa tu 'app.log' para ver qué error reportó tu script")
