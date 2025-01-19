from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
import os

kv_path = os.path.join(os.path.dirname(__file__), "../tamplate/main.kv")
Builder.load_file(kv_path)


class GameWidget(Widget):
    count = 0
    obj_pos = [250, 250]
    sizes = [[100, 100], [80, 80], [70, 70]]
    obj_size = ListProperty(sizes[count])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)
        self._mouse = Window.bind(mouse_pos=self._on_mouse_move)
        self.pressed_keys = set()

        self.combo = 0
        self.game_active = True

        Clock.schedule_interval(self.update_object, 0.5)
        Clock.schedule_interval(self.on_point, 0)

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        print("Key down:", text)
        self.pressed_keys.add(text)

    def _on_key_up(self, keyboard, keycode):
        text = keycode[1]
        print("Key up:", text)
        if text in self.pressed_keys:
            self.pressed_keys.remove(text)

    def is_mouse_inside_object(self, mouse_pos, obj):
        x, y = mouse_pos
        obj_x, obj_y = obj[0]
        obj_width, obj_height = obj[1]

        return obj_x <= x <= obj_x + obj_width and obj_y <= y <= obj_y + obj_height

    def on_point(self, dt):
        if not self.game_active:
            return

        if "s" in self.pressed_keys:
            if self.is_mouse_inside_object(self._mouse, (self.obj_pos, self.obj_size)):
                print("s onclick!!!!!!!!!!")
                self.combo += 1
            else:
                print("game over")
                self.end_game()

        if "d" in self.pressed_keys:
            if self.is_mouse_inside_object(self._mouse, (self.obj_pos, self.obj_size)):
                print("d onclick!!!!!!!!!!")
                self.combo += 1
            else:
                print("game over")
                self.end_game()

    def _on_mouse_move(self, window, pos):
        self._mouse = pos
        self.create_effect(self._mouse)

    def create_effect(self, pos):
        adjusted_pos = (pos[0] - 10, pos[1] - 10)
        with self.canvas:
            effect = Rectangle(pos=adjusted_pos, size=(20, 20))
        Clock.schedule_once(lambda dt: self.remove_effect(effect), 0.1)

    def remove_effect(self, effect):
        self.canvas.remove(effect)

    def update_object(self, dt):
        """
        อัปเดตขนาดและตำแหน่งของวัตถุ (obj) ทุก ๆ 0.5 วินาที
        """
        if self.count < len(self.sizes):  # ตรวจสอบให้ count ไม่เกินขอบเขต
            self.obj_size = self.sizes[self.count]  # ตั้งค่าขนาดใหม่ตาม index
            self.count += 1  # เพิ่มตัวนับ
        else:
            self.count = 0  # รีเซ็ตตัวนับ

    def end_game(self):
        self.game_active = False
        self.ids.game_over_label.text = f"GAME OVER\nCombo: {self.combo}"
        self.ids.game_over_label.opacity = 1


class MyApp(App):
    def build(self):
        return GameWidget()


if __name__ == "__main__":
    app = MyApp()
    app.run()
