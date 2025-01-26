from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.properties import ListProperty, NumericProperty
from kivy.core.window import Window
from start import new_game, object_in_start  # ใช้ object_in_start
from music_logic import MusicLogic


class GameWidget(Widget):
    count = 0
    combo = NumericProperty(0)
    obj_pos = ListProperty([250, 250])
    sizes = [[100, 100], [95, 95], [98, 98], [88, 88], [80, 80], [85, 85]]
    obj_size = ListProperty(sizes[count])
    combo_font_size = NumericProperty(40)

    song_sequence = [
        {"time": 1, "position": [250, 250]},  # จังหวะแรก
        {"time": 2, "position": [300, 300]},  # จังหวะที่สอง
        {"time": 3, "position": [350, 200]},  # จังหวะที่สาม
        {"time": 4, "position": [250, 150]},  # จังหวะที่สี่
        {"time": 5, "position": [250, 250]},  # จังหวะที่ห้า
        {"time": 6, "position": [300, 300]},  # จังหวะที่หก
        {"time": 7, "position": [350, 200]},  # จังหวะที่เจ็ด
        {"time": 8, "position": [250, 150]},  # จังหวะที่แปด
        {"time": 9, "position": [250, 250]},  # จังหวะที่เก้า
        {"time": 10, "position": [300, 300]},  # จังหวะที่สิบ
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)
        self._mouse = Window.bind(mouse_pos=self._on_mouse_move)
        self.game_active = False
        self.pressed_keys = set()

        Clock.schedule_once(lambda dt: new_game.start_game(self), 0)
        Clock.schedule_interval(self.update_object, 0.1)
        Clock.schedule_interval(self.on_point, 0)

        # เริ่มใช้งาน MusicLogic
        self.music_logic = MusicLogic(self, self.song_sequence)

    def move_object(self):
        if not self.song_sequence:
            return

        current_time = int(self.music_logic._song_time)

        for song in self.song_sequence:
            if current_time == song["time"]:  # เช็คว่าเวลาในเพลงตรงกับเวลาที่ต้องการ
                self.obj_pos = song["position"]  # เปลี่ยนตำแหน่ง
                print(f"Object moved to: {self.obj_pos}")
                break

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        self.pressed_keys.add(text)

        if text == "r" and not self.game_active:
            if self.ids.game_over_label.opacity == 1:  # หากมี game over ปรากฏ
                new_game.reset_game(self)  # รีเซ็ตเกม
                self.ids.game_over_label.text = ""
                print("Resetting the game!")

            if self.ids.start_label.opacity == 1:
                if self.is_mouse_inside_object(
                    self._mouse, (self.obj_pos, self.obj_size)
                ):
                    self.game_active = True
                    object_in_start.remove_center_object(self)
                    self.ids.start_label.opacity = 0
                    print("Mouse is inside center_object, start game!")
                    self.music_logic.start_music()  # เริ่มเล่นเพลง

                else:
                    print("Mouse not inside center_object, cannot start game.")

    def _on_key_up(self, keyboard, keycode):
        text = keycode[1]
        if text in self.pressed_keys:
            self.pressed_keys.remove(text)

    def is_mouse_inside_object(self, mouse_pos, obj):
        x, y = mouse_pos
        obj_x, obj_y = obj[0]
        obj_width, obj_height = obj[1]
        return obj_x <= x <= obj_x + obj_width and obj_y <= y <= obj_y + obj_height

    def on_point(self, dt):
        """
        ฟังก์ชั่นที่ใช้ในการตรวจจับการคลิก
        """
        if not self.game_active:
            return

        if "s" in self.pressed_keys or "d" in self.pressed_keys:
            key_pressed = "s" if "s" in self.pressed_keys else "d"
            if self.is_mouse_inside_object(self._mouse, (self.obj_pos, self.obj_size)):
                self.combo += 1
                self.animate_combo_label()
                print(f"Clicked on {key_pressed}, combo: {self.combo}")
            else:
                print(f"Missed {key_pressed}")
                self.end_game()

    def is_mouse_inside_object(self, mouse_pos, obj):
        """
        ตรวจจับตำแหน่งของเมาส์ว่าคลิกในออบเจกต์หรือไม่
        """
        x, y = mouse_pos
        obj_x, obj_y = obj[0]
        obj_width, obj_height = obj[1]
        return obj_x <= x <= obj_x + obj_width and obj_y <= y <= obj_y + obj_height

    def _on_mouse_move(self, window, pos):
        """
        เมื่อเมาส์ขยับ
        """
        self._mouse = pos
        self.create_effect(self._mouse)

    def create_effect(self, pos):
        """
        สร้างเอฟเฟ็กต์เมื่อเมาส์ขยับ
        """
        adjusted_pos = (pos[0] - 10, pos[1] - 10)
        with self.canvas:
            effect = Rectangle(pos=adjusted_pos, size=(15, 15))
        Clock.schedule_once(lambda dt: self.remove_effect(effect), 0.1)

    def remove_effect(self, effect):
        self.canvas.remove(effect)

    def update_object(self, dt):
        """
        อัพเดตขนาดของออบเจกต์ตามเวลาที่กำหนด
        """
        if self.count < len(self.sizes):
            new_size = self.sizes[self.count]
            self.obj_pos[0] += (self.obj_size[0] - new_size[0]) / 2
            self.obj_pos[1] += (self.obj_size[1] - new_size[1]) / 2
            self.obj_size = new_size
            self.count += 1
        else:
            self.count = 0

    def end_game(self):
        """
        ฟังก์ชั่นจบเกม
        """
        self.game_active = False
        self.ids.game_over_label.text = f"GAME OVER\nCombo: {self.combo}"
        self.ids.game_over_label.opacity = 1

    def animate_combo_label(self):
        """
        สร้างอนิเมชันสำหรับคอมโบ
        """
        anim = Animation(combo_font_size=60, duration=0.1) + Animation(
            combo_font_size=40, duration=0.1
        )
        anim.start(self)
