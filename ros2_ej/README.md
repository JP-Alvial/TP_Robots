
# Empezar a trabajar con ROS2

Para generar trabajos en ROS2, es necesario gerenar un conjunto de archivos que permitan organizar el código a realizar para mantener la legibilidad con uno y los pares. en general se puede usar uno de las siguientes posibles estructuras de paquetes dependiendo del lenguaje a utilizar.

- CMake (C++)
´´´
my_package/
     CMakeLists.txt
     include/my_package/
     package.xml
     src/

´´´
- Python
´´´
my_package/
      package.xml
      resource/my_package
      setup.cfg
      setup.py
      my_package/
´´´
Para la generación de este formato ya existe un comando que facilita su implementación:


´´´
cd ~/work_space/src
ros2 pkg create --build-type ament_python --license Apache-2.0 <package_name>
´´´
o
´´´
cd ~/<work_space>/src
ros2 pkg create --build-type ament_cmake --license Apache-2.0 <package_name>
´´´

> [!NOTE]
> De ser generado por primera vez el espacio de trabajo puede ser necesario revisar las dependencias de ros dentro del directorio, para no generar conflictos a posteriori.
> Para esto se puede tener en cuenta el siguiente comando

´´´
cd ~/<work_space>
rosdep install -i --from-path src --rosdistro <distro> -y
´´´
