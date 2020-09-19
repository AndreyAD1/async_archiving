import subprocess


def main():
    subprocess.run(['zip', '-r', 'test_data', 'test_data'])


if __name__ == '__main__':
    main()
