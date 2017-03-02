""".mt2 file parser written in Python"""

from libmodpy._common import Common

class MT2(Common):
    """"""
    def __init__(self, filename=None):
        """"""
        super().__init__()
        if filename:
            self.load_module(filename)
            self.setup()

    def setup(self):
        self.identifier = self.file[0:4].decode() 
        if self.identifier != "MT20":
            raise ValueError("Not a valid MadTracker 2 file")
        
        # Metadata
        self.module_version = self.file[8:9].decode()
        self.tracker_name = self.file[10:42].decode().replace("\x00", "")
        self.module_title = self.file[42:106].decode().replace("\x00", "")
        self.number_of_positions = self.file[106]
        self.restart_position = self.file[108]
        self.number_of_patterns = self.file[110]
        self.number_of_tracks = self.file[112]
        self.samples_per_tick = self.file[114]
        self.ticks_per_line = self.file[116]
        self.lines_per_beat = self.file[117]
        self.number_of_instruments = self.file[122:124]
        self.number_of_samples = self.file[124]
        
        # Flags
        self.packed_patterns = self.file[118]
        self.automation = self.file[119]
        self.pattern_order = [hex(i) for i in self.file[126:127 + self.number_of_patterns]]
        # Very "hackish" right now, I know.
        