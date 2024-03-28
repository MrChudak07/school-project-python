from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint, QSize
from PyQt5.QtGui import QContextMenuEvent
import sys
import os
import markdown
import matplotlib






# TODO Add:
# * main +
# * hint area + 
# * content area +
# * * work area +
# * * button area +
# * * tools area +
# * * * search area +
# * * * menu area +
# * * * note area +





# ! переменные 
# * Database
config = {"codehilite": {"linenums": "True"},
    # "mdx_math": {"enable_dollar_delimiter": True},
                    }
# Список заметок
l_notes = []
gpu_notes = []

# * Main
# Размеры
WIDTH = 1600
HEIGHT = 900
# координаты
x_win = 0
y_win = 0

# * hint
# размеры
width_hint = 1600
height_hint = 32
# координаты
x_hint = 0
y_hint = 0

# * content area
# size
width_content_area = 1600
height_content_area = 868
# locate
x_content_area = 0
y_content_area = 32

# *  name zone
# size
width_name_zone = 1178
height_name_zone = 52

# locate
x_name_zone = 326
y_name_zone = 0
# * work area
# size
width_work_area = 1178
height_work_area = 816
# координаты
x_work_area = 326
y_work_area = 52
# * buttons
# size
width_buttons_area = 96
height_buttons_area = 874
# locate
x_buttons_area = 1504
y_buttons_area = 0




# * tools
# size
width_tools = 326
height_tools = 868
# locate 
x_tools = 0
y_tools = 0

# * search area
# size
width_search_area = 326
height_search_area = 38
# locate
x_search_area = 0
y_search_area = 12

# * note area
# size
width_note_area = 326
height_note_area = 770
# locate
x_note_area = 0
y_note_area = 130




# * Menu
# размеры
width_widget_menu = 207
height_widget_menu = 124
# print(width_widget_menu, height_widget_menu)
# координаты
x_widget_menu = 0
y_widget_menu = 32




# * Кнопка выхода(крестик)
# размеры
width_push_exit = 24
height_push_exit = 24
# координаты
x_push_exti = 1568
y_push_exit = 2

# * Кнопка сворачивания экрана 
# размеры 
width_push_hider = 24
height_push_hider = 24
# координаты
x_push_hider = 1536
y_push_hider = 2

# * Кнопка вызова меню
# размеры
width_menu_show = 24
height_menu_show = 24
# координаты
x_menu_show = 8
y_menu_show = 2 # height_hint + 2

# * Кнопка отзыва меню
# размеры
# width_menu_hide = width_menu_show
# height_menu_hide = height_menu_show
# # координаты
# x_menu_hide = x_menu_show
# y_menu_hide = height_hint * 0.4
# * Кнопка открытия файла
# size
width_open_file = 191
height_open_file = 27
# locate
x_open_file = 8
y_open_file = 8

# * Кнопка сохранения
# size

width_save_project = 191
height_save_project = 27
# locate
x_save_project = 8
y_save_project = 35

# * Кнопка смены темы
# size

width_change_theme = 191
height_change_theme = 27
# locate
x_change_theme = 8
y_change_theme = 62

# * Кнопка помощи
# size

width_help = 191
height_help = 27
# locate
x_help = 8
y_help = 89



# * строка поиска
# размеры
width_search_line = 302
height_search_line = 38
# координаты
x_search_line = 12
y_search_line = 0


# * Строка с именем заметки
# размеры
width_choice_name =  1010
height_choice_name = 28
# координаты
x_choice_name = 16
y_choice_name = 16

# * Кнопка показа результата
# size
width_button_result = 136
height_button_result = 29
# locate
x_button_result = 1026
y_button_result = 16

# * Кнопка добавления заметки
# размеры
width_add_note = 32
height_add_note = 32
# Координаты
x_add_note =  18
y_add_note = 74

# * Подпись "добавить заметку" 

# размеры
width_note_lb = 126
height_note_lb = 19
# Координаты
x_note_lb = 62
y_note_lb = 80

# * QColorDialog (Выбор цвета)
# size
width_button_color = 32
height_button_color = 32
# locate
x_button_color = 12
y_button_color = 12




