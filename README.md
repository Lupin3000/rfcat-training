# rfcat-training
RfCat classes for training

**Notes**

Ensure [RfCat](https://github.com/atlas0fd00m/rfcat) and all needed libraries are installed! Insert the RfCat dongle before using this script. Please follow all local, state, federal, and international laws. The author of this code take no responsibility for your use or misuse.

## SendSignal.py

This Python script (_[SendSignal.py](./classes/SendSignal.py)_) is for sending a simple text message (_currently just as MOD_ASK_OOK_). See usage for all information.

### Usage

```shell
# show help
$ SendSignal.py -h

# send signal with defaults
$ SendSignal.py 'HelloWorld'

# send signal (with specific frequency and baut rate)
$ SendSignal.py 'HelloWorld' -f 868000000 -b 2000

# send signal (with specific padding and repeats)
$ SendSignal.py 'HelloWorld' -p 3 -r 5

# send signal (with specific frequency, baut, padding, repeats and max power)
$ SendSignal.py 'HelloWorld' -f 434300000 -b 2000 -p 2 -r 3 -m

# send signal with verbose mode (Info)
$ SendSignal.py 'HelloWorld' -v

# send signal with verbose mode (Debug)
$ SendSignal.py 'HelloWorld' -vv
```
