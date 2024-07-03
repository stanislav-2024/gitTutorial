#импортируем модуль для работы с датой и временем
from datetime import datetime 
#программа предназначеня для получения текущей даты и времени

now = datetime.now().strftime('%d.%m.%Y %H:%M')
print(now)

