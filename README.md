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

#### Como correr Docker 

[Docker file] (Directorio al archivo Docker)

```
docker run --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" --privileged --device /dev/snd -v /home/leandro/gnuradio_38:/home/gnuradio/persistent --group-add=audio    -e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native  -v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native -v ~/.config/pulse/cookie:/root/.config/pulse/cookie --group-add $(getent group audio | cut -d: -f3) --device /dev/snd  -it ubuntu:gnuradio_38 bash
```

#### Build instructions

    * mkdir build
    * cd build
    * cmake ..
    * make
    * sudo make install
    * sudo ldconfig


Despues de correr esos comandos dentro de Docker, el bloque "gr-pdb" deberia aparecer en la categoria "" en GNU Radio Companion.

## Descripcion del modulo 

asdasd

