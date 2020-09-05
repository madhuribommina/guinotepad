from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog
from fpdf import FPDF
#pdf=FPDF()
r=Tk()
r.title("converter")


#creating new file
def new_file():
    new_f=Tk()
    new_f.title("converter")
    def open_file():
        files=[('all files','*.*'),
           ('python files','*.py'),
           ('text files','*.txt'),
           ('pdf files','*.pdf')]
        r.filename=filedialog.askopenfilename(initialdir="E:\guiicon",filetypes=files)
        txt=r.filename
        fl=r.filename
        fle=fl.show()
        if fle != '':
            f = open(fl, "r")
            text = f.read()
            self.txt.insert(END, text)


        
    def save_file():
        files=[('all files','*.*'),
           ('python files','*.py'),
           ('text files','*.txt'),
           ('pdf files','*.pdf')]
        file=asksaveasfile(initialdir='/',filetypes=files,defaultextension=files)
        text2save=str(text.get(0.0,END))
        file.write(text2save)
        file.close

    #creating scrollbar
    sbar=Scrollbar(new_f)
    sbar.pack(side=RIGHT,fill='y')

    #creating menubar
    my_menu=Menu(new_f)
    new_f.config(menu=my_menu)

    #creating menu items
    file_menu=Menu(my_menu,tearoff=0)
    my_menu.add_cascade(label="file",menu=file_menu)
    file_menu.add_command(label="new",command=new_file)
    file_menu.add_command(label="open",command=open_file)
    file_menu.add_command(label="save",command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="exit",command=new_f.destroy)




    #creating text box
    text=Text(new_f,width=50,height=30,yscrollcommand=sbar.set)
    text.pack(fill=BOTH)
    sbar.config(command=text.yview)



    new_f.mainloop()

def open_file():
    files=[('all files','*.*'),
           ('python files','*.py'),
           ('text files','*.txt'),
           ('pdf files','*.pdf')]
    r.filename=filedialog.askopenfilename(initialdir="E:\guiicon",filetypes=files)
    txt=r.filename
    fl=r.filename
    fle=fl.show()
    if fle != '':
        f = open(fl, "r")
        text = f.read()
        self.txt.insert(END, text)
   
def save_file():
    files=[('all files','*.*'),
           ('python files','*.py'),
           ('text files','*.txt'),
           ('pdf files','*.pdf')]
    file=asksaveasfile(initialdir='/',filetypes=files,defaultextension=files)
    text2save=str(text.get(0.0,END))
    file.write(text2save)
    file.close

def pdf():
    pdf=FPDF()
    pdf.add_page() 
   
    # set style and size of font  
    # that you want in the pdf 
    pdf.set_font("Arial", size = 15)
    r.filename=filedialog.askopenfilename(initialdir="E:\guiicon",filetypes=(("all files","*.*"),("text files","*.txt")))
    txt=r.filename
      
    # open the text file in read mode 
    f = open(txt, "r") 
      
    # insert the texts in pdf 
    for x in f: 
        pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 
       
    # save the pdf with name .pdf 
    pdf.output("pdfsmake.pdf")   

    


#creating scrollbar
sbar=Scrollbar(r)
sbar.pack(side=RIGHT,fill='y')

#creating menubar
my_menu=Menu(r)
r.config(menu=my_menu)

#creating menu items
file_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="file",menu=file_menu)
file_menu.add_command(label="new",command=new_file)
file_menu.add_command(label="open",command=open_file)
file_menu.add_command(label="save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="exit",command=r.destroy)

#creating pdf
pdf_b=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="PDF",menu=pdf_b)
pdf_b.add_command(label="pdf",command=pdf)



#creating text box
text=Text(r,width=50,height=30,yscrollcommand=sbar.set)
text.pack(fill=BOTH)
sbar.config(command=text.yview)



r.mainloop()
