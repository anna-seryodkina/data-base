import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import data_backend


def counter(sitename):
    gdata = data_backend.get_site_data_for_counter(sitename)

    print('yesterday: ', gdata[0])
    print('last week: ', gdata[1])
    print('last month: ', gdata[2])
    print('last year: ', gdata[3])


def make_graph():
    gdata = data_backend.get_data_for_graph()
    x = []
    y = []
    for d in gdata:
        y.append(d[1])
        x.append(d[0])

    x.sort()
    y.sort()

    plt.figure(figsize=(14, 8))
    plt.bar(x, y, align='center', width=0.8)
    plt.ylabel('visits', fontsize=17)
    plt.title('websites visits over the last week', fontsize=18)
    fname = 'graph'
    plt.savefig(fname)
    return fname


def make_popular_diagram(sitename):
    gdata = data_backend.get_data_for_diagram(sitename)
    print(gdata)

    p_v = dict()
    visits = []
    for d in gdata:
        if d[1] == 0:
            continue

        if d[0] in p_v:
            p_v[d[0]] = p_v[d[0]] + d[1]
        else:
            p_v[d[0]] = d[1]

    pages = list(p_v)
    for p in pages:
        visits.append(p_v[p])

    fig1, ax1 = plt.subplots()
    ax1.pie(visits, labels=pages, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')

    fname = 'diagram'
    plt.savefig(fname)
    return fname

