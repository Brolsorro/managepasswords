#Python 3.7.1 32 bit и выше
#Обратная совместимость есть
from tkinter import messagebox
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from os import remove as deleting_file
import os.path

# Объявление последовательностей из символов и букв русского и английского алфавитов
left = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
left = left+"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*,/1234567890:;<.>?@\^№|-+=_~`{} []\"\'"
up="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
up=up+"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*,/1234567890:;<.>?@\^№|-+=_~`{} []\"\'"
left_side=list(left)
up_side=list(up)

sta_us=False
current_file=""
path_2="bin/pass"


root=tk.Tk()
image=PhotoImage(file="image/file.png")
root.title("Реестр v.1.02")


##################RESOLUTION###################

# Разрешение окна приложение
x_resolution=280
y_resolution=150
root.geometry(str(x_resolution)+"x"+str(y_resolution))

# Запрет на изменение окна
root.resizable(width=False, height=False)

# Определение местоположения окна
x = root.winfo_screenwidth()
y = root.winfo_screenheight()
kif=2.5
root.wm_geometry("+%d+%d" % ((x/kif),(y/kif)))

#################################################

# Местоположение файла данных

# Для нулевого запуска программы
in_bool=False
name_keys=[]
st_input=False
settings="bin/ini"
st_0=False
if os.path.exists(settings)==False:
    st_0=True
    os.mkdir("bin")
    f=open(settings,"w",encoding="cp1251")
    f.write("По умолчанию ключ: Ключ")
    f.close()

def start():
    global f,file_buf,file,name_keys,st_input
    f = current_file
    file_buf=f  # Запись данных в переменную file_bufы
    try:
        file={} # объявление типа словарь
        file=eval(file_buf.rstrip()) #перевод str в словарь
        name_keys=eval(str(file.keys())[10:-1]) # Программный вид | Cписок
        name_keys.sort()
        st_input=True
    except BaseException as e:
        messagebox.showerror(title="Ошибка",message="Неверный код доступа! \n Закрытие программы...")
        raise SystemExit


####################FRAME##################
account_type = Label(text="Тип аккаунта:")
email_log = Label(text="E-mail/login:")
password=Label(text="Password:")
add_inf=Label(text="Доп. Инфо.:")

padx_val=7
xx=7
yy=5
width=200
mas=[0,22,44,66,95,120]
mas2=mas
mas=[i+yy for i in mas]

account_type.place(width=200,height=20,x=xx,y=mas[0])
email_log.place(width=200,height=20,x=xx,y=mas[1])
password.place(width=200,height=20,x=xx,y=mas[2])
add_inf.place(width=200,height=20,x=xx,y=mas[3])
s="2"

x=100

combo_t=StringVar()
combo_box=Combobox(values=name_keys,textvariable=combo_t)
combo_box.place(width=150,height=20,x=x,y=mas[0])
combo_box.insert(0,"<Выберите аккаунт>")
email_t=StringVar()
pass_t=StringVar()
add_t=StringVar()
email_entry = Entry(textvariable=email_t)
email_entry.place(width=150,height=20,x=x,y=mas[1])
password_entry = Entry(textvariable=pass_t)
password_entry.place(width=150,height=20,x=x,y=mas[2])
add_inf_entry = Entry(textvariable=add_t)
add_inf_entry.place(width=150,height=20,x=x,y=mas[3])

x1=250
y1=19

mas2=[i+3 for i in mas2]

st=Style()
st.configure("U.TButton",padding=-1)

button_email = Button(text="К",image=image,style="U.TButton")
button_email.place(width=25,height=23,x=x1,y=mas2[1])
button_pass = Button(text="К",image=image,style="U.TButton")
button_pass.place(width=25,height=23,x=x1,y=mas2[2])
button_add = Button(text="К",image=image, style="U.TButton")
button_add.place(width=25, height=23, x=x1, y=mas2[3])

