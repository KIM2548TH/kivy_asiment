from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import ListProperty, NumericProperty
from kivy.animation import Animation
import os
from game_widget import GameWidget

kv_path = os.path.join(os.path.dirname(__file__), "../tamplate/main.kv")
Builder.load_file(kv_path)


class MyApp(App):
    def build(self):
        return GameWidget()


if __name__ == "__main__":
    app = MyApp()
    app.run()
