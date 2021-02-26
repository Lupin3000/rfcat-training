#!/usr/bin/env python

from rflib import *
import sys


class ReceiveSignal:
    __SIGNAL_SETTINGS = {"frequency": 434000000,
                         "baud_rate": 4800,
                         "lowball": False,
                         "max_power": False}
    # __SIGNAL_OBJ = RfCat(idx=0)
    __SIGNAL_OBJ = RfCat()

    def __init__(self):
        ReceiveSignal.__SIGNAL_OBJ.setMdmModulation(MOD_ASK_OOK)

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

        if ReceiveSignal.__verify_range(*checklist):
            ReceiveSignal.__SIGNAL_SETTINGS['frequency'] = int(value)
            ReceiveSignal.__SIGNAL_OBJ.setFreq(int(value))
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

        if ReceiveSignal.__verify_range(*checklist):
            ReceiveSignal.__SIGNAL_SETTINGS['baud_rate'] = int(value)
            ReceiveSignal.__SIGNAL_OBJ.setMdmDRate(int(value))
        else:
            sys.stdout.write("Error: baud rate {} not between {} and {}".format(*checklist))
            sys.exit(2)

    @staticmethod
    def set_lowball(value):
        """
        set lowball

        :type value: bool
        :param value: true or false
        """
        ReceiveSignal.__SIGNAL_SETTINGS['lowball'] = bool(value)

        if bool(value) and isinstance(value, bool):
            ReceiveSignal.__SIGNAL_OBJ.lowball()

    @staticmethod
    def set_max_power(value):
        """
        set max power

        :type value: bool
        :param value: true or false
        """
        ReceiveSignal.__SIGNAL_SETTINGS['max_power'] = bool(value)

        if bool(value) and isinstance(value, bool):
            ReceiveSignal.__SIGNAL_OBJ.setMaxPower()

    @staticmethod
    def get_signal_dump():
        """
        dump signal information to STDOUT
        """
        divider = '-' * 80
        frequency = [ReceiveSignal.__SIGNAL_SETTINGS['frequency'], ReceiveSignal.__SIGNAL_OBJ.getFreq()]
        baud_rate = [ReceiveSignal.__SIGNAL_SETTINGS['baud_rate'], ReceiveSignal.__SIGNAL_OBJ.getMdmDRate()]

        print("SIGNAL RECEIVE INFORMATION")
        print(divider)
        print('== Frequency Configuration ==')
        print("Frequency          : {0} MHz - {1} MHz".format(frequency[0], frequency[1][0]))
        print("Channel            : {0}".format(ReceiveSignal.__SIGNAL_OBJ.getChannel()))
        print("\n== Modem Configuration ==")
        print("Modulation         : {0}".format(ReceiveSignal.__SIGNAL_OBJ.getMdmModulation()))
        print("Baud rate          : {0} MHz - {1} MHz".format(baud_rate[0], baud_rate[1]))
        print("Channel bandwidth  : {0} MHz".format(ReceiveSignal.__SIGNAL_OBJ.getMdmChanBW()))
        print("Channel spacing      : {0} MHz".format(ReceiveSignal.__SIGNAL_OBJ.getMdmChanSpc()))
        print("Deviation          : {0} MHz".format(ReceiveSignal.__SIGNAL_OBJ.getMdmDeviatn()))
        print("Sync Mode          : {0}".format(ReceiveSignal.__SIGNAL_OBJ.getMdmSyncMode()))
        print("Preamble           : {0}".format(ReceiveSignal.__SIGNAL_OBJ.getMdmNumPreamble()))
        print('Lowball            : {0}'.format(ReceiveSignal.__SIGNAL_SETTINGS['lowball']))
        print('Max Power          : {0}'.format(ReceiveSignal.__SIGNAL_SETTINGS['max_power']))
        print("\n== Packet Configuration ==")
        print("Sync Word          : {0}".format(ReceiveSignal.__SIGNAL_OBJ.getMdmSyncWord()))
        print(divider)

    @staticmethod
    def get_signal():
        """
        receive signal with rfcat
        """
        print('... start listen')
        ReceiveSignal.__SIGNAL_OBJ.RFlisten()

        print('... set USB Dongle idle')
        ReceiveSignal.__SIGNAL_OBJ.setModeIDLE()


# for debug only
# if __name__ == '__main__':
#     receive_rf = ReceiveSignal()
#     receive_rf.set_frequency(868000000)
#     receive_rf.set_baud_rate(4800)
#     receive_rf.set_lowball(True)
#     receive_rf.set_max_power(True)
#     receive_rf.get_signal_dump()
#     receive_rf.get_signal()
#     sys.exit(0)
# else:
#     sys.exit(1)
