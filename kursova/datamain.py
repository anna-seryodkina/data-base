import random
import data_backend
import generator

filename1 = './data/numbers.txt'
filename2 = './data/words.txt'
filename3 = './data/dates.txt'


def get_numbers(filename):
    n_list = []
    f = open(filename, 'r')
    for line in f:
        line = line.strip("\n")
        n_list.append(int(line))
    f.close()
    return n_list


def get_text(filename):
    l = []
    f = open(filename, 'r')
    for line in f:
        line = line.strip("\n")
        l.append(line)
    f.close()
    return l


def get_dates(filename):
    l = []
    f = open(filename, 'r')
    for line in f:
        line = line.strip("\n")
        l.append(line)
    f.close()
    return l


def add_websites(numbers, words):
    counter = 0
    for i in numbers:
        counter = counter + 1
        if data_backend.website_exists(counter):
            continue
        w = random.choice(words) + str(i)
        data_backend.add_website(counter, w)


def add_pages(numbers, words):
    counter = 0
    for i in numbers:
        counter = counter + 1
        if data_backend.page_exists(counter):
            continue
        name = random.choice(words) + str(i)
        w_id = random.choice(numbers)
        while not data_backend.website_exists(w_id):
            w_id = random.choice(numbers)
        data_backend.add_page(counter, name, w_id)


def add_webs_visits(numbers, dates):
    counter = 0
    for i in numbers:
        counter = counter + 1
        if data_backend.websitevisit_exists(counter):
            continue
        date = random.choice(dates)
        visits = random.choice(numbers)
        w_id = random.choice(numbers)
        while not data_backend.website_exists(w_id):
            w_id = random.choice(numbers)
        data_backend.add_websitevisit(counter, date, visits, w_id)


def add_pages_visits(numbers, dates):
    counter = 0
    for i in numbers:
        counter = counter + 1
        if data_backend.pagevisit_exists(counter):
            continue
        date = random.choice(dates)
        visits = random.choice(numbers)
        p_id = random.choice(numbers)
        while not data_backend.page_exists(p_id):
            p_id = random.choice(numbers)
        data_backend.add_pagevisit(counter, date, visits, p_id)



def run():
    generator.generate_num(filename1)
    generator.generate_text(filename2)
    generator.generate_date(filename3)

    numbers = get_numbers(filename1)
    words = get_text(filename2)
    dates = get_dates(filename3)

    add_websites(numbers, words)
    add_pages(numbers, words)
    add_webs_visits(numbers, dates)
    add_pages_visits(numbers, dates)


