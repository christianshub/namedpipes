import subprocess
import win32file
import errno

def map_network_drive(ip, username, password):
    command = ["net", "use", ip, "/user:{}".format(username), password]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print("Success")
    else:
        print("Failure")

def open_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()
    except IOError as e:
        if e.errno == errno.ENOENT:
            print(f"File not found: {file_path}")
        elif e.errno == errno.EACCES:
            print(f"Permission denied: {file_path}")
        else:
            print(f"An error occurred while reading the file: {e}")
    return file_content

def open_pipe(pipe_name):
    pipe = win32file.CreateFile(
        pipe_name,
        win32file.GENERIC_WRITE,
        0,
        None,
        win32file.OPEN_EXISTING,
        0,
        None
    )
    return pipe

def send_file(pipe, file_content):
    win32file.WriteFile(pipe, file_content)

if __name__ == "__main__":
    # Map network drive
    map_network_drive(ip="\\\\192.168.138.128", username="desktop-hjm0h0c\\flare", password="password")

    # Open pipe and send file
    pipe_name = r'\\192.168.138.128\pipe\my_pipe'
    pipe = open_pipe(pipe_name)
    file_content = open_file("sample_file.txt")
    send_file(pipe, file_content)
