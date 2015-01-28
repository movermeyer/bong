from bong.notify import notify
import sys
from io import StringIO

from unittest.mock import patch
from nose.tools import eq_

class FakeSys(object):
    def __init__(self, **kwargs):
        self._fake = kwargs

    def __getattr__(self, name):
        try:
            return self._fake[name]
        except KeyError:
            return getattr(sys, name)

@patch('subprocess.check_call')
def test_notify_linux(system):
    notify('bees', sys=FakeSys(platform='linux'))
    system.assert_called_with(['notify-send', 'bees'])

@patch('subprocess.check_call')
def test_notify_darwin(system):
    notify('bees', sys=FakeSys(platform='darwin'))
    system.assert_called_with(['terminal-notifier', '-message', 'bees'])

def test_notify_other():
    with patch('sys.stdout', new=StringIO()) as fake_out:
        notify('bees', sys=FakeSys(platform='aix'))
        eq_(fake_out.getvalue(), 'bees\n')

