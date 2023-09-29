from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint


# ! переменные 
# * Главное окно
# Размеры
WEIGHT = 1600
HEIGHT = 900
# координаты
x_win = 0
y_win = 0

# * Верхняя панель
# размеры
weight_hint = WEIGHT
height_hint = int(HEIGHT * 0.033)
# координаты
x_hint = x_win
y_hint = y_win

# * горизонтальная разделительная линия
# размеры
weight_widget_4 = WEIGHT
height_widget_4 = 6
# кординаты
x_widget_4 = 0
y_widget_4 = int(HEIGHT * 0.08)

# * вертикальная разделительная линия
# размеры
weight_widget_3 = 6
height_widget_3 = HEIGHT - height_hint
# кординаты
x_widget_3 = int(WEIGHT * 0.2)
y_widget_3 = height_hint

# * Менюшка
# размеры
weight_widget_5 = x_widget_3
height_widget_5 = HEIGHT - height_hint
# координаты
x_widget_5 = x_hint
y_widget_5 = height_hint

# * Кнопка выхода(крестик)
# размеры
weight_push_exit = 39
height_push_exit = height_hint
# координаты
x_push_exti = WEIGHT - weight_push_exit
y_push_exit = 0

# * Кнопка сворачивания экрана 
# размеры 
weight_push_hider = 39
height_push_hider = height_hint
# координаты
x_push_hider = WEIGHT - weight_push_exit - weight_push_hider
y_push_hider = 0

