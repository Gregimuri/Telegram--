# Telegram Bot "Личный помощник"

Простой Telegram-бот для управления личными задачами.  
Реализован на **Python + aiogram 3 + SQLite**.  

---

## ✨ Возможности
- `/add <дело>` — добавить задачу  
- `/list` — показать список задач  
- `/done <номер>` — отметить задачу выполненной  

---

## 🚀 Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/Gregimuri/telegram-helper-bot.git
cd telegram-helper-bot
```

### 2. Создать виртуальное окружение (рекомендуется)

```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Создать бота в Telegram

1. Открыть **@BotFather**  
2. Выполнить команду `/newbot`  
3. Скопировать **API Token**  

### 5. Запустить бота

В файле `bot.py` вставить свой токен:

```python
API_TOKEN = "ВАШ_ТОКЕН"
```

Запустить:

```bash
python bot.py
```

---

## 🛠 Технологии
- Python 3.10+  
- [aiogram 3](https://docs.aiogram.dev/)  
- SQLite (через aiosqlite)  

---

## 📸 Пример работы

```
/add Купить хлеб  
-> Задача добавлена: Купить хлеб  

/list  
-> 1. Купить хлеб ❌  

/done 1  
-> Задача №1 отмечена как выполненная ✅
```

---

## 👨‍💻 Автор

Титков Григорий Ильич  
[GitHub](https://github.com/Gregimuri)  
