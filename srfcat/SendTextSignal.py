#!/usr/bin/env python

from rflib import *


class SendSignal:
    __SIGNAL_SETTINGS = {"frequency": 434000000,
                         "baud_rate": 4800,
                         "modulation": MOD_ASK_OOK,
                         "text_message": '',
                         "repeats": 0}

    def __init__(self):
        pass

    @staticmethod
    def set_frequency(value):
        """
        set frequency in MHz

        :type value: int
        :param value: integer in MHz
        """

        SendSignal.__SIGNAL_SETTINGS['frequency'] = int(value)

    @staticmethod
    def set_baud_rate(value):
        """
        set baud rate in MHz

        :type value: int
        :param value: integer in MHz
        """

        SendSignal.__SIGNAL_SETTINGS['baud_rate'] = int(value)

    @staticmethod
    def set_repeats(value):
        """
        set transmit repeats

        :type value: int
        :param value: integer for repeats
        """

        SendSignal.__SIGNAL_SETTINGS['repeats'] = int(value)

    @staticmethod
    def set_message(value):
        """
        set message to transmit

        :type value: str
        :param value: string to transmit
        """

        SendSignal.__SIGNAL_SETTINGS['text_message'] = value

    @staticmethod
    def get_debug_signal():
        """
        dump signal to STDOUT
        """
        divider = '-' * 80

        print("SIGNAL TRANSMIT INFORMATION")
        print(divider)
        print('Frequency in Hz : {0}'.format(SendSignal.__SIGNAL_SETTINGS['frequency']))
        print('Baud rate in Hz : {0}'.format(SendSignal.__SIGNAL_SETTINGS['baud_rate']))
        print('Modulation      : {0}'.format('MOD_ASK_OOK'))
        print('Text            : {0}'.format(SendSignal.__SIGNAL_SETTINGS['text_message']))
        print('Repeats         : {0}'.format(SendSignal.__SIGNAL_SETTINGS['repeats']))
        print(divider)

    @staticmethod
    def send_signal():
        """
        Transmit signal with rfcat
        """
        rfc_obj = RfCat()
        rfc_obj.setMdmModulation(MOD_ASK_OOK)
        rfc_obj.setFreq(SendSignal.__SIGNAL_SETTINGS['frequency'])
        rfc_obj.setMdmDRate(SendSignal.__SIGNAL_SETTINGS['baud_rate'])
        rfc_obj.RFxmit(SendSignal.__SIGNAL_SETTINGS['text_message'] * SendSignal.__SIGNAL_SETTINGS['repeats'])
        rfc_obj.setModeIDLE()