x2=15
button_change= Button(text="Изменить")
button_change.place(width=100,height=23,x=47-x2,y=mas2[4])
button_clear= Button(text="Очистить поля")
button_clear.place(width=100,height=23,x=153-x2,y=123)
button_addit= Button(text="Добавить",state=DISABLED)
button_addit.place(width=100,height=23,x=153-x2,y=mas2[4])


style = Style()
style.layout("C.TMenubutton", [
   ("Menubutton.background", None),
   ("Menubutton.button", {"children":
       [("Menubutton.focus", {"children":
           [("Menubutton.padding", {"children":
               [("Menubutton.label", {"side": "left", "expand": 1})]
           })]
       })]
   }),
])

button_exit= Button(text="X",style="C.TMenubutton")
button_exit.place(width=35,height=33,x=270-x,y=106)

select=""

#### Функция для инициализации данные по выбранному варианту combox ###
st_bool=False
def inizil_data(event):
    global select
    global button_addit
    global st_bool
    if st_bool==False:
           button_addit= Button(text="Добавить",command=add_data)
           button_addit.place(width=100,height=23,x=153-x2,y=mas2[4])

    st_bool=True
    select=combo_box.get()
    if select in name_keys:
        s=file[select]
        email_entry.delete(0,END)
        email_entry.insert(0,s[0])
        password_entry.delete(0,END)
        password_entry.insert(0,s[1])
        add_inf_entry.delete(0,END)
        add_inf_entry.insert(0,s[2])

# Обновляет список ключение в листе combobox
def combobox_update():
    global combo_box
    global name_keys
    name_keys=eval(str(file.keys())[10:-1])
    name_keys.sort()
    combo_box.config(value=name_keys)


# Меняет данные согласно выбранному в базе аккаунту
def change_data(event):
    if combo_t.get()!="<Выберите аккаунт>":
        global select,current_file

        file[combo_t.get()]=file.pop(select)
        select=combo_t.get()
        file[select][0]=email_t.get()
        file[select][1]=pass_t.get()
        file[select][2]=add_t.get()
        current_file=str(file)
        combobox_update()


# Добавляет новые данные в базу
def add_data():
    global current_file
    answer=True
    if combo_t.get()!="<Выберите аккаунт>":
        if combo_box.get() in name_keys:
            answer=messagebox.askyesno(title="Внимание...", message="Такая запись в базе уже есть.\n"+
                                         "Вы хотите обновить информацию о записи? \n"+"<"+combo_t.get()+">")

        if answer == True:
            file[combo_t.get()]=[email_t.get(),pass_t.get(),add_t.get()]
            current_file=str(file)
            combobox_update()

#Выход
def exit_fun(event):
    create_pattern_of_crypt()
    encrypting()
    raise SystemExit

combo_box.bind(sequence='<<ComboboxSelected>>',func=inizil_data)
button_change.bind(sequence='<ButtonPress>',func=change_data)

#для того чтобы было...да х*й его знает зачем....но не трогать!
if st_bool==True:
    button_addit= Button(text="Добавить",command=add_data)
    button_addit.place(width=100,height=23,x=153-x2,y=mas2[4])

button_exit.bind(sequence='<ButtonPress>',func=exit_fun)


#  перключение кнопок для использования одной и той же функции
add=0


def f_1(event):
    global add
    add=1
    buttons()


def f_2(Event):
    global add
    add=2
    buttons()


def f_3(event):
    global add
    add=3
    buttons()


# копирование данные из текстбоксов в буфер обмена
def buttons():
        global add
        if (select in name_keys):
            if (add==1):
                root.clipboard_clear()
                root.clipboard_append(file[select][0])
            if (add==2):
                root.clipboard_clear()
                root.clipboard_append(file[select][1])
            if (add==3):
                root.clipboard_clear()
                root.clipboard_append(file[select][2])

# очистка данных со всех текстовых полей
def fun_f(event):
    global button_addit
    email_entry.delete(0,END)
    password_entry.delete(0,END)
    add_inf_entry.delete(0,END)
    combo_box.delete(0,END)
    global select
    select=""
    button_addit.config(state=NORMAL)
    global st_bool
    if st_bool==False:
           button_addit= Button(text="Добавить",command=add_data)
           button_addit.place(width=100,height=23,x=153-x2,y=mas2[4])

