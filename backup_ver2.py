import os
import time

#1 Фаилы и каталоги, которые необходимо скопировать, собираем в список
sourse = ['/home/nikita/PycharmProjects/untitled1/ariphm.py',
         '/home/nikita/PycharmProjects/untitled1/arithmetic.py']
#Для имен, содержащих пробелы, необходимо использовать двойные кавычки внутри строки

#2 Резервные копии должны храниться в основном каталоге резерва
target_dir ='/home/nikita/backup'

#3 Фаилы помещаются в ЗИП архив
#4 Именем ЗИП архива служит текущая дата и время
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
#функцией time.strftime() генерируется текущая дата и время. ей передаем что хотим увидеть(от года до часа)
#переменная 'os.sep' - Содержит разделитель для конкретной ОС (в Windows,Linux,MacOS они разные), можно использовать
#разделитель '/' для linux, но программа с использованием os.sep становится универсальной

#5 Используем команду 'zip' для помещения фаилов в zip архив
zip_command = "zip -qr {0} {1}".format(target, ' '.join(sourse))
#Параметр -q используется для указания того, что команда должна сработать тихо???
#параметр -r указывает что команда архивации должна работать рекурсвно для каталагов, т.е.
#должна включать все подкаталоги и фаилы
#методом джоин превращаем список source в строку

# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    #команда возвращает 0, если выполнена успешно
    print('Резервная копия упешно создана в', target)

else:
    print('Создание резервной копии не удалось')