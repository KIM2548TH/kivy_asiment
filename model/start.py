from kivy.animation import Animation
from kivy.graphics import Rectangle
from kivy.properties import ListProperty


from kivy.uix.button import Button


def start_game(widget):
    widget.combo = 0
    widget.count = 0
    widget.obj_pos = [250, 250]
    widget.game_active = False

    # ซ่อนออบเจกต์
    # widget.ids.obj.opacity = 0

    # แสดงข้อความเริ่มต้น
    widget.ids.start_label.opacity = 1
    widget.ids.start_label.text = "Press R to Start"

    # เพิ่มปุ่ม "ทดลองเล่น" และ "เลือกเพลง"
    if not hasattr(widget, "try_button") and not hasattr(widget, "song_button"):
        try_button = Button(
            text="ทดลองเล่น",
            size_hint=(0.3, 0.1),
            pos_hint={"center_x": 0.3, "center_y": 0.5},
        )
        try_button.bind(on_press=lambda *args: widget.start_trial())

        song_button = Button(
            text="เลือกเพลง",
            size_hint=(0.3, 0.1),
            pos_hint={"center_x": 0.7, "center_y": 0.5},
        )
        song_button.bind(on_press=lambda *args: widget.select_song())

        widget.add_widget(try_button)
        widget.add_widget(song_button)

        widget.try_button = try_button
        widget.song_button = song_button


class object_in_start:
    obj_pos = ListProperty([250, 250])
    sizes = [[100, 100], [95, 95], [98, 98], [88, 88], [80, 80], [85, 85]]

    @staticmethod
    def create_center_object(widget):
        center_x = (widget.width - widget.obj_size[0]) / 2
        center_y = (widget.height - widget.obj_size[1]) / 2
        widget.obj_pos = [center_x, center_y]

    @staticmethod
    def remove_center_object(widget):
        # เช็คและลบ center object ใน canvas
        if hasattr(widget, "center_obj"):
            widget.canvas.remove(widget.center_obj)  # ลบออกจาก canvas
            del widget.center_obj
