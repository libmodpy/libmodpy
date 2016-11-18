""".mt2 file parser written in Python"""

from libmodpy._common import Common

class MT2(Common):
    """"""
    def __init__(self):
        """"""
        super().__init__()

    def identifier(self):
        """This should be "MT20".
        If not, this isn't a MadTracker .mt2 file."""
        return self.file[0:4].decode()

    def module_title(self):
        """"""
        return self.file[42:105].decode().replace("\x00", "")