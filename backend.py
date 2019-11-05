from os import remove as deleting_file
import os.path


class Backend:

    def __init__(self, interface_gui):
        # Объявление последовательностей из символов и букв русского и английского алфавитов
        self.add = None
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
        self.functions = interface_gui
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
            while (len(self.key) < len(self.file)):
                self.key = self.key * 2
            if len(self.key) != len(self.file):
                self.key = self.key[:-1 * (len(self.key) - len(self.file))]

            self.encrypted_message = ""
            for i in range(len(self.file)):
                self.encrypted_message = self.encrypted_message + self.context_matrix[self.left_side.index(self.file[i])][self.up_side.index(self.key[i])]
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
            self.functions.message_box_error(title="Ошибка", message="Неверный код доступа! \n Закрытие программы...")
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

    def encrypting(self):
        # шифрование
        file = self.current_file
        encrypted_message = ""
        for i in range(len(file)):
            encrypted_message = encrypted_message + self.context_matrix[self.left_side.index(file[i])][self.up_side.index(self.key[i])]
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
        self.ui_interface.comboBox_check.setEditText(self.choice_account)

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
            while len(self.key) < len(file):
                self.key = self.key * 2
            if len(self.key) != len(file):
                self.key = self.key[:-1 * (len(self.key) - len(file))]

    def change_data(self):
        if self.ui_interface.comboBox_check.currentText() != "<Выберите аккаунт>":
            self.file[self.ui_interface.comboBox_check.currentText()] = self.file.pop(self.select)
            self.select = self.ui_interface.comboBox_check.currentText()
            self.file[self.select][0] = self.ui_interface.textbox_email.text()
            self.file[self.select][1] = self.ui_interface.textbox_password.text()
            self.file[self.select][2] = self.ui_interface.textbox_add_inf.text()
            self.current_file = str(self.file)
            self.combobox_update()

            # self.ui_interface.textbox_email.clear()
            # self.ui_interface.textbox_password.clear()
            # self.ui_interface.textbox_add_inf.clear()

    def add_data(self):
        answer = True
        if self.ui_interface.comboBox_check.currentText() != "<Выберите аккаунт>":
            if self.ui_interface.comboBox_check.currentText() in self.name_keys:
                answer = self.functions.message_box_yes_no(title="Внимание...", message="Такая запись в базе уже есть.\n" +
                                                                          "Вы хотите обновить информацию о записи? \n" + "<" + self.ui_interface.comboBox_check.currentText() + ">")

            if answer == 1:
                self.file[self.ui_interface.comboBox_check.currentText()] = [self.ui_interface.textbox_email.text(),
                                                                        self.ui_interface.textbox_password.text(),
                                                                        self.ui_interface.textbox_add_inf.text()]
                self.current_file = str(self.file)
                self.combobox_update()
                # self.ui_interface.comboBox_check.setEditText(self.choice_account)

    # Выход
    def exit_fun(self, raise_call=True):
        raise_call = not raise_call
        self.create_pattern_of_crypt()
        self.encrypting()
        print(raise_call)
        if raise_call:
            raise SystemExit(0)

    def f_1(self):
        self.add = 1
        self.buttons()

    def f_2(self):
        self.add = 2
        self.buttons()

    def f_3(self):
        self.add = 3
        self.buttons()

    # копирование данные из текстбоксов в буфер обмена
    def buttons(self):
        if self.select in self.name_keys:
            if self.add == 1:
                # root.clipboard_clear()
                # root.clipboard_append(file[select][0])
                ...
            if self.add == 2:
                # root.clipboard_clear()
                # root.clipboard_append(file[select][1])
                ...
            if self.add == 3:
                # root.clipboard_clear()
                # root.clipboard_append(file[select][2])
                ...

    # удаление выбранного аккаунта
    def del_acc(self):
        current_text = self.ui_interface.comboBox_check.currentText()
        if current_text != "<Выберите аккаунт>" and current_text in self.name_keys:

            answer = 1
            answer = self.functions.message_box_yes_no(title="Внимание...", message="Вы уверены что хотите удалить запись:\n" +
                                                                   "<" + current_text + ">")
            if answer == 1:
                if self.select in self.name_keys:
                    del self.file[self.select]
                    self.current_file = str(self.file)
                    index = self.ui_interface.comboBox_check.currentIndex()
                    self.ui_interface.comboBox_check.removeItem(index)
                    self.select = ""
                    self.combobox_update()

                    self.ui_interface.comboBox_check.setEditText(self.choice_account)
                    self.ui_interface.textbox_email.clear()
                    self.ui_interface.textbox_password.clear()
                    self.ui_interface.textbox_add_inf.clear()
                    self.ui_interface.textbox_email.setEnabled(False)
                    self.ui_interface.textbox_password.setEnabled(False)
                    self.ui_interface.textbox_add_inf.setEnabled(False)

    def ex_cop(self):
        warni = self.functions.message_box_yes_no(title="Внимание!", message="Вы уверены, что хотите экспортировать \nрасшифрованные данные в корень программы?")
        if warni == 1:
            ff = self.current_file
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

    def change_message_fun(self):
        f = open(self.settings, "w", encoding="cp1251")
        f.write(self.ui_interface.textbox_change_message.text())
        f.close()
        self.functions.message_box_information(title="Уведомление", message="Был изменен текст подсказки!")

    def main_funn(self):
        self.create_pattern_of_crypt()
        self.decrypting()

        # деактивация всех кнопок вторичной формы
        if self.st_0 == True or self.ui_interface.textbox_answer.text() == "Ключ":
            self.st_0 = False
            self.functions.message_box_warnning(title="Внимание!", message="Настоятельно рекомендуется поменять\nключ шифрования на cвой, особый!")

    def change_key(self):
        self.will_changed = True
        self.context_matrix = []
        for i in range(len(self.left_side)):
            self.context_matrix.append(self.up_side[i + 1:] + self.up_side[0:i + 1])
        self.key = self.ui_interface.textbox_change_key.text()

        buf_kk = self.key

        file = self.current_file
        while len(self.key) < len(file):
           self.key = self.key * 2
        if len(self.key) != len(file):
            self.key = self.key[:-1 * (len(self.key) - len(file))]

        encrypted_message = ""
        for i in range(len(file)):
            encrypted_message = encrypted_message + \
                                self.context_matrix[self.left_side.index(file[i])][self.up_side.index(self.key[i])]
        f = open(self.path_2, 'w', encoding="cp1251")
        f.write(encrypted_message)
        f.close()
        file = encrypted_message
        decrypted_message = ""
        for i in range(len(file)):
            buf_mes = []
            for j in range(len(self.left_side)):
                buf_mes = buf_mes + list(self.context_matrix[j][self.up_side.index(self.key[i])])
            decrypted_message = decrypted_message + self.left_side[buf_mes.index(file[i])]
        self.key = buf_kk
        self.current_file = decrypted_message
        self.combobox_update()
        self.functions.message_box_information(title="Уведомление", message="Был изменен ключ шифрования!")
