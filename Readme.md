
# Rise of Antares

Un juego de estrategia espacial donde debes gestionar tus recursos, colonizar planetas y expandir tu imperio en la galaxia.

## :zap: Uso

Este juego está basado en la exploración, gestión de recursos y expansión de colonias. A continuación te explicamos cómo jugar y qué controles utilizar.

### Comandos

- **Tecla `1`**: Avanzar un turno. Esto incrementará tus recursos (dinero, minerales y comida).
- **Tecla `2`**: Explorar un sistema estelar. Esto te permitirá ver información sobre el primer sistema estelar que está disponible.
- **Tecla `3`**: Explorar la galaxia. Esto muestra todos los planetas en la galaxia, con su información y posiciones.

## :wrench: Desarrollo

Explica cómo configurar el entorno de desarrollo para contribuir al proyecto.

### :nut_and_bolt: Entorno de Desarrollo

Para contribuir al desarrollo o probar el juego en tu máquina local, sigue estos pasos:

```bash
# Clonar el repositorio desde GitHub
git clone https://github.com/usuario/repo.git
cd repo

# Crear un entorno virtual para aislar dependencias
python -m venv venv
source venv/bin/activate  # En Linux/Mac
venv\Scriptsctivate     # En Windows

# Instalar las dependencias necesarias
pip install -r requirements.txt
```

### :file_folder: Estructura de Archivos

```plaintext
.
├── src
│   ├── main.py       # Archivo principal de ejecución
│   ├── utils.py      # Utilidades generales
├── tests
│   ├── test_main.py  # Pruebas unitarias del archivo main.py
├── README.md         # Este archivo de documentación
└── requirements.txt  # Dependencias necesarias para ejecutar el proyecto
```

## :cherry_blossom: Contribución

Este proyecto está abierto a contribuciones. Si deseas mejorar el juego o añadir nuevas funcionalidades, por favor sigue los pasos a continuación:

### :exclamation: Guía de Contribución

```bash
# Crear una nueva rama de características
git checkout -b feat/nueva-funcionalidad

# Agregar cambios a la nueva rama
git add .

# Confirmar cambios
git commit -m "Agrega nueva funcionalidad"

# Enviar la rama al repositorio remoto
git push origin feat/nueva-funcionalidad
```

## :lock: Licencia

Este proyecto está bajo la Licencia MIT.

MIT License
Copyright (c) 2024 [Tu Nombre]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
