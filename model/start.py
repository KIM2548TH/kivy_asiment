from kivy.animation import Animation
from kivy.clock import Clock


def start_game(widget):
    print("Starting game...")

    widget.initializing = True  # ตั้งค่าสถานะกำลังเริ่ม
    widget.combo = 0
    widget.count = 0
    widget.obj_pos = [250, 250]
    widget.game_active = False

    # ตั้งค่า opacity ให้ข้อความเริ่มต้นแสดงขึ้นมาหากยังไม่เริ่มเกม
    widget.ids.start_label.opacity = 1

    # สถานะเริ่มต้นที่แสดงข้อความตลอด
    widget.ids.start_label.text = "Press R to Start"
