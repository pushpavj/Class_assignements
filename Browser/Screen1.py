def start1():
    root=Tk()
    root.title("Directory Browser and File Finder")
    label1=Label(root,text="Please enter the directory path")
    label1.grid(row=0,column=0)
    e1=Entry(root,width=100,border=5)
    e1.grid(row=0,column=1)
    sb = Scrollbar(root)
    sb.grid(row=1,column=1)
    e2=Entry(root,width=100,border=5,xscrollcommand=sb)
    e2.grid(row=1,column=1)
  #  ver=Scale(root,from_=0,to=200)
 #   ver.pack()
   # ver.grid(row=1,column=1)
    button1=Button(root,text='Click here',command=lambda:getpath(e1.get(),e2))
    button1.grid(row=0,column=2)
    root.mainloop()

def getpath(pathname,e2):

    path=pathname
    lst_dir=getlist(path)
    e2.delete(0)
    e2.insert(0,str(lst_dir))
 #   print(lst_dir)
 #  lstscreen(lst_dir)

def getlist(path1):
    import os
    lst = os.walk(top=str(path1))
    l1 = []

    for i in list(lst):
        l1.append("Direcotory Path: " + i[0])
        l1.append("Files :")
        l1.append(i[2])
        l1.append("Folders:")
        l1.append(i[1])
        l1.append("*************************************************************************")
    return l1

#def lstscreen(files):
 #   e2=Entry(root,width=100,border=10)
 #   e2.insert(files)
 #   e2.grid(row=2,column=0)


from tkinter import *
root=Tk()
start1()
