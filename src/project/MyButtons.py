from gi.repository import Gtk, Gio

class BaseButton(Gtk.Button):
    
    def __init__(self):
        Gtk.Button.__init__(self)
        
        self.connect("clicked", self._click_cb)
        
    def _click_cb(self, widget):
        raise NotImplementedError()
        
    def _set_textview_content(self, text):
        if self.textview is None:
            return
        txt_buf = self.textview.get_buffer()
        txt_buf.set_text(text)
        
    def _get_textview_buffer(self):
        if self.textview is None:
            return
        txt_buf = self.textview.get_buffer()
        return txt_buf

        
class NewButton(BaseButton):
    
    def __init__(self, textview, chooser):
        BaseButton.__init__(self)
        
        self.set_label("New")
        
        self.textview = textview
        
        self.chooser = chooser
        
    def _click_cb(self, widget):
        self._set_textview_content("")
        self.chooser.reset_file_path()

        
class OpenButton(BaseButton):
    
    def __init__(self, textview, chooser):
        BaseButton.__init__(self)
        
        self.set_label("Open")
        
        self.textview = textview
        
        self.chooser = chooser
         
    def _click_cb(self, widget):
        (done, ctx) = self.chooser.run()
        if done is True:
            self._set_textview_content(ctx)       
        
        
class SaveButton(BaseButton):
    
    def __init__(self, textview, chooser):
        BaseButton.__init__(self)
        
        self.set_label("Save")
        
        self.textview = textview
        
        self.chooser = chooser
        
    def _click_cb(self, widget):
        buf = self._get_textview_buffer()
        self.chooser.save_to_file(buf.get_text(buf.get_start_iter(),
                                               buf.get_end_iter(),
                                               True))
 
