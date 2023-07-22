from resize import *
import flet as ft
import time
import os
from init_start import init_s
from init_help import init_h
from logger import Logger

logger = Logger('print')

def main(page: ft.Page):

    def change(e: ft.ControlEvent):
        page.controls.clear()

        match e.control.selected_index:
            case 0:
                init_s(page, logger)
            case 1:
                init_h(page, logger)
        page.update()
    
    page.title = 'Resizer AoH2'

    page.window_resizable = False
    page.window_maximizable = False
    page.window_focused = True

    page.window_width = 340
    page.window_height = 460

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.navigation_bar = ft.NavigationBar(destinations=[
        ft.NavigationDestination(icon=ft.icons.PHOTO_SIZE_SELECT_ACTUAL_OUTLINED, selected_icon=ft.icons.PHOTO_SIZE_SELECT_ACTUAL, label='Изменить размер'),
        ft.NavigationDestination(icon=ft.icons.HELP_OUTLINE_ROUNDED, selected_icon=ft.icons.HELP_ROUNDED, label='Помощь')
    ], selected_index=0, on_change=change)

    init_s(page, logger)

    page.update()

    

if __name__ == '__main__':
    try:
        ft.app(target=main)
    except Exception as ex:
        logger.log('error', str(type(ex)))
