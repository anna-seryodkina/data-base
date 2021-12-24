import random
import datetime


def generate_num(filename):
    l = []
    for i in range(1000):
        l.append(random.randint(1, 1000))

    f = open(filename, 'w')

    for index in l:
        f.write(str(index) + '\n')

    f.close()


def generate_text(filename):
    l = []
    words1 = ["interesting", "code", "site", "great", "my", "cyber", "meme", "check", "world", "guide", "tutorial", "easy", "super"]
    words2 = ["python", "java", "banana", "cat", "apple", "concert", "ticket", "buy", "wooow"]

    for i in range(100000):
        s1 = random.choice(words1)
        s2 = random.choice(words2)

        l.append(s1 + '-' + s2)

    f = open(filename, 'w')

    for index in l:
        f.write(str(index) + '\n')

    f.close()


def generate_date(filename):
    l = []
    start_date = datetime.date(2021, 1, 1)
    end_date = datetime.date.today()
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days

    for i in range(100000):
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        l.append(str(random_date))

    f = open(filename, 'w')

    for index in l:
        f.write(str(index) + '\n')

    f.close()
