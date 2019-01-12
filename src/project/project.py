# project.py

from gi.repository import Gtk

from .MyHeaderBar import MyHeaderBar
from .MyMainBox import MyMainBox

class MyTextEditor(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self)
        
        # MyHeaderBar


        # MyMainBox
        

        self.set_default_size(700, 400)
        self.connect("destroy", Gtk.main_quit)
        
        self.show_all()

def project():
    MyTextEditor()
 
