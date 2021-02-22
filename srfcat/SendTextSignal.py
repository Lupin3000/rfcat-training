#!/usr/bin/env python

from rflib import *


class SendSignal:

    __FREQUENCY = 434000000
    __BAUD_RATE = 4800
    __TEXT_MESSAGE = str()
    __MODULATION = MOD_ASK_OOK
    __REPEATS = 10

    def __init__(self):
        pass

    @staticmethod
    def set_frequency(value):
        """
        set frequency in MHz

        :type value: int
        :param value: integer in MHz
        """

        SendSignal.__FREQUENCY = int(value)

    @staticmethod
    def set_baud_rate(value):
        """
        set baud rate in MHz

        :type value: int
        :param value: integer in MHz
        """

        SendSignal.__BAUD_RATE = int(value)

    @staticmethod
    def set_message(value):
        """
        set message to transmit

        :type value: str
        :param value: string to transmit
        """

        SendSignal.__TEXT_MESSAGE = value

    @staticmethod
    def get_debug_signal():
        """
        dump signal to STDOUT
        """

        divider = '-' * 80
        print("SIGNAL INFORMATION")
        print(divider)
        print('Frequency in Hz : {0}'.format(SendSignal.__FREQUENCY))
        print('Baud rate in Hz : {0}'.format(SendSignal.__BAUD_RATE))
        print('Modulation      : {0}'.format('MOD_ASK_OOK'))
        print('Text            : {0}'.format(SendSignal.__TEXT_MESSAGE))
        print('Repeats         : {0}'.format(SendSignal.__REPEATS))
        print(divider)

    @staticmethod
    def send_signal():
        rfc_obj = RfCat()
        rfc_obj.setMdmModulation(MOD_ASK_OOK)
        rfc_obj.setFreq(SendSignal.__FREQUENCY)
        rfc_obj.setMdmDRate(SendSignal.__BAUD_RATE)
        rfc_obj.RFxmit(SendSignal.__TEXT_MESSAGE * SendSignal.__REPEATS)
        rfc_obj.setModeIDLE()
