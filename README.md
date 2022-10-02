# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

1. Скачайте код
---
2. Установите виртуальное окружение
```angular2html
python - m venv venv
```
и активируйте его
- код для системы Windows
```angular2html
\venv\Scripts\activate.ps1
```
- код для системы Linux
```angular2html
source venv/bin/activate
```
___
3. Установите зависимости
```angular2html
pip install -r requirements.txt
```
___
4. Запустите сайт, в параметре -p передайте путь к файлу с напитками для реализации, в параметре -s передайте имя рабочего листа в Excel файле (по умолчанию передается лист Лист1 в файле wine3.xlsx)
```
python3 main.py -p wine3.xlsx -s Лист1
```
___
5. Образец файла для передачи скрипту

|Категория    | Название | Сорт           | Цена | Картинка    | Акция        |
|:-----------:|:--------:|:--------------:|:----:|:-----------:|:-------------:|
|Белые вина   | Ркацители| Дамский пальчик| 499  |rkaciteli.png|
|Напитки      | Коньяк   |                | 399  |kognac.png   |Выгодное предложение
___
6. Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

