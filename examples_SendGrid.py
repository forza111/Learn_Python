def send_email(email,name):
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail
    message = Mail(
        from_email='lxey@ya.ru',
        to_emails=email,
        subject='Важное сообщение',
        plain_text_content='{} у вас вылезло гавно'.format(name))
    try:
        sg = SendGridAPIClient('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')
        response = sg.send(message)
    except Exception as e:
        print(str(e))

send_email('n.rikko@mail.ru','Olya')