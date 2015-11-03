import sys
from mock import Mock as MagicMock

class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
            return Mock()

MOCK_MODULES = ['gnureadline']
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)