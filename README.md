## Indice
***
* [Introduccion](#introduccion)
  * [Instalacion de Software](#instalacion-de-software)
    + [Instalacion de Python](#instalacion-de-python)
    + [Instalacion de GitHub](#instalacion-de-github)
    + [Instalacion de Chrome y Chromedriver](#instalacion-de-chrome-y-chromedriver)
      - [Instalacion de Chrome](#instalacion-de-chrome)
      - [Instalacion de Chromedriver](#instalacion-de-chromedriver)
    + [Instalacion de Dependencias](#instalacion-de-dependencias)
    + [Instalacion PostgreSQL - exclusivo del maestro](#instalacion-postgresql---exclusivo-del-maestro)
  * [Configuracion de Las Maquinas](#configuracion-de-las-maquinas)
    + [Configurar Variables de Ambiente](#configurar-variables-de-ambiente)
    + [Crear Tablas Base de Datos](#crear-tablas-base-de-datos)
    + [Actualizar Copia Local del Codigo](#actualizar-copia-local-del-codigo)
    + [Instalar Servicios](#instalar-servicios)
    + [Instalar Cronjobs](#instalar-cronjobs)
  * [Logging](#logging)
    + [Cambiar Nivel del Log](#cambiar-nivel-del-log)
    + [Activar Output en la Consola](#activar-output-en-la-consola)
  * [Query de Reasignación Manual de Casos](#query-de-reasignaci-n-manual-de-casos)
***
## Instalacion de Software

### Instalacion de Python

[Seguir las instrucciones de DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-ubuntu-20-04-quickstart).

Actualizar paquetes:

    sudo apt update
    sudo apt -y upgrade


Instalar pip:

    sudo apt install -y python3-pip

Instalar herramientas adicionales:

    sudo apt install build-essential libssl-dev libffi-dev python3-dev

Instalar venv:

    sudo apt install -y python3-venv

Crear un ambiente virtual:

    python3 -m venv nombre_ambiente

Activar el ambiente virtual:


    source nombre_ambiente/bin/activate

Cada vez que se requiera correr algún código del programa, debe hacerse DESDE el ambiente virtual (es decir, cada vez 
que se abra la consola y se ejecute código python).
***

### Instalacion de Apache
 Instalar Apache:

    sudo apt update

    sudo apt install apache2

    sudo ufw app list

    sudo ufw allow 'Apache'

    sudo ufw status

    sudo systemctl status apache2

 Comprobar Apache:

    hostname -I

    curl -4 icanhazip.com
    
### Instalacion de GitHub

Instalar y configurar GitHub:
   - Se recomienda [Seguir las instrucciones de DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-20-04).

Generar una llave SSH para GitHub: 
   - [Instrucciones](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).
   - (Opcional) puedes utilizar la misma llave para las otras máquinas copiando los archivos generados (id_xxx e 
id_xxx.pub) a la carpeta `~/.ssh/` de las otras máquinas. Esto te evita generar nuevas llaves SSH y tener que agregarlas
a tu GitHub.

Agregar la llave SSH generada a tu cuenta de GitHub:
   - [Instrucciones](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?platform=linux). 
   - **Nota:** Las máquinas actualmente corriendo (y la imagen creada para los esclavos) actualmente tiene una llave
   de acceso de mi cuenta que permite hacer operaciones git. Esta llave está protegida con password. 
   

Clonar repositorio

    git clone git@github.com:OscarPoblete/empleadosPublicos.git
***
### Instalacion de Chrome y Chromedriver
Acá hay [instrucciones detalladas](https://skolo.online/documents/webscrapping/#step-1-download-chrome)
para la instalación de Chrome y su WebDriver.

#### Instalacion de Chrome

    sudo apt update
    sudo apt install zip
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo dpkg -i google-chrome-stable_current_amd64.deb

Nota: es posible que aparezca un error, esto es esperable. Continuar con el proceso.

    sudo apt-get install -f

#### Instalacion de Chromedriver
Verificar la versión instalada de Chrome:

    google-chrome --version

Buscar la versión del Chromedriver que es necesaria [en esta página](https://chromedriver.chromium.org/downloads).

(Opcional): crear una carpeta include dentro del proyecto:

    mkdir ~/OficinaVirtualPJUD_Civil/include
    cd ~/OficinaVirtualPJUD_Civil/include

Descargar Chromedriver usando wget:

    wget https://chromedriver.storage.googleapis.com/XXX.X.XXXX.XX/chromedriver_linux64.zip

Extraer el chromedriver:

    unzip chromedriver_linux64.zip
***
