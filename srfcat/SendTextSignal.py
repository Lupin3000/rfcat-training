#!/usr/bin/env python

from rflib import *
import sys


class SendSignal:
    __SIGNAL_SETTINGS = {"frequency": 434000000,
                         "baud_rate": 4800,
                         "modulation": "ASK/OOK",
                         "text_message": '',
                         "repeats": 0}

    def __init__(self):
        pass

    @staticmethod
    def __verify_range(value, minimum, maximum):
        """
        verify frequency inside given range

        :type value: int
        :param value: value of frequency to verify
        :type minimum: int
        :param minimum: minimum value to verify
        :type maximum: int
        :param maximum: maximum value to verify

        :return: bool
        """
        if value in range(minimum, maximum):
            return True
        else:
            return False

    @staticmethod
    def set_frequency(value):
        """
        set frequency in MHz

        :type value: int
        :param value: integer in MHz
        """
        min_yst = 300000000
        max_yst = 928000000
        checklist = [int(value), min_yst, max_yst]

        if SendSignal.__verify_range(*checklist):
            SendSignal.__SIGNAL_SETTINGS['frequency'] = int(value)
        else:
            sys.stdout.write("Error {} not between {} and {}".format(*checklist))
            sys.exit(2)

    @staticmethod
    def set_baud_rate(value):
        """
        set baud rate in MHz

        :type value: int
        :param value: integer in MHz
        """
        min_yst = 210
        max_yst = 250000
        checklist = [int(value), min_yst, max_yst]

        if SendSignal.__verify_range(*checklist):
            SendSignal.__SIGNAL_SETTINGS['baud_rate'] = int(value)
        else:
            sys.stdout.write("Error: baud rate {} not between {} and {}".format(*checklist))
            sys.exit(2)

    @staticmethod
    def set_repeats(value):
        """
        set transmit repeats

        :type value: int
        :param value: integer for repeats
        """
        minimum = 0
        maximum = 50
        checklist = [int(value), minimum, maximum]

        if SendSignal.__verify_range(*checklist):
            SendSignal.__SIGNAL_SETTINGS['repeats'] = int(value)
        else:
            sys.stdout.write("Error: repeats {} not between {} and {}".format(*checklist))
            sys.exit(2)

    @staticmethod
    def set_message(value):
        """
        set message to transmit

        :type value: str
        :param value: string to transmit
        """

        SendSignal.__SIGNAL_SETTINGS['text_message'] = value.strip()

    @staticmethod
    def get_signal_dump():
        """
        dump signal information to STDOUT
        """
        divider = '-' * 80

        print("SIGNAL TRANSMIT INFORMATION")
        print(divider)
        print('Frequency in Hz : {0}'.format(SendSignal.__SIGNAL_SETTINGS['frequency']))
        print('Baud rate in Hz : {0}'.format(SendSignal.__SIGNAL_SETTINGS['baud_rate']))
        print('Modulation      : {0}'.format(SendSignal.__SIGNAL_SETTINGS['modulation']))
        print('Text            : {0}'.format(SendSignal.__SIGNAL_SETTINGS['text_message']))
        print('Repeats         : {0}'.format(SendSignal.__SIGNAL_SETTINGS['repeats']))
        print(divider)

    @staticmethod
    def send_signal():
        """
        transmit signal with rfcat
        """
        rfc_obj = RfCat()
        # @ToDo: create set method for modulation
        rfc_obj.setMdmModulation(MOD_ASK_OOK)
        rfc_obj.setFreq(SendSignal.__SIGNAL_SETTINGS['frequency'])
        rfc_obj.setMdmDRate(SendSignal.__SIGNAL_SETTINGS['baud_rate'])
        rfc_obj.RFxmit(SendSignal.__SIGNAL_SETTINGS['text_message'] * SendSignal.__SIGNAL_SETTINGS['repeats'])
        rfc_obj.setModeIDLE()
