#!/usr/bin/env python

import pytest
from srfcat import SendTextSignal
from srfcat import ReceiveTextSignal


def test_send_frequency_true():
    assert SendTextSignal.SendSignal.set_frequency(300000000) is None


def test_send_frequency_false():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        SendTextSignal.SendSignal.set_frequency(100000000)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2


def test_send_baud_rate_true():
    assert SendTextSignal.SendSignal.set_baud_rate(4000) is None


def test_send_baud_rate_false():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        SendTextSignal.SendSignal.set_baud_rate(200)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2


def test_send_repeats_true():
    assert SendTextSignal.SendSignal.set_repeats(5) is None


def test_send_repeats_false():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        SendTextSignal.SendSignal.set_repeats(100)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2


def test_receive_frequency_true():
    assert ReceiveTextSignal.ReceiveSignal.set_frequency(300000000) is None


def test_receive_frequency_false():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        ReceiveTextSignal.ReceiveSignal.set_frequency(100000000)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2


def test_receive_baud_rate_true():
    assert ReceiveTextSignal.ReceiveSignal.set_baud_rate(4000) is None


def test_receive_baud_rate_false():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        ReceiveTextSignal.ReceiveSignal.set_baud_rate(200)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2
