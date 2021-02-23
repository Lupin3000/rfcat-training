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

    # set send signal values
    >>> SendSignal.set_frequency(433000000)
    >>> SendSignal.set_baud_rate(4000)
    >>> SendSignal.set_message('Hello World')
    >>> SendSignal.set_repeats(5)

    # show send signal configuration
    >>> SendSignal.get_signal_dump()

    # send signal
    >>> SendSignal.send_signal()

To receive a signal, simply do::

   # import
   >>> from srfcat import ReceiveSignal

   # set receive signal values
   >>> ReceiveSignal.set_frequency(433000000)
   >>> ReceiveSignal.set_baud_rate(4000)
   >>> ReceiveSignal.set_lowball(True)
   >>> ReceiveSignal.set_max_power(True)

   # show receive signal configuration
   >>> ReceiveSignal.get_signal_dump()

   # receive signal
   >>> ReceiveSignal.get_signal()
