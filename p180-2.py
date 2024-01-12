from tkinter import*
from tkinter import ttk
from googletrans import Translator,LANGUAGES
root=Tk()
root.geometry("1080x400")
root.config(bg="lightblue")
root.title("Language Translator")
lan=list(LANGUAGES.values())
l=Label(root,text="LANGUAGE TRANSLATOR",bg="lightblue")
l.place(relx=0.5,rely=0.1,anchor=CENTER)
il=Label(root,text="ENTER TEXT",bg="lightblue")
il.place(relx=0.02,rely=0.2,anchor=W)
sl=ttk.Combobox(root,values=lan,width=22,state="readonly")
sl.place(relx=0.13,rely=0.2,anchor=W)
sl.set('english')

ol=Label(root,tetx="Output",bg="lightblue")
ol.place(relx=0.81,rely=0.2,anchor=E)
dl=ttk.Combobox(root,values=lan,width=22,state="readonly")
dl.place(relx=0.98,rely=0.2,anchor=E)
dl.set("Choose ouput language")
it=Text(root,height=11,wrap=WORD,padx=5,pady=5,width=60,bg="grey",bd=0)
it.place(relx=0.02,rely=0.5,anchor=W)
ot=Text(root,height=11,wrap=WORD,padx=5,pady=5,width=60,bg="grey",bd=0)
ot.place(relx=0.98,rely=0.5,anchor=E)
def translate():
    translator=Translator()
    try:
        translated=translator.translate(text=it.get(1.0,END),src=sl.get(),dest=dl.get())
        ot.delete(1.0,END)
        ot.insert(END,translated.text)
    except:
        print("try again!")
btn=Button(root,text="translate",command=translate,relief=FLAT)
btn.place(relx=0.5,rely=0.85,anchor=CENTER)
root.mainloop()