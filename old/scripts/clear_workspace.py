import subprocess


def clear_workspace() -> None:
    # process command and digest output
    process = subprocess.Popen(
        'rm -rf workspace/*',
        shell=True, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE
    )

    out, err = process.communicate()

    out_msg = out.decode('utf-8')
    err_msg = err.decode('utf-8')

    print(f'Output: {out_msg}')
    print(f'Error: {err_msg}')


if __name__ == '__main__':
    clear_workspace()