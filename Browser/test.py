def start1():

    root.title("Directory Browser and File Finder")

    label1=Label(root,text="Please enter the directory path")
    label1.grid(row=0,column=0)
    e1=Entry(root,width=100,border=5)
    e1.grid(row=0,column=1)
    button1 = Button(root, text='Click here', command=lambda: getpath(e1.get(), e2))
    button1.grid(row=0, column=2)

    label=Label(root,text="List of files and Folders inside the given directory are: ")
    label.grid(row=1,column=0)
    sb = Scrollbar(root,orient=VERTICAL)
    sb.grid(row=2,column=2,sticky=NS)
    e2=Text(root,height=10,width=60)
    e2.grid(row=2, column=1)
    e2.config(yscrollcommand=sb.set)
    sb.config(command=e2.yview)

    label2=Label(root,text="Enter the directory path to fetch .pdf files in it:  ")
    label2.grid(row=3,column=0)
    e3=Entry(root,width=100,border=5)
    e3.grid(row=3,column=1)
    button2 = Button(root, text="Click here", command=lambda: fetchfile(e3.get(),e4,e5))
    button2.grid(row=3, column=2)

    e4=Text(root,height=5,width=60)
    e4.grid(row=4,column=1)
    label3=Label(root,text="List of pdf files in the given directory are:")
    label3.grid(row=4,column=0)
    label4=Label(root,text="The final Merged pdf file created is ")
    label4.grid(row=5,column=1)
    e5=Text(root,height=5,width=40)
    e5.grid(row=6,column=1)

    root.mainloop()

def getpath(pathname,e2):

    path=pathname
    lst_dir=getlist(path)
 #   e2.delete(0)
    e2.insert(END,str(lst_dir))

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


def fetchfile(file_path,e4,e5):
    '''
    This function will help you to filter only word file from a directory
    '''
    import os
    a = os.walk(file_path)
    l = []
    dir_lst = list(a)

    import re
    pattern = re.compile(r"\.pdf$")
    import PyPDF2 as pdf
    import os
    from os import path

    f_writer = pdf.PdfFileWriter()


    for lst in dir_lst:
        if type(lst) == tuple:
            for dirct in lst:
                if type(dirct) == list:
                    for file in dirct:
                        matches = pattern.finditer(file)
                        for match in matches:
                            l.append(file)
                            f1 = open(path.join(lst[0],file), 'rb')
                            print(lst[0])
                            print(file)
                            f1_read = pdf.PdfFileReader(f1)
                            print(type(f1))
                            print(lst[0])
                            print(file)
                            print(f1_read.numPages)


                            for page_no in range(f1_read.numPages):
                                f1_pages = f1_read.getPage(page_no)
                                f_writer.addPage(f1_pages)

                            f1.close()
    fnew = open("Mergedfile.pdf", 'wb')
    f_writer.write(fnew)
    filename=path.join(os.getcwd(),'Mergedfile.pdf')


    e4.insert(END, str(l))
    e5.insert(END, filename)


from tkinter import *
root=Tk()
start1()

