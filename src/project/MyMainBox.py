
from gi.repository import Gtk

from .MyButtons import OpenButton, NewButton, SaveButton
from .MyFileChooser import MyFileChooser

class MyMainBox(Gtk.Box):
    
    def __init__(self):
        Gtk.Box.__init__(self,
                         orientation=Gtk.Orientation.VERTICAL,
                         spacing=6)
        
        self.file_chooser = MyFileChooser()

        # ScrolledWindow & TextView


        # Horizontal Box for Buttons
        # Border width is 10
        

        # New / Open / Save 버튼 만들기
        # Quiz 1
        

        # Horizontal Box for CheckButtons
        # Border width is 10
        

        # CheckButton for Editable


        # CheckButton for WORD wrap mode


        # Horizontal Box for Label and Switch
        # Border width is 10
        

        # WORD wrap mode Label and Switch
        

    # Callbacks



