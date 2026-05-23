<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/static/content/main.css">
    <link rel="stylesheet" href="/static/content/reviews.css">
</head>
<body>
    <div class="page-wrapper">
        <!-- Навигация -->
        <div class="top-nav-fixed">
            <div class="container">
                <div class="text-center">
                    <a href="/home" class="nav-btn">Дота</a>
                    <a href="/deadlock" class="nav-btn secondary">Дедлок</a>
                    <a href="/about" class="nav-btn tertiary">Об авторах</a>
                    <a href="/reviews" class="nav-btn quaternary">Отзывы</a>
                </div>
            </div>
        </div>

        <div class="container">
            <!-- Заголовок страницы -->
            <h1 class="main-title text-center mb-5">Отзывы игроков</h1>

            <!-- Список отзывов -->
            <div class="row justify-content-center">
                <div class="col-md-10">
                    %if reviews:
                        %for review in reviews:
                            <div class="review-card">
                                <div class="d-flex justify-content-between align-items-start flex-wrap">
                                    <div>
                                        <div class="review-author">👤 {{review['author']}}</div>
                                        <div class="review-date">📅 {{review['date']}}</div>
                                    </div>
                                    %if review.get('phone'):
                                        <div class="review-phone">📞 {{review['phone']}}</div>
                                    %end
                                </div>
                                <div class="review-text">
                                    {{review['text']}}
                                </div>
                            </div>
                        %end
                    %else:
                        <div class="empty-state">
                            <p>📭 Пока нет отзывов. Будьте первым!</p>
                        </div>
                    %end
                </div>
            </div>

            <!-- Форма добавления отзыва -->
            <div class="row justify-content-center">
                <div class="col-md-10">
                    <div class="form-section">
                        <h2 class="text-center mb-4">Добавить отзыв</h2>
                        <form method="POST" action="/reviews">
                            <!-- Поле Автор -->
                            <div class="mb-3">
                                <label for="author" class="form-label">Автор (Имя/Ник) *</label>
                                <input type="text" 
                                       class="form-control" 
                                       id="author" 
                                       name="author" 
                                       value="{{form_data.get('author', '')}}" 
                                       placeholder="Введите ваше имя или ник">
                                %if 'author' in errors:
                                    <div class="error-message">{{errors['author']}}</div>
                                %end
                            </div>
                            
                            <!-- Поле Текст -->
                            <div class="mb-3">
                                <label for="text" class="form-label">Текст отзыва *</label>
                                <textarea class="form-control" 
                                          id="text" 
                                          name="text" 
                                          rows="4" 
                                          placeholder="Напишите ваш отзыв">{{form_data.get('text', '')}}</textarea>
                                %if 'text' in errors:
                                    <div class="error-message">{{errors['text']}}</div>
                                %end
                            </div>
                            
                            <!-- Дата и Телефон в одной строке -->
                            <div class="row">
                                <div class="col-md-6 mb-3">
                                    <label for="date" class="form-label">Дата (ДД.ММ.ГГГГ) *</label>
                                    <input type="text" 
                                           class="form-control" 
                                           id="date" 
                                           name="date" 
                                           value="{{form_data.get('date', '')}}" 
                                           placeholder="21.05.2026">
                                    %if 'date' in errors:
                                        <div class="error-message">{{errors['date']}}</div>
                                    %end
                                </div>
                                
                                <div class="col-md-6 mb-3">
                                    <label for="phone" class="form-label">Телефон (+7 format)</label>
                                    <input type="text" 
                                           class="form-control" 
                                           id="phone" 
                                           name="phone" 
                                           value="{{form_data.get('phone', '')}}" 
                                           placeholder="+7 (999) 999-99-99">
                                    %if 'phone' in errors:
                                        <div class="error-message">{{errors['phone']}}</div>
                                    %end
                                </div>
                            </div>
                            
                            <!-- Кнопка отправки -->
                            <div class="text-center mt-4">
                                <button type="submit" class="btn-submit">
                                    📤 Разместить отзыв
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap JS (опционально) -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>