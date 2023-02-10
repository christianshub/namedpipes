# Named pipes

Remote procedure calls and named pipes can be used for IPC communication between
two processes. It's not widely used nor documented and thus this technique is
quite useful when building C2 communications.

## Named pipes and RPC using ioninja

The following section demonstrates how to use IPC to make a RPC into a target
machine (server) from ones own machine (client). More concretely, the client
will open a pipe in the server machine.

1. Setup a VM acting as the server
    * Ensure its network settings is set to "Host-Only"
    * Ensure
      [pipelist](https://learn.microsoft.com/en-us/sysinternals/downloads/pipelist)
      is installed at the VMs `C:\` drive
    * Get the VMs username (`whoami`) and password
    * Ping the VM (e.g. `ping 192.168.138.128`) from the client PC
1. Setup a Client PC (the local PC)
    * Ensure [ioninja](https://ioninja.com/downloads.html) is installed
1. From the client PC, go to `Start -> Run` and connect to the VM by inserting
   the IP address (`\\192.168.138.128`) in the Run `window`. Now insert the
   username and password for the VM.
1. From the client PC, open ioninja, go to `File -> New Session` and choose
   `File Stream` (check "Run as Administrator")
1. From within the VM, go to the `cmd` and navigate to `C:\` and start
   `pipelist.exe`. Copy the name of any pipe with a free thread (e.g pipe:
   `MsFteWds`)
1. From the client PC, go to ioninja and insert the following
   `\\192.168.138.128\pipe\MsFteWds` at the `File` field.
1. Write any transmit message and press enter
1. Upon success the following will be displayed:

    ```
    Session started
    Opened file \\192.168.138.128\pipe\MsFteWds (pipe)
    File closed
    ```

## Named pipes and RPC using python

Simple PoC that writes text-content from `sample_file.txt` residing on client PC
to a new file on the server PC.

Provided this repo are two scripts, `client.py`, that is supposed to be executed
from the controller PC (the local PC). The second script is the  `server.py`,
this script should be ran from the server PC. The server script uses a local
pipe (`\\.\pipe\my_pipe`) since its only the client PC that connects remotely to
the server PC and access the servers pipe.

> Remember to edit username, password and the IP address to reflect the details
> of the server.

## Escelate privileges

The following is indicators of privilege escelation so that

```bat
@echo off
reg add HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters /v NullSessionPipes /t REG_MULTI_SZ /d \\.\pipe\test_pipe /f
reg add HKLM\SYSTEM\CurrentControlSet\Control\LSA /v restrictanonymous /t REG_DWORD /d 0 /f

pause
```

Nullsession and anonymous pipes allows a RPC to be run with escelated rights.

## References

* [DEF CON 25 - Gil Cohen - Call the plumber: You have a leak in your named
  pipe](https://www.youtube.com/watch?v=6xt0lEj-sac)
* [Interprocess
  Communincation](https://learn.microsoft.com/en-us/windows/win32/ipc/interprocess-communications)

## TODO

- [ ] How can it connect without password and only localdomain/username?
- [ ] Find out how to talk with malware
