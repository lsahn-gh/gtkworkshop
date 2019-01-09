
from gi.repository import Gtk

'''
- Gtk.Window 를 상속하는 클래스를 이용하여 Window 만들기
- destroy 메세지를 출력하는 함수 정의 후 destroy 시그널에 연결
'''

def lesson1():
    # Window 생성
    window = Gtk.Window()
    
    # Title 설정
    window.set_title("Lesson 1")
    
    # 윈도우 크기 조절
    window.set_default_size(600, 200)
    
    # destroy 시그널에 main_quit 메서드 연결
    window.connect("destroy", Gtk.main_quit)
    
    window.show()
    
