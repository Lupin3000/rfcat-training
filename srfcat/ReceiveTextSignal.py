#!/usr/bin/env python

from rflib import *


class ReceiveSignal:

    __FREQUENCY = 434000000
    __BAUD_RATE = 4800
    __MODULATION = MOD_ASK_OOK

    def __init__(self):
        pass

    @staticmethod
    def set_frequency(value):
        """
        set frequency in MHz

        :type value: int
        :param value: integer in MHz
        """

        ReceiveSignal.__FREQUENCY = int(value)

    @staticmethod
    def set_baud_rate(value):
        """
        set baud rate in MHz

        :type value: int
        :param value: integer in MHz
        """

        ReceiveSignal.__BAUD_RATE = int(value)

    @staticmethod
    def get_debug_signal():
        """
        dump signal to STDOUT
        """

        divider = '-' * 80
        print("SIGNAL INFORMATION")
        print(divider)
        print('Frequency in Hz : {0}'.format(ReceiveSignal.__FREQUENCY))
        print('Baud rate in Hz : {0}'.format(ReceiveSignal.__BAUD_RATE))
        print('Modulation      : {0}'.format('MOD_ASK_OOK'))
        print(divider)

    @staticmethod
    def get_signal():
        """

        """
        rfc_obj = RfCat()
        rfc_obj.setMdmModulation(MOD_ASK_OOK)
        rfc_obj.setFreq(ReceiveSignal.__FREQUENCY)
        rfc_obj.setMdmDRate(ReceiveSignal.__BAUD_RATE)
        rfc_obj.setMaxPower()
        rfc_obj.lowball()
        rfc_obj.RFlisten()
        rfc_obj.setModeIDLE()
