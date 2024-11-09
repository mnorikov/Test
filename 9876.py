import os

def get_size(path):
    total_size = 0
    if os.path.isfile(path):
        total_size = os.path.getsize(path)
    else:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                total_size += os.path.getsize(file_path)
    return total_size / (1024 * 1024)  # Переводим размер в Мб

path = '/home/dom/Рабочийстол/'
rez = sorted(os.listdir(path))

with open("out_ok.txt", "w") as file:
    for n, item in enumerate(rez):
        item_path = os.path.join(path, item)
        size = get_size(item_path)
        file.write(f"{n + 1} {item} ({size:.2f} Мб)\n")
        
print('Список файлов смотрим здесь - out_ok.txt')
