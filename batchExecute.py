import subprocess
import os

def open_batch(dierectory):
    subprocess.call(dierectory)
    os.remove(dierectory)
