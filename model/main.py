from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class GameWidget(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)

        Window.bind(mouse_pos=self._on_mouse_move)
        self._mouse = (0, 0)
        self.pressed_keys = set()
        Clock.schedule_interval(self.on_point, 0)

        self.combo = 0
        self.game_over_label = Label(
            text="GAME OVER",
            font_size="50sp",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(None, None),
            size=(300, 100),
            color=(1, 0, 0, 1),
        )
        self.add_widget(self.game_over_label)

        with self.canvas:
            self.hero = Rectangle(source="hero.png", pos=(250, 250), size=(100, 100))

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
        """
        Check if the mouse is inside the object's area.
        """
        x, y = mouse_pos
        obj_x, obj_y = obj.pos
        obj_width, obj_height = obj.size

        return obj_x <= x <= obj_x + obj_width and obj_y <= y <= obj_y + obj_height

    def on_point(self, dt):
        if "s" in self.pressed_keys:
            if self.is_mouse_inside_object(self._mouse, self.hero):
                print("s onclick!!!!!!!!!!")
                self.combo += 1
            else:
                print("game over")
                self.end_game()

        if "d" in self.pressed_keys:
            if self.is_mouse_inside_object(self._mouse, self.hero):
                self.combo += 1
                print("d onclick!!!!!!!!!!")
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

    def end_game(self):
        self.game_active = False
        self.game_over_label.text = f"GAME OVER\nCombo: {self.combo}"
        self.game_over_label.pos = (
            self.width / 2 - self.game_over_label.width / 2,
            self.height / 2 - self.game_over_label.height / 2,
        )
        self.game_over_label.opacity = 1

        print("Game over! Final combo:", self.combo)


class MyApp(App):
    def build(self):
        return GameWidget()


if __name__ == "__main__":
    app = MyApp()
    app.run()
