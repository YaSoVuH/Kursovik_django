# Работоспособность данной инструкции была проверена на Windows 10 и python 3.12.0

# Запуск проекта персолнально для компьютера (PAN):

## Шаг 1:
    python -m venv .venv

## Шаг 2:
    .\.venv\Scripts\activate

## Шаг 3:
    python -r requirements.txt

## Шаг 4:
    cd siteforkursovik

## Шаг 5:
    python manage.py runserver

## Шаг 6:
    Пройти в браузере по адерсу: 127.0.0.1:8000

# Запуск проекта (LAN):

## Шаг 1:
    python -m venv .venv

## Шаг 2:
    .\.venv\Scripts\activate

## Шаг 3:
    python -r requirements.txt

## Шаг 4:
    cd siteforkursovik

## Шаг 5:
    Зайти в settings.py в папке siteforkursovik
    В листе ALLOWED_HOSTS, добавить IPv4-адрес (хоста), который можно узнать в консоле при вводе команды ipconfig

## Шаг 6:
    python manage.py runserver 0.0.0.0:8000
    Разрешить работу в брандмауэр'e

## Шаг 6:
    На устройстве в одной сети пройти в браузере по адерсу:
    {IPv4-адрес}:8000

# Выход из виртуальной среды:
    deactivate

![Выдра на последок](https://i.imgur.com/Ua7ARDP.png)