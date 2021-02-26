# RfCat notes

## Modulation

setMdmModulation(self, mod, radiocfg=None, invert=False)

```python
# set modulation
In [1]: d.setMdmModulation()

# set modulation ASK/OOK
In [1]: d.setMdmModulation(MOD_ASK_OOK)

# get current modulation
In [2]: d.getMdmModulation()
```
- MSK
cannot be used if Manchester encoding/decoding is enabled
  

- MOD_2FSK
- MOD_GFSK
- MOD_ASK_OOK
- MOD_MSK
- MANCHESTER
- MOD_2FSK | MANCHESTER (2FSK/Manchester encoding)
- MOD_GFSK | MANCHESTER (GFSK/Manchester encoding)
- MOD_ASK_OOK | MANCHESTER (ASK/OOK/Manchester encoding)

## Frequency

setFreq(self, freq=902000000, mhz=24, radiocfg=None, applyConfig=True)

```python
# set frequency
In [1]: d.setFreq()

# set frequency 434.500 MHz
In [1]: d.setFreq(434500000)

# get current frequency
In [2]: d.getFreq()
```

Official operating frequencies (_YardStick One_):

- 300-348 MHz
- 391-464 MHz
- 782-928 MHz

Unofficial operating frequencies (_YardStick One_):

- 281-361 MHz
- 378-481 MHz
- 749-962 MHz

## Baud Rate

setMdmDRate(self, drate, mhz=24, radiocfg=None)

```python
# set baud rate
In [1]: d.setMdmDRate()

# set baud rate 4800 Baud
In [1]: d.setMdmDRate(4800)

# get current baud rate
In [2]: d.getMdmDRate()
```

- MSK is only supported for data rates above 26 kBaud
- GFSK,ASK and OOK is only supported for data rate up until 250 kBaud

## Package length

makePktFLEN(self, flen=255, radiocfg=None)

```python
# set package length
In [1]: d.makePktFLEN()

# set package length 6
In [1]: d.makePktFLEN(6)
```

## Deviation

setMdmDeviatn(self, deviatn, mhz=24, radiocfg=None)

```python
# set deviation
In [1]: d.setMdmDeviatn()

# set deviation 37.5 kHz
In [1]: d.setMdmDeviatn(37500)

# get deviation
In [2]: d.getMdmDeviatn()
```

## Preamble

setMdmNumPreamble(self, preamble=32, radiocfg=None)

```python
# set preamble
In [1]: setMdmNumPreamble()

# set preamble to 255
In [1]: setMdmNumPreamble(255)

# get preamble
In [2]: getMdmNumPreamble()
```

## Sync Word

setMdmSyncWord(self, word, radiocfg=None)

```python
In [1]: d.setMdmSyncWord()

In [1]: d.setMdmSyncWord(0xcccc)

In [2]: d.getMdmSyncWord()
```

## Sync Mode

setMdmSyncMode(self, syncmode=1, radiocfg=None)

```python
# set sync mode
In [1]: d.setMdmSyncMode()

# disable sync word and preamble
In [1]: d.setMdmSyncMode(0)

# get current sync mode
In [2]: d.getMdmSyncMode()
```

- SYNCM_NONE: "None",
- SYNCM_15_of_16: "15 of 16 bits must match"
- SYNCM_16_of_16: "16 of 16 bits must match"
- SYNCM_30_of_32: "30 of 32 sync bits must match"
- SYNCM_CARRIER: "Carrier Detect"
- SYNCM_CARRIER_15_of_16: "Carrier Detect and 15 of 16 sync bits must match"
- SYNCM_CARRIER_16_of_16: "Carrier Detect and 16 of 16 sync bits must match"
- SYNCM_CARRIER_30_of_32: "Carrier Detect and 30 of 32 sync bits must match"

## Channel

setChannel(self, channr, radiocfg=None)

```python
# set channel
In [1]: d.setChannel()

# set channel 0
In [1]: d.setChannel(0)

# get current channel
In [2]: d.getChannel()
```

## Channel Bandwidth

setMdmChanBW(self, bw, mhz=24, radiocfg=None)

```python
# set channel bandwidth
In [1]: d.setMdmChanBW()

# set channel bandwidth 125k
In [1]: d.setMdmChanBW(125000)

# get current channel bandwidth
In [2]: d.getMdmChanBW()
```

## Channel spacing

setMdmChanSpc(self, chanspc=None, chanspc_m=None, chanspc_e=None, mhz=24, radiocfg=None)

```python
# set channel spacing
In [1]: d.setMdmChanSpc()

# set channel spacing 24000 kHz
In [1]: d.setMdmChanSpc(24000)

# get current channel spacing
In [2]: d.getMdmChanSpc()
```

## lowball

lowball(self, level=1, sync=43690, length=250, pqt=0, crc=False, fec=False, datawhite=False)

```python
#
In [1]: d.lowball()
```

- level == 0 changes the Sync Mode to SYNCM_NONE (wayyy more garbage)
- level == 1 (default) sets the Sync Mode to SYNCM_CARRIER (requires a valid carrier detection for the data to be considered a packet)
- level == 2 sets the Sync Mode to SYNCM_CARRIER_15_of_16 (requires a valid carrier detection and 15 of 16 bits of SYNC WORD match for the data to be considered a packet)
- level == 3 sets the Sync Mode to SYNCM_CARRIER_16_of_16 (requires a valid carrier detection and 16 of 16 bits of SYNC WORD match for the data to be considered a packet)

## Power

setPower(self, power=None, radiocfg=None, invert=False)

```python
# set power level
In [1]: d.setPower()

# set power level 100
In [1]: d.setPower(100)
```

## Max Power

setMaxPower(self, radiocfg=None, invert=False)

```python
# enable max power
In [1]: d.setMaxPower()
```

## Send

RFxmit(self, data, repeat=0, offset=0)

```python
# start transmit
In [1]: d.RFxmit()
```
