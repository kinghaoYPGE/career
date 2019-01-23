from tkinter import *
import os
import time
def backup():
    source_dir = entry_source.get() or '/home/shiyanlou/Code'
    target_dir = entry_target.get() or '/home/shiyanlou/Desktop'
    today_dir = os.path.join(target_dir, time.strftime('%Y%m%d'))
    zip_file = os.path.join(today_dir, time.strftime('%H%M%S')+'.zip')
    zip_cmd = 'zip -qr %s %s' % (zip_file, source_dir)
    if not os.path.exists(today_dir):
        os.mkdir(today_dir)

    if os.system(zip_cmd) == 0:
        print('Backup successfully!')
    else:
        print('Backup failed')

root = Tk()
root.title('文件备份')
root.geometry('200x200')
# 第一行控件
lab_source = Label(root, text='源文件')
lab_source.grid(row=0, column=0)
entry_source = Entry(root)
entry_source.grid(row=0, column=1)
# 第二行控件
lab_target= Label(root, text='目标文件')
lab_target.grid(row=1, column=0)
entry_target = Entry(root)
entry_target.grid(row=1, column=1)

# 第三行控件
commit_button = Button(root, text='备份')
commit_button.grid(row=3, column=0)
commit_button['command'] = backup
root.mainloop()
