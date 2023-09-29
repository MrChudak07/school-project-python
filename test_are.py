from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint






class Ui_programm(object): # Может быть вариант с class Ui_programm(object) # ! понять зачем нужен object  
    def setupUi(self, note_win):
        note_win.setObjectName('note_win')
        note_win.resize(1600, 900)

        # * Добавление иконки для программы
        icon = QtGui.QIcon()
        # продолжить добавление чуть позже

        # Создание рабочего окна
        self.widget = QtWidgets.QWidget(note_win)
        # Настройка размеров рабочего окна
        self.widget.setGeometry(QtCore.QRect(0,0, 1600, 900))
        # Настройка вида рабочего окна
        # Присвоение имени для окна
        self.widget.setObjectName('widget')

        
        # * Создание верхней панели
        # Объявление верхней панели
        self.widget2 = QtWidgets.QWidget(self.widget)
        
        # Настройка размеров верхней панели
        self.widget2.setGeometry(QtCore.QRect(0,0, 1600, 31))

        # Присвоения имени для верхней панели
        self.widget2.setObjectName('widget_2')



        # * Создание вертикальной разделительной панели
        # Объявдение
        self.widget3 = QtWidgets.QWidget(self.widget)

        #  Настройка размеров
        self.widget3.setGeometry(QtCore.QRect(300, 31, 9, 866))

        # Присвоение имени объекта
        self.widget3.setObjectName('widget_3')


        # * Создание горизонтальной разделительной линии
        # Объявление
        self.widget4 = QtWidgets.QWidget(self.widget)

        # Настройка размеров
        self.widget4.setGeometry(QtCore.QRect(0, 70, 300, 10))

        # Присвоение имени объекта
        self.widget4.setObjectName('widget_4')

        
        # * Создание горизонтаьной панели с именем и тэгами
        # Объявление
        self.widget5 = QtWidgets.QWidget(self.widget)

        # Настройка размеров
        self.widget5.setGeometry(QtCore.QRect(309, 70, 1289, 10))

        # Присвоение имени объекта
        self.widget5.setObjectName('widget_5')

        # * Создание менюшки 
        self.widget6 = QtWidgets.QWidget(self.widget)

        self.widget6.setGeometry(QtCore.QRect(0, 31, 300, 866))

        self.widget6.setObjectName('widget_6')

        self.widget6.hide()



        # * Крестик
        # Создание кнопки выхода (крестика)
        self.push_exit = QtWidgets.QPushButton(self.widget2)

        # Настройка размеров и расположения крестика
        self.push_exit.setGeometry(QtCore.QRect(1575, 7, 20, 20))

        # Вносим внутрь кнопки сам крестик
        self.push_exit.setText("X")

        # Установка максимально возможного размера для крестика
        self.push_exit.setMaximumSize(33,23)

        # ? просто пусть так
        # self.push_exit.setStyleSheet("")

        # Присвоение имени объекта 
        self.push_exit.setObjectName('push_exit')


        # * Сворачивание экрана
        # Создание кнопки сворачивания экрана
        self.push_hider = QtWidgets.QPushButton(self.widget2)

        # Настройка размеров и расположения кнопки сворачивания
        self.push_hider.setGeometry(QtCore.QRect(1550, 7, 20, 20))

        # Вносим внутрь кнопки полоску
        self.push_hider.setText("▬")

        # Установка максимально возможного размера для кнопки сворачивания
        self.push_hider.setMaximumSize(33,23)


        # Присвоение имени объекта 
        self.push_hider.setObjectName('push_hider')


        # * Строка поиска
        # Создание строки 
        self.search_line = QtWidgets.QLineEdit(self.widget)

        self.search_line.setGeometry(QtCore.QRect(75, 40, 150, 25))

        self.search_line.setObjectName('search_line')

        
        # * Кнопка выхода в меню
        # Создание кнопки
        self.menu_show = QtWidgets.QPushButton(self.widget)

        # Настройка размеров кнопки
        self.menu_show.setGeometry(QtCore.QRect(15, 40, 25, 25))

        # Настройка текста кнопки
        self.menu_show.setText('==\n==\n==')

        # Присвоение имени объекта
        self.menu_show.setObjectName("menu_show")

        # * Кнопка закрытия меню
        self.menu_hide = QtWidgets.QPushButton(self.widget)

        self.menu_hide.setGeometry(QtCore.QRect(15, 40, 25, 25))

        # Настройка текста кнопки
        self.menu_hide.setText('==\n==\n==')

        # Присвоение имени объекта
        self.menu_hide.setObjectName("menu_hide")

        self.menu_hide.hide()

        
        # * Создание QLineEdit имени
        # объявление
        self.choice_name = QtWidgets.QLabel(self.widget)

        # Настройка размеров и местополодения
        self.choice_name.setGeometry(QtCore.QRect(315, 33, 200, 30))

        # Присвоение имени объекта
        self.choice_name.setObjectName('choice_name')

        # Настройка текста
        self.choice_name.setText('name:')


        # * Рабочая зона
        # Объявление
        self.work_area = QtWidgets.QTextEdit(self.widget)

        # Настройка размеров
        self.work_area.setGeometry(310, 80, 1210, 818)

        # Присвоение имени объекта
        self.work_area.setObjectName('work_area')



        '''
        установить текст кнопки "▬\n▬\n▬\n" - got it

        сделать полосу с названием и тэгами в рабочей зоне - got it

        сделать QTextEdit - got it

        сделать меню с кнопками справа - not got it

        попробовать сделать перемещение за кастомную панель сверху - not got it

        подключить css-файл - got it     

        Сделать переменные:

        1. Размеры всего окна: высота и ширина
        2. Размеры WindowHint(панель с крестиком): ширина окна; высота 50
        3. Размеры вертикальной разделительной линии: ширина 5-10 px; высота= высота всего окна - высота WindowsHint
        4. Размеры горизонтальной разделительной линии линии: ширина = координаты х(вертикаьной разделительной линии); высота 5-10px
        5. Размеры горизонтальной линии отделяющей рабочую зону от имени выбранной заметки: ширина = вся ширина  окна - самая правая координата вертикальной линии; высота = вся высота окна - нижняя кордина горизонтальной линии
        6. 
        '''































