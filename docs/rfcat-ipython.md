# RfCat (ipython)

**Show RfCat-IPython help**

```python
# show help
In [0]: help(d.setMdmModulation)

# show current settings (optional)
In [2]: print(d.reprRadioConfig())
```

## USB Timeouts

_Note:_ To prevent the unplug/plug-in of YardStick One (_after your actions like receive or transmit_).

```python
# set idle mode
In [n]: d.setModeIDLE()
```

## Spectrum Analyzer

```shell
# start spectrum analyzer without frequency
In [1]: d.specan()

# set frequency
In [2]: d.specan(413000000)
```

![RfCat Spectrum Analyzer](../img/rfcat-spectrum_analyzer.png)

## Work with multiple dongels

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

[Go back](./readme.md)
