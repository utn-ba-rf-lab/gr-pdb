[Spanish Readme](./README.md)

# gr-pdb

## introduction

This repository describes the progress of an educational resource to notice the impact of limiting the bandwidth of an audio signal and the effect of an inappropriate adoption of signal quantization.

Pulse Code Modulation (PCM) is a digital representation of an analog signal that takes samples of the amplitude of the analog signal at regular intervals. It allows analog signal such as Voice, Audio or Video to be converted into digital signals, in this way they can be transmitted or stored with the desired fidelity.

Sampling theorem is one of the fundamental pillars upon which the PCM signal was built, the other is Quantization. The process of digitizing the domain is called sampling and the process of digitizing the range is called quantization. 
The Sampling theorem requires that the signals to be sampled are limited in bandwidth and this may result in a challenge interpreting the message. At the same time these analog samples require quantification for their treatment in communications. This resource allows treating both situations and allows the student to experiment and draw their own conclusions.

It is software developed in a GNU Radio environment that allows to carry out useful experiences for training by competencies centered on the student, when dealing with the topic Pulse Coding Modulation in initial Communications Systems courses.

## Authors

  Marcelo Doallo                    |  Leandro Bottinelli                    | Fuschetto Martin
:----------------------------------:|:--------------------------------------:|:-------------------------:
Email: <m.doallo@frba.utn.edu.ar>   | Email: <leandrobottinelli@gmail.com>   | Email: <marfus@hotmail.es>


## Index
1. [Dependencies](#dependencias)
2. [How to run Docker on Linux](#docker_linux)
3. [How to install Docker on Windows](#docker_dekstop_windows)
4. [Running the Docker container on Windows](#docker_windows)
5. [Instructions to build the module](#cons_modulo)


#### Dependencies <a name="dependencias"></a>

    * GNU Radio 3.8
    * libboost-all-dev   
    * libcppunit-dev
    * liblog4cpp5-dev
    * liborc-dev
    * swig 
    * cmake 
    * git
    * vim 

How to implement the project on Linux <a name="docker_linux"></a>
============================================================

Download the Dockerfile from [Dockerfile](link) on a directory of your choise then proceed with:  

* Build the container:
```
docker build -t ubuntu:gnuradio_38_2 . 
```

* Run the container:
```
docker run --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" --privileged --device /dev/snd -v /home/leandro/gnuradio_38:/home/gnuradio/persistent --group-add=audio    -e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native  -v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native -v ~/.config/pulse/cookie:/root/.config/pulse/cookie --group-add $(getent group audio | cut -d: -f3) --device /dev/snd  -it ubuntu:gnuradio_38 bash
```

How to implement the project in Windows <a name="docker_dekstop_windows"></a>
============================================================

### System requirements for Docker Desktop 

#### WSL 2 backend

1) Windows 10 64-bit: Home or Pro 2004 (build 19041) or higher, Enterprise, or Education 1909 (build 18363) or higher.
2) Enable WSL 2 on Windows. [Microsoft documentation](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
3) The following hardware prerequisites are necessary to run WSL 2 on Windows 10.

* 64-bit processor with "Second Level Address Translation" (SLAT).
* 4GB of RAM memory.
* Hardware virtualization support at the BIOS level must be enabled in the BIOS settings. For more information go to [Virtualization](https://docs.docker.com/desktop/windows/install/#:~:text=more%20information%2C%20see-,Virtualization.,-Download%20and%20install).
* Download and install the [Linux kernel](https://docs.microsoft.com/windows/wsl/wsl2-kernel) update package.

**Note:** Docker only supports Docker Desktop on Windows for those versions of Windows 10 that are still within the [Microsoft service timeline](https://support.microsoft.com/en-us/help/13853/windows-lifecycle-fact-sheet).

#### Hyper-V backend and Windows containers

1) Hyper-V and Windows Containers must be enabled.

## Prerequisites

### Install Docker desktop

1) [Download Docker desktop](https://docs.docker.com/desktop/windows/install/)
2) Install following the installation wizard.

### Starting Docker desktop

Open "Docker Desktop".

1) Go to the hidden Windows icons, Docker desktop, right click, "Switch to Linux containers ...". If it says Switch to Windows containers ... proceed to the next step.

### Install Xming
1) Download a public domain version of [Xming](https://sourceforge.net/projects/xming/files/Xming/6.9.0.31/Xming-6-9-0-31-setup.exe/download).
2) Install following the installation wizard. 
3) Restart the PC.

### Starting Xming

Open "XLaunch" and adopt the following settings:

1) Select display Settings Multiple Windows, Display Number: 0
2) Select to start Xming Start no client.
3) Specify parameter settings Clipboard, No Access Control.

