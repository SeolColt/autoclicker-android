"""
Auto Clicker Android - Kivy版本
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.clock import Clock
import threading
import time
import random

class AutoClickerApp(App):
    def build(self):
        self.title = "Auto Clicker Android"

        # 主布局
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # 标题
        title = Label(
            text="⚡ Auto Clicker",
            font_size=24,
            size_hint_y=0.1
        )
        main_layout.add_widget(title)

        # 状态显示
        self.status_label = Label(
            text="Status: Stopped",
            font_size=18,
            size_hint_y=0.08
        )
        main_layout.add_widget(self.status_label)

        # 点击次数
        self.count_label = Label(
            text="Click Count: 0",
            font_size=16,
            size_hint_y=0.08
        )
        main_layout.add_widget(self.count_label)

        # 间隔设置
        interval_layout = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        interval_layout.add_widget(Label(text="Interval (sec):", font_size=14))

        self.interval_input = TextInput(
            text="0.1",
            font_size=14,
            size_hint_x=0.5,
            input_filter='float'
        )
        interval_layout.add_widget(self.interval_input)
        main_layout.add_widget(interval_layout)

        # 模式选择
        self.mode_spinner = Spinner(
            text='Fixed',
            values=('Fixed', 'Random'),
            size_hint_y=0.08
        )
        main_layout.add_widget(self.mode_spinner)

        # 控制按钮
        self.start_button = Button(
            text="▶ START",
            font_size=18,
            size_hint_y=0.12,
            background_color=(0, 0.8, 0.4, 1)
        )
        self.start_button.bind(on_press=self.toggle_clicking)
        main_layout.add_widget(self.start_button)

        # 退出按钮
        exit_button = Button(
            text="EXIT",
            font_size=16,
            size_hint_y=0.1
        )
        exit_button.bind(on_press=self.exit_app)
        main_layout.add_widget(exit_button)

        # 全局变量
        self.is_running = False
        self.click_count = 0
        self.click_interval = 0.1
        self.mode = "Fixed"

        return main_layout

    def toggle_clicking(self, instance):
        if self.is_running:
            self.stop_clicking()
        else:
            self.start_clicking()

    def start_clicking(self):
        try:
            self.click_interval = float(self.interval_input.text)
            if self.click_interval < 0.001:
                self.click_interval = 0.001
        except ValueError:
            self.click_interval = 0.1

        self.mode = self.mode_spinner.text
        self.is_running = True
        self.click_count = 0

        # 更新UI
        self.status_label.text = "Status: Running"
        self.start_button.text = "⏹ STOP"
        self.start_button.background_color = (0.8, 0.2, 0.2, 1)

        # 启动点击线程
        threading.Thread(target=self.click_worker, daemon=True).start()

    def stop_clicking(self):
        self.is_running = False

        # 更新UI
        self.status_label.text = "Status: Stopped"
        self.start_button.text = "▶ START"
        self.start_button.background_color = (0, 0.8, 0.4, 1)

    def click_worker(self):
        while self.is_running:
            # 点击
            self.click_count += 1

            # 更新UI
            Clock.schedule_once(lambda dt: self.update_count())

            # 根据模式选择间隔
            if self.mode == "Random":
                delay = self.click_interval * (0.5 + random.random())
            else:
                delay = self.click_interval

            time.sleep(delay)

    def update_count(self):
        self.count_label.text = f"Click Count: {self.click_count}"

    def exit_app(self, instance):
        self.is_running = False
        App.get_running_app().stop()

if __name__ == "__main__":
    AutoClickerApp().run()
