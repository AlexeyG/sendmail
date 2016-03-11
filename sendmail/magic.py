from IPython.core.magic import register_line_magic, register_cell_magic, register_line_cell_magic
import lepl.apps.rfc3696
import datetime
import time

import sendmail

@register_line_magic
def notify(line) :
    '''
    Notify cell magic.
    '''
    line = line.strip()
    is_valid_email = lepl.apps.rfc3696.Email()
    args = line.split()
    n_args = len(args)
    if n_args == 0 :
        return
    if not is_valid_email(args[0]) :
        if 'notify_email' in globals() :
            mail_to = globals['notify_email']
        else :
            raise Exception('No email provided for notification. Please set the `notify_email` global variable.')
        message = line
    else :
        mail_to = args[0]
        message = line[len(args[0]):].strip()

    timestamp = datetime.datetime.fromtimestamp(time.time())
    title = 'Notification'
    body = '%s\n\n%s' % (message, timestamp.strftime('%a %d/%m/%Y %H:%M'))
    sendmail.sendmail(None, mail_to, title, body)

del notify
