import itertools
import string
import time
import sys


def main():
    passw = input('Set password : ')
    print('Password telah diset sebagai : ', passw)
    accept = input('Lanjutkan proses penetrasi? (Y/N)')
    if accept == 'Y' or accept == 'y':
        global start
        start = time.perf_counter()
        print(penetrasiPassword(passw))
        input('Press enter to terminate program')
        sys.exit()


def penetrasiPassword(real):
    strings = string.ascii_lowercase
    percobaan = 0
    for password_length in range(1, len(real) + 1):
        for tempPass in itertools.product(strings, repeat=password_length):
            percobaan += 1
            tempPass = ''.join(tempPass)
            if tempPass == real:
                return 'Password match! Password : {}, ditemukan dalam percobaan ke-{}'.format(list(tempPass), percobaan)
            print('Testing : ', list(tempPass), ' || Nomor percobaan : ', percobaan, ' || ', time.perf_counter() - start)


if __name__ == '__main__':
    main()
