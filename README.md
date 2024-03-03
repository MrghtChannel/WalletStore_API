# Мій проект

Це API для застосунку та сайту WalletStore. На даний момент триває розробка магазину застосунків для Android (можливо, також для IOS).

## Встановлення

1. Клонуйте репозиторій на комп'ютер.
2. Встановіть бібліотеки Flask та psycopg2.

    ```
    pip install Flask
    pip install psycopg2
    ```

3. Запустіть проект командою `python main.py`.

## Використані технології

У цьому проекті я використовую:
- Мову програмування Python, [python.org](https://www.python.org/).
- Базу даних [PostgreSQL](https://www.postgresql.org/).
- Інструмент для роботи з базами даних [DBeaver](https://dbeaver.io/).
- Пакетний менеджер Python, [pypi.org](https://pypi.org/).

## Ліцензія

Цей проект ліцензований під [MIT License](https://github.com/MrghtChannel/WalletStore_API/blob/main/LICENSE).

![1](https://github.com/MrghtChannel/WalletStore_API/blob/main/img/1.png)
![2](https://github.com/MrghtChannel/WalletStore_API/blob/main/img/2.png)
![3](https://github.com/MrghtChannel/WalletStore_API/blob/main/img/3.png)


## Оновлення

Слідкуйте за [оновленнями](https://github.com/MrghtChannel/WalletStore_API/releases)

```sql
CREATE TABLE IF NOT EXISTS applications (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    version VARCHAR(50),
    type VARCHAR(50),
    status VARCHAR(50),
    age_restriction INT,
    author VARCHAR(255),
    apk VARCHAR(255),
    icon VARCHAR(255),
    banner1 VARCHAR(255),
    banner2 VARCHAR(255),
    banner3 VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS browser_assets (
    id SERIAL PRIMARY KEY,
    browser VARCHAR(255),
    asset VARCHAR(255),
    description TEXT,
    icon VARCHAR(255),
    banner1 VARCHAR(255),
    banner2 VARCHAR(255),
    banner3 VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS ios_applications (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    version VARCHAR(50),
    status VARCHAR(50),
    age_restriction INT,
    author VARCHAR(255),
    ipa VARCHAR(255),
    icon VARCHAR(255),
    banner1 VARCHAR(255),
    banner2 VARCHAR(255),
    banner3 VARCHAR(255)
);

