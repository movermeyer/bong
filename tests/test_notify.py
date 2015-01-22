from bong.notify import notify

from unittest.mock import patch

@patch('subprocess.check_call')
def test_notify(system):
    notify('bees')
    system.assert_called_with(['notify-send', 'bees'])

