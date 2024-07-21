def send_email(message: object, recipient: object, *, sender: object = "university.help@gmail.com"):
    b = ".com", ".ru", ".net"
    if recipient.endswith(b) == sender.endswith(b):
        if recipient.count("@") != 1 or sender.count("@") != 1:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        elif sender == recipient:
            print("Нельзя отправить письмо самому себе!")
        elif sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        elif sender != 'university.help@gmail.com':
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

