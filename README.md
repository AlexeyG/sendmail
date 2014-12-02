## About

*sendmail* is a simple Python wrapper around the unix sendmail utility. It allows for sending emails from python witout specifying an SMTP server.

The sendmail code was taken from the [webpy](https://github.com/webpy/webpy) framework.

## Usage

```python
import sendmail
sendmail.sendmail('from@user.com', 'to@another-user.com', 'Hello world', 'Hello from sendmail!')
```
