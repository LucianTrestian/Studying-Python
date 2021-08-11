import os
from PIL import Image


def change_name(path):
    for count, filename in enumerate(os.listdir(path)):
        dst = f"{str(count)}.png"
        src = f"{path}\{filename}"
        dst = f"{path}\{dst}"
        os.rename(src, dst)
    return "DONE change name" 

def convert_in_png(path):
    for filename in os.listdir(path):
        if filename.endswith(".jpg"):
            im = Image.open(f"{path}\{filename}")
            im.save(f'{path}\{filename.replace(".jpg", "")}.png')
        else:
            continue
    return "DONE convert .jpg files in .png"

def delete_jpg_files(path):
    for filename in os.listdir(path):
        if filename.endswith(".jpg"):
            os.remove(f"{path}\{filename}")
    return "DONE delete jpg files"

user_path = input("PATH:")
print("""1.Change the name according to its position in the folder.
2.Conver in png
3.Delete jpg images
4.Exit""")

while True:
    choose = input("Choose one:")
    if choose == "1":
        print(change_name(user_path))
    elif choose == "2":
        print(convert_in_png(user_path))
    elif choose == "3":
        print(delete_jpg_files(user_path))
    elif choose == "4" or choose.lower() == "exit":
        break
    else:
        print('Choose one number from list.')