# ! пока не разобрался
class Widget(QtWidgets.QWidget, Ui_programm):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def mousePressEvent(self, event):
        # Если нажата левая кнопка мыши
        if event.button() == QtCore.Qt.LeftButton:
            # получаем координаты окна относительно экрана
            x_main = programm.geometry().x()
            y_main = programm.geometry().y()
            # получаем координаты курсора относительно окна нашей программы
            cursor_x = QtGui.QCursor.pos().x()
            cursor_y = QtGui.QCursor.pos().y()
            # проверяем условием позицию курсора на нужной области программы(у нас это верхний бар) 
            # если всё ок - перемещаем
            # иначе игнорируем
            if x_main <= cursor_x <= x_main + programm.geometry().width():
                if y_main <= cursor_y <= y_main + programm.widget2.geometry().height():
                    self.old_pos = event.pos()
                else:
                    self.old_pos = None
        elif event.button() == QtCore.Qt.RightButton:
            self.old_pos = None

    # вызывается при отпускании кнопки мыши
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = None

    # вызывается всякий раз, когда мышь перемещается
    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return
        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)

    # Функция для закрытия приложения
    def close_app(self):
        self.close()

    # Функция для сворачивания приложения
    def hide_app(self):
        self.showMinimized()

    # Функция вызова меню
    def show_menu(self):
        self.widget6.show()
        self.menu_show.hide()
        self.search_line.hide()
        self.menu_hide.show()

    def hide_menu(self):
        self.widget6.hide()
        self.menu_hide.hide()
        self.menu_show.show()
        self.search_line.show()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    programm = Widget()

    programm.push_exit.clicked.connect(programm.close_app)
    programm.push_hider.clicked.connect(programm.hide_app)
    programm.menu_show.clicked.connect(programm.show_menu)
    programm.menu_hide.clicked.connect(programm.hide_menu)


    # ! -------------------------------------------------
    file = QtCore.QFile("school_project/school_style.css")                             
    file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
    stream = QtCore.QTextStream(file)
    app.setStyleSheet(stream.readAll())
    # ! -------------------------------------------------
    

    programm.show()
    sys.exit(app.exec_())