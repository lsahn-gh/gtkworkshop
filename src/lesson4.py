
from gi.repository import Gtk
from .MyWindow import MyWindow

'''
- Label 만들기
    - Markup 언어 사용해보기
        - a href 이용
    - Label에 Tooltip 구현하기
'''

class GtkWorkshopLesson4(MyWindow):
    
    def __init__(self):
        MyWindow.__init__(self)

        hb = Gtk.HeaderBar(title="Lesson 4")
        hb.set_show_close_button(True)
        self.set_titlebar(hb)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        label = Gtk.Label("This is new label")
        vbox.pack_start(label, True, True, 0)

        # Label 만들기 1


        markup = "Go to <i><b><a href=\"https://google.com\">google</a></b></i>"
        # Label 만들기 2
        # set_markup 이용


        # Label 만들기 3
        # tooltip 추가하기

        
        self.show_all()
        

def lesson4():
    GtkWorkshopLesson4()

