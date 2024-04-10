
from flet import *

import sys
sys.path.append(r'C:\Users\danie\VSCProjects\python-project')

from ui import UI


def main(page: Page):
    
    page.title = "Library of Alexandria"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.theme_mode = ThemeMode.LIGHT
    page.window_resizable = False
    login= UI()
    page.add(login)

if __name__ == "__main__":
    print('Running login screen...')
    app(target=main)
