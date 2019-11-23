import yagmail


def send_email(title, url, image_url, description, username, password):
    yag = yagmail.SMTP(username, password)

    if image_url:
        image_url_text = """<p><img src="{image_url}></p>"""

    content = (f"<p><b>{title}</b></p>{image_url_text}<p>{description}</p>"
               f'<p><a href="{url}">{url}</a></p>')

    yag.send('prooffreader@gmail.com', f'POCKET: {title}', content)
