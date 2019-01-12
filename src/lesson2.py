
from gi.repository import Gtk

'''
- Gtk.Box (Container)
    - Horizontal Box
    - Vertical Box

- Gtk.Entry 추가
- Horizontal Box 추가
    - Gtk.CheckButton 3개 추가
        - Second
            - Toggled 시그널 연결
            - 직접 구현해보기 (Entry에 본인 이름 영어로 출력)
        - Third
        - Fourth
'''

class GtkWorkshopLesson2(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self)
        
        self.set_title("Lesson 2")
        self.set_default_size(200, 100)
        self.connect("destroy", Gtk.main_quit)
        
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)
        
        # Gtk.Entry 구현
        # vbox에 추가

        # Horizontal Box 구현
        # vbox에 추가

        chbtn = Gtk.CheckButton("First")
        chbtn.connect("toggled", self._first_check_btn_cb)
        hbox.pack_start(chbtn, True, True, 0)

        # CheckButton 3개 추가

        
        self.show_all()
        
    def _first_check_btn_cb(self, widget):
        if widget.get_active():
            self.entry.set_text(widget.get_label())
        else:
            self.entry.set_text("")
    # Toggled 시그널 콜백 구현


def lesson2():
    GtkWorkshopLesson2()

