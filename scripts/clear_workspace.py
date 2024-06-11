import subprocess


def clear_workspace() -> None:
    # Execute the command
    process = subprocess.Popen(
        'rm -rf workspace/*',
        shell=True, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE
    )

    # Get the output and error (if any)
    out, err = process.communicate()

    # Decode bytes to string (assuming utf-8 encoding)
    output_str = out.decode('utf-8')
    error_str = err.decode('utf-8')

    print(f'Output: {output_str}')
    print(f'Error: {error_str}')


if __name__ == '__main__':
    clear_workspace()