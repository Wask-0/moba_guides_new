# -*- coding: utf-8 -*-
"""
Routes and views for the Bottle application.
"""

import json
import os
import re
import html
from datetime import datetime
from bottle import route, view, static_file, request, redirect

# ========== КОНФИГУРАЦИЯ ==========
DATA_FILE = 'reviews.json'
UPDATES_FILE = 'updates.json'
UPLOAD_DIR = 'static/images/updates'
ALLOWED_IMG_EXT = {'.jpg', '.jpeg', '.png', '.webp'}
MAX_IMG_SIZE = 5 * 1024 * 1024  # 5 МБ


# ========== ФУНКЦИИ ДЛЯ ОТЗЫВОВ ==========
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
    except (ValueError, TypeError):
        return False

def validate_phone(phone):
    """Проверка телефона в формате +7 (XXX) XXX-XX-XX или +7XXXXXXXXXX"""
    if not phone:
        return True
    pattern = r'^\+7\s?(\(?\d{3}\)?\s?)?\d{3}-?\d{2}-?\d{2}$'
    return bool(re.match(pattern, phone))

def validate_author(author):
    """Проверка имени автора: только латиница, цифры, спецсимволы"""
    if not author:
        return False, "Укажите автора"
    if len(author) < 2:
        return False, "Имя слишком короткое (минимум 2 символа)"
    if len(author) > 50:
        return False, "Имя слишком длинное (максимум 50 символов)"
    if re.search(r'<[^>]+>', author):
        return False, "Имя не должно содержать HTML-теги"
    
    # Только латиница, цифры, пробелы, дефис, апостроф, подчеркивание
    pattern = r'^[a-zA-Zа-яА-ЯёЁ0-9\s\-\'_]+$'
    if not re.match(pattern, author):
        return False, "Имя должно содержать только латинские буквы и цифры"
    
    # Защита от спама (повторяющиеся символы)
    if re.search(r'(.)\1{3,}', author):
        return False, "Имя содержит слишком много повторяющихся символов"
    
    return True, ""

def validate_review_text(text):
    """Проверка текста отзыва: только латиница, без спама"""
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
    
    
    # Должна быть хотя бы одна латинская буква
    if not re.search(r'[a-zA-Z]', text):
        return False, "Текст должен содержать латинские буквы"
    
    # Защита от спама
    if re.search(r'(.)\1{10,}', text):
        return False, "Текст содержит слишком много повторяющихся символов"
    
    # Проверка CAPS LOCK
    letters = re.findall(r'[a-zA-Z]', text)
    if letters:
        uppercase = sum(1 for c in letters if c.isupper())
        if uppercase / len(letters) > 0.7:
            return False, "Текст написан ЗАГЛАВНЫМИ БУКВАМИ"
    
    # Запрет ссылок
    if re.search(r'https?://|www\.', text):
        return False, "Текст не должен содержать ссылки"
    
    return True, ""

def sanitize_input(text):
    """Очистка ввода от опасных символов"""
    if text:
        text = html.escape(text)
        text = re.sub(r'\s+', ' ', text).strip()
    return text


