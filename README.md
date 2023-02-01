### Some Notes

- Shell scripts (files with `.sh` extension) won't run in Windows systems. Therefore, for a Windows system, check the [Run Instructions (Windows)](#run-instructions-windows) below.
- If running on a Linux/Mac, allow the shell scripts to run - for that, make the shell script executable:
  
  ```terminal
  chmod +x run_server.sh
  chmod +x run_client.sh
  ```

### Run Instructions (Linux/Mac)

- Execute `run_server.sh` before `run_client.sh` since the client doesn't wait for there to be a server. And so, the server has to run first.

  In terminal 1:
  
  ```terminal
  ./run_server.sh
  ```

  In terminal 2:

  ```terminal
  ./run_client.sh
  ```

### Run Instructions (Windows)

- Since `.sh` files cannot be run directly, WSL (Windows Subsystem for Linux) can be installed and then, shell scripts will run with the [Run Instructions (Linux/Mac)](#run-instructions-linuxmac) aforementioned.
- But, to run without installing WSL, one can run the following commands from their windows commandline:
  
  In terminal 1:
  
  ```cmd
  py -3 server.py
  ```

  In terminal 2:
  
  ```cmd
  py -3 client.py
  ```

- **NOTE**: Check `python3`'s Path settings in *Advanced System Settings* > *Environment Variables*.
