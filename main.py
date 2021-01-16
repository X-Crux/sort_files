import os, time, shutil


def start(path_src, path_dst):
    path_src_normalized = os.path.normpath(path_src)

    count = 0
    for dirpath, dirnames, filenames in os.walk(path_src_normalized):
        for file in filenames:
            full_path_src = os.path.join(dirpath, file)

            get_secs = os.path.getmtime(full_path_src)
            get_date = time.localtime(get_secs)
            get_year = time.strftime(format('%Y'), get_date)
            get_month = time.strftime(format('%m'), get_date)

            new_path_dst = f'{path_dst}/{get_year}/{get_month}'
            new_path_dst_normalized = os.path.normpath(new_path_dst)
            full_path_dst = os.path.join(new_path_dst_normalized, file)

            os.makedirs(new_path_dst_normalized, exist_ok=True)
            shutil.copy2(full_path_src, full_path_dst)
            count += 1

            print(full_path_dst)

    print(f'Скопировано файлов: {count}')


def menu():
    path_src = str(input('Введите директорию источника: '))
    path_dst = str(input('Введите директорию назначения: '))
    start(path_src=path_src, path_dst=path_dst)


if __name__ == '__main__':
    menu()
