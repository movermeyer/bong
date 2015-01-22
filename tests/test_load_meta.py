import bong.metadata as md
from distutils.version import StrictVersion

def test_version_format():
    StrictVersion(md.VERSION)

