import asyncio
import aiosqlite
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

API_TOKEN = "ВАШ_ТОКЕН"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# Инициализация базы данных
async def init_db():
    async with aiosqlite.connect("tasks.db") as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            task TEXT,
            done INTEGER DEFAULT 0
        )
        """)
        await db.commit()


@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Привет! Я твой помощник.\n\n"
                         "Команды:\n"
                         "/add <дело> — добавить задачу\n"
                         "/list — показать список задач\n"
                         "/done <номер> — отметить задачу выполненной")


@dp.message(Command("add"))
async def add_task(message: types.Message):
    task = message.text.replace("/add", "").strip()
    if not task:
        await message.answer("Напиши задачу после команды /add")
        return

    async with aiosqlite.connect("tasks.db") as db:
        await db.execute("INSERT INTO tasks (user_id, task) VALUES (?, ?)", (message.from_user.id, task))
        await db.commit()

    await message.answer(f"Задача добавлена: {task}")


@dp.message(Command("list"))
async def list_tasks(message: types.Message):
    async with aiosqlite.connect("tasks.db") as db:
        cursor = await db.execute("SELECT id, task, done FROM tasks WHERE user_id = ?", (message.from_user.id,))
        rows = await cursor.fetchall()

    if not rows:
        await message.answer("Список пуст.")
        return

    response = "Список задач:\n"
    for idx, (task_id, task, done) in enumerate(rows, 1):
        status = "✅" if done else "❌"
        response += f"{idx}. {task} {status}\n"

    await message.answer(response)


@dp.message(Command("done"))
async def mark_done(message: types.Message):
    try:
        task_number = int(message.text.replace("/done", "").strip())
    except ValueError:
        await message.answer("Укажи номер задачи после команды /done")
        return

    async with aiosqlite.connect("tasks.db") as db:
        cursor = await db.execute("SELECT id FROM tasks WHERE user_id = ?", (message.from_user.id,))
        rows = await cursor.fetchall()

        if 0 < task_number <= len(rows):
            task_id = rows[task_number - 1][0]
            await db.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
            await db.commit()
            await message.answer(f"Задача №{task_number} отмечена как выполненная ✅")
        else:
            await message.answer("Такой задачи нет.")


async def main():
    await init_db()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
