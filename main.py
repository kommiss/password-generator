from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QLabel,
                            QWidget, QPushButton,
                            QVBoxLayout, QHBoxLayout)
from random import randint

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.window_settings()
        self.initUI()
        self.connects()
        self.show()
    
    def window_settings(self):
        '''Функция устанавливает
        настройки экрана (размер, название и т.д.).'''
        self.setWindowTitle('рандомайзер паролей')
        self.resize(400,200)
    
    def initUI(self):
        '''Создаются все объекты, направляющие
        и направляющие крепятся на главный экран'''
        layout = QVBoxLayout()
        self.btn1 = QPushButton('сгенерировать пароль')
        self.btn1.setStyleSheet('width: 200px; height: 50px;')
        self.text = QLabel('')
        self.text.setStyleSheet('font-size: 18px;')
        layout.addWidget(self.btn1,alignment = Qt.AlignCenter)
        layout.addWidget(self.text,alignment = Qt.AlignCenter)

        self.setLayout(layout)


    def connects(self):
        '''Здесь подключаются все события'''
        self.btn1.clicked.connect(self.change_password)

    def change_password(self):
        new_password = self.generate_password()
        self.text.setText(new_password)

    def generate_password(self):
        alphabet = 'qwertyuiopasdfghjklzxcvbnm1234567890'
        lenght_password = randint(6, 12)
        password = ''
        for el in range(lenght_password):
            index = randint(0, len(alphabet)-1)
            symbol = alphabet[index]
            if randint(1, 2) == 1:
                symbol = symbol.upper()
            password += symbol
        return password

if __name__ == "__main__":
    app = QApplication([])
    win = MainWindow()
    app.exec_()