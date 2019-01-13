# project.py

from gi.repository import Gtk

from .MyHeaderBar import MyHeaderBar
from .MyMainBox import MyMainBox

class MyTextEditor(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self)
        
        self.headerbar = MyHeaderBar()
        self.set_titlebar(self.headerbar)
        
        self.mainbox = MyMainBox()
        self.add(self.mainbox)
        
        self.set_default_size(700, 400)
        self.connect("destroy", Gtk.main_quit)
        
        self.show_all()

def project():
    MyTextEditor()
 
