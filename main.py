from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

import datetime

year_of_start = 1920
now = datetime.datetime.now().strftime('%Y')
age_of_winery = int(now) - 2015

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)


def correct_years(year):
    goda = [2, 3, 4]
    negoda = [12, 13, 14]
    if (year % 10 == 1) and (year % 100 != 11):
        return "год"
    elif (year % 10 in goda) and (year % 100 not in negoda):
        return "года"
    else:
        return 'лет'


template = env.get_template('template.html')

rendered_page = template.render(
    age=age_of_winery,
    correct_word=correct_years(age_of_winery)
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
