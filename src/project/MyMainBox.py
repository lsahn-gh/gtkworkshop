
from gi.repository import Gtk

from .MyButtons import OpenButton, NewButton, SaveButton
from .MyFileChooser import MyFileChooser

class MyMainBox(Gtk.Box):
    
    def __init__(self):
        Gtk.Box.__init__(self,
                         orientation=Gtk.Orientation.VERTICAL,
                         spacing=6)
        
        # ScrolledWindow & TextView
        self.text_view = Gtk.TextView()
        self.scrolled_window = Gtk.ScrolledWindow()
        self.scrolled_window.add(self.text_view)
        self.pack_start(self.scrolled_window, True, True, 0)
        
        # First Horizontal Box
        hbox = Gtk.Box(spacing=6)
        hbox.set_border_width(10)
        self.pack_start(hbox, False, False, 0)
        
        # Buttons
        self.file_chooser = MyFileChooser()
        hbox.pack_start(NewButton(self.text_view, self.file_chooser),
                        False,
                        False,
                        0)
        hbox.pack_start(OpenButton(self.text_view, self.file_chooser),
                        False,
                        False,
                        0)
        hbox.pack_end(SaveButton(self.text_view, self.file_chooser),
                      False,
                      False,
                      0)
        
        # Horizontal Box
        hbox = Gtk.Box(spacing=6)
        hbox.set_border_width(10)
        self.pack_start(hbox, False, False, 0)
        
        # CheckButton for Editable
        chbtn = Gtk.CheckButton("Editable")
        chbtn.set_active(True)
        chbtn.connect("toggled", self._on_editable_cb)
        hbox.pack_start(chbtn, False, False, 0)
        
        # CheckButton for WORD wrap mode
        chbtn = Gtk.CheckButton("WORD wrap")
        chbtn.set_active(False)
        chbtn.connect("toggled", self._on_word_wrap_mode_cb)
        hbox.pack_start(chbtn, False, False, 0)
        
        # Horizontal Box
        hbox = Gtk.Box(spacing=6)
        hbox.set_border_width(10)
        self.pack_start(hbox, False, False, 0)
        
        # WORD wrap mode switch & label
        label = Gtk.Label(label="WORD wrap")
        hbox.pack_start(label, False, False, 0)
        
        switch = Gtk.Switch()
        switch.connect("notify::active", self._on_word_wrap_mode_cb)
        switch.set_active(False)
        hbox.pack_start(switch, False, False, 0)
        
    def _on_editable_cb(self, widget):
        if widget.get_active():
            state = True
        else:
            state = False
        self.text_view.set_editable(state)
        
    def _on_word_wrap_mode_cb(self, widget, gparam=None):
        if widget.get_active():
            state = Gtk.WrapMode.WORD
        else:
            state = Gtk.WrapMode.NONE
        self.text_view.set_wrap_mode(state)

