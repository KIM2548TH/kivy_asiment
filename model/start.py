from kivy.animation import Animation
from kivy.graphics import Rectangle


def start_game(widget):
    widget.combo = 0
    widget.count = 0
    widget.obj_pos = [250, 250]
    widget.game_active = False

    create_center_object(widget)

    widget.ids.start_label.opacity = 1
    widget.ids.start_label.text = "Press R to Start"


def create_center_object(widget):
    center_x = (widget.width - widget.obj_size[0]) / 2
    center_y = (widget.height - widget.obj_size[1]) / 2

    with widget.canvas:
        widget.center_obj = Rectangle(pos=(center_x, center_y), size=widget.obj_size)


def remove_center_object(widget):
    if hasattr(widget, "center_obj"):
        anim = Animation(opacity=0, duration=0.5)
        anim.bind(on_complete=lambda *args: widget.canvas.remove(widget.center_obj))
        anim.start(widget.ids.start_label)
        widget.canvas.remove(widget.center_obj)
        del widget.center_obj