# удаление выбранного аккаунта
def del_acc():
    global name_keys,current_file
    if (combo_box.get()!="<Выберите аккаунт>") and (combo_box.get() in name_keys):

        global select
        answer=True
        answer=messagebox.askyesno(title="Внимание...", message="Вы уверены что хотите удалить запись:\n"+
                                         "<"+combo_box.get()+">")
        if answer==True:
            if  (select in name_keys):
                del file[select]
                current_file=str(file)
                email_entry.delete(0,END)
                password_entry.delete(0,END)
                add_inf_entry.delete(0,END)
                combo_box.delete(0,END)
                select=""
                combobox_update()
                combo_box.insert(0,"<Выберите аккаунт>")



button_delete= Button(text="Удалить запись",command=del_acc)
button_delete.place(width=100,height=23,x=47-x2,y=123)
button_email.bind('<ButtonPress>',f_1)
button_pass.bind('<ButtonPress>',f_2)
button_add.bind('<ButtonPress>',f_3)
button_clear.bind('<ButtonPress>',fun_f)
will_changed=False
def create_pattern_of_crypt():
    ## Создание таблицы-указателя шифрования
    global key,context_matrix
    context_matrix=[]
    for i in range(len(left_side)):
            context_matrix.append(up_side[i+1:]+up_side[0:i+1])
    if will_changed==False:
        key=buf_key.get()
    f=open(path_2,encoding="cp1251")
    file=f.read()
    f.close()

    if st_input==False:
        if sta_us==True:
            key=key
        while (len(key)<len(file)):
            key=key*2
        if len(key)!=len(file):
            key=key[:-1*(len(key)-len(file))]

    if st_input==True:
        file=current_file
        if sta_us==True:
            key=key
            #смена ключа
            #key="Ключ"
        while (len(key)<len(file)):
            key=key*2
        if len(key)!=len(file):
            key=key[:-1*(len(key)-len(file))]




def encrypting():
    #шифрование
    global key,current_file
    file=current_file
    encrypted_message=""
    for i in range(len(file)):
          encrypted_message=encrypted_message+context_matrix[left_side.index(file[i])][up_side.index(key[i])]
    f=open(path_2,'w',encoding="cp1251")
    f.write(encrypted_message)
    f.close()


def decrypting():
    global key,sta_us,current_file
    sta_us=True
    decrypted_message=""
    f=open(path_2,encoding="cp1251")
    file=f.read()
    f.close()
    for i in range(len(file)):
        buf_mes=[]
        for j in range(len(left_side)):
            buf_mes=buf_mes+list(context_matrix[j][up_side.index(key[i])])
        decrypted_message=decrypted_message+left_side[buf_mes.index(file[i])]

    current_file=decrypted_message
    start()
    combobox_update()

#Выход
def exit_fun(event):
    create_pattern_of_crypt()
    encrypting()
    raise SystemExit




### сокрытие всех кнопок основной формы
account_type.place_forget()
email_log.place_forget()
password.place_forget()
add_inf.place_forget()
combo_box.place_forget()
email_entry.place_forget()
password_entry.place_forget()
add_inf_entry.place_forget()
button_email.place_forget()
button_pass.place_forget()
button_add.place_forget()
button_change.place_forget()
button_clear.place_forget()
button_addit.place_forget()
button_exit.place_forget()
button_delete.place_forget()



lb_ma=Label(text="Ответьте на вопрос:")
lb_ma.place(width=150,height=20,x=80,y=10)
name_text="< "+"- "*8+"text not found"+" -"*9+" >"


buf_key=StringVar()
mainquestion_Entry=Entry()
mainquestion_Entry.place(width=240,height=20,x=20,y=30)


mainanswer_Entry=Entry(textvariable=buf_key)
mainanswer_Entry.place(width=240,height=20,x=20,y=57)
key_decryption=""




