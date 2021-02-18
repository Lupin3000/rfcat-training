#!/usr/bin/env python

import logging
import argparse
import sys
import binascii
from datetime import datetime
from rflib import *


class SendSignal(object):

    def __init__(self):
        """
        Parse and assign user arguments
        """
        # initialize logging
        self.__logger = logging.getLogger(__name__)

        # define argparse description/epilog
        description = 'Simple RfCat message signal by Python'
        epilog = 'Ensure RfCat and all needed libraries are installed! ' \
                 'Insert the RfCat dongle before using this script. ' \
                 'Please follow all local, state, federal, and international laws. ' \
                 'The author of this code take no responsibility for your use or misuse.'

        # create argparse Object
        parser = argparse.ArgumentParser(prog='SendString.py', description=description, epilog=epilog)

        # set optional arguments
        parser.add_argument('-p', '--padding', help='Count of empty bytes', default=0, type=int)
        parser.add_argument('-f', '--frequency', help='Frequency in Hz', default=434000000, type=int)
        parser.add_argument('-b', '--baut', help='Baut rate in Hz', default=4800, type=int)
        parser.add_argument('-r', '--repeats', help='Send signal n times', default=0, type=int)
        parser.add_argument('-m', '--max_power', help='Enable maximum power', default=False, action='store_true')
        parser.add_argument('-v', '--verbosity', help='increase output verbosity', action="count")

        # set mandatory arguments
        parser.add_argument("message", help="Your message to send")

        # read arguments by user
        args = parser.parse_args()

        # set logging level
        if args.verbosity > 1:
            logging.basicConfig(level=logging.DEBUG)
        elif args.verbosity == 1:
            logging.basicConfig(level=logging.INFO)
        else:
            logging.basicConfig(level=logging.ERROR)

        # logging user input on level DEBUG
        self.__logger.debug('usr input message: %s', args.message)
        self.__logger.debug('usr input padding: %s', args.padding)
        self.__logger.debug('usr input baut: %s', args.baut)
        self.__logger.debug('usr input frequency: %s', args.frequency)
        self.__logger.debug('usr input repeats: %s ', args.repeats)
        self.__logger.debug('usr input max_power: %s', args.max_power)
        self.__logger.debug('usr input verbose: %s', args.verbosity)

        # assign all arguments to public vars
        self.text = args.message
        self.padding_count = args.padding
        self.baut_rate = args.baut
        self.frequency = args.frequency
        self.repeats = args.repeats
        if args.max_power:
            self.max_power = True
        else:
            self.max_power = False

        # strip double quotes from message
        self.text = self.text.strip(chr(34))
        # strip single quotes from message
        self.text = self.text.strip(chr(39))

        # currently protected variable will be later assigned as arguments
        self._modulation = 'MOD_ASK_OOK'

        # some default private variables
        self.__hex_value = None
        self.__bin_value = None
        self.__send_message = None
        self.__sample_list = []
        self.__byte_count = 0

        # run private verify_arguments method
        self.__verify_arguments()

    @staticmethod
    def verify_string(value):
        """
        Verify for string and not empty

        :param value: The string to verify
        :type value: str
        :return: True or False
        """
        # verify if string empty
        if value and value.strip():
            return True
        else:
            return False

    @staticmethod
    def verify_int_range(value, min_max_range):
        """
        Verify for int in specific range

        :param value: The integer to verify
        :type value: int
        :param min_max_range: The range as list (min:max)
        :type min_max_range: list
        :return: True or False
        """
        # verify value in range
        if value in range(min_max_range[0], min_max_range[1]):
            return True
        else:
            return False

    @staticmethod
    def string_to_hex(value):
        """
        Convert given value to HEX

        :param value: The string which get converted
        :type value: str
        :return: The HEX value of converted value
        """
        # return converted string as HEX
        return binascii.hexlify(value)

    def __verify_arguments(self):
        """
        Verify all arguments from user
        """
        self.__logger.debug('verify all user arguments')

        # verify message is string
        if not SendSignal.verify_string(self.text):
            self.__logger.critical('message is an empty string: {0} - {1}'.format(self.text,
                                                                                  type(self.text)))
            sys.exit(1)

        # verify padding is in range
        min_max_val = [0, 100]
        if not SendSignal.verify_int_range(self.padding_count, min_max_val):
            self.__logger.critical('padding is not in range: {0} - {1}'.format(self.padding_count,
                                                                               type(self.padding_count)))
            sys.exit(1)

        # verify frequency is in range (unofficial range)
        min_max_val = [281000000, 962000000]
        if not SendSignal.verify_int_range(self.frequency, min_max_val):
            self.__logger.critical('frequency is not in range {0} - {1}'.format(self.frequency,
                                                                                type(self.frequency)))
            sys.exit(1)

        # verify baut is in range (ASK OOK is only supported for data rate up until 250 kBaud.)
        min_max_val = [210, 250000]
        if not SendSignal.verify_int_range(self.baut_rate, min_max_val):
            self.__logger.critical('baut is not in range: {0} - {1}'.format(self.baut_rate,
                                                                            type(self.baut_rate)))
            sys.exit(1)

        # verify repeats is in range
        min_max_val = [0, 100]
        if not SendSignal.verify_int_range(self.repeats, min_max_val):
            self.__logger.critical('repeats is not in range: {0} - {1}'.format(self.repeats,
                                                                               type(self.repeats)))
            sys.exit(1)

        # run private create_message method
        self.__create_message()

    def __add_message_hex_to_list(self, value):
        """
        Split message HEX values into list
        """
        self.__logger.debug('split HEX to list')

        # append each string element to list
        for element in value:
            self.__sample_list.append(element)

    def __add_padding_hex_to_list(self):
        """
        Add padding bytes HEX to list
        """
        self.__logger.debug('append new padding to list')

        # append one '00' to list
        self.__sample_list.append('00')

    def __create_message(self):
        """
        Create full converted message
        """
        self.__logger.debug('create converted message to send')

        # convert string to BIN and set variable
        self.__bin_value = ''.join(format(ord(i), 'b') for i in self.text)

        # convert string to HEX and set variable
        self.__hex_value = SendSignal.string_to_hex(self.text)

        # split hex and add to list
        self.__add_message_hex_to_list(re.findall('..', self.__hex_value))

        # add padding hex to list
        count = 0
        while count < self.padding_count:
            self.__add_padding_hex_to_list()
            count = count + 1

        # count complete byte length of list
        self.__byte_count = len(self.__sample_list)

        # set variable with initial characters
        self.__send_message = '\\x'

        # convert list back to string for RfCat
        self.__send_message += '\\x'.join(map(str, self.__sample_list))

    def print_info(self):
        """
        Print information about signal
        """
        self.__logger.debug('print all information')

        # create simple divider
        divider = '-' * 80

        # print information
        print("SIGNAL INFORMATION")
        print(divider)
        print('Frequency in Hz : {0}'.format(self.frequency))
        print('Baud rate in Hz : {0}'.format(self.baut_rate))
        print('Modulation      : {0}'.format(self._modulation))
        print('Max Power       : {0}'.format(self.max_power))
        print('Packet length   : {0}'.format(self.__byte_count))
        print('Sending Repeats : {0}'.format(self.repeats))
        print('Padding bytes   : {0}'.format(self.padding_count))
        print('Text            : {0}'.format(self.text))
        print('BIN value       : {0}'.format(self.__bin_value))
        print('HEX value       : {0}'.format(self.__hex_value))
        print('HEX + Padding   : {0}'.format(self.__send_message))
        print(divider)

    def run_send(self):
        """
        Send via RfCat
        """
        self.__logger.debug('send signal with RfCat')

        # create datetime information
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        print("Transmission started", date_time)

        # execute RfCat
        try:
            rf = RfCat()
            rf.setFreq(self.frequency)  # set frequency
            rf.setMdmModulation(MOD_ASK_OOK)  # set modulation
            rf.makePktFLEN(int(self.__byte_count))  # set packet length
            rf.setMdmDRate(int(self.baut_rate))  # set baut rate
            rf.setMdmSyncMode(0)  # disable sync word and preamble
            if self.max_power:
                rf.setMaxPower()  # enable max power
            # self.__logger.info(rf.reprRadioConfig())
            rf.RFxmit(data=self.__send_message, repeat=int(self.repeats))
            rf.setModeIDLE()
        except Exception, e:
            sys.exit('Error: {0}'.format(str(e)))

        # create datetime information
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        print("Transmission complete", date_time)


if __name__ == '__main__':
    RUN = SendSignal()
    RUN.print_info()
    RUN.run_send()
    sys.exit(0)
else:
    sys.exit(1)
