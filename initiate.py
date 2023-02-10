import subprocess

# Script that map a network drive to a specified IP address
# This is ran prior to the RPC named pipe connection

ip = "\\\\192.168.138.128" # server
username = "desktop-hjm0h0c\\flare" # whoami on server
password = "password" # windows signin password

command = ["net", "use", ip, "/user:{}".format(username), password]
result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if result.returncode == 0:
    print("Success")
else:
    print("Failure")
