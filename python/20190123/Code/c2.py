"""
GUI图形编程
python通过TKinter实现
"""
import tkinter
from tkinter import *
from tkinter import Tk
import tkinter.messagebox as messagebox


class Application(Frame):
    """
    pack布局
    """
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets() # 创建组件
    
    def createWidgets(self):
        # self.helloLabel = Label(self, text='hello, world')
        # self.helloLabel.pack()
        # 事件监听机制
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()
    def hello(self):
        name = self.nameInput.get()
        messagebox.showinfo('message', 'hello %s' % name)

if __name__ == '__main__':
    app = Application()
    app.master.title('Hello')
    # GUI中主线程用来监听操作系统消息，依次处理每一个消息(消息队列)
    app.mainloop()

