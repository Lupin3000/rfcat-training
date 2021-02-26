srfcat
======

Install
_______

To install simply do following::

   # clone repository
   $ git clone https://github.com/Lupin3000/rfcat-training.git

   # run installer
   $ python rfcat-training/setup.py install

Usage
_____

To send a signal (with caution), simply do::

    # import
    >>> from srfcat import SendSignal

    # create object
    >>> send_rf = SendSignal()

    # set values
    >>> send_rf.set_frequency(434000000)
    >>> send_rf.set_baud_rate(4800)
    >>> send_rf.set_message('Hello World from RfCat...')
    >>> send_rf.set_repeats(10)

    # show send signal configuration
    >>> send_rf.get_signal_dump()

    # start send signal
    >>> send_rf.send_signal()

To receive a signal, simply do::

   # import
   >>> from srfcat import ReceiveSignal

   # create object
   >>> receive_rf = ReceiveSignal()

   # set values
   >>> receive_rf.set_frequency(868000000)
   >>> receive_rf.set_baud_rate(4800)
   >>> receive_rf.set_lowball(True)
   >>> receive_rf.set_max_power(True)

   # show receive signal configuration
   >>> receive_rf.get_signal_dump()

   # start receive signal
   >>> receive_rf.get_signal()

To uninstall::

   # uninstall
   $ pip uninstall srfc