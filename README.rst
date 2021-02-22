srfc
----

To send a signal (with caution), simply do::

    >>> from srfcat import SendSignal
    >>> SendSignal.set_frequency(433000000)
    >>> SendSignal.set_baud_rate(4000)
    >>> SendSignal.set_message('Hello World')
    >>> SendSignal.get_debug_signal()
    >>> SendSignal.send_signal()

To receive a signal, simply do::

   >>> from srfcat import ReceiveSignal
   >>> ReceiveSignal.set_frequency(433000000)
   >>> ReceiveSignal.set_baud_rate(4000)
   >>> ReceiveSignal.get_debug_signal()
   >>> ReceiveSignal.get_signal()
