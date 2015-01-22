from bong.settings import BongSettings
from bong.run import run

from unittest.mock import Mock

def test_run_length():
    notify = Mock()
    sleep = Mock()
    run(BongSettings(time=40, message='bees'), sleep=sleep, notify=notify)
    sleep.assert_called_with(40)

def test_notification():
    notify = Mock()
    sleep = Mock()
    run(BongSettings(time=40, message='bees'), sleep=sleep, notify=notify)
    notify.assert_called_with('bees')

