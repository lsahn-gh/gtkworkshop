
from gi.repository import Gtk

'''
- Button Widgets
    - Vertical Box
        - Toggle Button 2개 추가
        - Callback 연결
'''

class GtkWorkshopLesson6(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self)
        
        self.props.title = "Lesson 6"
        self.connect("destroy", Gtk.main_quit)
        self.props.border_width = 10
        
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)
        
        button = Gtk.ToggleButton(label="Toggle")
        button.connect("toggled", self._existed_cb)
        self.box.pack_start(button, True, True, 0)

        # Toggle Button 1

        
        # Toggle Button 2 with mnemonic

        
        self.show_all()
        
    def _existed_cb(self, button):
        pass

    # Callbacks

        
        
def lesson6():
    GtkWorkshopLesson6()

