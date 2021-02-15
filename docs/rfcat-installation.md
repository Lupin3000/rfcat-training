# RfCat Installation

I describe the installation "only" for Debian derivatives (_which using apt_) and macOS - I have not tried out yet on other systems. Important is that you need to decide which Python versions you wanna use and if you will enable all rfcat features plus take use of firmware updates.

## Minimum Packages

Start the installation with some "base" packages.

_Note:_ The packages `python-usb`, `libusb-1.0.0`, `make` and `sdcc` are mostly needed for firmware updates. But even if you don't want to use them yet, I would recommend to install some of them already now.

```shell
# ensure commandline tools are installed (macOS)
$ xcode-select --install

# update/upgrade your system via apt
$ apt update -y && apt upgrade -y

# install needed packages via apt
$ apt install git libusb-1.0.0
```

For macOS you can download, compile and install libusb by your self!

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

# verify installation (optional)
$ ls -la /usr/local/lib/libusb*
```

**Python2.x**

```shell
# install needed packages via apt
$ apt install -y python-pip python-usb

# install needed packages vi pip
$ pip install pyreadline libusb pyusb ipython

# for usage of specan (only macOS)
$ pip install PySide2
```

**Python3.x**

```shell
# install needed packages via apt
$ apt install -y python3-pip python3-usb

# install needed packages vi pip
$ pip3 install pyreadline libusb pyusb ipython

# for usage of specan
$ pip3 install PySide2
```

**RfCat**

The RfCat binaries will be installed on path `/usr/local/bin/`. After successful installation you will find following:

- rfcat
- rfcat_bootloader
- rfcat_msfrelay
- rfcat_server

```shell
# clone repository
$ git clone https://github.com/atlas0fd00m/rfcat.git

# change into directory (of cloned repository)
$ cd rfcat

# start compilation and installation
$ python setup.py install

# verify installed binaries (optional)
$ ls -la /usr/local/bin/rfcat*
```

**Prepare user and rules**

Normally you don't do all the actions as root user - so you need to provide minimum one user the proper rights and add this user to sudo group.

```shell
# add user to sudo group
$ usermod -a -G sudo $USER
```

You will also need permanent symlinks to the USB serial devices that will communicate with the YardStick One bootloader when required.

```shell
# copy rules from cloned repository directory
$ sudo cp etc/udev/rules.d/20-rfcat.rules /etc/udev/rules.d

# reload the udev rules
$ sudo udevadm control --reload-rules
```

## Packages for firmware updates

The packages `make` and `sdcc` are needed if you will do updates or compile and install new firmware on the dongle. Important here is newer/higher version of sdcc (_max. 3.5.0_) will not work!

```shell
# install via apt
$ apt install make sdcc=3.5.0
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

# show version (optional)
$ sdcc --version
```
