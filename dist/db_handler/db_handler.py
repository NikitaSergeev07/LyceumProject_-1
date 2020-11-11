import sqlite3  # Импортировали sqlite3 для работы с этой рсубд

""""Создаем функцию для авторизации пользователя"""


def login(login, passw, signal):
    # Подключаемся к нашей бд и создаем курсор
    con = sqlite3.connect('db_handler/users.db')
    cur = con.cursor()

    # Проверяем есть ли такой пользователь
    cur.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cur.fetchall()

    # Если такой пользователь существует, тогда авторизуем его
    if value != [] and value[0][2] == passw:
        signal.emit('Успешная авторизация!')
    else:
        signal.emit('Проверьте правильность ввода данных!')

    # Закрываем соединение и курсор
    cur.close()
    con.close()


""""Создаем функцию для регистрации пользователя"""


def register(login, passw, signal):
    # Подключаемся к нашей бд и создаем курсор
    con = sqlite3.connect('db_handler/users.db')
    cur = con.cursor()

    # Проверяем есть ли такой пользователь
    cur.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cur.fetchall()

    # Если пользователь с таким ником существует, выводим сообщение
    if value != []:
        signal.emit('Такой ник уже используется!')

    # Если все проверки прошли успешно, регистрируем пользователя, занося его данные в бд
    elif value == []:
        cur.execute(f"INSERT INTO users (name, password) VALUES ('{login}', '{passw}')")
        signal.emit('Вы успешно зарегистрированы!')
        con.commit()

    # Закрываем соединение и курсор
    cur.close()
    con.close()
