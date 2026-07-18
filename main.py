from pydantic import BaseModel, ValidationError
from pathlib import Path 
import logging
import shutil
import yaml
import sys
import os


RUTA_BASE = Path.home()
RUTA_PROYECTO = Path(__file__).resolve().parent
RUTA_LOG = RUTA_PROYECTO / "app.log"
RUTA_CONFIGURACION = RUTA_PROYECTO / "config.yaml"


logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(RUTA_LOG)
            ]
        )


class Contrato_datos_configuracion(BaseModel):
    origen: Path
    destino: Path
    nombre_zip: str 
    compresion: str = "zip"


with open(RUTA_CONFIGURACION, "r") as f:
    data = yaml.safe_load(f)


def generar_backup(r_origen, r_zip, t_compresion):
    ruta_zip_sinextension = r_zip.with_suffix("")

    if r_origen.exists():

        if not len(os.listdir(r_origen)): 
            logging.error("No encontro nada del directorio de origen para hacer la copia de seguridad")
            return

        r_zip.unlink(missing_ok=True)   # Se elimina el backup viejo
        logging.info("Borrado de backups antiguos en documentos")


        try: 
            shutil.make_archive(base_name=ruta_zip_sinextension, format=t_compresion, root_dir=r_origen)
            logging.info("Se ha creado el comprimible con exito")

        except Exception as e:
            logging.error(f"Hubo un error en comprimir: {e}")

    else:
        logging.error("No se encontro la carpeta de origen")


if __name__ == "__main__":
    try:
        config = Contrato_datos_configuracion(**data["backup"])

    except ValidationError as e:
        logging.error(f"Hubo un error en la validacion de datos")
        sys.exit(1)     # Se cierra el script para evitar conflictos
    

    if config.origen.is_absolute():
        ruta_origen = config.origen
    else:
        ruta_origen = RUTA_BASE / config.origen

    if config.destino.is_absolute():
        ruta_destino = config.destino
    else:
        ruta_destino = RUTA_BASE / config.destino 
    
    tipo_compresion = config.compresion
    ruta_zip = ruta_destino / config.nombre_zip

    generar_backup(ruta_origen, ruta_zip, tipo_compresion)
