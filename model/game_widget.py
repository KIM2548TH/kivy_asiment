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
        {"time": 0.0, "position": [226, 146]},
        {"time": 2.5, "position": [444, 154]},
        {"time": 5.0 - 1, "position": [416, 257]},
        {"time": 7.5 - 1, "position": [438, 249]},
        {"time": 11 - 1, "position": [326, 407]},
        {"time": 12.5 - 1, "position": [310, 209]},
        {"time": 14.0 - 1, "position": [115, 296]},
        {"time": 15.5 - 1, "position": [277, 409]},
        {"time": 17.0 - 1, "position": [165, 119]},
        {"time": 18.5 - 1, "position": [357, 139]},
        {"time": 20.0 - 1, "position": [124, 411]},
        {"time": 21.5 - 1, "position": [291, 310]},
        {"time": 23.0 - 1 - 0.5, "position": [354, 174]},
        {"time": 24.5 - 1 - 0.5, "position": [384, 417]},
        {"time": 26.0 - 1 - 0.5, "position": [165, 355]},
        {"time": 27.5 - 1 - 0.5, "position": [259, 89]},
        {"time": 29.0 - 1 - 0.5, "position": [287, 390]},
        {"time": 30.5 - 1 - 0.5, "position": [401, 261]},
        {"time": 32.0 - 1 - 0.5, "position": [72, 446]},
        {"time": 33.5 - 1 - 0.5, "position": [399, 79]},
        {"time": 35.0 - 1, "position": [222, 243]},
        {"time": 36.5 - 1, "position": [82, 210]},
        {"time": 38.0 - 1, "position": [295, 205]},
        {"time": 39.5 - 1, "position": [417, 243]},
        {"time": 41.0 - 1, "position": [393, 444]},
        {"time": 42.5 - 1, "position": [190, 272]},
        {"time": 44.0 - 1, "position": [363, 260]},
        {"time": 45.5 - 1, "position": [347, 54]},
        {"time": 47.0 - 1, "position": [195, 229]},
        {"time": 48.5 - 1, "position": [180, 76]},
        {"time": 50.0 - 1, "position": [58, 266]},
        {"time": 51.5 - 1, "position": [79, 308]},
        {"time": 53.0 - 1, "position": [151, 148]},
        {"time": 54.5 - 1, "position": [198, 138]},
        {"time": 56.0 - 1, "position": [419, 351]},
        {"time": 57.5 - 1, "position": [138, 198]},
        {"time": 59.0 - 1, "position": [328, 67]},
        {"time": 60.5 - 1, "position": [329, 403]},
        {"time": 62.0 - 1, "position": [299, 306]},
        {"time": 63.5 - 1, "position": [204, 135]},
        {"time": 65.0 - 1, "position": [299, 165]},
        {"time": 66.5 - 1, "position": [318, 264]},
        {"time": 68.0 - 1, "position": [235, 389]},
        {"time": 69.5 - 1, "position": [418, 330]},
        {"time": 71.0 - 1, "position": [60, 413]},
        {"time": 72.5 - 1, "position": [222, 178]},
        {"time": 74.0 - 1, "position": [327, 84]},
        {"time": 75.5 - 1, "position": [201, 251]},
        {"time": 77.0 - 1, "position": [345, 320]},
        {"time": 78.5 - 1, "position": [138, 376]},
        {"time": 80.0 - 0.5, "position": [174, 245]},
        {"time": 81 - 0.5, "position": [162, 158]},
        {"time": 82 - 0.5, "position": [310, 70]},
        {"time": 83 - 0.5, "position": [350, 101]},
        {"time": 84 - 0.5, "position": [183, 109]},
        {"time": 85 - 0.5, "position": [168, 138]},
        {"time": 86 - 0.5, "position": [209, 321]},
        {"time": 87 - 0.5, "position": [89, 385]},
        {"time": 88 - 0.5, "position": [368, 370]},
        {"time": 89 - 0.5, "position": [186, 100]},
        {"time": 90 - 0.5, "position": [214, 413]},
        {"time": 91 - 0.5, "position": [329, 153]},
        {"time": 92 - 0.5, "position": [318, 218]},
        {"time": 93 - 0.5, "position": [161, 184]},
        {"time": 94 - 0.5, "position": [331, 404]},
        {"time": 95 - 0.5, "position": [430, 85]},
        {"time": 96 - 0.5, "position": [368, 267]},
        {"time": 97 - 0.5, "position": [116, 151]},
        {"time": 98 - 0.5, "position": [127, 97]},
        {"time": 99 - 0.5, "position": [233, 439]},
        {"time": 100 - 0.5, "position": [434, 239]},
        {"time": 101 - 0.5, "position": [194, 185]},
        {"time": 102 - 0.5, "position": [87, 233]},
        {"time": 103 - 0.5, "position": [374, 395]},
        {"time": 104 - 0.5, "position": [225, 269]},
        {"time": 105 - 0.5, "position": [205, 268]},
        {"time": 106 - 0.5, "position": [67, 327]},
        {"time": 107 - 0.5, "position": [447, 142]},
        {"time": 108 - 0.5, "position": [408, 331]},
        {"time": 109 - 0.5, "position": [88, 280]},
        {"time": 110 - 0.5, "position": [208, 263]},
        {"time": 111 - 0.5, "position": [294, 233]},
        {"time": 112 - 0.5, "position": [134, 123]},
        {"time": 113 - 0.5, "position": [355, 88]},
        {"time": 114 - 0.5, "position": [340, 147]},
        {"time": 115 - 0.5, "position": [198, 358]},
        {"time": 116 - 0.5, "position": [269, 428]},
        {"time": 117 - 0.5, "position": [434, 450]},
        {"time": 118 - 0.5, "position": [161, 98]},
        {"time": 119 - 0.5, "position": [112, 102]},
        {"time": 120 - 0.5, "position": [388, 152]},
        {"time": 121 - 0.5, "position": [171, 212]},
        {"time": 123.5, "position": [250, 322]},
        {"time": 126.0 - 1, "position": [117, 394]},
        {"time": 128.5 - 1, "position": [424, 150]},
        {"time": 131.0 - 1, "position": [350, 190]},
        {"time": 133.5 - 1, "position": [360, 62]},
        {"time": 136.0 - 1, "position": [191, 416]},
        {"time": 138.5 - 1, "position": [104, 124]},
        {"time": 141.0 - 1, "position": [119, 378]},
        {"time": 143.5 - 1, "position": [393, 171]},
        {"time": 146.0 - 1, "position": [415, 97]},
        {"time": 148.5 - 1, "position": [322, 111]},
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
        self.obj_clicked = False

    def move_object(self):
        if not self.song_sequence:
            return

        current_time = self.music_logic._song_time  # ใช้เวลาเป็น float

        for song in self.song_sequence:
            if (
                current_time >= song["time"] and current_time < song["time"] + 1
            ):  # เปรียบเทียบแบบ float
                self.obj_pos = song["position"]
                print(f"Object moved to: {self.obj_pos}")
                self.obj_clicked = False
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

        if "d" in self.pressed_keys:
            if (
                self.is_mouse_inside_object(self._mouse, (self.obj_pos, self.obj_size))
                and not self.obj_clicked
            ):
                # กดถูก
                self.combo += 1
                self.obj_clicked = True  # กดถูกแล้วออบเจกต์จะหายไป
                self.animate_combo_label()
                print(f"Clicked on 'd', combo: {self.combo}")
                self.move_object()  # อัพเดตตำแหน่งของออบเจกต์
            else:
                # กดผิด
                print("Missed 'd' or clicked on the wrong object")
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
