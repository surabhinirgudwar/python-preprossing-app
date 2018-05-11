from tkinter import filedialog
from tkinter import *
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

##def show_entry_fields():
##    e2.insert(10,(e1.get()))

master = Tk()
master.minsize(width=500, height=200)

Label(master, text="enter url").grid(row=0)
Label(master, text="enter dataset").grid(row=1)
Label(master, text="know about your data").grid(row=300)
Label(master, text="visualise your data").grid(row=500)
Label(master, text="make your dataset ready for analysis").grid(row=800)

def browse():
    
    master.filename=filedialog.askopenfilename()
    print("file path is",master.filename)
    master.title(master.filename)
    text1=open(master.filename).read()
    print(text1)
    T=Text(master,height=30,width=60)
    T.grid(row=1000,column=2)
    T.insert(END,text1)
    #hr=pd.read_csv(master.filename)
    #print("describe gives",hr.describe())
    #print("length  gives",len(hr))
    
b1 =Button(master, text='browse..',command = browse).grid(row=0, column=2, sticky=W, pady=4)
e2 = Entry(master)

#e1.grid(row=0, column=2)
e2.grid(row=1, column=2)

def preprocess():
    new = Tk()
    new.minsize(width=500, height=200)
    Label(new, text="pre process your dataset").grid(row=0)
    Button(new, text='remove null values').grid(row=50, column=0, sticky=W, pady=4)
    Button(new, text='replacement').grid(row=60, column=0, sticky=W, pady=4)
    Button(new, text='data normalisation').grid(row=70, column=0, sticky=W, pady=4)
    Button(new, text='data binning').grid(row=80, column=0, sticky=W, pady=4)
       

def visualise():
    new1 = Tk()
    new1.minsize(width=500, height=200)
    Label(new1, text=" x axis").grid(row=0)
    Label(new1, text="y axis").grid(row=10)
    e3 = Entry(new1)
    e4 = Entry(new1)
    e3.grid(row=0, column=2)
    e4.grid(row=10, column=2)
    Label(new1, text="choose th graph type to plot").grid(row=15)
    Radiobutton(new1, text="bar graph").grid(row = 20)
    Radiobutton(new1, text="scatter plot").grid(row = 30)
    Radiobutton(new1, text="histo gram").grid(row = 40)
    def plot():
        plotwin=Tk()
        plotwin.minsize(width=500, height=200)
    Button(new1, text='plot',command=plot).grid(row=100, column=1)
    new1.mainloop()
    

def explore():
    new2 = Tk()
    new2.minsize(width=500, height=200)
    Label(new2, text="length of data").grid(row=0)
    Label(new2, text="shape of dataset").grid(row=10)
    Label(new2, text="column names").grid(row=20)
    Label(new2, text="explore 1st five rows").grid(row=30)
    Label(new2, text="explore botton five rows").grid(row=40)
    Label(new2, text="describe").grid(row=50)

    def length():
        len1 = Tk()
        len1.minsize(width=500, height=200)
        hr=pd.read_csv(master.filename)
        a=len(hr)
        T=Text(len1,height=15,width=60)
        T.grid(row=0,column=2)
        T.insert(END,a)

    def shape1():
        len1 = Tk()
        len1.minsize(width=500, height=200)
        hr=pd.read_csv(master.filename)
        a=hr.shape
        T=Text(len1,height=15,width=60)
        T.grid(row=0,column=2)
        T.insert(END,a)
    def column_name():
        len1 = Tk()
        len1.minsize(width=500, height=200)
        hr=pd.read_csv(master.filename)
        a=hr.columns
        T=Text(len1,height=15,width=100)
        T.grid(row=0,column=2)
        T.insert(END,a)
    def headd():
        len1 = Tk()
        len1.minsize(width=500, height=200)
        hr=pd.read_csv(master.filename)
        a=hr.head(5)
        T=Text(len1,height=15,width=100)
        T.grid(row=0,column=2)
        T.insert(END,a)
    def taill():
        len1 = Tk()
        len1.minsize(width=500, height=200)
        hr=pd.read_csv(master.filename)
        a=hr.tail(5)
        T=Text(len1,height=15,width=100)
        T.grid(row=0,column=2)
        T.insert(END,a)
    def describee():
        len1 = Tk()
        len1.minsize(width=500, height=200)
        hr=pd.read_csv(master.filename)
        a=hr.describe()
        T=Text(len1,height=15,width=100)
        T.grid(row=0,column=2)
        T.insert(END,a)
        
    
    
    Button(new2, text='length',command=length).grid(row=0, column=2, sticky=W, pady=4)
    Button(new2, text='click for rows and column',command=shape1).grid(row=10, column=2, sticky=W, pady=4)
    Button(new2, text='click for column names',command=column_name).grid(row=20, column=2, sticky=W, pady=4)
    Button(new2, text='click for head values',command=headd).grid(row=30, column=2, sticky=W, pady=4)
    Button(new2, text='click for tail values',command=taill).grid(row=40, column=2, sticky=W, pady=4)
    Button(new2, text='click to get description',command=describee).grid(row=50, column=2, sticky=W, pady=4)


Button(master, text='data exploration',command = explore).grid(row=300, column=2, sticky=W, pady=4)
Button(master, text='data visualisation',command = visualise).grid(row=500, column=2, sticky=W, pady=4)
Button(master ,text='data preprocessing',command = preprocess).grid(row=800, column=2, sticky=W, pady=4)

##def show_entry_fields():
##    e2.insert(10,(e1.get()))

mainloop( )

