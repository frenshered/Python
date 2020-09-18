newUserName = input('Enter your name:')
newUserAge = input('Enter your age:')
newUserUsername = input('Enter your username:')
newUserPassword = input('Enter your password:')


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class UserProfile(User):
    def __init__(self, username, password, name, age):
        super().__init__(name, age)
        self.username = username
        self.password = password


class outputDataClass:
    def __init__(self, className, name, age, userName, userPassword):
        self.className = className
        self.name = name
        self.age = age
        self.userName = userName
        self.userPassword = userPassword

    def outputUserData(self):
        # self.className(self.name, self.age).output()
        print('UserData: ', self.className(self.name, self.age).name, self.className(self.name, self.age).age)

    def outputProfileData(self):
        # self.className(self.userName, self.userPassword, self.name, self.age).outputAllInfo()
        print('UserProfileData:')
        print(self.className(self.userName, self.userPassword, self.name, self.age).username)
        print(self.className(self.userName, self.userPassword, self.name, self.age).password)
        print(self.className(self.userName, self.userPassword, self.name, self.age).name)
        print(self.className(self.userName, self.userPassword, self.name, self.age).age)


outputDataClass(User, newUserName, newUserAge, newUserUsername, newUserUsername).outputUserData()
outputDataClass(UserProfile, newUserName,  newUserAge, newUserUsername, newUserPassword).outputProfileData()
