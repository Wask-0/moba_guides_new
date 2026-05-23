<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/static/content/main.css">
    <link rel="stylesheet" href="/static/content/updates.css">
</head>
<body>
    <div class="page-wrapper bg-dota">
        <!-- Навигация -->
        <div class="side-nav-fixed">
            <a href="/home" class="nav-btn">Дота</a>
            <a href="/deadlock" class="nav-btn secondary">Дедлок</a>
            <a href="/about" class="nav-btn tertiary">Об авторах</a>
            <a href="/reviews" class="nav-btn reviews">Отзывы</a>
            <a href="/updates" class="nav-btn secondary">Обновления</a>
        </div>

        <h1 class="main-title text-center mb-5">Обновления</h1>

        <div class="row justify-content-center">
            <div class="col-lg-8">
                
                <!-- Список обновлений -->
                %if updates_list:
                %for u in updates_list:
                <div class="review-card">
                    <div class="review-date">📅 {{u['date']}}</div>
                    %if u.get('image'):
                    <img src="{{u['image']}}" class="update-image mb-3" alt="Update" style="width:100%; max-height:300px; object-fit:cover; border-radius:5px;">
                    %end
                    <div class="review-text">{{u['text']}}</div>
                </div>
                %end
                %else:
                <div class="empty-state"><p>📭 Нет обновлений</p></div>
                %end

                <!-- Форма -->
                <div class="form-section">
                    <h2 class="text-center mb-4">Добавить обновление</h2>
                    <form method="POST" action="/updates" enctype="multipart/form-data">
                        <div class="mb-3">
                            <label class="form-label">Изображение</label>
                            <input type="file" class="form-control" name="image" accept="image/*">
                            %if 'image' in errors:
                            <div class="error-message">{{errors['image']}}</div>
                            %end
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Текст *</label>
                            <textarea class="form-control" name="text" rows="4" placeholder="Описание обновления...">{{form_data.get('text', '')}}</textarea>
                            %if 'text' in errors:
                            <div class="error-message">{{errors['text']}}</div>
                            %end
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Дата (ДД.ММ.ГГГГ) *</label>
                            <input type="text" class="form-control" name="date" placeholder="21.05.2026" value="{{form_data.get('date', '')}}">
                            %if 'date' in errors:
                            <div class="error-message">{{errors['date']}}</div>
                            %end
                        </div>
                        <div class="text-center mt-4">
                            <button type="submit" class="btn-submit">📤 Опубликовать</button>
                        </div>
                    </form>
                </div>

            </div>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>