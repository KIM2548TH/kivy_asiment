from kivy.animation import Animation
from kivy.graphics import Rectangle
from kivy.properties import ListProperty


def start_game(widget):
    widget.combo = 0
    widget.count = 0
    widget.obj_pos = [250, 250]
    widget.game_active = False

    # สร้าง center object
    object_in_start.create_center_object(widget)

    widget.ids.start_label.opacity = 1
    widget.ids.start_label.text = "Press R on object to Start"


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
        # ลบ center object
        if hasattr(widget, "center_obj"):
            widget.canvas.remove(widget.center_obj)
            del widget.center_obj