class Ui_programm(object): # Может быть вариант с class Ui_programm()  
    # def __init__(self):
    def setupUi(self, note_win):
        self.pressed = None
        note_win.setObjectName('note_win')
        note_win.resize(WIDTH, HEIGHT)

        # * Добавление иконки для программы
        icon = QtGui.QIcon()
        
        # продолжить добавление чуть позже

        # Создание рабочего окна
        self.main = QtWidgets.QWidget(note_win)
        # Настройка размеров рабочего окна
        self.main.setGeometry(QtCore.QRect(x_win, y_win, WIDTH, HEIGHT))
        # Настройка вида рабочего окна
        # Присвоение имени для окна
        self.main.setObjectName('main')

        
        # * Создание верхней панели
        # Объявление верхней панели
        self.hint = QtWidgets.QWidget(self.main)
        
        # Настройка размеров верхней панели
        self.hint.setGeometry(QtCore.QRect(x_hint, y_hint, width_hint, height_hint))

        # Присвоения имени для верхней панели
        self.hint.setObjectName('window_hint')

        # ! --------------------------------------------------------------------
        self.content_area = QtWidgets.QWidget(self.main)
        self.content_area.setGeometry(QtCore.QRect(x_content_area, y_content_area, width_content_area, height_content_area))
        self.content_area.setObjectName('content')

        self.tools = QtWidgets.QWidget(self.content_area)
        self.tools.setGeometry(QtCore.QRect(x_tools, y_tools, width_tools, height_tools))
        self.tools.setObjectName('tools')
        self.tools.lower()

        self.buttons = QtWidgets.QWidget(self.content_area)
        self.buttons.setGeometry(QtCore.QRect(x_buttons_area, y_buttons_area, width_buttons_area, height_buttons_area))
        self.buttons.setObjectName('buttons')

        self.name_zone = QtWidgets.QWidget(self.content_area)
        self.name_zone.setGeometry(x_name_zone, y_name_zone, width_name_zone, height_name_zone )
        self.name_zone.setObjectName('name_zone')

        self.search = QtWidgets.QWidget(self.tools)
        self.search.setGeometry(QtCore.QRect(x_search_area, y_search_area, width_search_area, height_search_area))
        self.search.setObjectName('search')

        self.notes_area = QtWidgets.QWidget(self.tools)
        self.notes_area.setGeometry(QtCore.QRect(x_note_area, y_note_area, width_note_area, height_note_area))
        self.notes_area.setObjectName('notes')
       

        self.menu = QtWidgets.QWidget(self.main)
        self.menu.setGeometry(QtCore.QRect(x_widget_menu, y_widget_menu, width_widget_menu, height_widget_menu))
        self.menu.setObjectName('menu')
        self.menu.raise_()
        self.menu.hide()
        print(x_widget_menu, y_widget_menu, width_widget_menu, height_widget_menu)
        
        # ! ---------------------------------------------------------------------------
        self.work_area = QtWidgets.QTextEdit(self.content_area)
        
        # Настройка размеров
        self.work_area.setGeometry(x_work_area, y_work_area,width_work_area, height_work_area)

        # Присвоение имени объекта
        self.work_area.setObjectName('work_area')
        self.work_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        self.viewer = QtWidgets.QTextEdit(self.content_area, readOnly = True)
        # self.viewer = QtWidgets.QLabel()
        self.viewer.setGeometry(x_work_area, y_work_area, width_work_area, height_work_area)
        self.viewer.setObjectName('work_area')
        self.viewer.hide()
        # self.work_area.verticalScrollBar()
        # self.scrol = QtWidgets.QScrollBar(self.content_area)
        # self.scrol.setGeometry(QtCore.QRect(1178, 200, 20, 400))
        # self.scrol.setObjectName('scrol')
        

        # * tools components
        # * Строка поиска
        # Создание строки 
        self.search_line = QtWidgets.QLineEdit(self.search)
        self.search_line.setGeometry(QtCore.QRect(x_search_line, y_search_line,width_search_line, height_search_line))
        self.search_line.setPlaceholderText('поиск файла по имени')
        self.search_line.setObjectName('search_line')
        # * Кнопка открытия меню
        # Создание кнопки
        self.menu_show = QtWidgets.QPushButton(self.hint)

        # Настройка размеров кнопки
        self.menu_show.setGeometry(QtCore.QRect(x_menu_show, y_menu_show, width_menu_show, height_menu_show))

        # Настройка текста кнопки
        self.menu_show.setIcon(QtGui.QIcon('./images/menu_icon.svg'))
        self.menu_show.setIconSize(QSize(24, 24))

        # Присвоение имени объекта
        self.menu_show.setObjectName("menu_show")

        # * Component of notes area
        # * Создание кнопки добавления заметки
        # объявление
        self.add_note = QtWidgets.QPushButton(self.tools)

        # настройка размеров и местоположения
        self.add_note.setGeometry(QtCore.QRect(x_add_note, y_add_note, width_add_note, height_add_note))

        # Настройка текста
        self.add_note.setIcon(QtGui.QIcon('./images/add_icon.svg'))
        self.add_note.setIconSize(QSize(24, 24))

        # присвоение имени объекта
        self.add_note.setObjectName('add_note')

        self.note_lb = QtWidgets.QLabel(self.tools)
        self.note_lb.setGeometry(QtCore.QRect(x_note_lb, y_note_lb, width_note_lb, height_note_lb))
        self.note_lb.setText('создать заметку')
        self.note_lb.setObjectName('note_lb')
        


        # * Крестик
        # Создание кнопки выхода (крестика)
        self.push_exit = QtWidgets.QPushButton(self.hint)

        # Настройка размеров и расположения крестика
        self.push_exit.setGeometry(QtCore.QRect(x_push_exti, y_push_exit, width_push_exit, height_push_exit))

        # Вносим внутрь кнопки сам крестик
        self.push_exit.setIcon(QtGui.QIcon('./images/close_icon.svg'))
        self.push_exit.setIconSize(QSize(24, 24))

        # Присвоение имени объекта 
        self.push_exit.setObjectName('push_exit')


        # * Сворачивание экрана
        # Создание кнопки сворачивания экрана
        self.push_hider = QtWidgets.QPushButton(self.hint)

        # Настройка размеров и расположения кнопки сворачивания
        self.push_hider.setGeometry(QtCore.QRect(x_push_hider, y_push_hider, width_push_hider, height_push_hider))

        # Вносим внутрь кнопки полоску
        self.push_hider.setIcon(QtGui.QIcon('./images/hide_icon.svg'))
        self.push_hider.setIconSize(QSize(24, 24))

        # Присвоение имени объекта 
        self.push_hider.setObjectName('push_hider')



        


        # self.menu_hide.hide()

        
        # * Создание QLabel имени
        # объявление
        self.choice_name = QtWidgets.QLabel(self.name_zone)

        # Настройка размеров и местоположения
        self.choice_name.setGeometry(QtCore.QRect(x_choice_name, y_choice_name, width_choice_name, height_choice_name))

        # Присвоение имени объекта
        self.choice_name.setObjectName('choice_name')


        # * Кнопка просмотра
        self.button_result = QtWidgets.QPushButton(self.name_zone)
        self.button_result.setText('смотреть html')
        self.button_result.setGeometry(QtCore.QRect(x_button_result, y_button_result, width_button_result, height_button_result))
        self.button_result.setObjectName('result')

        # Настройка текста
        # self.choice_name.setText('name:')

        # # * QColorDIalog
        # self.button_color = QtWidgets.QPushButton(self.buttons)
        # self.button_color.setGeometry(QtCore.QRect(x_button_color, y_button_color, width_button_color, height_button_color))
        # self.button_color.setText('ll')
        # self.button_color.setObjectName('button_color')

        
        # * Кнопки меню

        self.open_file = QtWidgets.QPushButton(self.menu)
        self.open_file.setText('открыть файл')
        self.open_file.setObjectName('buttons_menu')
        self.open_file.setGeometry(QtCore.QRect(x_open_file, y_open_file, width_open_file, height_open_file))

        self.save_project = QtWidgets.QPushButton(self.menu)
        self.save_project.setText('сохранить как проект')
        self.save_project.setObjectName('buttons_menu')
        self.save_project.setGeometry(QtCore.QRect(x_save_project, y_save_project, width_save_project, height_save_project))

        self.change_theme = QtWidgets.QPushButton(self.menu)
        self.change_theme.setText('сменить тему')
        self.change_theme.setObjectName('buttons_menu')
        self.change_theme.setGeometry(QtCore.QRect(x_change_theme, y_change_theme, width_change_theme, height_change_theme))

        self.help = QtWidgets.QPushButton(self.menu)
        self.help.setText('помощь')
        self.help.setObjectName('buttons_menu')
        self.help.setGeometry(QtCore.QRect(x_help, y_help, width_help, height_help))


        # * Контекстное меню
        self.context_menu = QtWidgets.QMenu(self.main)
        self.context_menu.setObjectName('context_menu')
        
        self.context_rename = self.context_menu.addAction('переименовать')
        self.context_rename.setObjectName('buttons_action')
        self.context_rename.triggered.connect(self.action_rename_click)

        self.context_save = self.context_menu.addAction('сохранить')
        self.context_save.setObjectName('buttons_action')
        self.context_save.triggered.connect(self.action_save_click)

        self.context_close = self.context_menu.addAction('закрыть')
        self.context_close.setObjectName('buttons_action')
        self.context_close.triggered.connect(self.action_close_click)

        # * Окно смены имеи заметки
        self.rename_win = QtWidgets.QWidget(note_win)
        self.rename_win.setGeometry(QtCore.QRect(650, 250, 500, 200))
        self.rename_win.setObjectName('rename_win')
        self.rename_win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.rename_win.hide()


        self.rename_line = QtWidgets.QLineEdit(self.rename_win)
        self.rename_line.setGeometry(QtCore.QRect(80, 100, 360, 35))
        self.rename_line.setObjectName('rename_line')
        self.rename_line.setPlaceholderText('Имя заметки')


        self.rename_label = QtWidgets.QLabel(self.rename_win) 
        self.rename_label.setGeometry(QtCore.QRect(175, 20, 200, 50))  
        self.rename_label.setText('Переименовать заметку?') 
        self.rename_label.setObjectName('rename_label')


        self.rename_cancel = QtWidgets.QPushButton(self.rename_win)
        self.rename_cancel.setGeometry(QtCore.QRect(20, 160, 100, 25))
        self.rename_cancel.setText('Отменить')
        self.rename_cancel.setObjectName('rename_cancel')


        self.rename_accept = QtWidgets.QPushButton(self.rename_win)  
        self.rename_accept.setGeometry(QtCore.QRect(380, 160, 100, 25)) 
        self.rename_accept.setText('Потвердить') 
        self.rename_accept.setObjectName('rename_accept')





    def note_add(self):
        
        self.note = QtWidgets.QPushButton(self.notes_area)
        self.note.setObjectName('note')
        name = QtWidgets.QLineEdit(self.notes_area)
        
        if len(l_notes) != 0:
            i = len(l_notes)
            l_notes.append(self.note)
            # name.setGeometry(12, l_notes[i-1].y() + l_notes[i-1].geometry().height(),  302, 31)
            # if Widget.event.key() == QtCore.Qt.Key_Enter:
            #     if len(name.text().replace(' ', '')) > 0:
                #     l_notes[i].setText(name.text())
                #     name.hide()
                #     l_notes[i].setGeometry(12, l_notes[i-1].y() + l_notes[i-1].geometry().height(),  302, 31)
                # else:
            l_notes[i].setText(f'Unnamed-{i}')
            # name.hide()
            l_notes[i].setGeometry(12, l_notes[i-1].y() + l_notes[i-1].geometry().height(),  302, 31)
            print(l_notes[i].x(), l_notes[i].geometry().y())
        else:
            l_notes.append(self.note)
            # name.setGeometry(12, 0, 302, 31)
            # if self.event.key() == QtCore.Qt.Key_Enter:
            #     if len(name.text().replace(' ', '')) > 0:
            #         name.hide()
            l_notes[0].setGeometry(12, 0, 302, 31)
            # l_notes[0].setText(name.text())
                # else:

                    # l_notes[0].setGeometry(12, 0, 302, 31)
            l_notes[0].setText(f'Unnamed-{0}')

        for i in l_notes:
            i.show()
            i.clicked.connect(programm.click_note)
        programm.save_newNote()
        # self.add_note.raise_()
        
        # self.note = QtWidgets.QPushButton(self.notes_area)
        # self.note.setObjectName('note')


   
            
     

