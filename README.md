## About

*sendmail* is a simple Python wrapper around the unix sendmail utility. It allows for sending emails from python witout specifying an SMTP server.

The sendmail code was taken from the [webpy](https://github.com/webpy/webpy) framework.

## Usage

Inside a python script:
```python
import sendmail
sendmail.sendmail('from@user.com', 'to@another-user.com', 'Hello world', 'Hello from sendmail!')
```

From IPython shell:
```ipython
import magic
%notify user@that-likes-updat.es Script execution is now at stage B!
```

## To do
1. Add a setup script
2. Verify that the `notify_email` global variable setting works.
