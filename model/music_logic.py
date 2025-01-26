from kivy.clock import Clock
from kivy.core.audio import SoundLoader


class MusicLogic:
    def __init__(self, widget, song_sequence):
        self.widget = widget
        self.song_sequence = song_sequence  # เก็บ sequence ของเพลง
        self.music_file = "assets/music/music.mp3"  # เพลงที่ต้องการ
        self.music = SoundLoader.load(self.music_file)  # โหลดเพลง
        self.beat_interval = 1  # ทุก 2 วินาที ถือว่าเป็นจังหวะใหม่ (สามารถปรับได้)
        self.is_playing = False
        self._song_time = 0.0  # เวลาในเพลง
        self.combo = 0  # คอมโบของผู้เล่น

    def start_music(self):
        if self.music:
            self.music.play()
            self.is_playing = True
            self._song_time = 0  # รีเซ็ตเวลาเพลง
            Clock.schedule_interval(self._on_beat, 0.1)  # เช็คทุก 0.1 วินาที

    def stop_music(self):
        if self.music:
            self.music.stop()
            self.is_playing = False
            Clock.unschedule(self._on_beat)

    def _on_beat(self, dt):
        if not self.is_playing:
            return

        self._song_time += dt  # เพิ่มเวลาในเพลง
        # ตรวจสอบเวลาในเพลง ว่าครบจังหวะใหม่หรือยัง
        if int(self._song_time) % self.beat_interval == 0:  # ทุก 2 วินาที
            self.widget.move_object()

    def handle_user_click(self, key, mouse_pos):
        # ตรวจจับการกดของผู้เล่น
        if key in ["s", "d"]:  # ถ้าผู้เล่นกด 's' หรือ 'd'
            if self._is_click_valid(mouse_pos):  # ถ้าคลิกในตำแหน่งที่ถูกต้อง
                self.combo += 1
                self.widget.animate_combo_label()
            else:
                self.widget.end_game()  # ถ้าคลิกผิดให้จบเกม
                self.stop_music()  # หยุดเพลงเมื่อเกมจบ

    def _is_click_valid(self, mouse_pos):
        # ตรวจสอบว่าคลิกในตำแหน่งออบเจกต์หรือไม่
        obj_pos = self.widget.obj_pos
        obj_size = self.widget.obj_size
        x, y = mouse_pos
        obj_x, obj_y = obj_pos
        obj_width, obj_height = obj_size
        return obj_x <= x <= obj_x + obj_width and obj_y <= y <= obj_y + obj_height
