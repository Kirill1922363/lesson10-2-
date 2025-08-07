from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Головна сторінка</h1>
    <p>Вітаємо на нашому сайті ITpro!</p>
    <ul>
        <li><a href="/">Головна</a></li>
        <li><a href="/about/">Про нас</a></li>
        <li><a href="/services/">Послуги</a></li>
        <li><a href="/contact/">Контакти</a></li>
    </ul>
    '''

@app.route('/about/')
def about():
    return '''
    <h1>Про нас</h1>
    <p>Наша компанія працює з 2020 року.</p>
    <p>Ми надаємо якісні послуги для наших клієнтів.</p>
    <ul>
        <li><a href="/">Головна</a></li>
        <li><a href="/about/">Про нас</a></li>
        <li><a href="/services/">Послуги</a></li>
        <li><a href="/contact/">Контакти</a></li>
    </ul>
    '''

@app.route('/services/')
def services():
    return '''
    <h1>Наші послуги</h1>
    <p>Ми пропонуємо:</p>
    <ul>
        <li>Machine Learning</li>
        <li>Web Development</li>
        <li>GameDev</li>
    </ul>
    <p><a href="/">Назад на головну</a></p>
    '''

@app.route('/contact/')
def contact():
    return '''
    <h1>Контакти</h1>
    <p>Зв'яжітеся з нами:</p>
    <p>Телефон: +380 68 333 33 33</p>
    <p>Email: info@example.com</p>
    <p>Адреса: м. Київ, вул. Хрещатик</p>
    <p><a href="/">Назад на головну</a></p>
    '''

if __name__ == '__main__':
    app.run(debug=True)