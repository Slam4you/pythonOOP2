# поиск всех файлов формата .py с выводом их дирикторий
import os.path

print(os.listdir("main"))
for cur_dir, dir, files in os.walk("main"):
    for i in files:
        if i[-3:] == ".py":
            print(cur_dir)
            break