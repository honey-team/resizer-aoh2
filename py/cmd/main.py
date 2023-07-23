from resize import resizePhotos
import keyboard
import time
import colorama

all_page_size = '\n' * 35

def wait_for_keys(*keys):
    res = ''
    while res not in keys:
        res = keyboard.read_key()
    return res

if __name__ == '__main__':
    colorama.init()

    print(all_page_size)
    print(f'{colorama.Fore.GREEN}Starting program...')
    time.sleep(0.5)

    print(all_page_size)

    print(f'{colorama.Fore.BLUE}Starting program...')
    time.sleep(0.5)

    print(all_page_size)

    print(f'{colorama.Fore.RED}Starting program...')
    time.sleep(0.5)

    print(all_page_size)

    print(f'{colorama.Fore.YELLOW}Starting program...')
    time.sleep(0.5)

    print(all_page_size)

    print(f'{colorama.Fore.RESET}Starting program...')
    time.sleep(0.5)

    print('s - start command - Start a resizing')
    print('r - reset command - Reset a storage or output or all')
    print('(press a key)')

    command = wait_for_keys('s', 'r')

    print(all_page_size)
    time.sleep(0.2)

    match command:
        case 's':
            print('f - flags mode')
            print('c - crowns mode')
            print('(press a key)')

            key = wait_for_keys('f', 'c')
            
            match key:
                case 'f':
                    print('Started flags mode')
                case 'c':
                    print('Started crowns mode')

        case 'r':
            ...
