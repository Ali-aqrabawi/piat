import argparse
import os


def compile(path):
    for filename in os.listdir(path):
        cmd = 'mibdump.py --rebuild file://%s' % os.path.join(path,filename)
        print('##############################################')
        print('##############################################')
        print(cmd)
        print('##############################################')
        print('##############################################')

        if filename.endswith(".my") or filename.endswith(".mib"):
            os.system(cmd)

compile('/home/aaqrabaw/Desktop/cisco_mibs/arista')

