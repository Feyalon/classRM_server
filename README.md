<ul>
    <h1>
        API:
    </h1>
    <li>
        admin/ - Админка
    </li>
    <li>
        api/users/ - Авторизация, регистрация и тому подобное (после users/ добавляете /login - для авторизация с боди и методом постом, /register - для регистрации с боди и методом постом, /logout тоже так же и только /user - это гет запрос без никакого боди)
        <p>
            Что должно быть в боди:
                "username": "test",
                "email": "test@gmail.com",
                "password": "test123"
        </p>
    </li>
    <li>
        api/leads - Клиенты
    </li>
</ul>
<h2>
    Как запустить сервак:
</h2>
<ul>
    <li>
        Запуск виртуалки с консоли:
            cd venv 
            Scripts/Activate
    </li>
    <li>
        Запуск сервера тоже с консоли:
            python manage.py runserver
    </li>
</ul>