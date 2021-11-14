import random
import datetime

def generate_num():
    l = []
    for i in range(100000):
        l.append(random.randint(0, 1000))

    f = open('./kursova/data/numbers.txt', 'w')

    for index in l:
        f.write(str(index) + '\n')

    f.close()


def generate_text():
    l = []
    words1 = ["interesting", "code", "site", "great", "my", "cyber", "meme", "check", "world", "guide", "tutorial", "easy", "super"]
    words2 = ["python", "java", "banana", "cat", "apple", "concert", "ticket", "buy", "wooow"]
    words3 = [".com", ".ua", ".it", ".net"]


    for i in range(100000):
        s1 = random.choice(words1)
        s2 = random.choice(words2)
        s3 = random.choice(words3)

        l.append(s1 + '-' + s2 + s3)

    f = open('./kursova/data/words.txt', 'w')

    for index in l:
        f.write(str(index) + '\n')

    f.close()


def generate_date():
    l = []
    start_date = datetime.date(2018, 1, 1)
    end_date = datetime.date(2021, 2, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days

    for i in range(100000):
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        l.append(str(random_date))

    f = open('./kursova/data/dates.txt', 'w')

    for index in l:
        f.write(str(index) + '\n')

    f.close()


generate_num()
generate_text()
generate_date()