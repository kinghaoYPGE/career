import os
def tree(dir):
    dirs =[os.path.join(dir, i) for i in os.listdir(dir)]
    for file in dirs:
        if os.path.isdir(file):
            tree(file)
        else:
            print(file)

