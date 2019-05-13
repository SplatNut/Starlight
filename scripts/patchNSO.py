# patchNSO.py
# Patches the MOD0 section of an NSO to properly set the user-runtime object offset

import ntpath, os, subprocess, sys

if len(sys.argv) < 2:
    print("Syntax: patchNSO.py <nso>")
    sys.exit()

subprocess.run("../tools/nsnsotool " + sys.argv[1])

with open(sys.argv[1], 'r+b') as nso_file:
    nso = nso_file.read()
    mod0_offset = nso.find(b'MOD0')
    nso_file.seek(mod0_offset + 8)
    bss_start = nso_file.read(4)
    nso_file.seek(mod0_offset + 24)
    nso_file.write(bss_start)

    #nso_file.seek(0x3C, 0)
    #bss_size = int.from_bytes(nso_file.read(4), byteorder='little')
    #nso_file.seek(0x1C, 0)
    #nso_file.write(bss_size.to_bytes(4, byteorder='little'))
    #bss_size += 0xB8
    #nso_file.seek(0x3C, 0)
    #nso_file.write(bss_size.to_bytes(4, byteorder='little'))

    nso_file.close()

print('patched')