# YardStick One + RfCat Documentation

As I could not find any online documentations - I started to write my own. I'm new to this whole topic and try my best to be so correct as possible. Please feel free to add or correct me!

_Note:_ This documentation is more about [YardStick One](https://greatscottgadgets.com/yardstickone/) and [RfCat](https://github.com/atlas0fd00m/rfcat)! YardStick One comes with RfCat firmware installed and also has CC Bootloader installed, so you can upgrade RFCat or install your own firmware without any additional programming hardware.

## Important notes

First things first ...

### Frequencies

Following official operating frequencies are supported by YardStick One:

- 300-348 MHz
- 391-464 MHz
- 782-928 MHz

Following unofficial operating frequencies are supported by YardStick One:

- 281-361 MHz
- 378-481 MHz
- 749-962 MHz

_Note:_ Official operating frequencies are guaranteed to work. Unofficial operating frequencies work in our experience.

### Modulation

Following modulations are supported currently:

- MOD_2FSK (0x00)
- MOD_GFSK (0x10)
- MOD_ASK_OOK (0x30)
- MOD_MSK (0x70)
- MANCHESTER (0x08)

### Limitations of Modulation

Mostly everything is limited:

- data rates up to 500 kbps
- MSK is only supported for data rates above 26 kBaud
- GFSK, ASK and OOK is only supported for data rate up until 250 kBaud
- MSK cannot be used if Manchester encoding/decoding is enabled

## RfCat Installation

I describe the installation "only" for Debian Derivatives and macOS - I have not tried out yet on other systems. Important is that you need to decide which Python versions you wanna use and if you will enable all rfcat features plus take use of firmware updates.

### Minimum Packages

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

### Packages for firmware updates

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

## RfCat via command line

The value of RfCat is that you can use it via Terminal (_command line_) or via Python scripts. So here now all important about the work with Terminal.

```shell
# run rfcat in terminal (start ipython terminal)
$ rfcat -r
```

### Getting help

Take use of RfCat (_binary_) help!

```shell
# show rfcat help
$ rfcat -h

# show rfcat_bootloader help
$ rfcat_bootloader --help
```

Take use of internal IPython RfCat help!

```python
# show help
In [0]: help(d.setMdmModulation)

# show current settings (optional)
In [2]: print(d.reprRadioConfig())
```

### USB Timeouts

To prevent the unplug/plug-in of YardStick One (_after your actions like receive or transmit_) you should run always following:

```python
In [n]: d.setModeIDLE()
```

### Work with multiple dongels

If you work on same device with more then one YardStick One (_Dongle_):

```shell
$ sudo rfcat -i 0 -r
```

1st interactive IPython terminal:

```python
In [0]: d.setFreq(434000000)
In [1]: d.setMdmModulation(MOD_ASK_OOK)
In [2]: print(d.reprRadioConfig())
```

```shell
$ sudo rfcat -i 1 -r
```

2nd interactive IPython terminal:

```python
In [0]: d.setFreq(868000000)
In [1]: d.setMdmModulation(MOD_2FSK)
In [2]: print(d.reprRadioConfig())
```

... will continue soon ...
