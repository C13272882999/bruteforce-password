import itertools
import string
import time


def mainExec():
    passw = input('Set password : ')
    print('Password telah diset sebagai : ', passw)
    accept = input('Lanjutkan proses penetrasi? (Y/N)')
    if accept == 'Y' or accept == 'y':
        global start
        start = time.perf_counter()
        print(penetrasiPassword(passw))
        acc = input('Penetrasi password lain? (Y/N)')
        if acc == 'Y' or acc == 'y':
            mainExec()
        else:
            print('Eksekusi dihentikan')
    else:
        print('Eksekusi dihentikan')
    input()


def penetrasiPassword(real):
    strings = string.ascii_lowercase + string.digits
    percobaan = 0
    for password_length in range(1, len(real) + 1):
        for tempPass in itertools.product(strings, repeat=password_length):
            percobaan += 1
            tempPass = ''.join(tempPass)
            if tempPass == real:
                return 'Password match! Password : {}, ditemukan dalam percobaan ke-{}'.format(tempPass, percobaan)
            print('Testing : ', tempPass, ' || Nomor percobaan : ', percobaan, ' || ', time.perf_counter() - start)


mainExec()