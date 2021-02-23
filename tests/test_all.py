#!/usr/bin/env python

import pytest
from srfcat.SendTextSignal import SendSignal
from srfcat.ReceiveTextSignal import ReceiveSignal


def test_send_frequency_true():
    assert SendSignal.set_frequency(300000000) is None


def test_send_frequency_false():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        SendSignal.set_frequency(100000000)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2


def test_send_baud_rate_true():
    assert SendSignal.set_baud_rate(4000) is None


def test_send_baud_rate_false():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        SendSignal.set_baud_rate(200)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2


def test_send_repeats_true():
    assert SendSignal.set_repeats(5) is None


def test_send_repeats_false():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        SendSignal.set_repeats(100)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2


def test_receive_frequency_true():
    assert ReceiveSignal.set_frequency(300000000) is None


def test_receive_frequency_false():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        ReceiveSignal.set_frequency(100000000)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2


def test_receive_baud_rate_true():
    assert ReceiveSignal.set_baud_rate(4000) is None


def test_receive_baud_rate_false():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        ReceiveSignal.set_baud_rate(200)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2


def test_receive_lowball_true():
    assert ReceiveSignal.set_lowball(True) is None


def test_receive_max_power_true():
    assert ReceiveSignal.set_max_power(True) is None
