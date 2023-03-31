from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.graphics import Color, Line
from kivy.config import Config

Config.set('graphics', 'width', '450')
Config.set('graphics', 'height', '800')


class MyPaintWidget(Widget):

    Except_num = 0
    line_width = 2

    def on_touch_down(self, touch):
        if self.Except_num == 0:
            self.color = (1, 1, 1, 1)
        else:
            pass

        with self.canvas:
            Color(*self.color)
            touch.ud['line'] = Line(
                points=(touch.x, touch.y), width=self.line_width)

    def on_touch_move(self, touch):
        if 'line' in touch.ud:
            touch.ud['line'].points += [touch.x, touch.y]

    def red(self):
        self.color = (176, 0, 0)
        self.Except_num = 1

    def darkblue(self):
        self.color = (0, 0, 139)
        self.Except_num = 2

    def pink(self):
        self.color = (255, 105, 180)
        self.Except_num = 5

    def yellow(self):
        self.color = (255, 255, 0)
        self.Except_num = 4

    def green(self):
        self.color = (0, 176/255, 80/255)
        self.Except_num = 3

    def set_line_width(self, width):
        self.line_width = width


class MyPaintApp(App):

    def build(self):
        parent = Widget()
        self.color = (random(), 1, 1)
        self.painter = MyPaintWidget()
        clearbtn = Button(text='Clear', size=(50, 50))
        clearbtn.bind(on_release=self.clear_canvas)
        red_color_btn = Button(text='Brush', pos=(50, 0), size=(
            50, 50), background_normal='', background_color=(176, 0, 0))
        red_color_btn.bind(on_release=self.red)
        darkblue_color_btn = Button(text='Brush', pos=(100, 0), size=(
            50, 50), background_normal='', background_color=(0, 0, 139))
        darkblue_color_btn.bind(on_release=self.darkblue)
        green_color_btn = Button(text='Brush', pos=(150, 0), size=(
            50, 50), background_normal='', background_color=(0, 1, 0, 1))
        green_color_btn.bind(on_release=self.green)
        yellow_color_btn = Button(text='Brush', pos=(200, 0), size=(
            50, 50), background_normal='', background_color=(255, 165, 0))
        yellow_color_btn.bind(on_release=self.yellow)
        pink_color_btn = Button(text='Brush', pos=(250, 0), size=(
            50, 50), background_normal='', background_color=(255, 105, 180))
        pink_color_btn.bind(on_release=self.pink)

        sld = Slider(min=1, max=30, value=10, orientation='horizontal',
                     size=(300, 50), pos=(0, 50))
        sld.bind(value=self.on_value_change)

        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        parent.add_widget(red_color_btn)
        parent.add_widget(darkblue_color_btn)
        parent.add_widget(green_color_btn)
        parent.add_widget(yellow_color_btn)
        parent.add_widget(pink_color_btn)
        parent.add_widget(sld)
        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()

    def red(self, obj):
        self.color = (176/255, 0, 0)
        self.painter.red()

    def darkblue(self, obj):
        self.color = (0, 0, 139/255)
        self.painter.darkblue()

    def yellow(self, obj):
        self.color = (255/255, 165/255, 0)
        self.painter.yellow()

    def green(self, obj):
        self.color = (0, 176/255, 80/255)
        self.painter.green()

    def pink(self, obj):
        self.color = (255, 105, 180)
        self.painter.pink()

    def on_value_change(self, instance, value):
        self.painter.set_line_width(value)


if __name__ == '__main__':
    MyPaintApp().run()
