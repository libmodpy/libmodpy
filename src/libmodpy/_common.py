

class Common(object):
    def load_module(self, filename):
        """Loads file into memory.
        "rb" is needed, as we're dealing with hex here."""
        with open(filename, "rb") as f:
            self.file = f.read()