# * Кнопка вызова меню
# размеры
weight_menu_show = (x_widget_3 // 2) // 3
height_menu_show = int((y_widget_4 - height_hint) * 0.6)
# координаты
x_menu_show = int(x_widget_3 * 0.02)
y_menu_show =  (((y_widget_4 - height_hint) //2) + height_hint) - height_menu_show // 2  # height_hint + 2

# * Кнопка отзыва меню
# размеры
weight_menu_hide = weight_menu_show
height_menu_hide = height_menu_show
# координаты
x_menu_hide = x_menu_show
y_menu_hide = y_menu_show


# * строка поиска
# размеры
weight_search_line = x_widget_3 // 2
height_search_line = height_menu_show
# координаты
x_search_line =int( weight_menu_show + x_menu_show + ((x_widget_3- (weight_menu_show + x_menu_show)) * 0.05))
y_search_line = y_menu_show

# * Строка с именем заметки
# размеры
weight_choice_name = (WEIGHT - (x_widget_3 + weight_widget_3)) // 5
height_choice_name = y_widget_4 - height_hint
# координаты
x_choice_name = x_widget_3 + weight_widget_3 + 5
y_choice_name = height_hint + 2

# * Кнопка добавления заметки
# размеры
weight_add_note = int(x_widget_3 * 0.15)
height_add_note = weight_add_note 
# Координаты
x_add_note =  x_widget_3 - weight_add_note * 2
y_add_note = int(HEIGHT - weight_add_note * 1.5)

# * Рабочая зона
# размеры 
weight_work_area = int((WEIGHT - x_widget_3 + weight_widget_3) * 0.94)
height_work_area = HEIGHT - y_widget_4 + weight_widget_4
# координаты
x_work_area = x_widget_3 + weight_widget_3
y_work_area = y_widget_4 + height_widget_4





class Ui_programm(object): # Может быть вариант с class Ui_programm(object) # ! понять зачем нужен object  
    def setupUi(self, note_win):
        note_win.setObjectName('note_win')
        note_win.resize(WEIGHT, HEIGHT)

        # * Добавление иконки для программы
        icon = QtGui.QIcon()
        # продолжить добавление чуть позже

        # Создание рабочего окна
        self.widget = QtWidgets.QWidget(note_win)
        # Настройка размеров рабочего окна
        self.widget.setGeometry(QtCore.QRect(x_win, y_win, WEIGHT, HEIGHT))
        # Настройка вида рабочего окна
        # Присвоение имени для окна
        self.widget.setObjectName('widget')

        
        # * Создание верхней панели
        # Объявление верхней панели
        self.widget2 = QtWidgets.QWidget(self.widget)
        
        # Настройка размеров верхней панели
        self.widget2.setGeometry(QtCore.QRect(x_hint, y_hint, weight_hint, height_hint))

        # Присвоения имени для верхней панели
        self.widget2.setObjectName('widget_2')



        # * Создание вертикальной разделительной панели
        # Объявдение
        self.widget3 = QtWidgets.QWidget(self.widget)

        #  Настройка размеров
        self.widget3.setGeometry(QtCore.QRect(x_widget_3, y_widget_3, weight_widget_3, height_widget_3))

        # Присвоение имени объекта
        self.widget3.setObjectName('widget_3')


        # * Создание горизонтальной разделительной линии
        # Объявление
        self.widget4 = QtWidgets.QWidget(self.widget)

        # Настройка размеров
        self.widget4.setGeometry(QtCore.QRect(x_widget_4, y_widget_4, weight_widget_4, height_widget_4))

        # Присвоение имени объекта
        self.widget4.setObjectName('widget_4')

        
        # * Создание менюшки 
        # Создание
        self.widget5 = QtWidgets.QWidget(self.widget)

        # Настройка размеров
        self.widget5.setGeometry(QtCore.QRect(x_widget_5, y_widget_5, weight_widget_5, height_widget_5))

        # Присвоение имени объекта
        self.widget5.setObjectName('widget_6') # ! Не забыть сделать widget_5

        # "Прячем" виджет
        self.widget5.hide()



        # * Крестик
        # Создание кнопки выхода (крестика)
        self.push_exit = QtWidgets.QPushButton(self.widget2)

        # Настройка размеров и расположения крестика
        self.push_exit.setGeometry(QtCore.QRect(x_push_exti, y_push_exit, weight_push_exit, height_push_exit))

        # Вносим внутрь кнопки сам крестик
        self.push_exit.setText("X")

        # Присвоение имени объекта 
        self.push_exit.setObjectName('push_exit')


        # * Сворачивание экрана
        # Создание кнопки сворачивания экрана
        self.push_hider = QtWidgets.QPushButton(self.widget2)

        # Настройка размеров и расположения кнопки сворачивания
        self.push_hider.setGeometry(QtCore.QRect(x_push_hider, y_push_hider, weight_push_hider, height_push_hider))

        # Вносим внутрь кнопки полоску
        self.push_hider.setText("▬")

        


        # Присвоение имени объекта 
        self.push_hider.setObjectName('push_hider')


        # * Строка поиска
        # Создание строки 
        self.search_line = QtWidgets.QLineEdit(self.widget)

        self.search_line.setGeometry(QtCore.QRect(x_search_line, y_search_line, weight_search_line, height_search_line))

        self.search_line.setObjectName('search_line')

        
        # * Кнопка открытия меню
        # Создание кнопки
        self.menu_show = QtWidgets.QPushButton(self.widget)

        # Настройка размеров кнопки
        self.menu_show.setGeometry(QtCore.QRect(x_menu_show, y_menu_show, weight_menu_show, height_menu_show))

        # Настройка текста кнопки
        self.menu_show.setText('==\n==\n==')

        # Присвоение имени объекта
        self.menu_show.setObjectName("menu_show")

        # * Кнопка закрытия меню 
        self.menu_hide = QtWidgets.QPushButton(self.widget)

        self.menu_hide.setGeometry(QtCore.QRect(x_menu_hide, y_menu_hide, weight_menu_hide, height_menu_hide))

        # Настройка текста кнопки
        self.menu_hide.setText('back')

        # Присвоение имени объекта
        self.menu_hide.setObjectName("menu_hide")

        self.menu_hide.hide()

        
        # * Создание QLineEdit имени
        # объявление
        self.choice_name = QtWidgets.QLabel(self.widget)

        # Настройка размеров и местоположения
        self.choice_name.setGeometry(QtCore.QRect(x_choice_name, y_choice_name, weight_choice_name, height_choice_name))

        # Присвоение имени объекта
        self.choice_name.setObjectName('choice_name')

        # Настройка текста
        self.choice_name.setText('name:')

        # * Создание кнопки добавления заметки
        # объявление
        self.add_note = QtWidgets.QPushButton(self.widget)

        # настройка размеров и местоположения
        self.add_note.setGeometry(QtCore.QRect(x_add_note, y_add_note, weight_add_note, height_add_note))

        # Настройка текста
        self.add_note.setText('+')

        # присвоение имени объекта
        self.add_note.setObjectName('add_note')


        # * Рабочая зона
        # Объявление
        self.work_area = QtWidgets.QTextEdit(self.widget)

        # Настройка размеров
        self.work_area.setGeometry(x_work_area, y_work_area, weight_work_area, height_work_area)

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
        6. got it
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

# ! ---------------------------------------------------------

    # Функция для закрытия приложения
    def close_app(self):
        self.close()

    # Функция для сворачивания приложения
    def hide_app(self):
        self.showMinimized()

    # Функция для показа меню
    def show_menu(self):
        self.menu_show.hide()
        self.search_line.hide()
        self.add_note.hide()
        self.widget5.show()
        self.menu_hide.show()

    def hide_menu(self):
        self.widget5.hide()
        self.menu_hide.hide()
        self.menu_show.show()
        self.search_line.show()
        self.add_note.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    programm = Widget()


    # * Подключение кнопок
    programm.push_exit.clicked.connect(programm.close_app)
    programm.push_hider.clicked.connect(programm.hide_app)
    programm.menu_show.clicked.connect(programm.show_menu)
    programm.menu_hide.clicked.connect(programm.hide_menu)


    # TODO -------------------------------------------------
    file = QtCore.QFile("./school_style.css")                             
    file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
    stream = QtCore.QTextStream(file)
    app.setStyleSheet(stream.readAll())
    # TODO -------------------------------------------------
    

    programm.show()
    sys.exit(app.exec_())