import os
import subprocess
import tempfile
import platform

apktool_addr = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'apktool', 'apktool')
if platform.system() == 'Windows':
    apktool_addr += '.bat'

def decomp(apk_path):
    output_addr = tempfile.NamedTemporaryFile().name

    subprocess.call(apktool_addr + " d " + apk_path + " -o " + output_addr, shell=True)
    return output_addr


if __name__ == "__main__":
    import sys
    output_addr = decomp(sys.argv[1])
    print(output_addr)
