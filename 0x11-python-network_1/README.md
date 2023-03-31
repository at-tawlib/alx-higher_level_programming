# 0x11. Python - Network #1
### `Python` - `Scripting` - `Back-end` - `API`

## [0-hbtn_status.py](0-hbtn_status.py)
script that fetches  `https://alx-intranet.hbtn.io/status`  using `urllib` package
```
guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
guillaume@ubuntu:~/0x11$ 
```
## [1-hbtn_header.py](1-hbtn_header.py)
takes in a URL, sends a request to the URL and displays the value of the  `X-Request-Id`  variable found in the header of the response using `urllib` package
```
guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
guillaume@ubuntu:~/0x11$ 
guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
guillaume@ubuntu:~/0x11$ 
```
## [2-post_email.py](2-post_email.py)
script that takes in a URL and an email, sends a  `POST`  request to the passed URL with the email as a parameter, and displays the body of the response (decoded in  `utf-8`)
-   The email must be sent in the  `email`  variable
Please test your script in the sandbox provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x11$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
guillaume@ubuntu:~/0x11$ 
```
## [3-error_code.py](3-error_code.py)
script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in  `utf-8`).
-   You have to manage  `urllib.error.HTTPError`  exceptions and print:  `Error code:`  followed by the HTTP status code
Please test your script in the sandbox provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000
Index
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
guillaume@ubuntu:~/0x11$ 
```
## [4-hbtn_status.py](4-hbtn_status.py)
script that fetches  `https://alx-intranet.hbtn.io/status` using `requests` packages
```
guillaume@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
guillaume@ubuntu:~/0x11$ 
```
## [5-hbtn_header.py](5-hbtn_header.py)
script that takes in a URL, sends a request to the URL and displays the value of the variable  `X-Request-Id`  in the response header  using `requests` package
```
guillaume@ubuntu:~/0x11$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
5e52e160-c822-4669-8b3a-8b3bbca7b090
guillaume@ubuntu:~/0x11$ 
guillaume@ubuntu:~/0x11$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
eaceaf35-bc0f-4f74-994a-7be0728ec654
guillaume@ubuntu:~/0x11$ 
```



> Written with [StackEdit](https://stackedit.io/).