class Widget(QtWidgets.QWidget, Ui_programm):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.setupUi(self)
        self.check_menu = False

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
                if y_main <= cursor_y <= y_main + programm.hint.geometry().height():
                    self.old_pos = event.pos()
                else:
                    self.old_pos = None
            


            # Убирание меню при клике мимо самой менюшки
            if programm.check_menu:
                menu_x = programm.menu.geometry().x()
                menu_y = programm.menu.geometry().x()

                if (menu_x <= cursor_x <= menu_x + programm.geometry().width()) or (menu_y <= cursor_y <= menu_y + programm.geometry().height()):
                    programm.check_menu == False
                    programm.menu.hide()


        elif event.button() == QtCore.Qt.RightButton:
            self.old_pos = None

        
        

    # вызывается при отпускании кнопки мыши
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = None

    # вызывается всякий раз, когда мышь перемещается
    def mouseMoveEvent(self, event):
        
        if  programm.geometry().y() <= QtGui.QCursor.pos().y() <= programm.geometry().y() + programm.hint.geometry().height():
            if not self.old_pos:
                return
            delta = event.pos() - self.old_pos
            self.move(self.pos() + delta)
        

# ! ---------------------------------------------------------
    def contextMenuEvent(self, event):
        if len(l_notes) > 0:
            for button in l_notes:
                if ((event.pos().x() >  button.geometry().x() and event.pos().x() < button.geometry().width()) and
                (event.pos().y() >  button.geometry().y() + 162 and event.pos().y()  < (button.geometry().y() + button.geometry().height() + 162))):
                    self.context_menu.exec_(self.mapToGlobal(event.pos()))
                    break
    
    def action_rename_click(self):
        # self.rename_win = QtWidgets.QWidget()
        # self.rename_win.setGeometry(QtCore.QRect(710,440, 500, 200))
        # self.rename_win.setObjectName('rename_win')
        # self.rename_win.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.rename_line = QtWidgets.QLineEdit()
        old_name = self.pressed.text()
        self.rename_line.setPlaceholderText(old_name)
        self.rename_win.show()
        pass


    def accept_rename(self):
        new_name = self.rename_line.text()
        print(new_name)
        old_name = self.pressed.text()
        print(old_name)
        for but in l_notes:
            if but.text() == old_name:
                
                but.setText(new_name)
                self.choice_name.setText(new_name)
        
        os.rename(f'./prog_notes/{old_name}', f'./prog_notes/{new_name}' )
        os.rename(f'./prog_notes/{new_name}/{old_name}.txt', f'./prog_notes/{new_name}/{new_name}.txt' )
        os.rename(f'./prog_notes/{new_name}/others/{old_name}.html', f'./prog_notes/{new_name}/others/{new_name}.html' )

        self.rename_win.close()
        


    def cancel_rename(self):
        self.rename_win.close()


        # ! -------------------------------------------------------------------------
    def action_save_click(self):
        # TODO определить от какой заметки было вызванно модальное окно и собственно переделать сохранение и удаление из оперативки
        flag = False
        if not self.choice_name.text():
            return None
        for dict in gpu_notes:
                
            if self.choice_name.text() == dict['name']:
                dict['text'] = self.work_area.toPlainText()
                text = dict['text']
                gpu_notes.remove(dict)
                with open(f'./prog_notes/{self.choice_name.text()}/{self.choice_name.text()}.txt', 'w', encoding='utf-8') as f:
                    f.write(text)
                flag = True
                
            
        if not flag:
            text = self.work_area.toPlainText()
            with open(f'./prog_notes/{self.choice_name.text()}/{self.choice_name.text()}.txt', 'w', encoding='utf-8') as f:
                f.write(text)
                    

        with open(f'./prog_notes/{self.choice_name.text()}/others/{self.choice_name.text()}.html', 'w', encoding='utf-8') as f_html:
            text_html = markdown.markdown(text,  extension = ["codehilite"], extension_configs=config)
            f_html.write(text_html)
            # else:
            #     with open(f'./prog_notes/{self.choice_name.text()}/{self.choice_name.text()}.txt', 'w', encoding='utf-8') as f:
            #         text = self.work_area.toPlainText()
            #         f.write(text)
        print(gpu_notes)
        

