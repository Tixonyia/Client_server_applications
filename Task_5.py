# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
# преобразовать результаты из байтовового в строковый тип.

import subprocess

for ping_res in ['yandex.ru', 'youtube.com']:
    ping_proc = subprocess.Popen(['ping', ping_res], stdout=subprocess.PIPE)
    i = 0
    for line in ping_proc.stdout:
        print(line)
        print(line.decode())
        if i > 5:
            break
        i += 1