def ex_cop():
    warni=False
    warni=messagebox.askyesno(title="Внимание!",message="Вы уверены, что хотите экспортировать \nрасшифрованные данные в корень программы?")
    if warni==True:
        ff=current_file
        s=""
        file={} # объявление типа словарь
        file=eval(ff.rstrip()) #перевод str в словарь
        name_keys=eval(str(file.keys())[10:-1]) # Программный вид | Cписок
        name_keys.sort()
        for i in range(len(file)):
            s=s+"[Тип аккаунта]: "+name_keys[i]+"\n"+"||login/.@||: "+file[name_keys[i]][0]+"\n"+"||password||: "+file[name_keys[i]][1]+"\n"+"||add_info||: "+file[name_keys[i]][2]+"\n\n"

        f=open("export_file.txt",'w',encoding="cp1251")
        f.write(s)
        f.close()

def fun_03():
    f=open(settings,"w",encoding="cp1251")
    f.write(box_quest_change.get())
    f.close()
    messagebox.showinfo(title="Уведомление",message="Был изменен текст подсказки!")



hider=Button(text="▼")


box_quest_change=Entry()
button_quest_change=Button(text="Сменить подсказку",command=fun_03)
box_change_key=Entry()
button_change_key=Button(text="Сменить ключ")
### активация всех кнопок основной формы
def main_funn():
    global current_file,st_0
    create_pattern_of_crypt()
    decrypting()
    account_type.place(width=200,height=20,x=xx,y=mas[0])
    email_log.place(width=200,height=20,x=xx,y=mas[1])
    password.place(width=200,height=20,x=xx,y=mas[2])
    add_inf.place(width=200,height=20,x=xx,y=mas[3])
    combo_box.place(width=150,height=20,x=x,y=mas[0])
    email_entry.place(width=150,height=20,x=x,y=mas[1])
    password_entry.place(width=150,height=20,x=x,y=mas[2])
    add_inf_entry.place(width=150,height=20,x=x,y=mas[3])
    button_email.place(width=25,height=23,x=x1,y=mas2[1])
    button_pass.place(width=25,height=23,x=x1,y=mas2[2])
    button_add.place(width=25,height=23,x=x1,y=mas2[3])
    button_change.place(width=100,height=23,x=47-x2,y=mas2[4])
    button_clear.place(width=100,height=23,x=153-x2,y=123)
    button_addit.place(width=100,height=23,x=153-x2,y=mas2[4])
    button_delete.place(width=100,height=23,x=47-x2,y=123)
    button_exit.place(width=35,height=33,x=270-x2,y=106)
    button_export= Button(text="   Ex",style="C.TMenubutton",command=ex_cop)
    hider.place(width=20,height=20,x=237,y=126)
    button_change_key.config(state=DISABLED)
    button_quest_change.config(state=DISABLED)
    button_export.place(width=39,height=33,x=-x2,y=106)
    #деактивация всех кнопок вторичной формы
    lb_ma.destroy()
    mainquestion_Entry.destroy()
    mainanswer_Entry.place_forget()
    main_recieve_button.place_forget()
    if st_0==True or mainanswer_Entry.get()=="Ключ":
        st_0=False
        messagebox.showwarning(title="Внимание!",message="Настоятельно рекомендуется поменять\nключ шифрования на cвой, особый!")





def fff(event):
    if mainanswer_Entry.get()=="":
        main_recieve_button.config(state=DISABLED)
    if mainanswer_Entry.get()!="":
        main_recieve_button.config(state=NORMAL)

def b1(event):
    if box_change_key.get()=="":
        button_change_key.config(state=DISABLED)
    if box_change_key.get()!="":
        button_change_key.config(state=NORMAL)

def b2(event):
    if box_quest_change.get()=="":
        button_quest_change.config(state=DISABLED)
    if box_quest_change.get()!="":
        button_quest_change.config(state=NORMAL)

def fun_001(event):
    global name_text
    mainquestion_Entry.delete(0,END)
    mainquestion_Entry.insert(0,name_text)
