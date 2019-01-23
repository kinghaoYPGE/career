#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
import sys
def backup():
    try:
       source_dir = sys.argv[1]
       target_dir = sys.argv[2]
    except Exception as e:
        raise ValueError('wrong format: backup.py "dir1[,dir2,dir3...]" "target"')
    source_dir = source_dir.replace(',', ' ')
    today_dir = os.path.join(target_dir, time.strftime('%Y%m%d'))
# zip_file = today_dir + os.sep +  time.strftime('%H%M%S')+'.zip'
    zip_file = os.path.join(today_dir, time.strftime('%H%M%S')+'.zip')
    zip_cmd = 'zip -qr %s %s' % (zip_file, source_dir)
    if not os.path.exists(today_dir):
        os.mkdir(today_dir)

    if os.system(zip_cmd) == 0:
        print('Backup successfully!')
    else:
        print('Backup failed')

if __name__ == '__main__':
    backup()

