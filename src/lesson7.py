
from gi.repository import Gtk

'''
- Button Widgets
    - Horizontal Box
        - Switch Button 2개 추가
        - Callback 연결
'''

class GtkWorkshopLesson7(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self)
        
        self.props.title = "Lesson 7"
        self.connect("destroy", Gtk.main_quit)
        self.props.border_width = 10
        
        self.box = Gtk.Box(spacing=6)
        self.add(self.box)
        
        switch = Gtk.Switch()
        switch.connect("notify::active", self._switch_test_cb)
        switch.set_active(False)
        self.box.pack_start(switch, True, True, 0)

        # Switch Button 1

        
        # Switch Button 2 

        
        self.show_all()
        
    def _switch_test_cb(self, switch, gparam):
        pass

    # Callback

        
        
def lesson7():
    GtkWorkshopLesson7()

