# Bot для Сервиса BakeCake

Сайт и Бот позволяет создавать заказы на торты, просматривать свои заказы. 
На сайте в админ панели можно добавлять в галерею новые торты, просматривать заказы. 
В боте можно просматривать заказы, делать рекламную рассылку, например по акциям. 

### Как установить

* Скачать [этот script](https://github.com/miazigoo/BakeCake)

**Python3 уже должен быть установлен**. 
Используйте `pip` (или `pip3`, если возникает конфликт с Python2) для установки зависимостей:
```sh
pip install -r requirements.txt
```
Создайте базу данных SQLite:

```sh
python manage.py makemigrations
python manage.py migrate
```

### Если хотите работать с админ панелью:

Создайте супер пользователя (администратора) командой:
```sh
python manage.py createcuperuser
```

Запустить сервер:
```sh
python manage.py runserver
```
1. Перейти по ссылке [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) или [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


### Как запустить:

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.
Доступны 4 переменные:
- `TELEGRAM_BOT_API_KEY` — Получите токен у [@BotFather](https://t.me/BotFather), вставте в `.env` например: `TELEGRAM_BOT_API_KEY=588535421721:AAFYtrO5YJhpUEXgyw6r1tr5fqZYY8ogS45I2E`.
- `TELEGRAM_ADMIN_ID` - Получите свой ID у [@userinfobot](https://t.me/userinfobot)
- `U_KASSA_TOKEN` -Токен ЮКАССА [Получить](https://yookassa.ru/docs/support/merchant/payments/implement/test-store#how-to-add-a-test-store)
- `ACCOUT_ID` - ID магазина на ЮКАССА [Получить](https://yookassa.ru/docs/support/merchant/payments/implement/test-store#how-to-add-a-test-store)

Запуск производится командой: 
```sh
python manage.py bot
```


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).