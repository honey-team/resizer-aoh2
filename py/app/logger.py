from typing import Literal, Any

class Logger:
    def __init__(self, method: Literal['print', 'return'], format: str = None):
        self.logs = []
        self.__method = method
        
        __default = '{level}: {info}'
        self.__format = format if format else __default
    
    def log(self, level: Literal['info', 'warning', 'error'], information: Any):
        formated_log = self.__format.format(
                level=level.upper(),
                info=information
                )
        self.logs.append(formated_log)

        if self.__method == 'print':
            print(formated_log)
        elif self.__method == 'return':
            return formated_log
