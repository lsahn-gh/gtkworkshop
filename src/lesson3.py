
from gi.repository import Gtk

'''
- HeaderBar
    - HeaderBar를 상속하는 MyTitleBar 클래스 구현
    - HeaderBar에 CheckButton 추가하기
'''

# 상속을 통한 Gtk.Window 객체 생성
class GtkWorkshopLesson3(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)
        
        self.set_default_size(600, 400)
        
        # 1. Gtk.HeaderBar 구현
        # 2. Class로 구현
        hb = Gtk.HeaderBar()
        hb.set_title("Lesson 3")
        hb.set_subtitle("This is lesson 3")
        hb.set_show_close_button(True)

        self.set_titlebar(hb)
        
        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        

def lesson3():
    GtkWorkshopLesson3()
 
