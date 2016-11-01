import os
import sys
import imp

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)



def parseWaves(singenLocation):
    with cd(singenLocation):
        print(os.getcwd())
        sys.path.append(singenLocation)
        import singen_cli
        
        return singen_cli.dumpOneWave("./config.ini")
