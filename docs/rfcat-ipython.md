# RfCat (ipython)

## Start rfcat-ipython terminal (Single Dongle)

```shell
# start rfcat-ipython
$ sudo rfcat -r
```

Interactive Python with the "d" instance to talk to

## Start rfcat-ipython (Multiple dongels)

**ttys000**

```shell
# start rfcat-ipython
$ sudo rfcat -i 0 -r
```

```python
# set frequency
In [1]: d.setFreq(434000000)

# set modulation
In [2]: d.setMdmModulation(MOD_ASK_OOK)

# print current configuration
In [3]: print(d.reprRadioConfig())
```

**ttys001**

```shell
$ sudo rfcat -i 1 -r
```

```python
# set frequency
In [1]: d.setFreq(868000000)

# set modulation
In [2]: d.setMdmModulation(MOD_2FSK)

# print current configuration
In [3]: print(d.reprRadioConfig())
```

## rfcat-ipython help

```python
# print help
In [1]: help(d.setMdmModulation)
```

## USB Timeouts

_Note:_ To prevent the unplug/plug-in (_after your actions like receive or transmit_).

```python
# set idle mode
In [n]: d.setModeIDLE()
```

## Spectrum Analyzer

```python
# start spectrum analyzer without frequency
In [1]: d.specan()

# set frequency
In [2]: d.specan(434000000)
```

![RfCat Spectrum Analyzer](../img/rfcat-spectrum_analyzer.png)

## Receive signal (print to terminal)

```python
# set frequency
In [1]: d.setFreq(434000000)

# set modulation
In [2]: d.setMdmModulation(MOD_ASK_OOK)

# set baud rate
In [3]: d.setMdmDRate(4800)

# drops most blocks to pkts (CARRIER)
In [4]: d.lowball()

# enable max power
In [5]: d.setMaxPower()

# start listen and dump data to screen
In [6]: d.RFlisten()

...

# set idle mode
In [7]: d.setModeIDLE()
```

## Send signal

```python
# set frequency
In [1]: d.setFreq(434000000)

# set modulation
In [2]: d.setMdmModulation(MOD_ASK_OOK)

# set baud rate
In [3]: d.setMdmDRate(4800)

# send signal
In [4]: d.RFxmit("\xA2\x03\xB4\x42\x10\xA4\xE5\x38\x00\x00\x00\x00\x00\x00" * 10)

...

# set idle mode
In [5]: d.setModeIDLE()
```


... will continue soon ...

[Go back](./readme.md)
