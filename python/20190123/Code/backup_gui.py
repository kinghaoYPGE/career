from tkinter import *
from tkinter.filedialog import askdirectory
import tkinter.messagebox as msgbox
import os
import time
# import zipfile
from shutil import make_archive

dir_list = []
def tree(dir):
    dirs =[os.path.join(dir, i) for i in os.listdir(dir)]
    for file in dirs:
        if os.path.isdir(file):
            tree(file)
        else:
            dir_list.append(file)
    
def tree_source():
    source_dir = entry_source.get()
    tree(os.path.abspath(source_dir))
    msgbox.showinfo('文件列表', '\n'.join(dir_list))
    dir_list.clear()
def tree_target():
    target_dir = entry_target.get()
    tree(os.path.abspath(target_dir))
    msgbox.showinfo('文件列表', '\n'.join(dir_list))
    dir_list.clear()
    
def selectPath_source():
    path_ = askdirectory()
    path_source.set(path_)

def selectPath_target():
    path_ = askdirectory()
    path_target.set(path_)
    
def backup():
    source_dir = entry_source.get() # or '/home/shiyanlou/Code'
    target_dir = entry_target.get() # or '/home/shiyanlou/Desktop'
    today_dir = os.path.join(target_dir, time.strftime('%Y%m%d'))
    # zip_file = os.path.join(today_dir, time.strftime('%H%M%S')+'.zip')
    # zip_cmd = 'zip -qr %s %s' % (zip_file, source_dir)
    zip_file = os.path.join(today_dir, time.strftime('%H%M%S')) # 压缩的zip文件名
    if not os.path.exists(today_dir):
        os.mkdir(today_dir)
    # 如果没有安装zip该方法不可行，采用shutil.make_archive方法更加通用，也可以使用zipfile，但zipfile麻烦一些
    # if os.system(zip_cmd) == 0:
    try:
        r = make_archive(zip_file, 'zip', source_dir)
        print('Backup successfully!--> %s' % r)
        msgbox.showinfo('成功', '备份成功!输出文件为：%s' % r)
    except:
        print('Backup failed')
        msgbox.showinfo('失败', '备份失败，请检查文件')
        raise

root = Tk()
path_source = StringVar()
path_target = StringVar()
root.title('文件备份')
root.geometry('280x200')
# 第一行控件
lab_source = Label(root, text='源文件')
lab_source.grid(row=0, column=0)
entry_source = Entry(root, textvariable=path_source)
entry_source.grid(row=0, column=1)
select_button1 = Button(root, text='选择', command=selectPath_source)
select_button1.grid(row=0, column=2)
query_button1 = Button(root, text='查看', command=tree_source)
query_button1.grid(row=0, column=3)
# 第二行控件
lab_target= Label(root, text='目标文件')
lab_target.grid(row=1, column=0)
entry_target = Entry(root, textvariable=path_target)
entry_target.grid(row=1, column=1)
select_button2 = Button(root, text='选择', command=selectPath_target)
select_button2.grid(row=1, column=2)
query_button2 = Button(root, text='查看', command=tree_target)
query_button2.grid(row=1, column=3)

# 第三行控件
commit_button = Button(root, text='备份')
commit_button.grid(row=3, column=0)
commit_button['command'] = backup
root.mainloop()
