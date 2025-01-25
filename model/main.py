from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import ListProperty, NumericProperty
from kivy.animation import Animation
import os
from game_widget import GameWidget

kv_path = os.path.join(os.path.dirname(__file__), "../tamplate/main.kv")


class StartScreen(Screen):
    """หน้าจอเริ่มเกม"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self.game_active = False

        # สร้างอ็อบเจกต์ที่จะให้กด "R" เริ่มเกม
        Clock.schedule_once(lambda dt: start_game(self), 0)

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        if text == "r" and not self.game_active:
            # เช็คว่าเมาส์อยู่ในอ็อบเจกต์นั้นหรือไม่
            if self.is_mouse_inside_object(self._mouse, (self.obj_pos, self.obj_size)):
                self.game_active = True
                object_in_start.remove_center_object(self)
                start_game(self)  # เริ่มเกม

                self.manager.current = "game_screen"  # เปลี่ยนไปหน้า GameScreen
                print("Mouse is inside the object, starting the game!")

    def is_mouse_inside_object(self, mouse_pos, obj):
        x, y = mouse_pos
        obj_x, obj_y = obj[0]
        obj_width, obj_height = obj[1]
        return obj_x <= x <= obj_x + obj_width and obj_y <= y <= obj_y + obj_height


class GameScreen(Screen):
    """หน้าจอเกมหลัก"""

    pass


class MyApp(App):
    def build(self):
        return Builder.load_file(kv_path)  # โหลดไฟล์ KV


if __name__ == "__main__":
    app = MyApp()
    app.run()
