import flet as ft
import os
import time
from resize import resizePhotos

def init_s(page: ft.Page):
    Mode = 'f'

    def change_mode(e):
        if switch.value:
            switch.label = 'Режим корон (crowns mode)'
            Mode = 'c'
        else:
            switch.label = 'Режим флагов (flags mode)'
            Mode = 'f'

        switch.update()
    
    def start(e):
        path = resizePhotos(Mode)
        button.text = 'Готово!'
        button.disabled = True
        button.update()
        os.startfile(path)
        
        time.sleep(1)

        button.text = 'Начать'
        button.disabled = False
        button.update()

    switch = ft.Switch(label='Режим флагов (flags mode)', value=False, on_change=change_mode)
    button = ft.ElevatedButton('Начать', on_click=start)

    page.window_center()
    page.add(switch, button)