hide=True
def fun_002(event):
    global hide
    if hide==True:
        hide=False
        x_resolution=280
        y_resolution=250
        root.geometry(str(x_resolution)+"x"+str(y_resolution))
        hider.place(width=20,height=20,x=237,y=228)
        hider.config(text="▲")
        box_change_key.place(width=205,height=23,x=32,y=150)
        button_change_key.place(width=205,height=23,x=32,y=175)
        box_quest_change.place(width=205,height=23,x=32,y=200)
        button_quest_change.place(width=205,height=23,x=32,y=225)
    else:
        hide=True
        x_resolution=280
        y_resolution=150
        root.geometry(str(x_resolution)+"x"+str(y_resolution))
        hider.place(width=20,height=20,x=237,y=126)
        hider.config(text="▼")

def change_key():
    global key,context_matrix,current_file,will_changed
    will_changed=True
    context_matrix=[]
    for i in range(len(left_side)):
            context_matrix.append(up_side[i+1:]+up_side[0:i+1])
    key=box_change_key.get()
    buf_kk=key


    file=current_file
    while (len(key)<len(file)):
        key=key*2
    if len(key)!=len(file):
        key=key[:-1*(len(key)-len(file))]

    encrypted_message=""
    for i in range(len(file)):
          encrypted_message=encrypted_message+context_matrix[left_side.index(file[i])][up_side.index(key[i])]
    f=open(path_2,'w',encoding="cp1251")
    f.write(encrypted_message)
    f.close()
    file=encrypted_message
    decrypted_message=""
    for i in range(len(file)):
        buf_mes=[]
        for j in range(len(left_side)):
            buf_mes=buf_mes+list(context_matrix[j][up_side.index(key[i])])
        decrypted_message=decrypted_message+left_side[buf_mes.index(file[i])]
    key=buf_kk
    current_file=decrypted_message
    combobox_update()
    messagebox.showinfo(title="Уведомление",message="Был изменен ключ шифрования!")

styl=Style()
styl.configure("C.TButton",font=20)

button_change_key=Button(text="Сменить ключ",command=change_key)

main_recieve_button=Button(text="Отправить ответ",command=main_funn,style="C.TButton")
main_recieve_button.place(width=240,height=45,x=20,y=83)
mainanswer_Entry.bind("<KeyRelease>",func=fff)
box_change_key.bind("<KeyRelease>",func=b1)

main_recieve_button.config(state=DISABLED)

mainquestion_Entry.bind("<KeyRelease>",fun_001)

hider.bind("<Button>",fun_002)

box_quest_change.bind("<KeyRelease>",func=b2)


if(os.path.exists(path_2)==False):
    key=""; context_matrix=""
    f=open(settings,"w",encoding="cp1251")
    ss1="По умолчанию ключ: Ключ"
    name_text=ss1
    f.write(ss1)
    f.close()
    in_bool=True

    context_matrix=[]
    for i in range(len(left_side)):
            context_matrix.append(up_side[i+1:]+up_side[0:i+1])
    key="Ключ"
    buf_kk=key

    current_file="{'<Пример>': ['<email>', '<pass>', '<info>'], '<Пример_2>': ['<email>', '<pass>', '<info>'],"+" '<Пример_3>': ['<email>', '<pass>', '<info>']}"
    file=current_file
    while (len(key)<len(file)):
        key=key*2
    if len(key)!=len(file):
        key=key[:-1*(len(key)-len(file))]

    encrypted_message=""
    for i in range(len(file)):
          encrypted_message=encrypted_message+context_matrix[left_side.index(file[i])][up_side.index(key[i])]
    f=open(path_2,'w',encoding="cp1251")
    f.write(encrypted_message)
    f.close()

try:
    fuf=""
    f=open(settings,'r',encoding="cp1251")
    fuf=f.read()
    f.close()
    name_text=fuf
except BaseException: None
mainquestion_Entry.insert(0,name_text)

root.wm_attributes('-topmost',True)
root.mainloop()
if sta_us==True:
    create_pattern_of_crypt()
    encrypting()
