import tkinter.messagebox

import customtkinter
from tkinter import filedialog
from PIL import Image, ImageTk
from datetime import datetime
from tkinter import messagebox



time_now = datetime.now()
current_time = time_now.strftime("%H")

file2 = open("theme.txt","r")
thm = file2.readline()

file3 = open("color.txt","r")
col = file3.readline()

def tam():

    file1 = open("theme.txt", "w")
    file1.write("dark")
    tkinter.messagebox.showinfo("Tamno", "Vaš će se izgled primjeniti nakon ponovnog pokretanja programa!")
    x = messagebox.askquestion("Pitanje", "Želite li sada ponovno pokrenuti program?")
    if x == 'yes':
        quit()


def svj():
    file1 = open("theme.txt", "w")
    file1.write("light")
    tkinter.messagebox.showinfo("Svijetlo", "Vaš će se izgled primjeniti nakon ponovnog pokretanja programa!")
    x = messagebox.askquestion("Pitanje", "Želite li sada ponovno pokrenuti program?")
    if x == 'yes':
        quit()

def magentad():
    file4 = open("color.txt", "w")
    file4.write("magenta.json")
    tkinter.messagebox.showinfo("Magenta", "Vaš će se izgled boja primjeniti nakon ponovnog pokretanja programa!")
    x = messagebox.askquestion("Pitanje", "Želite li sada ponovno pokrenuti program?")
    if x == 'yes':
        quit()

def plavd():
    file4 = open("color.txt", "w")
    file4.write("blue")
    tkinter.messagebox.showinfo("Plava", "Vaš će se izgled boja primjeniti nakon ponovnog pokretanja programa!")
    x = messagebox.askquestion("Pitanje", "Želite li sada ponovno pokrenuti program?")
    if x == 'yes':
        quit()

def zelend():
    file4 = open("color.txt", "w")
    file4.write("green")
    tkinter.messagebox.showinfo("Zelena", "Vaš će se izgled boja primjeniti nakon ponovnog pokretanja programa!")
    x = messagebox.askquestion("Pitanje", "Želite li sada ponovno pokrenuti program?")
    if x == 'yes':
        quit()

customtkinter.set_appearance_mode(f"{thm}")
customtkinter.set_default_color_theme(f"{col}")

root = customtkinter.CTk()
root.geometry("1200x1000")
root.resizable(False, False)
root.title("Orgify")

dark = customtkinter.CTkImage(Image.open("dark.png"), size=(240, 240))
light = customtkinter.CTkImage(Image.open("light.png"), size=(240, 240))

file3 = open("theme.txt", "r")
ds = file3.readline()
if ds == "dark":
    magenta = customtkinter.CTkImage(Image.open("dark-magenta.png"), size=(240, 240))
    blue = customtkinter.CTkImage(Image.open("dark-blue.png"), size=(240, 240))
    green = customtkinter.CTkImage(Image.open("dark-green.png"), size=(240, 240))
    logo = customtkinter.CTkImage(Image.open("logo-dark.png"), size=(246, 246))

else:
    magenta = customtkinter.CTkImage(Image.open("light-magenta.png"), size=(240, 240))
    blue = customtkinter.CTkImage(Image.open("light-blue.png"), size=(240, 240))
    green = customtkinter.CTkImage(Image.open("light-green.png"), size=(240, 240))
    logo = customtkinter.CTkImage(Image.open("logo-light.png"), size=(246, 246))

def postavke():



    root2 = customtkinter.CTkToplevel()
    root2.geometry("1000x800")
    root2.title("Postavke")
    root2.resizable(False, False)
    frame2 = customtkinter.CTkFrame(master=root2)
    frame22 = customtkinter.CTkFrame(master=root2)
    frame2.pack(pady=20, padx=20, fill="both", expand=True)
    frame22.pack(pady=20, padx=20, fill="both", expand=True)
    label3 = customtkinter.CTkLabel(master=frame2, text="Prikaz", font=("Calibri", 45, "bold"))
    label3.pack()
    label4 = customtkinter.CTkLabel(master=frame22, text="Prikaz boja", font=("Calibri", 45, "bold"))
    label4.pack()
    dark_button = customtkinter.CTkButton(master=frame2, image=dark, text="Tamno", command=tam)
    dark_button.pack(side="left")
    light_button = customtkinter.CTkButton(master=frame2, image=light, text="Svijetlo", command=svj)
    light_button.pack(side="left", padx=12)
    magenta_button = customtkinter.CTkButton(master=frame22, image=magenta, text="Magenta", command=magentad)
    magenta_button.pack(side="left")
    blue_button = customtkinter.CTkButton(master=frame22, image=blue, text="Plava", command=plavd)
    blue_button.pack(side="left", padx=12)
    green_button = customtkinter.CTkButton(master=frame22, image=green, text="Zelena", command=zelend)
    green_button.pack(side="left")

