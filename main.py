from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

import datetime
import pandas
import collections
import argparse


def correct_years(year):
    for_year = [2, 3, 4]
    for_years = [12, 13, 14]
    if (year % 10 == 1) and (year % 100 != 11):
        return "год"
    elif (year % 10 in for_year) and (year % 100 not in for_years):
        return "года"
    else:
        return 'лет'


def main():
    foundation_year = 1920
    now = datetime.datetime.now().year
    winery_age = now - foundation_year

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    parser = argparse.ArgumentParser(
        description='Сайт производителей вина и других напитков'
    )
    parser.add_argument('-p', '--path', help='Путь в файлу с данными', default='wine_for_sale.xlsx')
    parser.add_argument('-s', '--sheet', help='Название рабочего листа', default='Лист1')
    args = parser.parse_args()

    excel_data = pandas.read_excel(args.path, sheet_name=args.sheet, na_values=None, keep_default_na=False)
    all_wines = excel_data.to_dict(orient='records')
    all_wines_by_categories = collections.defaultdict(list)

    for category in all_wines:
        all_wines_by_categories[category['Категория']].append(category)

    template = env.get_template('template.html')

    rendered_page = template.render(
        age=winery_age,
        correct_word=correct_years(winery_age),
        wines=all_wines_by_categories,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
