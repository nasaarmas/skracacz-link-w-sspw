import secrets
import string
def short_link(length = 10):
    alphabet = string.ascii_letters + string.digits
    short_link = ''.join(secrets.choice(alphabet) for i in range(length))

    return "link.sspw.pl/" + short_link