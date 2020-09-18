class DataBase:
    def __init__(self):
        self.admins = []
        self.admins.append(Admin('ser', '123'))  # objects

    def addData(self, login, password):
        self.admins.append(Admin(login, password))
        print(self.admins)

    def outputAdmins(self):
        for admin in self.admins:
            admin.outputData()

    def returnAdmins(self):
        return self.admins


class CheckCommand:
    def commandForGenAdmin(self, command):
        if command == 'na':
            GeneralAdmin().addAdmin()
        elif command == 'nu':
            pass
        elif command == 'nup':
            pass
        elif command == 'da':
            pass
        elif command == 'du':
            pass
        elif command == 'dup':
            pass
        elif command == 'em':
            OutputMessage().generalMessage()
        else:
            print('Команду не розпізнано! Повторіть ще раз')
            OutputMessage().genAdminMess()

    def commandForGeneralMenu(self, command):
        if command == 'lga':
            GeneralAdmin().isGenAdmin()
        elif command == 'la':
            if len(DataBase().returnAdmins()) == 0:
                OutputMessage().noAdmins()
            else:
                data = OutputMessage().loginAdmin()
                for admin in DataBase().returnAdmins():
                    if admin.login == data[0] and admin.password == data[1]:
                        print('ok')
                    else:
                        print('bad')

        elif command == 'nu':
            pass
        elif command == 'nup':
            pass
        elif command == 'du':
            pass
        elif command == 'dup':
            pass
        else:
            print('Команду не розпізнано! Повторіть ще раз')
            OutputMessage().generalMessage()

    def commandForAdmin(self):
        pass


class GeneralAdmin:
    def __init__(self):
        self.login = 'toor'
        self.password = 'root'

    def messGemAdmin(self):
        print('Ви увійшли як головний адміністатор')
        OutputMessage().genAdminMess()

    def addAdmin(self):
        newAdminLogin = input('Введіть логін для нового Адміністратора: ')
        newAdminPassword = input('Введіть пароль для нового Адміністратора: ')

        if newAdminLogin == self.login or newAdminPassword == self.password:
            print('Неприпустимі дані! Спробуйте ще раз')
            self.addAdmin()
        else:
            if len(DataBase().returnAdmins()) == 0:
                DataBase().addData(newAdminLogin, newAdminPassword)
                print('Ви успішно додали нового адміністратора! ')

                answer = input(' -- Переглянути? (y/n): ')

                if answer == 'y':
                    DataBase().outputAdmins()
                    continueCommand = input(' -- Продовжити ? (y/n): ')

                    if continueCommand == 'y':
                        print('Ви у режимі головного адміністратора')
                        OutputMessage().genAdminMess()
                    else:
                        OutputMessage().generalMessage()

                else:
                    print('Ви у режимі головного адміністратора')
                    OutputMessage().genAdminMess()

            else:
                for admin in DataBase().returnAdmins():
                    if admin.login == newAdminPassword or admin.password == newAdminPassword:
                        print('Неприпустимі дані! Введіть інші дані')
                        self.addAdmin()
                    else:
                        DataBase().addData(newAdminLogin, newAdminPassword)
                        print(len(DataBase().returnAdmins()))

    def isGenAdmin(self):
        print('Для підтвердження статусу головного адміністратора введіть наступні дані')
        login = input('Введіть логін: ')
        password = input('Введіть пароль: ')

        if login == self.login and password == self.password:
            self.messGemAdmin()
        else:
            print('Невірні дані! Попробуйте ще раз')
            self.isGenAdmin()


class Admin:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def outputData(self):
        print(' -- login:', self.login, ' -- password:', self.password)


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def returnData(self):
        data = {
            'username': self.username,
            'password': self.password
        }
        return data


class UserProfile(User):
    def __init__(self, username, password, name, age):
        User.__init__(self, username, password)

        self.name = name
        self.age = age

    def returnData(self):
        data = {
            'username': self.username,
            'password': self.password,
            'name': self.name,
            'age': self.age
        }
        return data


class TransformationUserToUserProfile:
    def __init__(self):
        pass


class OutputMessage:
    def generalMessage(self):
        print('Ви в головному меню.')
        print(' -- Ввійти як головний адміністратор (lga): ')
        print(' -- Ввійти як адміністратор (la): ')
        print(' -- Додати нового користувача (nu): ')
        print(' -- Додати новий профіль користувача (nup): ')
        print(' -- Видалити користувача (du): ')
        print(' -- Видалити профіль користувача (dup): ')

        command = input('Введіть потрібну команду: ')
        CheckCommand().commandForGeneralMenu(command)

    def genAdminMess(self):
        print(' -- Додати нового адміністратора (na): ')
        print(' -- Додати нового користувача (nu): ')
        print(' -- Додати новий профіль користувача (nup): ')
        print(' -- Видалити адміністратора (da): ')
        print(' -- Видалити користувача (du): ')
        print(' -- Видалити профіль користувача (dup): ')
        print(' -- Повернутися до головного меню (em): ')

        command = input('Введіть команду: ')
        CheckCommand().commandForGenAdmin(command)

    def noAdmins(self):
        print('Адміністратори відсутрні!')
        answer = input(' -- Продовжити ? (y/n): ')

        if answer == 'y':
            self.noAdmins()
        else:
            self.generalMessage()

    def loginAdmin(self):
        print('Щоб увіти як адміністратор введіть наступні дані')
        login = input('Введіть логін: ')
        password = input('Введыть пароль: ')

        data = [login, password]
        return data


class create:
    def __init__(self):
        pass

    def createUser(self):
        pass

    def createUserProfile(self):
        pass


class delete:
    def __init__(self):
        pass

    def deleteUser(self):
        pass

    def deleteUserProfile(self):
        pass


OutputMessage().generalMessage()
