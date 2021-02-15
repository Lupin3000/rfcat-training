# RfCat via command line

The value of RfCat is that you can use it via Terminal (_command line_) or via Python scripts. So here now all important topics about the work with terminal.

```shell
# run rfcat in terminal (start ipython terminal)
$ rfcat -r
```

## Getting help

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

## USB Timeouts

To prevent the unplug/plug-in of YardStick One (_after your actions like receive or transmit_) you should run always following:

```python
In [n]: d.setModeIDLE()
```

## Work with multiple dongels

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

[Go back](./readme.md)