# TODO ----------------------------------------------------------------------------------

    def action_close_click(self):
        pass
                


    # Функция для закрытия приложения
    def close_app(self):
        self.close()

    # Функция для сворачивания приложения
    def hide_app(self):
        self.showMinimized()

    # Функция для показа меню
    def open_menu(self):
        if self.check_menu == False:
            self.menu.show()
            self.check_menu = True
        else:
            self.menu.hide()
            self.check_menu = False



    # Функция, которую вызывают по кликанью на любую заметку
            # ! переделать полностью----------------------------------------------------------------
    def click_note(self):
        
        # if self.pressed == None:
            
        #     self.pressed = QtWidgets.QApplication.instance().sender()
        #     with open(f'./prog_notes/{self.pressed.text()}/{self.pressed.text()}.txt', 'r', encoding='utf-8') as f:
        #         text = f.read()
        #         self.work_area.setText(text)
        #     self.pressed.setObjectName('choiced_note')
        #     self.choice_name.setText(self.pressed.text())
        #     dict_note = {'name': self.choice_name, 'text': text}
        #     gpu_notes.append(dict_note)
        #     self.css_update()
            
        # else: 
        #     # * Возращаю старую заметку
        #     self.pressed.setObjectName('note')
            
        #     check = False
        #     for i in gpu_notes:
        #         if i['name'] == self.pressed.text():
        #             text = i['text']
        #             # self.work_area.setText(text)
        #             check = True
        #             break

        #     if check:
        #         self.pressed = QtWidgets.QApplication.instance().sender()
                
        #         with open(f'./prog_notes/{self.pressed.text()}/{self.pressed.text()}.txt', 'r', encoding='utf-8') as f:
        #             text = f.read()
                
        #             dict_note = {'name': self.choice_name, 'text': text}
        #             gpu_notes.append(dict_note)
        #             print('s')
        #         # Переписываю новую
                
        #         self.pressed = QtWidgets.QApplication.instance().sender()
        #         with open(f'./prog_notes/{self.pressed.text()}/{self.pressed.text()}.txt', 'r', encoding='utf-8') as f:
        #             text = f.read()
        #             self.work_area.setText(text)
        #     self.pressed.setObjectName('choiced_note')
        #     self.choice_name.setText(self.pressed.text())
            check = None
            update = False
        # * Логика: если ранее не было выбранно хаметки, то:
            # * получение выбранно заметки (pressed) -> обращение к файлу заметки -> запись текста файла в text -> отображение текста в work_area 
            if self.pressed == None:
                self.pressed = QtWidgets.QApplication.instance().sender()
                with open(f'./prog_notes/{self.pressed.text()}/{self.pressed.text()}.txt', 'r', encoding='utf-8') as f:
                    text = f.read()
                    self.work_area.setText(text)
                self.pressed.setObjectName('choiced_note')
                self.choice_name.setText(self.pressed.text())
            else: 
                # dict_note = {'name': self.pressed.text(), 'text':self.work_area.toPlainText()}
                # for d in gpu_notes:
                #     if d['name'] == dict_note['name']:
                #         d['text'] = dict_note['text'] 
                #         update = True
                #         break
                #     else:
                #         update = False
                #         print(d['name'], dict_note['name'], 'Добавление!!!!!')
                # if not update:
                #     gpu_notes.append(dict_note)
                self.pressed.setObjectName('note')
                self.pressed = QtWidgets.QApplication.instance().sender()
                for i in gpu_notes:
                    if i['name'] == self.pressed.text():
                        check = True
                        note = i
                        break

                    #sadsad
                if check != None:
                    self.choice_name.setText(note['name'])
                    self.work_area.setText(note['text'])
                    # print(note)
                else:
                    with open(f'./prog_notes/{self.pressed.text()}/{self.pressed.text()}.txt', 'r', encoding='utf-8') as f:
                        text = f.read()
                    self.work_area.setText(text)
                    self.choice_name.setText(self.pressed.text())

                self.pressed.setObjectName('choiced_note')
            self.css_update()
            print('CLIIIIIIIIIIIIIIIIIIIICKKFKFKKF')
            self.init_conffg_signals()
            print(len(gpu_notes))
            return None
            # print(gpu_notes)
            

            

    def css_update(self):
        # TODO -------------------------------------------------
        file = QtCore.QFile("./school_style.css")                             
        file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
        stream = QtCore.QTextStream(file)
        app.setStyleSheet(stream.readAll())
        # TODO -------------------------------------------------
    
    def notes_update(self):
        if os.path.exists('./prog_notes'):
            print(os.listdir('./prog_notes'))
            notes = os.listdir('./prog_notes')
            num_notes = len(os.listdir('./prog_notes'))
            for i in range(num_notes):
                self.note = QtWidgets.QPushButton(self.notes_area)
                self.note.setObjectName('note')
                
                if len(l_notes) != 0:
                    i = len(l_notes)
                    l_notes.append(self.note)
                
                    l_notes[i].setText(notes[i])
                    # name.hide()
                    l_notes[i].setGeometry(12, l_notes[i-1].y() + l_notes[i-1].geometry().height(),  302, 31)
                    print(l_notes[i].x(), l_notes[i].geometry().y())
                else:
                    l_notes.append(self.note)
                   
                    l_notes[0].setGeometry(12, 0, 302, 31)
                  
                    l_notes[0].setText(notes[i])

                for i in l_notes:
                    i.show()
                    i.clicked.connect(programm.click_note)


        # TODO: Тут должно быть прочтение всех папок из папки главной папки и добавление их в качестве кнопок для работы с их txt-шниками
        # * done


    
    # def void_color(self):
    #     self.color_dialog = QtWidgets.QColorDialog(self.main)
    #     self.color_dialog.setGeometry(50,50, 100, 100)
    #     self.color_dialog.setObjectName('color_dialog')
    
    def save_newNote(self):
        # if os.path.exists('C://prog_notes'):
        #     os.mkdir(f'C://prog_notes/{l_notes[-1].text()}')
        #     file = open(f'C://prog_notes/{l_notes[-1].text()}/{l_notes[-1].text()}.txt', 'w')
        #     file.write('')

        #     # os.replace('C://vsCodeProjects/school_project/'+file.name, f'C://prog_notes/{l_notes[-1].text()}/{file.name}')
        #     print('file added')

        # else: 
        #     os.mkdir('C://prog_notes')
        #     os.mkdir(f'C://prog_notes/{l_notes[-1].text()}')
            
        #     file = open(f'C://prog_notes/{l_notes[-1].text()}/{l_notes[-1].text()}.txt', 'w')
        #     file.write('')
            # print(file)
            # os.replace(f'C://vsCodeProjects/school_project/'+file.name, f'C://prog_notes/{l_notes[-1].text()}/{file.name}')
