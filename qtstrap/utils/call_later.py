from qtstrap import *


_call_timers = []

def call_later(what, msec:int=1):
    """call the given function after a specified delay"""
    timer = QTimer(singleShot=True)
    timer.timeout.connect(what)
    timer.start(msec)
    _call_timers.append(timer)