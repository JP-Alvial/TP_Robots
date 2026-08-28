
# Empezar a trabajar con ROS2

Para generar trabajos en ROS2, es necesario gerenar un conjunto de archivos que permitan organizar el código a realizar para mantener la legibilidad con uno y los pares. en general se puede usar uno de las siguientes posibles estructuras de paquetes dependiendo del lenguaje a utilizar.

```
  CMake (C++)
my_package/
     CMakeLists.txt
     include/my_package/
     package.xml
     src/

  (Python)
my_package/
      package.xml
      resource/my_package
      setup.cfg
      setup.py
      my_package/
```

## Creación de paquete

Para la generación de este formato ya existe un comando que facilita su implementación:


```
cd ~/work_space/src
ros2 pkg create --build-type ament_python --license Apache-2.0 <package_name>
```
o
```
cd ~/<work_space>/src
ros2 pkg create --build-type ament_cmake --license Apache-2.0 <package_name>
```

> [!NOTE]
> De ser generado por primera vez el espacio de trabajo puede ser necesario revisar las dependencias de ros dentro del directorio, para no generar conflictos a posteriori.
> Para esto se puede tener en cuenta el siguiente comando
>```
>cd ~/<work_space>
>rosdep install -i --from-path src --rosdistro <distro> -y
>```

## Creación de subcriptores y publicadores en python

Con el paquete creado y las dependencias actualizadas se puede comenzar con la creación de los nodos, topicos, servicios y acciones. Para realizar esto de la forma correcta se debe seguir los siguientes pasos.

1. Crear el código a realizar:

    La generación del paquete crea de entrada una carpeta en la dirección `<work_space>/src/<package>/package` en donde colocar todos los códigos relevantes.

    >[!NOTE]
    > Para conocer con más detalle se puede seguir el tutorial explicado por la documentación de [ROS](https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html#create-a-package)

2. Adición de dependencias:
    
    Dentro del la raiz del paquete existe el archivo `package.xml` que permite a grandes rasgos actualizar todos los archivos y dependencias necesarios para el funcionamiento del sistema. Principalmente se utiliza para actualizar las dependencias de los archivos a utilizar, para esto se utiliza el siguiente código.

    ```
    <exec_depend>dependencia</exec_depend>
    ```

3. Adición de los puntos de entrada
    
    Finalmente, para que ROS2 reconosca los distintos nodos existentes, estos se "inicializan" en el archivo `setup.py` agregando el nodo como punto de entrada utilizando el siguiente formato.

    ```entry_points={
            'console_scripts': [
                    '<node_name> = <folder>.<archive>:main',
            ],
    },
    ```

## Construcción y puesta en marcha

Una vez creados todos los código necesarios se debe de construir el paquete, para esto ROS2 utiliza la herramienta de `colcon` mediante el siguiente comando:

```
colcon build
```
o
```
colcon build --packages-select <package>
```

Una vez terminado el proceso ya se puede poner en marcha los nodos o sistemas creados. Para esto se debe posicionar en la raiz del espacio de trabajo y hacer un `source`(como aparece inmediatamente abajo), para luego correr los nodos utilizando `ros2 run`.

```
source install/setup.<SHELL>
```


