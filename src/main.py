# main.py

import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

from .lesson1 import lesson1
from .lesson2 import lesson2
from .lesson3 import lesson3
from .lesson4 import lesson4
from .lesson5 import lesson5
from .lesson6 import lesson6
from .lesson7 import lesson7

from .project import project


def main(version):
    
    lesson1()
    #lesson2()
    #lesson3()
    #lesson4()
    #lesson5()
    #lesson6()
    #lesson7()
    
    #project()
    
    Gtk.main()      # main loop
    
