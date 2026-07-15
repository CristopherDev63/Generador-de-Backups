from pathlib import Path 
import logging
import shutil
import os


logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("app.log")
            ]
        )


ruta_icloud = Path.home() / "Library/Mobile Documents/iCloud~md~obsidian/Documents/Wiki Cris"
ruta_destino = Path.home() / "Documents" / "Backup Obsidian"
ruta_zip = ruta_destino / "Wiki Cris.zip"
ruta_zip_sinextension = ruta_zip.with_suffix("")


def decargar_de_icloud():
    if ruta_icloud.exists():

        if not len(os.listdir(ruta_icloud)): 
            logging.error("No encontro nada del directorio de origen para hacer la copia de seguridad")
            return

        ruta_zip.unlink(missing_ok=True)   # Se elimina el backup viejo
        logging.info("Borrado de backups antiguos en documentos")


        try: 
            shutil.make_archive(base_name=ruta_zip_sinextension, format="zip", root_dir=ruta_icloud)
            logging.info("Se ha creado el comprimible con exito")

        except Exception as e:
            logging.error(f"Hubo un error en comprimir: {e}")

    else:
        logging.error("No se encontro la carpeta de origen")


if __name__ == "__main__":
    decargar_de_icloud()
