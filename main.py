from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

# 导入初始选择界面UI
from UI.Initial_ui import Ui_Initial_widget

# 导入登入界面UI
from UI.Login_ui import Ui_Login_MainWindow

# 导入注册界面UI
from UI.Registered_ui import Ui_registered_Widget

# 导入学生界面UI
from UI.Student_ui import Ui_Student_Widget

# 学生信息界面
from UI.Managing_Student_ui import Ui_Managing_Student_Widget


# 注册界面
class Registered(QWidget):
    def __init__(self):
        super(Registered, self).__init__()
        self.ui = Ui_registered_Widget()  # UI实例化
        self.ui.setupUi(self)

        # 确定注册
        self.ui.PushButton_Submit.clicked.connect(self.__submit)

    def __submit(self):
        # 检测注册信息是否合法
        # ........................

        # 关闭注册窗口
        registered.close()


# 登入界面
class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_Login_MainWindow()  # UI实例化
        self.ui.setupUi(self)  # 导入UI

        # PushButton-返回
        self.ui.PushButton_back.clicked.connect(self.__back)

        # PushButton-注册
        self.ui.PushButton_Register.clicked.connect(self.__registered)

        # PushButton-登入
        self.ui.PushButton_Login.clicked.connect(self.__login)

    def __back(self):
        login.close()
        initial.show()

    # 打开打开注册窗口
    def __registered(self):
        registered.show()

    def __login(self):
        # 教师
        if initial.attribute == 0:
            login.close()
            managing_student.show()
        # 学生
        else:
            login.close()
            student.show()


# 选择自己身份界面
class Initial(QWidget):
    def __init__(self):
        super(Initial, self).__init__()
        # attribute(-1, 0, 1)      -1 => 没做选择  0 => 选择教师   1 => 选择学生
        self.attribute = -1

        # pyside6 导入UI
        self.ui = Ui_Initial_widget()  # UI实例化
        self.ui.setupUi(self)

        # PushButton-教师
        self.ui.PushButton_teacher.clicked.connect(self.__initial)
        self.ui.PushButton_teacher.clicked.connect(self.__teacher)

        # PushButton-学生
        self.ui.PushButton_student.clicked.connect(self.__initial)
        self.ui.PushButton_student.clicked.connect(self.__student)

    def __initial(self):
        login.show()
        initial.close()

    def __teacher(self):
        self.attribute = 0
        print("Hi teacher")

    def __student(self):
        self.attribute = 1
        print("Hi Student")


class Student(QWidget):
    def __init__(self):
        super(Student, self).__init__()
        self.ui = Ui_Student_Widget()  # 实例化
        self.ui.setupUi(self)  # 导入UI


class ManagingStudent(QWidget):
    def __init__(self):
        super(ManagingStudent, self).__init__()
        self.ui = Ui_Managing_Student_Widget()  # 实例化
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])  # 启动一个应用

    # 实例化
    login = Login()  # 登入界面
    registered = Registered()  # 注册界面
    initial = Initial()  # 选择界面
    student = Student()  # 学生界面
    managing_student = ManagingStudent()  # 管理学生信息界面

    # 窗口显示
    initial.show()

    app.exec()  # 避免程序执行到这一行直接退出
