# Generador de Backups

Un generador de backups de seguridad en un comprimible en una ruta en específico hecho en Python. 

*Evita los dolores de cabeza en hacer una copia seguridad de forma manual.*

---

## Instalación
### Clonar Repositorio 
``` bash 
git clone https://github.com/CristopherDev63/Generador-de-Backups.git
```

### Creación de entorno virtual y activación

Windows:
``` bash 
python -m venv .venv 
.venv\Scripts\Activate.ps1
```

Unix(MacOS/Linux):
``` bash 
python -m venv venv 
source venv/bin/activate
```

### Instalación de dependencias 
``` bash 
pip install -r requerimientos.txt
```
---

## Ejecución 

``` bash
python main.py
```

---
## Guia de uso y configuración 
Se tiene que seguir una serie de pasos para su uso.

1. **Configure las rutas que usara**. Dentro del archivo de `config.yaml` se tiene que especificar las rutas a usar.
``` yaml
origen: ""
destino: ""
```
2. **Nombre del ZIP (el archivo comprimido)**. Muy importante darle el nombre al **backup** en donde se guardara en la ruta de **destino**. 

3. **Tipo de Compresión**: Se le puede asignar un tipo compresión que por defecto esta en `zip` y puede hacer también otros tipos como: 
- `zip`
- `gztar`
- `bztar`
- `xztar`
- `tar`
