# coding:utf-8
import random, string


def random_phone():
    # 前两位
    phone1 = '1'
    phone2 = str(random.choice([3, 4, 5, 7, 8]))

    # 第三位
    third = {
        '3': random.randint(0, 9),
        '4': [5, 7, 9][random.randint(0, 2)],
        '5': [i for i in range(10) if i != 4][random.randint(0, 8)],
        '7': [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        '8': random.randint(0, 9),
    }
    phone3 = str(third[phone2])
    phone = phone1 + phone2 + phone3

    for i in range(8):
        phone += str(random.randint(0, 9))

    return phone


def random_password():
    count = random.randint(6, 15)
    passwd = random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits, count)
    str_passwd = ''.join(passwd)
    return str_passwd

def random_mailpassword():
    count = random.randint(8, 12)
    passwd = random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits, count)
    str_passwd = ''.join(passwd)
    return str_passwd


def random_email():
    emailtype = ["@qq.com", "@163.com", "@126.com", "@sina.com", "@gmail.com"]
    randomEmail = random.choice(emailtype)
    rang = random.randint(4, 6)
    letter = "abcdefghijklmnopqrstuvwxyz"
    number = "0123456789"
    randomLetter = "".join(random.choice(letter) for i in range(rang))
    randomNumber = "".join(random.choice(number) for i in range(rang))
    if randomEmail == "@qq.com":
        email = randomNumber + "@qq.com"

    else:
        email = randomLetter + randomNumber + randomEmail
    return email


if __name__ == '__main__':

    print(random_phone())
    print(random_password())