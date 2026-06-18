# 🛒 Мой Магазин

Простое веб-приложение на Flask с вёрсткой на Bootstrap.

---

## 🚀 Запуск

```bash
# 1. Клонировать репозиторий
git clone https://github.com/ваш-username/homework_21.2.git
cd homework_21.2

# 2. Создать виртуальное окружение
python -m venv venv

# 3. Активировать (Windows)
venv\Scripts\activate
# или (Mac/Linux)
source venv/bin/activate

# 4. Установить зависимости
pip install -r requirements.txt

# 5. Запустить
python app.py

Открыть в браузере: http://localhost:5000

📁 Структура
text
project/
├── app.py              # Flask-приложение
├── requirements.txt    # Зависимости
├── .gitignore          # Игнорируемые файлы
└── templates/
    ├── index.html      # Главная страница
    ├── contacts.html   # Контакты + форма
    ├── 404.html        # Ошибка 404
    └── 500.html        # Ошибка 500


⚡ Что делает приложение
Страница	Метод	Что делает
/	GET	Показывает главную с товарами
/contacts	GET	Показывает форму контактов
/contacts	POST	Принимает данные, выводит в консоль
Любая другая	GET	Показывает страницу 404


🛠 Технологии
Python 3 + Flask
Bootstrap 5 (CDN)
HTML + CSS


✅ Выполненные требования
Header, main, footer
Bootstrap для вёрстки
Страница "Контакты" с формой
POST-запрос выводит данные в консоль
Обработка ошибок 404 и 500
.gitignore со всеми элементами