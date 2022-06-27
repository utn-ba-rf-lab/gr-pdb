# gr-pdb

## Autores

  Marcelo Doallo                    |  Leandro Bottinelli                    | Fuschetto Martin
:----------------------------------:|:--------------------------------------:|:-------------------------:
Email: <m.doallo@frba.utn.edu.ar>   | Email: <leandrobottinelli@gmail.com>   | Email: <marfus@hotmail.es>

La meta de este proyecto es crear un recurso didactico util para vivenciar el impacto de limitar el ancho de banda de una señal de audio, como así también el efecto de la adopción inadecuada en la cuantificación de la misma.


#### Dependencia de los siguientes paquetes

    * gnuradio          (Versión >= 3.8)
    * libboost-all-dev  (Verisón >= 1.71)
    * libcppunit-dev    (Versión >= 1.15.1)
    * liblog4cpp5-dev   (Versióin >= 1.1.3)
    * liborc-dev        (En revisíón)
    * swig              (Versión >= 4.0.1)
    * cmake             (Versión >= 3.16.3)
    * git               (Versión >= 2.25.1)
    
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