# ========== ФУНКЦИИ ДЛЯ ОБНОВЛЕНИЙ ==========
def load_updates():
    """Загрузка обновлений из JSON файла"""
    if not os.path.exists(UPDATES_FILE):
        return []
    with open(UPDATES_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_updates(updates):
    """Сохранение обновлений в JSON файл"""
    with open(UPDATES_FILE, 'w', encoding='utf-8') as f:
        json.dump(updates, f, ensure_ascii=False, indent=2)

def validate_update_text(text):
    """Валидация текста обновления (аналогично отзывам)"""
    if not text:
        return False, "Введите текст"
    if len(text) < 10:
        return False, "Минимум 10 символов"
    if len(text) > 1000:
        return False, "Максимум 1000 символов"
    if re.search(r'<[^>]+>|javascript:|https?://|www\.', text):
        return False, "HTML/ссылки запрещены"
    if re.search(r'(.)\1{10,}', text):
        return False, "Слишком много повторов"
    letters = re.findall(r'[a-zA-Z]', text)
    if letters and sum(1 for c in letters if c.isupper()) / len(letters) > 0.7:
        return False, "Текст написан ЗАГЛАВНЫМИ"
    return True, ""

def sanitize_filename(name):
    """Очистка имени файла от опасных символов"""
    name = re.sub(r'[^\w\-\.]', '_', name)
    return re.sub(r'_+', '_', name).strip('_')


# ========== МАРШРУТЫ ==========
@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static')

@route('/')
@route('/home')
@view('dota')
def home():
    """Главная страница (Dota 2 Guide)"""
    return dict(
        title='Dota 2 Guide',
        page_style='dota.css',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Страница Об авторах"""
    return dict(
        title='About Us',
        page_style='about.css',
        year=datetime.now().year
    )

@route('/deadlock')
@view('deadlock')
def deadlock():
    """Страница Deadlock Guide"""
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
        form_data = {
            'author': request.forms.get('author', '').strip(),
            'text': request.forms.get('text', '').strip(),
            'date': request.forms.get('date', '').strip(),
            'phone': request.forms.get('phone', '').strip()
        }
        
        # Валидация
        is_valid_author, author_error = validate_author(form_data['author'])
        if not is_valid_author:
            errors['author'] = author_error
        
        is_valid_text, text_error = validate_review_text(form_data['text'])
        if not is_valid_text:
            errors['text'] = text_error
        
        if not form_data['date']:
            errors['date'] = 'Укажите дату'
        elif not validate_date(form_data['date']):
            errors['date'] = 'Неверный формат даты. Используйте ДД.ММ.ГГГГ'
        
        if form_data['phone'] and not validate_phone(form_data['phone']):
            errors['phone'] = 'Неверный формат телефона. Используйте +7 (XXX) XXX-XX-XX'
        
        # Сохранение если нет ошибок
        if not errors:
            cleaned_data = {
                'author': sanitize_input(form_data['author']),
                'text': sanitize_input(form_data['text']),
                'date': form_data['date'],
                'phone': sanitize_input(form_data['phone'])
            }
            reviews_list = load_reviews()
            reviews_list.append(cleaned_data)
            reviews_list.sort(key=lambda x: datetime.strptime(x['date'], '%d.%m.%Y'), reverse=True)
            save_reviews(reviews_list)
            redirect('/reviews')
    
    reviews_list = load_reviews()
    reviews_list.sort(key=lambda x: datetime.strptime(x['date'], '%d.%m.%Y'), reverse=True)
    
    return dict(
        title='Отзывы',
        year=datetime.now().year,
        reviews=reviews_list,
        errors=errors,
        form_data=form_data
    )

@route('/updates', method=['GET', 'POST'])
@view('updates')
def updates():
    """Страница обновлений с загрузкой изображений"""
    errors = {}
    form_data = {'text': '', 'date': ''}
    
    if request.method == 'POST':
        form_data['text'] = request.forms.get('text', '').strip()
        form_data['date'] = request.forms.get('date', '').strip()
        upload = request.files.get('image')
        
        # Валидация даты
        if not form_data['date'] or not validate_date(form_data['date']):
            errors['date'] = 'Неверный формат даты (ДД.ММ.ГГГГ)'
        
        # Валидация текста
        valid_text, msg_text = validate_update_text(form_data['text'])
        if not valid_text:
            errors['text'] = msg_text
        
        # Обработка изображения
        img_path = None
        if upload and upload.filename:
            _, ext = os.path.splitext(upload.filename)
            if ext.lower() not in ALLOWED_IMG_EXT:
                errors['image'] = 'Только JPG, PNG, WEBP'
            elif upload.content_length > MAX_IMG_SIZE:
                errors['image'] = 'Файл больше 5 МБ'
            else:
                os.makedirs(UPLOAD_DIR, exist_ok=True)
                safe_name = sanitize_filename(upload.filename)
                # Защита от перезаписи
                base, _ = os.path.splitext(safe_name)
                counter = 0
                while os.path.exists(os.path.join(UPLOAD_DIR, safe_name)):
                    safe_name = f"{base}_{counter}{ext}"
                    counter += 1
                
                upload.save(os.path.join(UPLOAD_DIR, safe_name))
                img_path = f'/static/images/updates/{safe_name}'
        else:
            errors['image'] = 'Загрузите изображение'
        
        # Сохранение если нет ошибок
        if not errors:
            try:
                data = load_updates()
                data.append({
                    'date': form_data['date'],
                    'text': sanitize_input(form_data['text']),
                    'image': img_path
                })
                data.sort(key=lambda x: datetime.strptime(x['date'], '%d.%m.%Y'), reverse=True)
                save_updates(data)
        
                redirect('/updates', 303)
        
            except Exception as e:
                errors['save'] = f'Ошибка сохранения: {str(e)}'
                # Остаёмся на форме с ошибкой
    
    updates_list = load_updates()
    updates_list.sort(key=lambda x: datetime.strptime(x['date'], '%d.%m.%Y'), reverse=True)
    
    return dict(
        title='Обновления',
        year=datetime.now().year,
        updates_list=updates_list,
        errors=errors,
        form_data=form_data
    )