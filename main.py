import subprocess


def main():
    command_args = ['zip', '-r', '-', 'test_data']
    completed_process = subprocess.run(command_args, capture_output=True)
    archive = completed_process.stdout
    with open('archive.zip', 'wb') as archive_file:
        archive_file.write(archive)


if __name__ == '__main__':
    main()
