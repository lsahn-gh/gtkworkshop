
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self)
        
        # Set default size to 600 x 400
        self.set_default_size(600, 400)
        
        # Connect main_quit to destroy signal
        self.connect("destroy", Gtk.main_quit)

