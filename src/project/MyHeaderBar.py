from gi.repository import Gtk

class MyHeaderBar(Gtk.HeaderBar):
    
    def __init__(self):
        Gtk.HeaderBar.__init__(self)
        
        # Set title/subtitle and close button
        self.set_title("My Editor")
        self.set_subtitle("Put your name here")
        self.set_show_close_button(True)
        
