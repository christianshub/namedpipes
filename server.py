import win32pipe
import win32file
import errno

PIPE_NAME = r'\\.\pipe\my_pipe'
FILE_PATH = 'received_file.txt'

def create_pipe():
    return win32pipe.CreateNamedPipe(
        PIPE_NAME,
        win32pipe.PIPE_ACCESS_INBOUND,
        win32pipe.PIPE_TYPE_BYTE | win32pipe.PIPE_WAIT,
        1,
        65536,
        65536,
        0,
        None
    )

def wait_for_connection(pipe):
    win32pipe.ConnectNamedPipe(pipe, None)

def receive_file(pipe):
    try:
        with open(FILE_PATH, 'wb') as file:
            while True:
                data = win32file.ReadFile(pipe, 4096)[1]
                if not data:
                    break
                file.write(data)
            print(f"File received successfully. Path: {FILE_PATH}")
    except IOError as e:
        if e.errno == errno.EACCES:
            print(f"Permission denied: {FILE_PATH}")
        else:
            print(f"An error occurred while writing the file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def close_pipe(pipe):
    win32file.CloseHandle(pipe)

def run_server():
    pipe = create_pipe()
    wait_for_connection(pipe)
    receive_file(pipe)
    close_pipe(pipe)

if __name__ == "__main__":
    run_server()
