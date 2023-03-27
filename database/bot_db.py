import random
import sqlite3


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute("CREATE TABLE IF NOT EXISTS anketa "
               "(username VARCHAR (100), "
               "name VARCHAR (100), "
               "age INTEGER, "
               "direction VARCHAR (100), "
               "group_mentor INTEGER )")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO anketa VALUES (?, ?, ?, ?, ?, ? , ? )",
                       tuple(data.values()))
        db.commit()


async def sql_command_random():
    random_user = cursor.execute("SELECT * FROM anketa ORDER BY random()").fetchone()
    return random_user


async def sql_command_all():
    return cursor.execute("SELECT * FROM anketa").fetchall()


async def sql_command_delete(id):
    cursor.execute("DELETE FROM anketa WHERE id = ?", (id,))
    db.commit()


async def sql_command_get_id_name():
    return cursor.execute("SELECT id, name FROM anketa").fetchall()