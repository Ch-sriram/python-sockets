- Shell scripts (`.sh` files) won't run in a Windows system.
- If you're on Linux/Mac, you've to allow the executable to run, for that, you've to make the shell script executable:
```bash
$ chmod +x run_server.sh
$ chmod +x run_client.sh
```
- Execute `run_server.sh` before `run_client.sh` since the client doesn't wait for there to be a server. And so, the server has to run first.
