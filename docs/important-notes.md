# Important notes

First things first ...

## Frequencies

Following official operating frequencies are supported by YardStick One:

- 300-348 MHz
- 391-464 MHz
- 782-928 MHz

Following unofficial operating frequencies are supported by YardStick One:

- 281-361 MHz
- 378-481 MHz
- 749-962 MHz

_Note:_ Official operating frequencies are guaranteed to work. Unofficial operating frequencies work in our experience.

## Modulation

Following modulations are supported currently:

- MOD_2FSK (0x00)
- MOD_GFSK (0x10)
- MOD_ASK_OOK (0x30)
- MOD_MSK (0x70)
- MANCHESTER (0x08)

...

- MOD_2FSK | MANCHESTER (2FSK/Manchester encoding)
- MOD_GFSK | MANCHESTER (GFSK/Manchester encoding)
- MOD_ASK_OOK | MANCHESTER (ASK/OOK/Manchester encoding)
- MOD_MSK | MANCHESTER (MSK/Manchester encoding)

## AES modes

- ENCCS_MODE_CBC: CBC - Cipher Block Chaining
- ENCCS_MODE_CBCMAC: CBC-MAC - Cipher Block Chaining Message Authentication Code
- ENCCS_MODE_CFB: CFB - Cipher Feedback
- ENCCS_MODE_CTR: CTR - Counter
- ENCCS_MODE_ECB: ECB - Electronic Codebook
- ENCCS_MODE_OFB: OFB - Output Feedback

## Limitations of Modulation

Mostly everything is limited:

- data rates up to 500 kbps
- MSK is only supported for data rates above 26 kBaud
- GFSK, ASK and OOK is only supported for data rate up until 250 kBaud
- MSK cannot be used if Manchester encoding/decoding is enabled

[Go back](./readme.md)
