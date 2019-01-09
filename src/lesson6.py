
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
        button = Gtk.ToggleButton(label="Toggle 1")
        button.connect("toggled", self._on_toggle_cb, 1)
        self.box.pack_start(button, True, True, 0)
        
        # Toggle Button 2 with mnemonic
        button = Gtk.ToggleButton.new_with_mnemonic("_Toggle 2")
        button.connect("toggled", self._on_toggle_cb, 2)
        self.box.pack_start(button, True, True, 0)
        
        self.show_all()
        
    def _existed_cb(self, button):
        pass

    # Callbacks
    def _on_toggle_cb(self, button, data):
        if data == 1 and button.get_active():
            print("Toggle 1 is on")
        elif data == 2 and button.get_active():
            print("Toggle 2 is on")
        
        
def lesson6():
    GtkWorkshopLesson6()