# ! ---------------------------
        if os.path.exists('./prog_notes'):
            os.mkdir(f'./prog_notes/{l_notes[-1].text()}')
            os.mkdir(f'./prog_notes/{l_notes[-1].text()}/others')
            os.mkdir(f'./prog_notes/{l_notes[-1].text()}/others/style')
            os.mkdir(f'./prog_notes/{l_notes[-1].text()}/others/formuls')
            os.mkdir(f'./prog_notes/{l_notes[-1].text()}/others/images')
            _ = open(f'./prog_notes/{l_notes[-1].text()}/{l_notes[-1].text()}.txt', 'w')
            _ = open(f'./prog_notes/{l_notes[-1].text()}/others/{l_notes[-1].text()}.html', 'w')
            # file.write('check_0')

            # os.replace('C://vsCodeProjects/school_project/'+file.name, f'C://prog_notes/{l_notes[-1].text()}/{file.name}')
            # print('file added')

        else: 
            os.mkdir('./prog_notes')
            os.mkdir(f'./prog_notes/{l_notes[-1].text()}')
            os.mkdir(f'./prog_notes/{l_notes[-1].text()}/others')
            os.mkdir(f'./prog_notes/{l_notes[-1].text()}/others/style')
            os.mkdir(f'./prog_notes/{l_notes[-1].text()}/others/formuls')
            os.mkdir(f'./prog_notes/{l_notes[-1].text()}/others/images')
            
            _ = open(f'./prog_notes/{l_notes[-1].text()}/{l_notes[-1].text()}.txt', 'w')
            _ = open(f'./prog_notes/{l_notes[-1].text()}/others/{l_notes[-1].text()}.html', 'w')
            # file.write('check_'+'-1')

    def show_result(self):
        tag = False
        # with open(f'./prog_notes/{programm.choice_name.text()}/others/{programm.choice_name.text()}.html', 'r', encoding='utf-8') as f:
        #     for line in f:
        #         if "<style>" in line:
        #             tag = True
        #             break
        #     if not tag:    
        #         with open(f'./prog_notes/{programm.choice_name.text()}/others/{programm.choice_name.text()}.html', 'a', encoding='utf-8') as f:
        #             f.write("\n<style>\n@import url('./styles/base-styles.css');\n@import url('./styles/styles-gruvbox-dark.css');\n</style>")


        if len(programm.choice_name.text().replace(' ','')) == 0:
            return None
        flag = False
        if programm.button_result.text() == 'смотреть html':
            for note in gpu_notes:
                if programm.choice_name.text() == note['name']:
                    # TODO из оперативки в смотреть заметку и потом отображать 
                    text = note['text']
                    
                    flag = True
                    programm.button_result.setText('редактировать')
                    programm.work_area.hide()
                    programm.viewer.show()
                    
                    text = markdown.markdown(text, extension = ["codehilite"], extension_configs=config)
                    text = """<style>
@import url('./styles/base-styles.css');
@import url('./styles/styles-gruvbox-dark.css');
</style>""" + text
                    programm.viewer.setText(text)
                    # print(programm.viewer.toPlainText())
                    break
            
            if flag:
                return None
            else:
                programm.button_result.setText('редактировать')
                programm.work_area.hide()
                programm.viewer.show()
                with open(f'./prog_notes/{programm.choice_name.text()}/others/{programm.choice_name.text()}.html', 'r', encoding='utf-8') as f:
                    text = f.read()
                text = """<style>
@import url('./styles/base-styles.css');
@import url('./styles/styles-gruvbox-dark.css');
</style>""" + text
                programm.viewer.setText(text)

        else:
            programm.button_result.setText('смотреть html')
            programm.work_area.show()
            programm.viewer.hide()
            # with open(f'./prog_notes/{programm.choice_name.text()}/{programm.choice_name.text()}.txt', 'r', encoding='utf-8') as f:
            #     text = f.read()
            
            # programm.viewer.setText(text)



    def gpu_update(self):
        text = programm.work_area.toPlainText()
        name = programm.choice_name.text()
        for note in range(len(gpu_notes)):
            print('----------------------')
            print(name, gpu_notes[note]['name'])
            if name == gpu_notes[note]['name']:
                gpu_notes[note]['text'] = text
                print(gpu_notes)
                return None
            
        dict = {'name': name, 'text': text}
        
        print('CLICK') # ? Почему х4???????????????????
        gpu_notes.append(dict)
        print(gpu_notes)
        

    def init_conffg_signals(self):
        programm.work_area.textChanged.connect(programm.gpu_update)


        



if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    programm = Widget()


    # * Подключение кнопок
    programm.push_exit.clicked.connect(programm.close_app)
    programm.push_hider.clicked.connect(programm.hide_app)
    programm.menu_show.clicked.connect(programm.open_menu)
    # programm.menu_hide.clicked.connect(programm.hide_menu)
    programm.add_note.clicked.connect(programm.note_add)
    # programm.button_color.clicked.connect(programm.void_color)
    programm.button_result.clicked.connect(programm.show_result)
    programm.rename_accept.clicked.connect(programm.accept_rename)
    programm.rename_cancel.clicked.connect(programm.cancel_rename)
    
    
    programm.css_update()
    programm.notes_update()

    programm.show()
    sys.exit(app.exec_())