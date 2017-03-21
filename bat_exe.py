import subprocess
import os

def open_batch():
    dierectory = "C:\Secure_nj_project"
    dierectory += "\\nj$SeCureVaUlt@ThIsIsTeStIngPhAse4ME"
    dierectory += "\\batch.bat"
    subprocess.call(dierectory)
    os.remove(dierectory)
