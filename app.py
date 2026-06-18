from flask import Flask, request, render_template, abort
import os

app = Flask(__name__)


# ===== ОБРАБОТЧИК ГЛАВНОЙ СТРАНИЦЫ =====
@app.route('/')
def index():
    """Возвращает главную страницу"""
    return render_template('index.html')


# ===== ЗАДАНИЕ 2: СТРАНИЦА "КОНТАКТЫ" =====
@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    """
    GET — возвращает страницу контактов
    POST — принимает данные формы и выводит в консоль
    """
    if request.method == 'POST':
        # Читаем данные из формы
        name = request.form.get('name', 'Не указано')
        email = request.form.get('email', 'Не указано')
        message = request.form.get('message', 'Не указано')

        # Выводим в консоль (это требование задания)
        print("=" * 50)
        print("📩 НОВОЕ СООБЩЕНИЕ С САЙТА")
        print(f"Имя: {name}")
        print(f"Email: {email}")
        print(f"Сообщение: {message}")
        print("=" * 50)

        # Можно вернуть страницу с уведомлением об успехе
        return render_template('contacts.html', success=True)

    # GET-запрос — просто показываем страницу
    return render_template('contacts.html')


# ===== ОБРАБОТКА ОШИБОК =====
@app.errorhandler(404)
def page_not_found(e):
    """Кастомная страница для ошибки 404"""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    """Кастомная страница для ошибки 500"""
    return render_template('500.html'), 500


# ===== ЗАПУСК =====
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)