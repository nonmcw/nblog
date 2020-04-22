from threading import Thread
from flask import url_for, current_app
from flask_mail import Message

from app.extensions import mail

def _send_async_mail(app, message):
    with app.app_context():
        mail.send(message)

def send_mail(subject, to, html):
    app = current_app._get_current_object()
    message = Message(subject, recipients=[to], html=html)
    thr = Thread(target=_send_async_mail, args=[app, message])
    thr.start()
    return thr

def send_new_comment_mail(post):
    post_url = url_for('views.show_post', post_id=post.id, _external=True) + '#comments'
    send_mail(subject='New comment', to=current_app.config['NBLOG_EMAIL'],
              html='<p>New comment in post <i>%s</i>, click the link below to check.</p>'
                   '<p><a herf="%s">%s</a></p>'
                   '<p><small style="color: #868e96">Do not reply this email.</small></p>'
                   % (post.title, post_url, post_url))

def send_new_reply_mail(comment):
    post_url = url_for('views.show_post', post_id=comment.post_id, _external=True) + '#comments'
    send_mail(subject='New reply', to=comment.post_id,
              html='<p>New reply for comment you left in post <i>%s</i>, click the link below to check.</p>'
                   '<p><a herf="%s">%s</a></p>'
                   '<p><small style="color: #868e96">Do not reply this email.</small></p>'
                   % (comment.post.title, post_url, post_url))