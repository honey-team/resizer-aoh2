import flet as ft
from logger import Logger

def init_h(page: ft.Page, logger: Logger):
    text = ft.Text('Данная программа создана для того, чтобы упростить работу создателя модов для игры Age of History 2. С её помощью вы сможете изменять размеры для корон идеологий и флагов для цивилизаций.')
    text2 = ft.Text('Как пользоваться ей?')
    text3 = ft.Text('1. В папку Storage скиньте свои флаги и короны идеологий.')
    text4 = ft.Text('2. Выберите режим изменения размера (флаги или короны идеологий)')
    text5 = ft.Text('3. После нажатия кнопки "Старт" в папке flags или в crowns, появятся измененные фото в соответствующих папках. Для вашего удобства папка открывается автоматически.')

    page.add(text, text2, text3, text4, text5)
    logger.log('info', 'Help page is loaded')
