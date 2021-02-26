#!/usr/bin/env python

from rflib import *
import sys


class SendSignal:
    __SIGNAL_SETTINGS = {"frequency": 434000000,
                         "baud_rate": 4800,
                         "text_message": '',
                         "repeats": 0}
    # __SIGNAL_OBJ = RfCat(idx=1)
    __SIGNAL_OBJ = RfCat()

    def __init__(self):
        SendSignal.__SIGNAL_OBJ.setMdmModulation(MOD_ASK_OOK)

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
        # user input, minimum, maximum
        checklist = [int(value), 300000000, 928000000]

        if SendSignal.__verify_range(*checklist):
            SendSignal.__SIGNAL_SETTINGS['frequency'] = int(value)
            SendSignal.__SIGNAL_OBJ.setFreq(int(value))
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
        # user input, minimum, maximum
        checklist = [int(value), 210, 250000]

        if SendSignal.__verify_range(*checklist):
            SendSignal.__SIGNAL_SETTINGS['baud_rate'] = int(value)
            SendSignal.__SIGNAL_OBJ.setMdmDRate(int(value))
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
        # user input, minimum, maximum
        checklist = [int(value), 0, 50]

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
        frequency = [SendSignal.__SIGNAL_SETTINGS['frequency'], SendSignal.__SIGNAL_OBJ.getFreq()]
        baud_rate = [SendSignal.__SIGNAL_SETTINGS['baud_rate'], SendSignal.__SIGNAL_OBJ.getMdmDRate()]

        print("SIGNAL TRANSMIT INFORMATION")
        print(divider)
        print('== Frequency Configuration ==')
        print("Frequency          : {0} MHz - {1} MHz".format(frequency[0], frequency[1][0]))
        print("Channel            : {0}".format(SendSignal.__SIGNAL_OBJ.getChannel()))
        print("\n== Modem Configuration ==")
        print("Modulation         : {0}".format(SendSignal.__SIGNAL_OBJ.getMdmModulation()))
        print("Baud rate          : {0} MHz - {1} MHz".format(baud_rate[0], baud_rate[1]))
        print("Channel bandwidth  : {0} MHz".format(SendSignal.__SIGNAL_OBJ.getMdmChanBW()))
        print("Channel spacing    : {0} MHz".format(SendSignal.__SIGNAL_OBJ.getMdmChanSpc()))
        print("Deviation          : {0} MHz".format(SendSignal.__SIGNAL_OBJ.getMdmDeviatn()))
        print("Sync Mode          : {0}".format(SendSignal.__SIGNAL_OBJ.getMdmSyncMode()))
        print("Preamble           : {0}".format(SendSignal.__SIGNAL_OBJ.getMdmNumPreamble()))
        print("\n== Packet Configuration ==")
        print("Sync Word          : {0}".format(SendSignal.__SIGNAL_OBJ.getMdmSyncWord()))
        print("\n== Signal ==")
        print("Text               : {0}".format(SendSignal.__SIGNAL_SETTINGS['text_message']))
        print("Repeats            : {0}".format(SendSignal.__SIGNAL_SETTINGS['repeats']))
        print(divider)

    @staticmethod
    def send_signal():
        """
        transmit signal with rfcat
        """
        print("... run {0} transmission".format(SendSignal.__SIGNAL_SETTINGS['repeats']))
        SendSignal.__SIGNAL_OBJ.RFxmit(SendSignal.__SIGNAL_SETTINGS['text_message'] *
                                       SendSignal.__SIGNAL_SETTINGS['repeats'])
        print('... set USB Dongle idle')
        SendSignal.__SIGNAL_OBJ.setModeIDLE()


# for debug only
# if __name__ == '__main__':
#     send_rf = SendSignal()
#     send_rf.set_frequency(434000000)
#     send_rf.set_baud_rate(4800)
#     send_rf.set_message('Hello World from RfCat...')
#     send_rf.set_repeats(10)
#     send_rf.get_signal_dump()
#     send_rf.send_signal()
#     sys.exit(0)
# else:
#     sys.exit(1)
