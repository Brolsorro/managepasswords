from tkinter import messagebox
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from os import remove as deleting_file
import os.path


class Backend:

    def __init__(self, interface_gui):
        # Объявление последовательностей из символов и букв русского и английского алфавитов
        self.file_buf = None
        self.decrypted_message = ""
        self.left = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        self.left += "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*,/1234567890:;<.>?@\^№|-+=_~`{} []\"\'"
        self.up = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        self.up += "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*,/1234567890:;<.>?@\^№|-+=_~`{} []\"\'"
        self.left_side = list(self.left)
        self.up_side = list(self.up)

        self.sta_us = False
        self.current_file = ""
        self.path_2 = "bin/pass"

        # Для нулевого запуска программы
        self.in_bool = False
        self.name_keys = []
        self.st_input = False
        self.settings = "bin/ini"
        self.st_0 = False
        self.will_changed = False
        self.name_text = "< " + "- " * 8 + "text not found" + " -" * 9 + " >"
        self.key_decryption = ""
        self.hide = True
        self.ui_interface = interface_gui.ui
        self.select = None
        self.st_bool = False
        self.choice_account = '<Выберите аккаунт>'


        if os.path.exists(self.settings) == False:
            st_0 = True
            os.mkdir("bin")
            f = open(self.settings, "w", encoding="cp1251")
            f.write("По умолчанию ключ: Ключ")
            f.close()

        if (os.path.exists(self.path_2) == False):

            f = open(self.settings, "w", encoding="cp1251")
            self.ss1 = "По умолчанию ключ: Ключ"
            f.write(self.ss1)
            f.close()

            self.context_matrix = []
            for i in range(len(self.left_side)):
                self.context_matrix.append(self.up_side[i + 1:] + self.up_side[0:i + 1])
            self.key = "Ключ"

            self.current_file = "{'<Пример>': ['<email>', '<pass>', '<info>'], '<Пример_2>': ['<email>', '<pass>', '<info>']," + " '<Пример_3>': ['<email>', '<pass>', '<info>']}"
            self.file = self.current_file
            while (len(key) < len(file)):
                key = key * 2
            if len(key) != len(file):
                key = key[:-1 * (len(key) - len(file))]

            self.encrypted_message = ""
            for i in range(len(file)):
                self.encrypted_message = self.encrypted_message + self.context_matrix[self.left_side.index(file[i])][self.up_side.index(key[i])]
            f = open(self.path_2, 'w', encoding="cp1251")
            f.write(self.encrypted_message)
            f.close()

        try:
            fuf = ""
            with open(self.settings, 'r', encoding="cp1251") as f:
                self.fuf = f.read()
            self.name_text = self.fuf
        except BaseException:
            None

        if self.sta_us == True:
            self.create_pattern_of_crypt()
            self.encrypting()

    def text_question(self):
        return self.name_text

    def inizil_data(self):
        if not self.st_bool:
            # button_addit = Button(text="Добавить", command=add_data)
            # button_addit.place(width=100, height=23, x=153 - x2, y=mas2[4])
            ...

        self.st_bool = True
        self.select = self.ui_interface.comboBox_check.currentText()
        if self.select in self.name_keys:
            s = self.file[self.select]
            # email_entry.delete(0, END)

            self.ui_interface.textbox_email.clear()
            self.ui_interface.textbox_password.clear()
            self.ui_interface.textbox_add_inf.clear()
            self.ui_interface.textbox_email.setText(s[0])
            self.ui_interface.textbox_password.setText(s[1])
            self.ui_interface.textbox_add_inf.setText(s[2])


    def start(self):
        f = self.current_file
        self.file_buf = f  # Запись данных в переменную file_bufы

        try:
            self.file = {}  # объявление типа словарь
            self.file = eval(self.file_buf.rstrip())  # перевод str в словарь
            self.name_keys = eval(str(self.file.keys())[10:-1])  # Программный вид | Cписок
            self.name_keys.sort()
            self.st_input = True
        except BaseException as e:
            messagebox.showerror(title="Ошибка", message="Неверный код доступа! \n Закрытие программы...")
            raise SystemExit

    # Обновляет список ключение в листе combobox
    def combobox_update(self):
        self.name_keys = eval(str(self.file.keys())[10:-1])
        self.name_keys.sort()
        self.ui_interface.textbox_email.clear()
        self.ui_interface.textbox_password.clear()
        self.ui_interface.textbox_add_inf.clear()
        self.ui_interface.textbox_email.setEnabled(False)
        self.ui_interface.textbox_password.setEnabled(False)
        self.ui_interface.textbox_add_inf.setEnabled(False)
        self.ui_interface.comboBox_check.clear()
        self.ui_interface.comboBox_check.addItems(self.name_keys)
        self.ui_interface.comboBox_check.setEditText(self.choice_account)

    def encrypting(self):
        # шифрование
        global key, current_file
        file = current_file
        encrypted_message = ""
        for i in range(len(file)):
            encrypted_message = encrypted_message + context_matrix[self.left_side.index(file[i])][self.up_side.index(key[i])]
        f = open(self.path_2, 'w', encoding="cp1251")
        f.write(encrypted_message)
        f.close()

    def decrypting(self):
        self.sta_us = True
        f = open(self.path_2, encoding="cp1251")
        file = f.read()
        f.close()
        for i in range(len(file)):
            buf_mes = []
            for j in range(len(self.left_side)):
                buf_mes = buf_mes + list(self.context_matrix[j][self.up_side.index(self.key[i])])
            self.decrypted_message = self.decrypted_message + self.left_side[buf_mes.index(file[i])]

        self.current_file = self.decrypted_message
        self.start()
        self.combobox_update()

    def create_pattern_of_crypt(self):
        ## Создание таблицы-указателя шифрования
        # global key, context_matrix

        self.context_matrix = []
        for i in range(len(self.left_side)):
            self.context_matrix.append(self.up_side[i + 1:] + self.up_side[0:i + 1])

        if not self.will_changed:
            self.key = self.ui_interface.textbox_answer.text()
        f = open(self.path_2, encoding="cp1251")
        file = f.read()
        f.close()

        if not self.st_input:
            if self.sta_us:
                self.key = self.key
            while len(self.key) < len(file):
                self.key = self.key * 2
            if len(self.key) != len(file):
                self.key = self.key[:-1 * (len(self.key) - len(file))]

        if self.st_input:
            file = self.current_file
            if self.sta_us:
                self.key = self.key
                # смена ключа
                # key="Ключ"
            while len(key) < len(file):
                self.key = self.key * 2
            if len(key) != len(file):
                self.key = self.key[:-1 * (len(self.key) - len(file))]

    def change_data(self):
        if combo_t.get() != "<Выберите аккаунт>":
            global select, current_file

            file[combo_t.get()] = file.pop(select)
            select = combo_t.get()
            file[select][0] = email_t.get()
            file[select][1] = pass_t.get()
            file[select][2] = add_t.get()
            current_file = str(file)
            self.combobox_update()

    # Добавляет новые данные в базу
    def add_data(self):
        global current_file
        answer = True
        if combo_t.get() != "<Выберите аккаунт>":
            if combo_box.get() in name_keys:
                answer = messagebox.askyesno(title="Внимание...", message="Такая запись в базе уже есть.\n" +
                                                                          "Вы хотите обновить информацию о записи? \n" + "<" + combo_t.get() + ">")

            if answer == True:
                file[combo_t.get()] = [email_t.get(), pass_t.get(), add_t.get()]
                current_file = str(file)
                self.combobox_update()

    # Выход
    def exit_fun(self):
        self.create_pattern_of_crypt()
        self.encrypting()
        raise SystemExit

    def f_1(self):
        global add
        add = 1
        self.buttons()

    def f_2(self):
        global add
        add = 2
        self.buttons()

    def f_3(self):
        global add
        add = 3
        self.buttons()

    # копирование данные из текстбоксов в буфер обмена
    def buttons(self):
        global add
        if (select in name_keys):
            if (add == 1):
                # root.clipboard_clear()
                # root.clipboard_append(file[select][0])
                ...
            if (add == 2):
                # root.clipboard_clear()
                # root.clipboard_append(file[select][1])
                ...
            if (add == 3):
                # root.clipboard_clear()
                # root.clipboard_append(file[select][2])
                ...

    # очистка данных со всех текстовых полей
    def fun_f(self):
        global button_addit
        # email_entry.delete(0, END)
        # password_entry.delete(0, END)
        # add_inf_entry.delete(0, END)
        # combo_box.delete(0, END)
        global select
        select = ""
        button_addit.config(state=NORMAL)
        global st_bool
        if st_bool == False:
            ...
            # button_addit = Button(text="Добавить", command=add_data)
            # button_addit.place(width=100, height=23, x=153 - x2, y=mas2[4])

    # удаление выбранного аккаунта
    def del_acc(self):
        global name_keys, current_file
        if (combo_box.get() != "<Выберите аккаунт>") and (combo_box.get() in name_keys):

            global select
            answer = True
            answer = messagebox.askyesno(title="Внимание...", message="Вы уверены что хотите удалить запись:\n" +
                                                                      "<" + combo_box.get() + ">")
            if answer == True:
                if (select in name_keys):
                    del file[select]
                    current_file = str(file)
                    # email_entry.delete(0, END)
                    # password_entry.delete(0, END)
                    # add_inf_entry.delete(0, END)
                    combo_box.delete(0, END)
                    select = ""
                    self.combobox_update()
                    combo_box.insert(0, "<Выберите аккаунт>")

    def ex_cop(self):
        warni = False
        warni = messagebox.askyesno(title="Внимание!", message="Вы уверены, что хотите экспортировать \nрасшифрованные данные в корень программы?")
        if warni == True:
            ff = current_file
            s = ""
            file = {}  # объявление типа словарь
            file = eval(ff.rstrip())  # перевод str в словарь
            name_keys = eval(str(file.keys())[10:-1])  # Программный вид | Cписок
            name_keys.sort()
            for i in range(len(file)):
                s = s + "[Тип аккаунта]: " + name_keys[i] + "\n" + "||login/.@||: " + file[name_keys[i]][0] + "\n" + "||password||: " + file[name_keys[i]][
                    1] + "\n" + "||add_info||: " + file[name_keys[i]][2] + "\n\n"

            f = open("export_file.txt", 'w', encoding="cp1251")
            f.write(s)
            f.close()

    def fun_03(self):
        f = open(self.settings, "w", encoding="cp1251")
        f.write(box_quest_change.get())
        f.close()
        messagebox.showinfo(title="Уведомление", message="Был изменен текст подсказки!")

    def main_funn(self):
        self.create_pattern_of_crypt()
        self.decrypting()

        # деактивация всех кнопок вторичной формы
        # if st_0 == True or mainanswer_Entry.get() == "Ключ":
        #     st_0 = False
        #     messagebox.showwarning(title="Внимание!", message="Настоятельно рекомендуется поменять\nключ шифрования на cвой, особый!")

    def fff(self):
        ...
        # if mainanswer_Entry.get() == "":
        #     main_recieve_button.config(state=DISABLED)
        # if mainanswer_Entry.get() != "":
        #     main_recieve_button.config(state=NORMAL)

    def b1(self):
        ...
        # if box_change_key.get() == "":
        #     button_change_key.config(state=DISABLED)
        # if box_change_key.get() != "":
        #     button_change_key.config(state=NORMAL)

    def b2(self):
        ...
        # if box_quest_change.get() == "":
        #     button_quest_change.config(state=DISABLED)
        # if box_quest_change.get() != "":
        #     button_quest_change.config(state=NORMAL)

    def fun_001(self):
        global name_text
        # mainquestion_Entry.delete(0, END)
        # mainquestion_Entry.insert(0, name_text)

    def fun_002(self):

        if self.hide == True:
            hide = False
            x_resolution = 280
            y_resolution = 250
            # root.geometry(str(x_resolution) + "x" + str(y_resolution))
            # hider.place(width=20, height=20, x=237, y=228)
            # hider.config(text="▲")
            # box_change_key.place(width=205, height=23, x=32, y=150)
            # button_change_key.place(width=205, height=23, x=32, y=175)
            # box_quest_change.place(width=205, height=23, x=32, y=200)
            # button_quest_change.place(width=205, height=23, x=32, y=225)
        else:
            hide = True
            x_resolution = 280
            y_resolution = 150
            # root.geometry(str(x_resolution) + "x" + str(y_resolution))
            # hider.place(width=20, height=20, x=237, y=126)
            # hider.config(text="▼")

    def change_key(self):
        global key, context_matrix, current_file, will_changed
        will_changed = True
        context_matrix = []
        for i in range(len(self.left_side)):
            context_matrix.append(self.up_side[i + 1:] + self.up_side[0:i + 1])
        key = box_change_key.get()

        buf_kk = key

        file = current_file
        while (len(key) < len(file)):
            key = key * 2
        if len(key) != len(file):
            key = key[:-1 * (len(key) - len(file))]

        encrypted_message = ""
        for i in range(len(file)):
            encrypted_message = encrypted_message + context_matrix[self.left_side.index(file[i])][self.up_side.index(key[i])]
        f = open(self.path_2, 'w', encoding="cp1251")
        f.write(encrypted_message)
        f.close()
        file = encrypted_message
        decrypted_message = ""
        for i in range(len(file)):
            buf_mes = []
            for j in range(len(self.left_side)):
                buf_mes = buf_mes + list(context_matrix[j][self.up_side.index(key[i])])
            decrypted_message = decrypted_message + self.left_side[buf_mes.index(file[i])]
        key = buf_kk
        current_file = decrypted_message
        self.combobox_update()
        messagebox.showinfo(title="Уведомление", message="Был изменен ключ шифрования!")
