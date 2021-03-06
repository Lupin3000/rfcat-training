# RfCat Installation

## Preparation

**Debian**

```shell
# update/upgrade system
$ apt update -y && apt upgrade -y

# install some base packages
$ apt install -y git tar curl python3-pip

# install virtualenv (optional)
$ sudo pip3 install virtualenv

# add user to sudo group
$ usermod -a -G sudo $USER
```

**macOS**

```shell
# install commandline tools
$ sudo xcode-select --install

# install pip (Python2.7)
$ sudo easy_install pip

# install virtualenv (optional)
$ sudo pip install virtualenv
```

## Install RfCat (Minimal)

```shell
# clone repository
$ git clone https://github.com/atlas0fd00m/rfcat.git

# change into directory (of cloned repository)
$ cd rfcat

# copy rules from cloned repository directory (not on macOS)
$ sudo cp etc/udev/rules.d/20-rfcat.rules /etc/udev/rules.d

# reload the udev rules (not on macOS)
$ sudo udevadm control --reload-rules

# show some information (optional) 
$ ls -la && cat requirements.txt

# show local python information (optional)
$ ls -la /usr/bin/ | grep -i "python"
```

**Python 3 (_Debian/macOS_)**

```shell
# install needed packages
$ sudo pip3 install pyreadline ipython numpy

# start rfcat installation (repo folder)
$ sudo python3 setup.py install
```

**Python 2 (_macOS_)**

```shell
# install needed packages 
$ sudo pip install pyreadline ipython numpy

# start rfcat installation (repo folder)
$ sudo python setup.py install
```

## Verify minimal installation

RfCat binaries will be installed on path `/usr/local/bin/`:

- rfcat
- rfcat_bootloader
- rfcat_msfrelay
- rfcat_server

```shell
# verify installed binaries (optional)
$ ls -la /usr/local/bin/rfcat*

# show help (optional)
$ /usr/local/bin/rfcat --help
```

**Python 3 (_Debian/macOS_)**

```shell
# show installed packages (optional)
$ pip3 freeze

# filter output (optional)
$ pip3 freeze | grep -i "rfcat\|ipython\|pyreadline"
```

**Python 2 (_macOS_)**

```shell
# show installed packages (optional)
$ pip freeze

# filter output (optional)
$ pip freeze | grep -i "rfcat\|ipython\|pyreadline"
```

## Install RfCat: spectrum scan packages

**Python 3 (_Debian/macOS_)**

```shell
# start installation
$ sudo pip3 install PySide2
```

**Python 2 (_macOS_)**

```shell
# start installation
$ sudo pip install PySide2
```

## Verify packages for spectrum scan

**Python 3 (_Debian/macOS_)**

```shell
# show installed packages (optional) 
$ sudo pip3 freeze

# filter output (optional) 
$ sudo pip3 freeze | grep -i "pyside2"
```

**Python 2 (_macOS_)**

```shell
# show installed packages (optional) 
$ sudo pip freeze

# filter output (optional) 
$ sudo pip freeze | grep -i "pyside2"
```

## Install RfCat: bootloader/firmware update packages

## Install libraries for USB

**Debian**

```shell
# install needed packages via apt
$ apt install -y make libusb-1.0.0 python3-usb
```

**macOS**

```shell
# download via curl
$ curl -L -C - "https://github.com/libusb/libusb/releases/download/v1.0.24/libusb-1.0.24.tar.bz2"

# unzip archive
$ tar -xf libusb-1.0.24.tar.bz2

# change into extraced archive directory
$ cd libusb-1.0.24

# verify dependencies for build and install process are available
$ ./configure

# run build
$ make

# run installation
$ sudo make install
```

**Python 3 (_Debian/macOS_)**

```shell
# install python usb packages
$ sudo pip3 install libusb pyusb
```

**Python 2 (_macOS_)**

```shell
# install python usb packages
$ sudo pip install libusb pyusb
```

## Verify USB installation

```shell
# verify installation (optional)
$ ls -la /usr/local/lib/libusb*
```

**Python 3 (_Debian/macOS_)**

```shell
# show installed packages (optional)
$ sudo pip3 freeze

# filter output (optional)
$ sudo pip3 freeze | grep -i "libusb\|pyusb"
```

**Python 2 (_macOS_)**

```shell
# show installed packages (optional)
$ sudo pip freeze

# filter output (optional)
$ sudo pip freeze | grep -i "libusb\|pyusb"
```

## Install libraries for sdcc

**Debian**

```shell
# start installation
$ sudo apt install -y sdcc=3.5.0
```

If your package manager complain about the version you can take use of [Debian Stretch Repository](https://packages.debian.org/stretch/sdcc).

```shell
# download sdcc-libraries package (version 3.5.0)
$ curl -l -C- http://ftp.de.debian.org/debian/pool/main/s/sdcc/sdcc-libraries_3.5.0+dfsg-2_all.deb -o sdcc-libraries_3.5.0+dfsg-2_all.deb

# download sdcc package (version 3.5.0)
$ curl -l -C- http://ftp.de.debian.org/debian/pool/main/s/sdcc/sdcc_3.5.0+dfsg-2+b1_amd64.deb -o sdcc_3.5.0+dfsg-2+b1_amd64.deb

# install sdcc-libraries
$ sudo dpkg -i sdcc-libraries_3.5.0+dfsg-2_all.deb

# install sdcc package
$ sudo dpkg -i sdcc_3.5.0+dfsg-2+b1_amd64.deb
```

## Verify sdcc installation

```shell
# show version (optional)
$ sdcc --version
```

[Go back](./readme.md)