def nastavi():
    global name_save
    name_save = entry1.get()
    frame0.pack_forget()
    frame1.pack(pady=20, padx=20, fill="both", expand=True)
    pozdrav = customtkinter.CTkLabel(master=frame1, text=f"{text}", font=("Calibri", 45, "bold"))
    pozdrav.pack(pady=12, padx=10)
    ime2 = customtkinter.CTkLabel(master=frame1, text=f"{name_save}!", font=("Calibri", 45, "bold"))
    ime2.pack()
    frame11.pack(fill="y", side="left")
    frame111.pack(fill="y", side="right")



frame0 = customtkinter.CTkFrame(master=root)
frame0.pack(pady=20, padx=20, fill="both", expand=True)
frame1 = customtkinter.CTkFrame(master=root)

log = customtkinter.CTkLabel(master=frame0, text="", image=logo)
log.pack(pady=37)
customtkinter.CTkLabel(master=frame0, text="o", text_color="#ff258f", font=("Calibri", 66, "bold")).place(x=485, y=265)
customtkinter.CTkLabel(master=frame0, text="r", text_color="#2CC985", font=("Calibri", 66, "bold")).place(x=520, y=265)
customtkinter.CTkLabel(master=frame0, text="g", text_color="#3a7ebf", font=("Calibri", 66, "bold")).place(x=545, y=265)
customtkinter.CTkLabel(master=frame0, text="i", text_color="#3a7ebf", font=("Calibri", 66, "bold")).place(x=580, y=265)
customtkinter.CTkLabel(master=frame0, text="f", text_color="#2CC985", font=("Calibri", 66, "bold")).place(x=600, y=265)
customtkinter.CTkLabel(master=frame0, text="y", text_color="#ff258f", font=("Calibri", 66, "bold")).place(x=625, y=265)

#customtkinter.CTkLabel(master=frame0, text="", font=("Calibri", 35, "bold")).pack()

label1 = customtkinter.CTkLabel(master=frame0, text="Vaše ime:", font=("Calibri", 60, "bold"))
label1.pack(pady=20, padx=10)

entry1 = customtkinter.CTkEntry(master=frame0, placeholder_text="Vaše ime", font=("Calibri", 45, "bold"), width=250)
entry1.pack(pady=20, padx=12)
button1 = customtkinter.CTkButton(master=frame0, height=100, width=300, font=("Calibri", 45, "bold"), text="Nastavi", command=nastavi)
button1.pack(pady=20, padx=12)



if current_time == "05" or current_time == "06" or current_time == "07" or current_time == "08" or current_time == "09" or current_time == "10" or current_time == "11":
    text = "Dobro jutro"
elif current_time == "12" or current_time == "13" or current_time == "14" or current_time == "15" or current_time == "16" or current_time == "17":
    text="Dobar dan"
else:
    text="Dobra večer"



frame11 = customtkinter.CTkScrollableFrame(parent=frame1)
frame111 = customtkinter.CTkScrollableFrame(parent=frame1)
frame1111 = customtkinter.CTkFrame(master=frame1)

c_v1 = customtkinter.StringVar(value="off")
switch_var = customtkinter.StringVar(value="off")

def odustani():
    frame1111.place_forget()
    entry3.delete(0, customtkinter.END)
    c_v1.set(value="off")
    switch_var.set(value="off")

