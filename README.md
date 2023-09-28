# ReconocimientoFacial
Proyecto - inteligencia Artificial UPDS 2023

![LogoUpds](https://github.com/Tobeh06/ReconocimientoFacial/blob/main/ImgReadme/logoupds.jpg)



<H2 align="center">MATERIA: RECONOCIMIENTO FACIAL</H2>
<H2 align="center">DOCENTE: PHD. ING. JAIME ZAMBRANA CHACON</H2> 
<H2 align="center">GRUPO: DINAMITA</H2>
<H2 align="center">INTEGRANTES:</H2>
<H2 align="center">LUIS A. GARCIA RAMOS</H2>
<H2 align="center">HERLAND M. FLORES VARGAS</H2>
<H2 align="center">J. CARLOS RAMIREZ PEDRAZA</H2>

<H1>Resumen</H1> 

El presente proyecto fue realizado con las librerías open-cv, os, numpy, pygame, imutils en el entorno de VsCode, para poder realizar múltiples funciones de manera simultánea.
Las funciones más sobresalientes son poder entrenar a una inteligencia artificial para que pueda conocer rostros y familiarizarse con ellos, teniendo esta funcionalidad es posible un sinfín de objetivos en el ámbito de desarrollo, para lograr esto se utilizaron los algoritmos haar cascade y fisherface . 
Para poder llevar acabo este proyecto se desarrollo en 3 etapas: 

1.	Captura de los rostros: Se pueden capturar los rostros con la cámara en vivo del computador o por medio de fotos o videos tomados con anterioridad. 

2.	Entrenamiento del modelo de reconocimiento facial: En este script se leen las fotografías tomadas de los rostros a reconocer, entonces de esta manera la inteligencia artificial sabe quienes son los rostros conocidos y quienes los desconocidos. 

3.	Validaciones de rostros: En este script se realiza una validación con base a condiciones de que si el rostro tiene coincidencia de similitud con los rostros entrenados y registrados. 

<H1>Abstract</H1>

This project was carried out with the open-cv, os, numpy, pygame, and imutils libraries in the VsCode environment, to be able to perform multiple functions simultaneously.
The most outstanding functions are being able to train an artificial intelligence so that it can know faces and become familiar with them. Having this functionality, endless objectives are possible in the field of development. To achieve this, the haar cascade and fisherface algorithms were used.
In order to carry out this project, it was developed in 3 stages:

1. Capture of faces: Faces can be captured with the computer's live camera or through photos or videos taken previously.

2. Training of the facial recognition model: In this script, the photographs taken of the faces to be recognized are read, so in this way the artificial intelligence knows who are the known faces and who are the unknown ones.

3. Face validations: In this script a validation is carried out based on the conditions that the face has a similarity match with the trained and registered faces.


<H1>DESARROLLO</H1>
<H1>MARCO TEORICO</H1>
<H1>OPENCV</H1>
significa Open Source Computer Vision Library, es una biblioteca de código abierto ampliamente utilizada en el campo de la visión por computadora y el procesamiento de imágenes. Estas son algunas de las funciones que tiene OpenCV:

1.	Procesamiento de imágenes:* OpenCV proporciona herramientas y funciones para manipular imágenes de diversas maneras, como cambiar el tamaño, rotar, recortar, ajustar el brillo y el contraste, entre otras operaciones.

2.	Detección de objetos:* Es ampliamente utilizado en la detección de objetos en imágenes y videos. Puede ayudar a identificar objetos o patrones específicos en una imagen, como caras, objetos, marcas o características.

3.	Seguimiento de objetos:* OpenCV es útil para el seguimiento de objetos en videos en tiempo real. Puede rastrear el movimiento de objetos a lo largo del tiempo y proporcionar información sobre su posición y velocidad.

4.	Visión estéreo:* Se utiliza para la visión estéreo, que implica la captura y el análisis de imágenes desde múltiples cámaras para estimar la profundidad y la distancia entre objetos en una escena.

5.	Reconocimiento facial:* OpenCV ofrece herramientas para el reconocimiento facial, lo que permite detectar y reconocer caras en imágenes y videos, así como realizar tareas como el seguimiento facial.

6.	Procesamiento de video:* Puede usarse para procesar secuencias de video, aplicar filtros y efectos, estabilizar videos, y mucho más.

7.	Aprendizaje automático:* OpenCV también se integra con bibliotecas de aprendizaje automático como TensorFlow y PyTorch para aplicaciones de visión por computadora más avanzadas, como la clasificación de objetos y la segmentación de imágenes.

8.	Realidad aumentada:* Es utilizado en aplicaciones de realidad aumentada para superponer objetos virtuales en el mundo real, utilizando información de la cámara.

9.	Robótica:* OpenCV se utiliza en la robótica para la navegación, la percepción del entorno y la toma de decisiones basada en la visión.

OpenCV es una poderosa biblioteca de visión por computadora que proporciona un conjunto diverso de herramientas y funciones para el procesamiento de imágenes y videos, lo que la hace esencial en una amplia gama de aplicaciones que involucran la interpretación y el análisis de datos visuales.

<H1>LBPHFace</H1> 
El modelo de entrenamiento LBPH (Local Binary Pattern Histogram) para la detección y reconocimiento facial es una técnica utilizada en visión por computadora y procesamiento de imágenes para identificar y autenticar caras en imágenes y videos.

<H1>Local Binary Pattern (LBP)</H1>
 El LBP es un operador utilizado para describir la textura local en una imagen. Funciona comparando cada píxel de la imagen con sus píxeles vecinos y codificando esta información en un número binario. El resultado es una representación de la textura local de la imagen.
 
# Histograma de Patrones Binarios Locales (LBPH)

El LBPH es una extensión del LBP que se utiliza específicamente para el reconocimiento facial. En lugar de aplicar el LBP a cada píxel de la imagen, se aplica a una región de interés, como una ventana que contiene una cara. Luego, se crea un histograma que cuenta cuántas veces aparece cada patrón binario local en esa región. Esto crea una representación compacta de la textura facial.

# Entrenamiento del modelo
Para entrenar un modelo LBPHFace, se necesita un conjunto de imágenes de entrenamiento que contengan caras de las personas que se desea reconocer. El modelo calcula el LBPH para cada región de interés en estas imágenes y crea un histograma de patrones binarios locales para cada individuo.

# Reconocimiento facial
 Una vez que el modelo está entrenado, se puede usar para reconocer caras en imágenes o videos. Para hacerlo, el modelo calcula el LBPH para la cara en cuestión y compara su histograma con los histogramas de entrenamiento almacenados previamente. La cara se clasifica según la similitud de sus características con las de las caras de entrenamiento, y se identifica como una persona específica si existe una coincidencia cercana.

# Aplicaciones
 El modelo LBPHFace se utiliza en aplicaciones de seguridad, sistemas de acceso biométrico, sistemas de vigilancia, autenticación facial en dispositivos móviles y muchas otras áreas donde se requiere la identificación de individuos a partir de imágenes faciales.
En resumen, el modelo de entrenamiento LBPHFace utiliza el concepto de Local Binary Pattern Histogram para describir y comparar características faciales locales, lo que lo hace útil para el reconocimiento facial en una variedad de aplicaciones. Este enfoque se basa en la textura local de la cara y ha demostrado ser eficaz para la identificación de individuos en imágenes y videos.


# FISHERFace
El modelo de entrenamiento FisherFace, también conocido como Linear Discriminant Analysis (LDA) aplicado a caras, es una técnica utilizada en reconocimiento facial y visión por computadora para identificar y autenticar caras en imágenes y videos.

# Análisis Discriminante Lineal (LDA)
El LDA es una técnica de reducción de dimensionalidad que se utiliza para maximizar la separación entre clases en un conjunto de datos. En el contexto del reconocimiento facial, se aplica para encontrar las características más discriminativas que permiten distinguir entre diferentes individuos.

# FisherFace
El FisherFace es una extensión del LDA específicamente diseñada para el reconocimiento facial. A diferencia de otros métodos que se basan en la textura local, el FisherFace se enfoca en encontrar una representación lineal de las caras completas. Utiliza las imágenes de entrenamiento para calcular una transformación lineal que maximice la variabilidad entre las clases (diferentes individuos) y minimice la variabilidad dentro de las clases (diferentes expresiones o iluminaciones de la misma persona).

# Entrenamiento del modelo
 Para entrenar un modelo FisherFace, se necesita un conjunto de imágenes de entrenamiento que contengan caras de las personas que se desea reconocer. El modelo calcula una matriz de proyección que transforma las imágenes originales en una representación de baja dimensionalidad que es más discriminativa para la identificación de caras.

# Reconocimiento facial
Una vez que el modelo está entrenado, se puede usar para reconocer caras en imágenes o videos. Para hacerlo, el modelo proyecta una imagen de entrada en el espacio de características aprendido y compara esta proyección con las proyecciones de las imágenes de entrenamiento. La identidad se determina encontrando la imagen de entrenamiento más cercana en este espacio.

# Aplicaciones
 El modelo FisherFace se utiliza en aplicaciones de seguridad, sistemas de acceso biométrico, sistemas de vigilancia, autenticación facial en dispositivos móviles y muchas otras áreas donde se requiere la identificación de individuos a partir de imágenes faciales. Es especialmente eficaz cuando se enfrenta a variaciones en la iluminación y la expresión facial.
El modelo de entrenamiento FisherFace utiliza el Análisis Discriminante Lineal para encontrar una representación lineal de caras completas que sea altamente discriminativa para la identificación de individuos. Este enfoque se basa en la variabilidad entre clases y ha demostrado ser efectivo en el reconocimiento facial en una variedad de condiciones.

# PYGAME

La librería Pygame es una biblioteca de Python especializada en el desarrollo de videojuegos y aplicaciones multimedia interactivas.
Desarrollo de videojuegos y multimedia
Pygame proporciona una plataforma para crear videojuegos y aplicaciones multimedia de manera eficiente en Python. Esto lo hace adecuado para programadores que desean desarrollar juegos, simulaciones interactivas, animaciones y otras aplicaciones visuales y auditivas.
Características clave de Pygame

1.	Gráficos : Pygame permite crear gráficos 2D y manipular imágenes, lo que incluye dibujar formas, imágenes, fondos y animaciones en una ventana de juego.

2.	Sonido: Permite la reproducción de efectos de sonido y música de fondo en tus aplicaciones, lo que mejora la experiencia del usuario.

3.	Interacción con el usuario: Pygame maneja la entrada del usuario, como eventos de teclado y mouse, para permitir la interacción con tus juegos y aplicaciones.

4.	Física básica: Aunque no es un motor de física completo, Pygame proporciona herramientas para simular interacciones físicas simples, como colisiones y movimiento.

5.	Colisiones:Facilita la detección y manejo de colisiones entre objetos en tu juego, lo que es esencial para la jugabilidad.

6.	Facilidad de uso: Pygame está diseñado para ser accesible, lo que significa que es adecuado para programadores principiantes y experimentados. Su API es relativamente simple y fácil de aprender.


# Portabilidad: 
Las aplicaciones desarrolladas con Pygame son altamente portables, lo que significa que puedes ejecutarlas en múltiples plataformas, incluyendo Windows, macOS y Linux, sin modificar significativamente el código fuente.

# Comunidad activa:
Pygame tiene una comunidad activa de desarrolladores y una amplia base de usuarios. Esto significa que hay una gran cantidad de recursos, tutoriales y bibliotecas disponibles para ayudarte en tu desarrollo.

# Aplicaciones de Pygame: 
Además de juegos, Pygame se utiliza en una variedad de aplicaciones interactivas, como simulaciones, aplicaciones educativas, arte interactivo, visualización de datos y más.
La librería Pygame es una herramienta poderosa y versátil que facilita el desarrollo de videojuegos y aplicaciones multimedia interactivas en Python. Su simplicidad y facilidad de uso la hacen adecuada para una amplia gama de proyectos, y su comunidad activa la respalda con recursos y soporte para los desarrolladores.

 # VS CODE: 
Visual Studio Code (VS Code) es un popular entorno de desarrollo integrado (IDE) de código abierto desarrollado por Microsoft. Está diseñado para ser altamente configurable y extensible, y es ampliamente utilizado en el desarrollo de aplicaciones en diversos lenguajes de programación, incluido Python. A continuación, un marco teórico orientado a Python para comprender su utilidad:
Entorno de Desarrollo Integrado (IDE):VS Code es un IDE que proporciona una interfaz de usuario y herramientas integradas para simplificar el proceso de desarrollo de software en Python y otros lenguajes. Esto incluye un editor de código, herramientas de depuración, integración con control de versiones y más.

# Características claves para Python:
-	Resaltado de sintaxis: VS Code ofrece resaltado de sintaxis para Python, lo que facilita la lectura y escritura de código Python al resaltar palabras clave, variables, cadenas y otros elementos del lenguaje.
-	Autocompletado inteligente: Proporciona sugerencias contextuales mientras escribes código, lo que acelera el desarrollo y reduce errores de escritura.
-	Depuración integrada: Puedes depurar tus programas Python directamente desde VS Code, estableciendo puntos de interrupción, inspeccionando variables y ejecutando el código paso a paso.
-	Gestión de paquetes y entornos virtuales: VS Code se integra con herramientas como pip y conda para gestionar paquetes y entornos virtuales de Python, lo que es esencial para la gestión de dependencias en proyectos Python.
-	Extensiones Python: VS Code admite una amplia variedad de extensiones relacionadas con Python que añaden funcionalidad adicional, como soporte para linters (verificación de estilo y errores), frameworks de desarrollo web y más.


# Configuración personalizada:
VS Code permite a los desarrolladores personalizar su entorno de desarrollo según sus preferencias. Puedes instalar temas, ajustar la configuración de formato y personalizar atajos de teclado.

# Control de versiones: 
VS Code ofrece integración con sistemas de control de versiones como Git, lo que facilita el seguimiento de cambios en tus proyectos de Python y la colaboración con otros desarrolladores.

# Terminal integrada:
Incluye una terminal integrada que te permite ejecutar comandos y scripts Python directamente desde el IDE.
Depuración remota: VS Code admite la depuración remota, lo que significa que puedes depurar código Python que se ejecuta en un servidor o máquina remota.

# Desarrollo en la nube:
Puedes utilizar VS Code en conjunto con servicios en la nube como Microsoft Azure o Google Cloud para desarrollar, depurar y desplegar aplicaciones Python en la nube.

Visual Studio Code es una herramienta versátil y altamente personalizable que se utiliza ampliamente en el desarrollo de Python y otros lenguajes. Proporciona un entorno de desarrollo eficiente con numerosas características que ayudan a los desarrolladores a escribir, depurar y mantener código Python de manera efectiva.


<H1>PROYECTO</H1>

# INSTALACIÓN DE PROGRAMAS Y LIBRERÍAS  
# VS Code
Visual Studio Code es uno de los editores de código gratuitos más conocidos en todo el mundo. Su sencillez de uso y su interfaz gráfica son algunos de sus muchos puntos fuertes. Con su instalación se incorporan los lenguajes de JavaScript (junto con TypeScript y Node.js), HTML y CSS, aunque con las extensiones es posible utilizar lenguaje Java, C++, PHP o Python.
Pasos

1. Descargar el instalador del programa. Podemos elegir los sistemas operativos de Windows, Linux y Mac.
 
2. Ejecutar el fichero que se nos ha descargado. La instalación es muy sencilla. Simplemente debemos ir aceptando y avanzando en el proceso de instalación.

 ![Install](https://github.com/Tobeh06/ReconocimientoFacial/blob/main/ImgReadme/instalacode.png)
3. Abrir Visual Studio Code. Nos aparecerá una ventana como la siguiente.
  ![Install](https://github.com/Tobeh06/ReconocimientoFacial/blob/main/ImgReadme/codeini.png)

Y listo ya tenemos instalado vs code.

PYTHON
Para instalar Python es necesario primero descargarlo donde la pagina oficial 
 ![Install](https://github.com/Tobeh06/ReconocimientoFacial/blob/main/ImgReadme/1python.png)

Una ves descargado el ejecutable procedemos a instalarlo, debería aparecer así cuando este todo bien instalado.
 

Esto aparece cuando quisiéramos reparar desinstalar o modificar , y listo ya tenemos Python instalado en nuestro equipo.
 ![Install](https://github.com/Tobeh06/ReconocimientoFacial/blob/main/ImgReadme/repararpython.png)


# Pygame 2.5.2 y  Open CV 4.1.0.25
Para esta librería lo que tenemos que hacer es entrar en vscode abrir una terminal en la misma, para lograr ello tenemos que usar el siguiente comando control +  j
Luego en la terminal tenemos que escribir el siguiente comando para instalar pygame.

          pip install pygame



Lo mismo para open cv pero con otro comando.

          pip install opencv-contrib-python

Nota: este comando instala paquetes de la librería opencv adicionales, se sugiere trabajar con este. 

Y con ello esta todo listo para arrancar.

# DISEÑO

Este proyecto es considerado un proto tipo o un demo, ya que actualmente se ejecuta a travez de una terminal, a continuación una vista previa en funcionamiento. 
 ![Install](https://github.com/Tobeh06/ReconocimientoFacial/blob/main/ImgReadme/Reconociendo.png)

 


 # FUNCIONALIDADES

 El proyecto se basa en 3 etapas
 1. Captura de datos o imagenes con las cuales serán reconocidas: aqui utilizamos el algoritmo haar cascade para realizar el estudio de los rostros, ademas de imutils
Capturando imagenes:
![Install](https://github.com/Tobeh06/ReconocimientoFacial/blob/main/ImgReadme/1.png)
  
 3. Entrenamiento de las imagenes capturadas y a la vez etiquetadas.
Entrenamiento de imagenes:
![Install](https://github.com/Tobeh06/ReconocimientoFacial/blob/main/ImgReadme/2.png)
 5. Proceso de pruebas o reconocimiento facial.
![Install](https://github.com/Tobeh06/ReconocimientoFacial/blob/main/ImgReadme/Reconociendo.png)

#CODIGO FUENTE: 
https://github.com/Tobeh06/ReconocimientoFacial/

# CONCLUSIÓN 

En este proyecto de inteligencia artificial, implementamos con éxito un sistema de reconocimiento de rostros utilizando Python y OpenCV, con el método de entrenamiento FISHERFace. A lo largo de este proyecto, hemos logrado importantes avances en la detección y reconocimiento de rostros, lo que tiene aplicaciones significativas en diversos campos.
La elección de FISHERFace como algoritmo de entrenamiento demostró ser acertada, ya que permitió obtener representaciones efectivas de las caras en el conjunto de datos. La capacidad de FISHERFace para reducir la dimensionalidad y resaltar las características discriminativas de los rostros resultó en un rendimiento de reconocimiento sobresaliente.
La biblioteca OpenCV desempeñó un papel fundamental en la implementación de nuestro sistema. Nos proporcionó las herramientas necesarias para capturar y preprocesar imágenes, así como para entrenar y utilizar el modelo de reconocimiento facial. La versatilidad de OpenCV en el procesamiento de imágenes nos permitió abordar una variedad de desafíos, como la detección de rostros en condiciones de iluminación variable y cambios en la pose facial.
Durante el proceso de entrenamiento, optimizamos nuestros modelos y ajustamos los parámetros para lograr un alto nivel de precisión y una baja tasa de error. Esto se logró mediante la recopilación de un conjunto de datos diverso y representativo, lo que permitió al modelo aprender de manera efectiva las características distintivas de diferentes rostros.
En resumen, este proyecto demuestra la capacidad de Python, OpenCV y el método FISHERFace para desarrollar un sistema de reconocimiento de rostros preciso y robusto. Las aplicaciones de esta tecnología son variadas, desde la seguridad en el acceso de edificios hasta la identificación de personas en imágenes y videos. Este proyecto sienta las bases para futuras mejoras y desarrollos en el campo del reconocimiento facial y la inteligencia artificial.


# BIBLIOGRAFÍA 

https://appdatos.com/2019/09/17/python-instalar-manualmente-pygame-para-visual-studio-2019/

https://code.visualstudio.com/

https://opencv.org/

https://www.youtube.com/watch?v=cZkpaL36fW4&t=1046s

