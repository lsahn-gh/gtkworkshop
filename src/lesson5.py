
from gi.repository import Gtk

'''
- Button Widgets
    - Horizontal Box 생성
        - Normal Button 1개 추가 (Name)
        - Mnemonic Button 2개 추가 (Age, Click Me)
        - Callback 연결
'''

class GtkWorkshopLesson5(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self)
        
        self.props.title = "Lesson 5"
        self.set_border_width(10)
        self.connect("destroy", Gtk.main_quit)
        
        self.box = Gtk.Box(spacing=6)
        self.add(self.box)
        
        button = Gtk.Button(label="First")
        self.box.pack_start(button, False, False, 0)

        button = Gtk.Button.new_with_mnemonic("_Second")
        self.box.pack_start(button, False, False, 0)

        # Normal Button
        # 본인의 이름 출력

        
        # Mnemonic Button (_Age)
        # 본인의 나이 출력

        
        # Mnemonic Button (_Click Me)
        # Click Me 버튼이 눌렸다는 메세지 출력

        
        self.show_all()
        
    # Callbacks 구현

        
def lesson5():
    GtkWorkshopLesson5()

