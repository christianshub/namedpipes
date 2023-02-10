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

if __name__ == "__main__":
    # Map network drive
    map_network_drive(ip="\\\\192.168.138.128", username="desktop-hjm0h0c\\flare", password="password")
