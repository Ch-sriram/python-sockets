### Some Notes

- Shell scripts (`.sh` files) won't run in a Windows system.
- If you're on Linux/Mac, you've to allow the executable to run, for that, you've to make the shell script executable:
  
  ```terminal
  % chmod +x run_server.sh
  % chmod +x run_client.sh
  ```

### Run Instructions

- Execute `run_server.sh` before `run_client.sh` since the client doesn't wait for there to be a server. And so, the server has to run first.

- In terminal 1:
  
  ```terminal
  % ./run_server.sh
  ```

- In terminal 2:

  ```terminal
  % ./run_client.sh
  ```
