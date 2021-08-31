# gr-pdb

## Introducción

Este repositorio describe los avances de un recurso didáctico útil para vivenciar el impacto de limitar en ancho de banda una señal de audio, como así también el efecto de la adopción inadecuada en la cuantificación de la misma. 

La Modulación por Codificación de Pulsos (PCM) es un proceso fundamental en el desarrollo de las Comunicaciones del mundo de hoy, permite que señales analógicas como por ejemplo Voz, Audio o Video sean convertidas en señales digitales y así de este modo ser transmitidas o almacenadas con el grado de fidelidad que se desee.

El teorema del muestreo es uno de los pilares que dieron paso a las señales PCM, el otro es la cuantificación. El teorema exige que las señales a muestrear estén limitadas en ancho de banda y esta situación puede traer consecuencias al interpretar el mensaje tratado. A su vez estas muestras, aún analógicas, requieren de cuantificación para su tratamiento en comunicaciones y nuevamente esto también puede producir consecuencias. En ambas situaciones el alumno las puede experimentar y sacar sus propias conclusiones por medio del recurso propuesto.

Se trata de software desarrollado en ambiente de GNU Radio que permite realizar experiencias útiles para la formación por competencias centradas en el alumno, al momento de tratar el tema Modulación por Codificación de Pulsos en cursos iniciales de Sistemas de Comunicaciones.


## Autores

  Marcelo Doallo                    |  Leandro Bottinelli                    | Fuschetto Martin
:----------------------------------:|:--------------------------------------:|:-------------------------:
Email: <m.doallo@frba.utn.edu.ar>   | Email: <leandrobottinelli@gmail.com>   | Email: <marfus@hotmail.es>

#### Dependencias

    * GNU Radio 3.8
    * libboost-all-dev   
    * libcppunit-dev
    * liblog4cpp5-dev
    * liborc-dev
    * swig 
    * cmake 
    * git
    * vim 

Como correr Docker en Linux 
==============================

[Dockerfile](link)

* Construya el contenedor con:
```
docker build -t ubuntu:gnuradio_38_2 . 
```

* Corra el contenedor con:
```
docker run --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" --privileged --device /dev/snd -v /home/leandro/gnuradio_38:/home/gnuradio/persistent --group-add=audio    -e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native  -v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native -v ~/.config/pulse/cookie:/root/.config/pulse/cookie --group-add $(getent group audio | cut -d: -f3) --device /dev/snd  -it ubuntu:gnuradio_38 bash
```

Como correr Docker en windows 
==============================

## Prerequisitos

### Instalar Xming
1) Descargue una version de dominio publico de [Xming](https://sourceforge.net/projects/xming/files/Xming/6.9.0.31/Xming-6-9-0-31-setup.exe/download).
2) Instalar siguiendo el asistente de instalacion. 
3) Reiniciar la PC. 

### Iniciando Xming

Abra "XLaunch" y adopte la siguiente configuracion:

1) Select display Settings Multiple Windows, Display Number: 0
2) Select to start Xming Start no client.
3) Specify parameter settings Clipboard, No Access Control.

### Instalar Docker desktop

1) [Descargar Docker desktop](https://docs.docker.com/desktop/windows/install/)
2) Instalar siguiendo el asistente de instalacion. 

### Iniciando Docker desktop

Abra "Docker Desktop".

1) Dirigase a los iconos ocultos de Windows, Docker desktop, click derecho, "Switch to Linux containers...". Si dice Switch to Windows containers... siga con el siguiente paso.

### Instalar Pulseaudio

1) Descargue [Pulseaudio](http://bosmans.ch/pulseaudio/pulseaudio-1.1.zip) 

NOTA: Por algun motivo tuve que abrirlo en modo icongnito para que descargue el zip.

2) Siga los siguientes para abrir el servidor de pulseaudio. Basado en [link](https://x410.dev/cookbook/wsl/enabling-sound-in-wsl-ubuntu-let-it-sing/).

#### Descomprima los archivos del paso uno.
<img src=./.docs_repo/img/unzip.png alt="" />

#### Edite 'etc\pulse\default.pa'. 
<img src=./.docs_repo/img/edit1.png alt="" />

##### NOTA: Tenga en cuenta que por cuestiones de seguridad y privacidad Windows 10 (actualizacion de abril del 2018) restringe lel acceso a los dispositivos de grabacion de audio. Como solo queremos tener sonido simplemente lo deshabilitamos desde el servidor PulseAudio agregando el 'registro = 0'.
<img src=./.docs_repo/img/edit11.png alt="" />

Esto habilita al servidor PulseAudio a aceptar conexiones sollo desde 127.0.0.1 via TCP.

#### Edite 'etc\pulse\daemon.conf' 
<img src=./.docs_repo/img/edit2.png alt="" />

Si esta opcion esta seteada en un valor positivo representa el tiempo en segundos que el servidor tardara en terminar cuando el ultimo cliente se desconecte.

#### Corra 'bin\pulseaudio.exe'
<img src=./.docs_repo/img/run.png alt="" />

'pulseaudio.exe' es el ejecutable para el servidor PulseAudio (tambien conocido como 'Daemon' en los procesos de Linux).

<img src=./.docs_repo/img/run2.png alt="" />
Cuando corra 'bin\pulseaudio.exe' vera la alerta de 'Windows Firewall' que le preguntara si usted quiere permitir otros dispositivos para conectar al servidor, como usted solo esta usando (127.0.0.1) debe seleccionar cancelar, no tiene que permitir a otros dispositivos.

En el caso de que un error ocurra, el servidor se cierra inmediatamente. Si es el caso vuelva al paso 3 y este seguro de que hizo los cambios correctamente.

CTRL+C para detener el servidor.

### Editor de texto

1) Instale su editor de texto preferido, recomiendo Visual Studio Code ya que necesitara la consola.


Correr el contenedor Docker en Windows
=======================================


* Cree una carpeta donde permanecera el contenedor. Ej /Escritorio/Docker.
* Descargue el [Dockerfile](link) del repositorio y guardelo en esa carpeta.
* Construya el contenedor con:

```
docker build -t ubuntu:gnuradio_38_2 . 
```

* Corra el contenedor con:

```
docker run  --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" -e DISPLAY=$DISPLAY -i -t ubuntu:gnuradio_38_2 bash
```

NOTA: "gnuradio_38_2" hace referencia al nombre del contenedor.

###Una vez dentro del contenedor debera: 


1) ipconfig, guarde su IPv4-Adress
2) set-variable -name DISPLAY -value "IPv4-Adress":0.0
3) export PULSE_SERVER=tcp:"IPv4-Adress"


Felicitaciones ya podra utilizar gnuradio!!


Instrucciones para construir el modulo
=======================================
    * mkdir build
    * cd build
    * cmake ..
    * make
    * sudo make install
    * sudo ldconfig


Despues de correr esos comandos dentro de Docker, el bloque "PDB_Block" deberia aparecer en la categoria "PDB" en GNU Radio Companion.

<img src=./.docs_repo/img/pdb_block_gnu.png alt="" />
