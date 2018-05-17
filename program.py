__author__ = "byteme8bit"
import os
import cat_service
import subprocess
import platform


def main():
    print_header()
    print()

    folder = get_or_create_output_folder()
    print('Found or created folder: ' + folder)
    print()

    download_cats(folder)
    print()

    display_cats(folder)
    print()

    print("All done! Enjoy your cats!")
    quit()


def print_header():
    """
    Prints program title header
    :return: Prints program title header
    """

    print('--------------------------------------')
    print('                LOL CATS              ')
    print('--------------------------------------')
    print()


def get_or_create_output_folder():
    """
    Checks for existing output folder, creates if not found or uses found folder
    :return: Checks for existing output folder, creates if not found or uses found folder
    """

    base_folder = os.path.dirname(__file__)
    folder = 'cats_pictures'
    full_path = os.path.join(base_folder, folder)
    print(full_path)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    """
    Grabs cats from intrawebz
    :param folder: This parameter is the cats_pictures folder found/made in the directory where this program ran from
    :return: Grabs cats from intrawebz
    """

    print('Contacting server to download cats...')
    cat_count = 8

    for i in range(1, cat_count + 1):
        name = 'lolcat_{}'.format(format(i))
        print('Downloading cat ' + name)
        cat_service.get_cat(folder, name)

    print('Done.')


def display_cats(folder):
    """
    Calls the folder with the cat pictures to open
    :param folder: This parameter is the cats_pictures folder found/made in the directory where this program ran from
    :return: Calls the folder with the cat pictures to open
    """

    print('Displaying cats in OS window...')

    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])

    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])

    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])

    else:
        print("We don't support your OS: " + platform.system())


if __name__ == '__main__':
    main()