### Install Pulseaudio

1) Download [Pulseaudio](http://bosmans.ch/pulseaudio/pulseaudio-1.1.zip) 

**NOTE:** For some reason I had to open it in icon mode to download the zip.

2) Follow the below to open the pulseaudio server. Based on [link](https://x410.dev/cookbook/wsl/enabling-sound-in-wsl-ubuntu-let-it-sing/).

#### Unzip the files from step one.
<img src=./.docs_repo/img/unzip.png alt="" />

#### Edit 'etc\pulse\default.pa'. 
<img src=./.docs_repo/img/edit1.png alt="" />

##### NOTE: Please note that for security and privacy concerns Windows 10 (April 2018 Update) seems to restrict the access to audio recording devices. You can probably somehow override this feature, but since we just want to hear the sound we're simply disabling it from the PulseAudio server by adding the 'record=0'.
<img src=./.docs_repo/img/edit11.png alt="" />

This enables the PulseAudio server to accept connections only from 127.0.0.1 via TCP.

#### Edit 'etc\pulse\daemon.conf' 
<img src=./.docs_repo/img/edit2.png alt="" />

If this option is set to a non negative value, the server automatically terminates itself when the last client disconnects and the time is passed more than this option (in seconds).

#### Test run 'bin\pulseaudio.exe'
<img src=./.docs_repo/img/run.png alt="" />

The 'pulseaudio.exe' is the executable for PulseAudio server (also referred to as a daemon) that we need for our Linux apps.

<img src=./.docs_repo/img/run2.png alt="" />
When you first run pulseaudio.exe, you'll see the Windows Firewall Alert popup that asks you if you want to allow other devices for connecting to the server. Since we'll only be using a loopback address (= 127.0.0.1), you should select 'Cancel'; you don't have to allow other devices.

If there was an error, the server exits immediately. If that's the case, go to Step 3 and make sure you've changed the lines correctly.

Press CTRL+C to stop the server.

### Text editor

1) Install your preferred text editor.


Running the Docker container on Windows <a name="docker_windows"></a>
=======================================


* Create a folder. Ex /Desktop/Docker.
* Download the [Dockerfile](link) from the repository and save it in that folder.
* Build the container:

```
docker build -t ubuntu:gnuradio_38_2 . 
```

* Run the container:

```
docker run  --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" -e DISPLAY=$DISPLAY -i -t ubuntu:gnuradio_38_2 bash
```

NOTE: "gnuradio_38_2" refers to the name of the container.

### Inside the container you should:

1) ipconfig, save your IPv4-Adress.
2) set-variable -name DISPLAY -value "IPv4-Adress":0.0
3) export PULSE_SERVER=tcp:"IPv4-Adress"


**Congratulations, now you can use gnuradio !!**


Instructions to build the module <a name="cons_modulo"></a>
=======================================
    * mkdir build
    * cd build
    * cmake ..
    * make
    * sudo make install
    * sudo ldconfig


After running those commands within Docker, the "PDB_Block" block should appear in the "PDB" category in GNU Radio Companion.

<img src=./.docs_repo/img/pdb_block_gnu.png alt="" />