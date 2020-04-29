import signal

from pkg_resources import get_distribution

from . import utils

signal.signal(signal.SIGINT, lambda x, y: exit(0))

name = 'spliceai'
__version__ = get_distribution(name).version
