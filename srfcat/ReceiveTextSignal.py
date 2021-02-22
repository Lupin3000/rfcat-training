#!/usr/bin/env python

from rflib import *


class ReceiveSignal:

    __SIGNAL_SETTINGS = {"frequency": 434000000,
                         "baud_rate": 4800,
                         "modulation": MOD_ASK_OOK,
                         "lowball": False,
                         "max_power": False}

    def __init__(self):
        pass

    @staticmethod
    def set_frequency(value):
        """
        set frequency in MHz

        :type value: int
        :param value: integer in MHz
        """

        ReceiveSignal.__SIGNAL_SETTINGS['frequency'] = int(value)

    @staticmethod
    def set_baud_rate(value):
        """
        set baud rate in MHz

        :type value: int
        :param value: integer in MHz
        """

        ReceiveSignal.__SIGNAL_SETTINGS['baud_rate'] = int(value)

    @staticmethod
    def set_lowball(value):
        """
        set lowball

        :type value: bool
        :param value: true or false
        """

        ReceiveSignal.__SIGNAL_SETTINGS['lowball'] = bool(value)

    @staticmethod
    def set_max_power(value):
        """
        set max power

        :type value: bool
        :param value: true or false
        """

        ReceiveSignal.__SIGNAL_SETTINGS['max_power'] = bool(value)

    @staticmethod
    def get_debug_signal():
        """
        dump signal to STDOUT
        """
        divider = '-' * 80

        print("SIGNAL RECEIVE INFORMATION")
        print(divider)
        print('Frequency in MHz : {0}'.format(ReceiveSignal.__SIGNAL_SETTINGS['frequency']))
        print('Baud rate in MHz : {0}'.format(ReceiveSignal.__SIGNAL_SETTINGS['baud_rate']))
        print('Modulation       : {0}'.format('MOD_ASK_OOK'))
        print('LOWBALL          : {0}'.format(ReceiveSignal.__SIGNAL_SETTINGS['lowball']))
        print('MAX POWER        : {0}'.format(ReceiveSignal.__SIGNAL_SETTINGS['max_power']))
        print(divider)

    @staticmethod
    def get_signal():
        """
        Receive signal with rfcat
        """
        rfc_obj = RfCat()
        rfc_obj.setMdmModulation(MOD_ASK_OOK)
        rfc_obj.setFreq(ReceiveSignal.__SIGNAL_SETTINGS['frequency'])
        rfc_obj.setMdmDRate(ReceiveSignal.__SIGNAL_SETTINGS['baud_rate'])
        if ReceiveSignal.__SIGNAL_SETTINGS['lowball']:
            rfc_obj.lowball()
        if ReceiveSignal.__SIGNAL_SETTINGS['max_power']:
            rfc_obj.setMaxPower()
        rfc_obj.lowball()
        rfc_obj.RFlisten()
        rfc_obj.setModeIDLE()
