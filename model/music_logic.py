import time
from kivy.clock import Clock


class MusicLogic:
    def __init__(self, widget, song_sequence):
        self.widget = widget
        self.song_sequence = (
            song_sequence  # sequence ของตำแหน่ง (ตำแหน่งออบเจกต์) ที่จะเปลี่ยน
        )
        self.current_index = 0
        self.start_time = time.time()  # เวลาของการเริ่มเพลง
        self.game_active = True  # เกมอยู่ในสถานะทำงาน
        self.combo_timer = 0  # ตั้งเวลาตัวจับคอมโบ

        # กำหนดให้ Timer run
        Clock.schedule_interval(self.update_position, 1 / 30)  # ตั้งให้ทำงานทุกๆ 1/30 วินาที

    def update_position(self, dt):
        if not self.game_active:  # หากเกมสิ้นสุดไม่ต้องทำการอัปเดต
            return

        elapsed_time = time.time() - self.start_time

        # การใช้เวลาตามเพลงและตำแหน่ง
        target_time = self.song_sequence[self.current_index]["time"]
        if elapsed_time >= target_time:
            self.update_object_position(
                self.song_sequence[self.current_index]["position"]
            )
            self.current_index += 1

            if self.current_index >= len(self.song_sequence):
                self.end_game()  # สิ้นสุดเพลงและเกม
                return

    def update_object_position(self, position):
        self.widget.obj_pos = position  # เปลี่ยนตำแหน่งของออบเจกต์ที่ต้องการให้ตรงตามจังหวะ

    def end_game(self):
        self.game_active = False
        self.widget.end_game()  # เรียกฟังก์ชัน game over
        print("GAME OVER")

    def check_user_click(self, click_position):
        # ตรวจสอบว่าผู้เล่นคลิกโดนตามตำแหน่งในช่วงเวลานั้น
        if not self.game_active:
            return

        current_position = self.widget.obj_pos
        if click_position == current_position:
            self.combo_timer += 1
            self.widget.animate_combo_label()  # เสริมคอมโบให้ดู
            print("Correct click!")
        else:
            self.end_game()