def ucitaj():
    file1 = filedialog.askopenfilename(filetypes=[("txt file", ".txt")], defaultextension=".txt")
    fob=open(file1,"r")
    data = fob.readlines()
    name = data[0].split("\n")
    name2 = name[0]
    imps = data[1].split("\n")
    imps2 = imps[0]
    obvs = data[2].split("\n")
    obvs2 = obvs[0]
    print(name2)
    print(imps2)
    print(obvs2)
    if imps2 == "1":
        imp_color="darkred"
        text_color = "green"
        imp_text="Važno: Da"
    else:
        file4 = open("color.txt","r")
        co = file4.readline()
        if co == "magenta.json":
            imp_color="#ff258f"
        elif co == "blue":
            imp_color="#3a7ebf"
        else:
            imp_color="#2CC985"
        text_color = "red"
        imp_text = "Važno: Ne"
    if obvs2 == "1":
        text_color2 = "green"
        obv_text = "Obavjesti: Da"
    else:
        text_color2 = "red"
        obv_text = "Obavjesti: Ne"

    file3 = open("theme.txt","r")
    fg = file3.readline()
    if fg == "dark":
        colfg = "#2b2b2b"
    else:
        colfg="#dbdbdb"

    def obrisi():
        l00.pack_forget()
        l11.pack_forget()
        l22.pack_forget()
        l33.pack_forget()
        l44.pack_forget()
        l55.pack_forget()

    def gotovo():
        global l11, l22, l33, l44, l55, l00

        l00 = customtkinter.CTkLabel(master=frame111.scrollable_frame, text="", width=200, font=("Calibri", 20))
        l00.pack()
        l11 = customtkinter.CTkLabel(master=frame111.scrollable_frame, text="", fg_color=f"{imp_color}", width=200, font=("Calibri", 20))
        l11.pack()

        l22 = customtkinter.CTkLabel(master=frame111.scrollable_frame, text=f"{name2}", width=200, fg_color=f"{colfg}", font=("Calibri", 20))
        l22.pack()
        l33 = customtkinter.CTkLabel(master=frame111.scrollable_frame, text=f"{imp_text}", text_color=f"{text_color}", width=200, fg_color=f"{colfg}", font=("Calibri", 20))
        l33.pack()
        l44 = customtkinter.CTkLabel(master=frame111.scrollable_frame, text=f"{obv_text}", text_color=f"{text_color2}", width=200, fg_color=f"{colfg}", font=("Calibri", 20))
        l44.pack()
        l55 = customtkinter.CTkButton(master=frame111.scrollable_frame, text="Gotovo", fg_color=f"{imp_color}", width=200, command=obrisi, font=("Calibri", 20))
        l55.pack()

        l0.pack_forget()
        l1.pack_forget()
        l2.pack_forget()
        l3.pack_forget()
        l4.pack_forget()
        l5.pack_forget()


    def st():
        global l1, l2, l3, l4, l5, l0
        l0 = customtkinter.CTkLabel(master=frame11.scrollable_frame, text="", width=200, font=("Calibri", 20))
        l0.pack()
        l1 = customtkinter.CTkLabel(master=frame11.scrollable_frame, text="", fg_color=f"{imp_color}", width=200, font=("Calibri", 20))
        l1.pack()
        l2 = customtkinter.CTkLabel(master=frame11.scrollable_frame, text=f"{name2}", width=200, fg_color=f"{colfg}", font=("Calibri", 20))
        l2.pack()
        l3 = customtkinter.CTkLabel(master=frame11.scrollable_frame, text=f"{imp_text}", text_color=f"{text_color}", width=200, fg_color=f"{colfg}", font=("Calibri", 20))
        l3.pack()
        l4 = customtkinter.CTkLabel(master=frame11.scrollable_frame, text=f"{obv_text}", text_color=f"{text_color2}", width=200, fg_color=f"{colfg}", font=("Calibri", 20))
        l4.pack()
        l5 = customtkinter.CTkButton(master=frame11.scrollable_frame, text="Gotovo", fg_color=f"{imp_color}", width=200, command=gotovo, font=("Calibri", 20))
        l5.pack()

    st()

def create_screen():
    entry3.delete(0, customtkinter.END)
    frame1111.place(x=498, y=400)


def dodaj():
    global file
    file = filedialog.asksaveasfilename(filetypes=[("Text file", ".txt")], defaultextension=".txt")
    if file:
        create_screen()

def stvori():
    task_name = entry3.get()
    fob=open(file,"w")
    fob.write(f"{task_name}"+"\n")
    if c_v1.get() == "on":
        fob.write("1"+"\n")
    else:
        fob.write("0"+"\n")
    if switch_var.get() == "on":
        fob.write("1")
    else:
        fob.write("0")

    frame1111.place_forget()
    entry3.delete(0, customtkinter.END)
    c_v1.set(value="off")
    switch_var.set(value="off")


button2 = customtkinter.CTkButton(master=frame1, text="Učitaj zadatak", width=230, height=100, font=("Calibri", 30, "bold"), command=ucitaj)
#button2.place(x=465, y=1000)
button2.place(x=465, y=840)
button3 = customtkinter.CTkButton(master=frame1, text="Dodaj zadatak", width=230, height=100, font=("Calibri", 30, "bold"), command=dodaj)
#button3.place(x=465, y=860)
button3.place(x=465, y=700)
button4 = customtkinter.CTkButton(master=frame1, text="Postavke", width=160, height=70, font=("Calibri", 30, "bold"), command=postavke)
button4.place(x=20, y=20)

label2 = customtkinter.CTkLabel(master=frame11.scrollable_frame,text="Treba napraviti", font=("Calibri", 30, "bold"))
label2.pack()
label2 = customtkinter.CTkLabel(master=frame111.scrollable_frame, text="Napravljeno", font=("Calibri", 30, "bold"))
label2.pack()





#customtkinter.CTkLabel(master=frame1111, text="", font=("Calibri", 20, "bold")).pack()

imezad = customtkinter.CTkLabel(master=frame1111, text="Ime zadatka:", font=("Calibri", 20, "bold"))
imezad.pack(pady=12, padx=10)
entry3 = customtkinter.CTkEntry(master=frame1111, placeholder_text="        Ime zadatka         ", font=("Calibri", 14, "bold"))
entry3.pack(padx=10)
customtkinter.CTkLabel(master=frame1111, text="", font=("Calibri", 14, "bold")).pack()
imp = customtkinter.CTkSwitch(master=frame1111, text="Važno", onvalue="on", offvalue="off", variable=c_v1)
imp.pack(padx=12, pady=14)
obv = customtkinter.CTkSwitch(master=frame1111, text="Obavjesti", onvalue="on", offvalue="off", variable=switch_var)
obv.pack(padx=12, pady=0)
odustani = customtkinter.CTkButton(master=frame1111, text="Odustani", command=odustani)
odustani.pack(pady=12, padx=12)
stvori = customtkinter.CTkButton(master=frame1111, text="Stvori", command=stvori)
stvori.pack(pady=12, padx=12)
root.mainloop()