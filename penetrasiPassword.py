import itertools
import string
import time
import sys


def matched(a, b):
    if a == b:
        print('========================================================')
        print('=================== String matched! ====================')
        print('========================================================')
        print('Password is : {}'.format(a))
        print('Done in : {} seconds'.format(time.perf_counter() - start))
        print('========================================================')
        input('Press enter to terminate program...')
        sys.exit()


def penetrate(real):
    strings = string.ascii_lowercase
    for password_length in range(1, len(real) + 1):
        for temporary in itertools.product(strings, repeat=password_length):
            temporary = ''.join(temporary)
            a = temporary
            b = real
            matched(a, b)
            print('{}'.format(list(temporary)))


def main():
    password = input('Set password : ')
    print('Password telah diset sebagai : ', password)
    accept = input('Lanjutkan proses penetrasi? (Y/N)')
    if accept == 'Y' or accept == 'y':
        global start
        start = time.perf_counter()
        print(penetrate(password))


if __name__ == '__main__':
    main()
