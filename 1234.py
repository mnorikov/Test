import os
from os.path import getsize, join

"""
'.' это поиск в текущей папке
"""
for root, dirs, files in os.walk('/home/dom/Рабочийстол/'):
    total_size = sum(getsize(join(root, name)) for name in files)
    print(root, total_size)

