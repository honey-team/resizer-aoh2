import flet as ft
import os, shutil
import time
from resize import resizePhotos
from logger import Logger

def init_s(page: ft.Page, logger: Logger):
    Mode = 'f'

    def change_mode(e):
        global Mode
        if switch.value:
            switch.label = 'Режим корон (crowns mode)'
            Mode = 'c'
        else:
            switch.label = 'Режим флагов (flags mode)'
            Mode = 'f'

        switch.update()
    
    def start(e):
        path = str(resizePhotos(Mode))
        logger.log('info', f'Resizing {"flags" if Mode == "f" else "crowns"} is completed')

        button.text = 'Готово!'
        button.disabled = True
        button.update()
        os.startfile(path)
        
        time.sleep(1)

        button.text = 'Начать'
        button.disabled = False
        button.update()
    
    def reset_folder(e: ft.ControlEvent):
        what_to_reset = e.control.data # 'storage' or 'output'

        folders_to_reset = []

        match what_to_reset:
            case 'storage':
                folders_to_reset = ['Storage']
            case 'output':
                folders_to_reset = ['Output/crowns/H', 'Output/crowns/XH', 'Output/crowns/XXH', 'Output/crowns/XXXH', 'Output/crowns/XXXXH', 'Output/crowns/icons',
                                    'Output/flags/flags', 'Output/flags/flagsH']
            case _:
                return
        
        for folder in folders_to_reset:
            #
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    logger.log('error', 'Failed to delete %s. Reason: %s' % (file_path, e))
            # Source: https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder


    switch = ft.Switch(label='Режим флагов (flags mode)', value=False, on_change=change_mode)

    button = ft.ElevatedButton('Начать', on_click=start)

    reset_storage = ft.ElevatedButton('Сбросить Storage (Reset Storage)', data='storage', on_click=reset_folder)
    reset_storage.bgcolor = ft.colors.RED_100
    reset_storage.color = ft.colors.RED

    reset_output = ft.ElevatedButton('Сбросить Output (Reset Output)', data='output', on_click=reset_folder)
    reset_output.bgcolor = ft.colors.RED_100
    reset_output.color = ft.colors.RED

    page.window_center()
    page.add(switch, button, reset_storage, reset_output)
    logger.log('info', 'Start page is loaded')