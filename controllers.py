from ast import Bytes
from pynput import mouse, keyboard
from json import load
from time import sleep


class Youtube_viewer:
    def __init__(self, settings_path: str = 'settings.json') -> None:
        with open(settings_path) as settings:
            self.settings = load(settings)
        self.mouse = mouse.Controller()
        self.button = mouse.Button
        self.keyboard = keyboard.Controller()
        self.key = keyboard.Key

    def _open_apps_menu(self):
        self.mouse.position = (10, 10)
        self.mouse.click(self.button.left)

    def _press_enter(self):
        self.keyboard.press(self.key.enter)
        sleep(0.2)
        self.keyboard.release(self.key.enter)

    def _copy_text(self):
        self.keyboard.press(self.key.ctrl)
        self.keyboard.press('a')
        sleep(0.2)
        self.keyboard.release('a')
        sleep(0.2)
        self.keyboard.press('c')
        sleep(0.2)
        self.keyboard.release('c')

    def _open_browser(self):
        self.keyboard.type(self.settings['browser'])
        sleep(1)
        self._press_enter()

    def _open_youtube_channel(self):
        self.keyboard.type(f'youtube.com/{self.settings["channel"]}')
        sleep(1)
        self._press_enter()

    def _open_recent_video(self):
        self.mouse.position = (304, 654)
        self.mouse.click(self.button.left)

    def _get_url(self):
        self.mouse.position = (315, 109)
        self.mouse.click(self.button.left)
        self._copy_text()

    def open_recent_YT_video(self):
        self._open_apps_menu()
        sleep(0.2)
        self._open_browser()
        sleep(1)
        self._open_youtube_channel()
        sleep(3)
        self._open_recent_video()