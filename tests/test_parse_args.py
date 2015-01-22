from bong.parse_args import parse_args
from bong.settings import BongSettings, DEFAULT_MESSAGE

from nose.tools import eq_

combinations = [
    ([], BongSettings(time=60*25, message=DEFAULT_MESSAGE)), # Default, no args
    (['-s'], BongSettings(time=60*5, message=DEFAULT_MESSAGE)), # Short break
    (['-l'], BongSettings(time=60*15, message=DEFAULT_MESSAGE)), # Long break
    (['-s', '-l'], BongSettings(time=60*15, message=DEFAULT_MESSAGE)), # Later arguments take priority
    (['-s', '-p'], BongSettings(time=60*25, message=DEFAULT_MESSAGE)), # Pomodoro
    (['-t', '3'], BongSettings(time=60*3, message=DEFAULT_MESSAGE)), # Explicit time
    (['-m', 'bees'], BongSettings(time=60*25, message='bees')) # Message setting
]

def check_generation(args, settings):
    gen_settings = parse_args(args)
    eq_(gen_settings, settings)

def test_no_args():
    for args, settings in combinations:
        yield check_generation, args, settings

