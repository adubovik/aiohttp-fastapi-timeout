Run the server in a console 1:

```sh
python3 app.py
```

Send the requests in a console 2:

```sh
./locust.sh
```

Observe the timeout in the console 1:

```sh
2024-12-30 10:12:07,062 - INFO - 1 waiting
2024-12-30 10:12:08,067 - INFO - 1 requesting
2024-12-30 10:12:08,072 - INFO - 2 waiting
2024-12-30 10:12:09,074 - INFO - 2 requesting
2024-12-30 10:12:09,076 - ERROR - 1 fail: builtins.TimeoutError
2024-12-30 10:12:09,238 - INFO - 2 success
```