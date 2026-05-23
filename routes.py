import json
import os
import re
from datetime import datetime
from bottle import route, view, static_file, request, redirect
import html

DATA_FILE = 'reviews.json'

def load_reviews():
    """Загрузка отзывов из JSON файла"""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_reviews(reviews):
    """Сохранение отзывов в JSON файл"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(reviews, f, ensure_ascii=False, indent=2)

def validate_date(date_str):
    """Проверка корректности даты в формате ДД.ММ.ГГГГ"""
    try:
        datetime.strptime(date_str, '%d.%m.%Y')
        return True
    except ValueError:
        return False

def validate_phone(phone):
    """Проверка телефона в формате +7 (XXX) XXX-XX-XX или +7XXXXXXXXXX"""
    if not phone:  # Телефон не обязательный
        return True
    pattern = r'^\+7\s?(\(?\d{3}\)?\s?)?\d{3}-?\d{2}-?\d{2}$'
    return bool(re.match(pattern, phone))

def validate_author(author):
    """
    Проверка имени автора:
    - Только латиница, цифры и спецсимволы (- _ ')
    - Кириллица запрещена
    """
    if not author:
        return False, "Укажите автора"
    
    if len(author) < 2:
        return False, "Имя слишком короткое (минимум 2 символа)"
    
    if len(author) > 50:
        return False, "Имя слишком длинное (максимум 50 символов)"
    
    if re.search(r'<[^>]+>', author):
        return False, "Имя не должно содержать HTML-теги"
    
    # --- ИЗМЕНЕНИЕ ЗДЕСЬ: Только латиница ---
    pattern = r'^[a-zA-Z0-9\s\-\'_]+$'
    if not re.match(pattern, author):
        return False, "Имя должно содержать только латинские буквы и цифры"
    
    if re.search(r'(.)\1{3,}', author):
        return False, "Имя содержит слишком много повторяющихся символов"
    
    return True, ""

def validate_review_text(text):
    """
    Проверка текста отзыва:
    - Только латиница, цифры, знаки препинания
    - Кириллица запрещена
    - Длина от 10 до 1000 символов
    - Запрещены HTML-теги и скрипты
    - Проверка на спам
    """
    if not text:
        return False, "Введите текст отзыва"
    
    if len(text) < 10:
        return False, "Текст слишком короткий (минимум 10 символов)"
    
    if len(text) > 1000:
        return False, "Текст слишком длинный (максимум 1000 символов)"
    
    if re.search(r'<[^>]+>', text):
        return False, "Текст не должен содержать HTML-теги"
    
    if re.search(r'javascript:', text, re.IGNORECASE):
        return False, "Текст содержит запрещенный контент"
    
    # --- НОВОЕ: Проверка на кириллицу ---
    if re.search(r'[а-яА-ЯёЁ]', text):
        return False, "Текст должен содержать только латинские буквы (кириллица запрещена)"
    
    # Проверка что есть хотя бы одна буква (латинская)
    if not re.search(r'[a-zA-Z]', text):
        return False, "Текст должен содержать латинские буквы"
    # -------------------------------------
    
    if re.search(r'(.)\1{10,}', text):
        return False, "Текст содержит слишком много повторяющихся символов"
    
    letters = re.findall(r'[a-zA-Z]', text)
    if letters:
        uppercase = sum(1 for c in letters if c.isupper())
        if uppercase / len(letters) > 0.7:
            return False, "Текст написан ЗАГЛАВНЫМИ БУКВАМИ"
    
    if re.search(r'https?://|www\.', text):
        return False, "Текст не должен содержать ссылки"
    
    return True, ""

def sanitize_input(text):
    """Очистка ввода от потенциально опасных символов"""
    if text:
        # Экранирование HTML-тегов
        text = html.escape(text)
        # Удаление лишних пробелов
        text = re.sub(r'\s+', ' ', text).strip()
    return text

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static')

@route('/')
@route('/home')
@view('dota')
def home():
    """Renders the home page (Dota)."""
    return dict(
        title='Dota 2 Guide',
        page_style='dota.css',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About Us',
        page_style='about.css',
        year=datetime.now().year
    )

@route('/deadlock')
@view('deadlock')
def deadlock():
    """Renders the deadlock page."""
    return dict(
        title='Deadlock Guide', 
        page_style='deadlock.css',
        year=datetime.now().year
    )

@route('/reviews', method=['GET', 'POST'])
@view('reviews')
def reviews():
    """Страница отзывов с формой добавления"""
    errors = {}
    form_data = {}
    
    if request.method == 'POST':
        # Получаем данные из формы
        form_data = {
            'author': request.forms.get('author', '').strip(),
            'text': request.forms.get('text', '').strip(),
            'date': request.forms.get('date', '').strip(),
            'phone': request.forms.get('phone', '').strip()
        }
        
        # ВАЛИДАЦИЯ ПОЛЕЙ
        
        # Проверка имени автора
        is_valid_author, author_error = validate_author(form_data['author'])
        if not is_valid_author:
            errors['author'] = author_error
        
        # Проверка текста отзыва
        is_valid_text, text_error = validate_review_text(form_data['text'])
        if not is_valid_text:
            errors['text'] = text_error
        
        # Проверка даты
        if not form_data['date']:
            errors['date'] = 'Укажите дату'
        elif not validate_date(form_data['date']):
            errors['date'] = 'Неверный формат даты. Используйте ДД.ММ.ГГГГ'
        
        # Проверка телефона (не обязательный, но если есть - проверяем)
        if form_data['phone'] and not validate_phone(form_data['phone']):
            errors['phone'] = 'Неверный формат телефона. Используйте +7 (XXX) XXX-XX-XX'
        
        # Если ошибок нет, сохраняем отзыв
        if not errors:
            # Очистка данных перед сохранением
            cleaned_data = {
                'author': sanitize_input(form_data['author']),
                'text': sanitize_input(form_data['text']),
                'date': form_data['date'],
                'phone': sanitize_input(form_data['phone'])
            }
            
            reviews_list = load_reviews()
            reviews_list.append(cleaned_data)
            # Сортировка по дате (сначала новые)
            reviews_list.sort(
                key=lambda x: datetime.strptime(x['date'], '%d.%m.%Y'), 
                reverse=True
            )
            save_reviews(reviews_list)
            # Перенаправление для очистки формы
            redirect('/reviews')
    
    # Загружаем отзывы для отображения
    reviews_list = load_reviews()
    # Сортировка при отображении
    reviews_list.sort(
        key=lambda x: datetime.strptime(x['date'], '%d.%m.%Y'), 
        reverse=True
    )
    
    return dict(
        title='Отзывы',
        year=datetime.now().year,
        reviews=reviews_list,
        errors=errors,
        form_data=form_data
    )