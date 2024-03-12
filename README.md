# ProjectSync: Sistema de gestión y seguimiento de trabajos de grado ingeniería de sistemas de la Universidad del Sinú

Este proyecto de gestión y seguimiento de proyectos está diseñado para facilitar la administración y seguimiento de proyectos de grado e investigación en el programa de Ingeniería de Sistemas de la Universidad del Sinú.

### Descripción
El sistema permite a los estudiantes cargar sus trabajos de investigación, mientras que los administradores del sitio web pueden asignar evaluadores a cada proyecto. Los evaluadores pueden ver todos los proyectos asignados y evaluar cada uno de ellos. Los estudiantes pueden seguir el progreso de su trabajo, desde el momento en que lo cargan hasta que reciben una calificación del evaluador. Los administradores también pueden filtrar y buscar proyectos específicos.

### Características Principales
* **Gestión de proyectos**: Los estudiantes pueden cargar sus proyectos de investigación.
* **Asignación de Evaluadores**: Los administradores pueden asignar evaluadores a proyectos específicos.
* **Evaluación de Proyectos**: Los evaluadores pueden ver y evaluar los proyectos asignados.
* **Seguimiento del Progreso**: Los estudiantes pueden seguir el progreso de sus proyectos.
* **Filtrado y Búsqueda**: Los administradores pueden filtrar y buscar proyectos por diferentes criterios.


### Estructura del Proyecto
El proyecto sigue una estructura organizada, con los siguientes directorios principales:

* **src/**: Contiene los componentes principales del proyecto.
    * **routes/**: Directorio que contiene los archivos de enrutamiento para gestionar las solicitudes HTTP.
        *  **templates/**: Directorio que contiene las plantillas HTML utilizadas en el proyecto.
    * **database/**: Directorio que contiene archivos relacionados con la base de datos.
    * **models/**: Directorio que contiene los modelos de base de datos definidos para el proyecto.
* **static/**: Contiene archivos estáticos, como JavaScript, CSS, fuentes, y *assets*.
    * **js/**: Directorio que contiene archivos JavaScript utilizados en el proyecto.
    * **assets/**: Directorio que contiene otros activos estáticos, como imágenes.
    * **uploads/**: Directorio donde se almacenan los trabajos de investigación cargados por los estudiantes.
   * **fonts/**: Directorio que contiene las fuentes utilizadas en el proyecto.
   * **css/**: Directorio que contiene archivos CSS utilizados en el proyecto.

### Instalación y Configuración
1. Clone este repositorio en su máquina local.
2. Asegúrese de tener Python instalado en su sistema.
3. Instale las dependencias del proyecto ejecutando pip install -r requirements.txt.
4. Configure las variables de entorno necesarias, como la cadena de conexión a la base de datos y las claves secretas.
5. Ejecute la aplicación utilizando el comando python app.py.
6. Abra su navegador web y vaya a http://localhost:5000 para acceder al proyecto.

### Principales Tecnologías Utilizadas
**Flask**: Framework web utilizado para el desarrollo del backend.
**SQLAlchemy**: Biblioteca de mapeo objeto-relacional (ORM) para interactuar con la base de datos.
**Tailwind CSS**: Framework de diseño CSS utilizado para el desarrollo del frontend.
**MySQL**: Sistema de gestión de bases de datos relacional utilizado para almacenar los datos del proyecto.


### Licencia
Este proyecto está bajo la Licencia MIT.