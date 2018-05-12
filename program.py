__author__ = "byteme8bit"
import os


def main():
    print_header()

    folder = get_or_create_output_folder()
    print('Found or created folder: ' + folder)

    # download cats
    # display cats


def print_header():
    print('--------------------------------------')
    print('                LOL CATS              ')
    print('--------------------------------------')
    print()


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    # print(base_folder)
    folder = 'cats_pictures'
    full_path = os.path.join(base_folder, folder)
    # print(full_path)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


if __name__ == '__main__':
    main()
