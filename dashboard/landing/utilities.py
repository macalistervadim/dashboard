from django.template.loader import render_to_string
from django.core.signing import Signer
from django.conf import settings
from datetime import datetime
from os.path import splitext

signer = Signer()

def send_activation_notification(user):
    if settings.ALLOWED_HOSTS:
        host = 'http://' + settings.ALLOWED_HOST[0]
    else:
        host = 'http://127.0.0.1:8000/'

    context = {'user': user, 'host': host, 'sign': signer.sign(user.username)}
    subject = render_to_string('email/activation_letter_subject.txt', context)
    body_text = render_to_string('email/activation_letter_body.txt', context)
    user.email_user(subject, body_text)

def get_timestamp_path(instance, filename):
    return '%s%s' % (datetime.now().timestamp(), splitext(filename)[1])

def send_new_comment_notification(comment):
    if settings.ALLOWED_HOSTS:
        host = 'http://' + settings.ALLOWED_HOST[0]
    else:
        host = 'http://localhost:8000'

    author = comment.bb.author
    context = {'author': author, 'host': host, 'comment': comment}
    subject = render_to_string('email/new_comment_letter_subject.txt', context)
    body_text = render_to_string('email/new_comment_letter_body.txt', context)
    author.email_user(subject, body_text)