from kivy.animation import Animation
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.properties import ListProperty, NumericProperty


class new_game:
    @staticmethod
    def start_game(widget):
        # รีเซ็ตค่าคอมโบ
        widget.combo = 0  # รีเซ็ตค่า combo
        widget.count = 0  # รีเซ็ตค่า counts
        widget.obj_pos = [250, 250]  # รีเซ็ตตำแหน่งออบเจกต์
        widget.game_active = False  # ปิดสถานะเกม

        # ซ่อนข้อความ "GAME OVER" ถ้ามี
        if widget.ids.game_over_label.opacity == 1:
            widget.ids.game_over_label.text = ""  # ล้างข้อความ
            widget.ids.game_over_label.opacity = 0  # ซ่อนข้อความ

        # สร้าง center object
        object_in_start.create_center_object(widget)

        # แสดงข้อความ "Press R on object to Start"
        widget.ids.start_label.opacity = 1
        widget.ids.start_label.text = "Press R on object to Start"

    @staticmethod
    def reset_game(widget):
        widget.combo = 0
        widget.count = 0
        widget.obj_pos = [250, 250]


class object_in_start:
    obj_pos = ListProperty([250, 250])
    sizes = ListProperty([])
    sizes = [[100, 100], [95, 95], [98, 98], [88, 88], [80, 80], [85, 85]]

    @staticmethod
    def create_center_object(widget):
        center_x = (widget.width - widget.obj_size[0]) / 2
        center_y = (widget.height - widget.obj_size[1]) / 2
        widget.obj_pos = [center_x, center_y]
        print(widget.obj_pos)

    @staticmethod
    def remove_center_object(widget):
        # ลบ center object
        if hasattr(widget, "center_obj"):
            widget.canvas.remove(widget.center_obj)
