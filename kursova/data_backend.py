import datetime
import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from sqlalchemy import ForeignKey


Base = declarative_base()


class WebSite(Base):
    __tablename__ = "websites"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Page(Base):
    __tablename__ = "pages"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    website_id = Column(Integer, ForeignKey(WebSite.id))


class WebsiteVisit(Base):
    __tablename__ = "website_visits"
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    visits = Column(Integer)
    website_id = Column(Integer, ForeignKey(WebSite.id))


class PageVisit(Base):
    __tablename__ = "page_visits"
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    visits = Column(Integer)
    page_id = Column(Integer, ForeignKey(Page.id))


DATABASE_URI = 'postgres+psycopg2://postgres:postgresServer@localhost:5432/websiteDatabase'

engine = create_engine(DATABASE_URI)

# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


def website_exists(idd):
    s = Session()
    res = s.query(exists().where(WebSite.id == idd)).scalar()
    s.close()

    return res


def website_exists_by_name(wname):
    s = Session()
    res = s.query(exists().where(WebSite.name == wname)).scalar()
    s.close()

    return res


def page_exists(idd):
    s = Session()
    res = s.query(exists().where(Page.id == idd)).scalar()
    s.close()

    return res


def page_exists_by_name(pname):
    s = Session()
    res = s.query(exists().where(Page.name == pname)).scalar()
    s.close()

    return res


def websitevisit_exists(idd):
    s = Session()
    res = s.query(exists().where(WebsiteVisit.id == idd)).scalar()
    s.close()

    return res


def pagevisit_exists(idd):
    s = Session()
    res = s.query(exists().where(PageVisit.id == idd)).scalar()
    s.close()

    return res


def add_website(w_id, w_name):
    s = Session()

    obj = WebSite(
        id = w_id,
        name = w_name
    )

    s.add(obj)
    s.commit()

    s.close()


def add_page(p_id, p_name, web_id):
    s = Session()

    obj = Page(
        id = p_id,
        name = p_name,
        website_id = web_id
    )

    s.add(obj)
    s.commit()

    s.close()


def add_websitevisit(w_id, wdate, wvisit, wwid):
    s = Session()

    obj = WebsiteVisit(
        id = w_id,
        date = wdate,
        visits = wvisit,
        website_id = wwid
    )

    s.add(obj)
    s.commit()

    s.close()


def add_pagevisit(pId, pdate, pvis, ppid):
    s = Session()

    obj = PageVisit(
        id = pId,
        date = pdate,
        visits = pvis,
        page_id = ppid
    )

    s.add(obj)
    s.commit()

    s.close()


def get_site_id(sitename):
    con = psycopg2.connect(host="localhost", database="websiteDatabase", user="postgres")

    cur = con.cursor()

    cur.execute("select id from websites where name = (%s)", (sitename,))

    rows = cur.fetchall()
    siteId = rows[0][0]

    cur.close()
    con.close()

    return siteId


def get_site_data_for_counter(sitename):
    siteId = get_site_id(sitename)

    date_from = datetime.date.today()
    counter_array = []

    counter_array.append(get_yesterday_data(date_from, siteId))
    counter_array.append(get_week_data(date_from, siteId))
    counter_array.append(get_month_data(date_from, siteId))
    counter_array.append(get_year_data(date_from, siteId))

    return counter_array


def get_yesterday_data(date_from, siteId):
    custom_day = date_from.day - 1
    custom_month = date_from.month
    if custom_day == 0:
        custom_month = custom_month - 1
        custom_day = 29
    date_yesterday = datetime.date(date_from.year, custom_month, custom_day)
    con = psycopg2.connect(host="localhost", database="websiteDatabase", user="postgres")

    cur = con.cursor()

    cur.execute("select visits from website_visits where website_id = (%s) and date = (%s)", (siteId, date_yesterday))

    rows = cur.fetchall()

    number = 0
    if len(rows) != 0:
        for r in rows:
            number = number + r[0]

    cur.close()
    con.close()

    return number


def get_week_data(date_from, siteId):
    custom_day = date_from.day - 8
    custom_month = date_from.month
    if custom_day == 0:
        custom_month = custom_month - 1
        custom_day = 29
    elif custom_day < 0:
        custom_month = custom_month - 1
        custom_day = 29 + custom_day
    date_last_week = datetime.date(date_from.year, custom_month, custom_day)
    con = psycopg2.connect(host="localhost", database="websiteDatabase", user="postgres")

    cur = con.cursor()

    cur.execute("select visits from website_visits where website_id = (%s) and date > (%s) and date < (%s)", (siteId, date_last_week, date_from))

    rows = cur.fetchall()

    number = 0
    if len(rows) != 0:
        for r in rows:
            number = number + r[0]

    cur.close()
    con.close()

    return number


def get_month_data(date_from, siteId):
    custom_month = date_from.month - 1
    if custom_month == 0:
        custom_month = 12
    date_last_month = datetime.date(date_from.year, custom_month, date_from.day)
    con = psycopg2.connect(host="localhost", database="websiteDatabase", user="postgres")

    cur = con.cursor()

    cur.execute("select visits from website_visits where website_id = (%s) and date > (%s) and date < (%s)",
                (siteId, date_last_month, date_from))

    rows = cur.fetchall()

    number = 0
    if len(rows) != 0:
        for r in rows:
            number = number + r[0]

    cur.close()
    con.close()

    return number


def get_year_data(date_from, siteId):
    custom_year = date_from.year - 1
    date_last_year = datetime.date(custom_year, date_from.month, date_from.day)
    con = psycopg2.connect(host="localhost", database="websiteDatabase", user="postgres")

    cur = con.cursor()

    cur.execute("select visits from website_visits where website_id = (%s) and date > (%s) and date < (%s)",
                (siteId, date_last_year, date_from))

    rows = cur.fetchall()

    number = 0
    if len(rows) != 0:
        for r in rows:
            number = number + r[0]

    cur.close()
    con.close()

    return number


def get_data_for_diagram(sitename):
    siteId = get_site_id(sitename)

    con = psycopg2.connect(host="localhost", database="websiteDatabase", user="postgres")

    cur = con.cursor()

    cur.execute("select name, visits from pages cross join page_visits where pages.id = page_visits.page_id and "
                "website_id = (%s)", (siteId,))

    rows = cur.fetchall()
    data_arr = []

    if len(rows) != 0:
        for r in rows:
            data_arr.append((r[0], r[1]))

    cur.close()
    con.close()

    return data_arr


def get_data_for_graph():
    date_from = datetime.date.today()
    custom_day = date_from.day - 8
    custom_month = date_from.month
    if custom_day == 0:
        custom_month = custom_month - 1
        custom_day = 29
    elif custom_day < 0:
        custom_month = custom_month - 1
        custom_day = 29 + custom_day
    date_last2week = datetime.date(date_from.year, custom_month, custom_day)

    con = psycopg2.connect(host="localhost", database="websiteDatabase", user="postgres")

    cur = con.cursor()

    cur.execute("select name, visits from websites, website_visits where website_id = websites.id and date > ("
                "%s) and date < (%s)",
                (date_last2week, date_from))

    rows = cur.fetchall()
    data_arr = []

    if len(rows) != 0:
        for r in rows:
            data_arr.append((r[0], r[1]))

    cur.close()
    con.close()

    return data_arr

