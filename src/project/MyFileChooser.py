from gi.repository import Gtk, Gio

class MyFileChooser:
    class __MyFileChooser:
        def __init__(self):
            pass
                
    instance = None
    
    def __init__(self):
        if not MyFileChooser.instance:
            MyFileChooser.instance = MyFileChooser.__MyFileChooser()
        self.file_path = None
        
            
    def _load_content_from_path(self, fpath):
        file = Gio.File.new_for_path(fpath)
        (is_succ, contents, _) = file.load_contents(None)
        return (is_succ, contents.decode('utf-8'))
            
    def run(self):
        self.dialog = Gtk.FileChooserDialog(
            title="Open file",
            action=Gtk.FileChooserAction.OPEN,
            buttons=("Cancel", Gtk.ResponseType.CANCEL,
                     "Open", Gtk.ResponseType.OK))
        res = Gtk.Dialog.run(self.dialog)
        self.file_path = self.dialog.get_filename()
        self.dialog.destroy()
        
        if res == Gtk.ResponseType.OK:
            return self._load_content_from_path(self.file_path)
        return (False, "")
        
    def save_to_file(self, text):
        if self.get_file_path() is None:
            return
        with open(self.get_file_path(), "w") as file:
            file.write(text)
        
    def get_file_path(self):
        return self.file_path
    
    def set_file_path(self, path):
        self.file_path = path
        
    def reset_file_path(self):
        self.file_path = None
    
