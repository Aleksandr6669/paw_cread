import flet as ft
import flet_webview as ftwv
import configparser
import os

# Определяем путь к файлу config.ini относительно текущего файла
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')

config = configparser.ConfigParser()
config.read(config_path)

URL = config['Settings']['URL']
PAGE_TITLE = config['Settings']['PAGE_TITLE']


def main(page: ft.Page):
    page.title = PAGE_TITLE
    page.padding = 0
    wv = ftwv.WebView(
        url=URL,
        expand=True,
    )
    page.add(wv)


ft.app(main)