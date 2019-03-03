from ftplib import FTP
import os


def write(password):
    ftp = FTP(host='christian-gr.bplaced.net', user='christian-gr_paris', passwd=password)
    ftp.cwd('www/christian-groeber')
    print(ftp.pwd())
    images = go_in_directory('../Data', [], 'png', 'csv')
    for image in images:
        ftp.storbinary('STOR ' + image['absolute_path'], image['file'])
        image['file'].close()
    print('done saving')


def go_in_directory(dir, arr, wanted_ending, not_wanted_ending):
    os.chdir(dir)
    dirs = os.listdir(".")
    for dirc in dirs:
        if os.path.isdir(dirc):
            arr = go_in_directory(dirc, arr)
        elif dirc.endswith('.' + wanted_ending):
            arr.append({'absolute_path': dirc, 'file': open(dirc, 'rb')})
            os.chdir("../")
            return arr
        elif dirc.endswith('.' + not_wanted_ending):
            pass
        else:
            while not os.path.isdir(dirc):
                os.chdir('../')
            go_in_directory(dirc, arr)
    return arr


def get_images():
    if not os.getcwd().split(os.sep)[-1] == str(id):
        change_directory(sub=sub, id=id)


def change_directory(sub=None, id=None):
    print(os.getcwd())
    dirs = os.getcwd().split(os.sep)
    try:
        if sub is not None:
            if dirs[-1] == "Code" or dirs[-1] == "Data":
                os.chdir("../Data")
                try:
                    os.mkdir(sub)
                    os.chdir(sub)
                except FileExistsError:
                    os.chdir(sub)
                change_directory(id=id)
            elif dirs[-1] == id:
                return
            else:
                os.chdir(".." + os.sep)
                change_directory(sub=sub, id=id)
    except ValueError:
        print(dirs)
    if id is not None and dirs[-1] == sub:
        try:
            os.mkdir(id)
            os.chdir(id)
        except FileExistsError:
            os.chdir(id)
