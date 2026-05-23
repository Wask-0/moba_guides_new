<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/static/content/main.css">
    <link rel="stylesheet" href="/static/content/updates.css">
</head>
<body>
    <div class="page-wrapper bg-dota">
        <div class="top-nav-fixed">
            <a href="/home" class="nav-btn">Дота</a>
            <a href="/deadlock" class="nav-btn secondary">Дедлок</a>
            <a href="/about" class="nav-btn tertiary">Об авторах</a>
            <a href="/reviews" class="nav-btn reviews">💬 Отзывы</a>
            <a href="/updates" class="nav-btn updates">🔄 Обновления</a>
        </div>

        <div class="container pt-4">
            <div class="text-center mb-5">
                <h1 class="main-title dota-title-shift">{{ title }}</h1>
                <div class="accent-line line-orange"></div>
            </div>

            <div class="row justify-content-center">
                <div class="col-lg-8">
                    <div class="card game-card">
                        <div class="card-h-dark-cyan"><h4 class="m-0"><strong></strong> Добавить обновление</h4></div>
                        <div class="card-body-p">
                            <form method="POST" action="/updates" enctype="multipart/form-data">
                                <div class="mb-3">
                                    <label class="form-label">Изображение *</label>
                                    <input type="file" class="form-control" name="image" accept="image/*">
                                    %if 'image' in errors: <div class="error-message">{{errors['image']}}</div> %end
                                </div>
                                <div class="mb-3">
                                    <label class="form-label">Текст *</label>
                                    <textarea class="form-control" name="text" rows="4" placeholder="Описание обновления...">{{form_data.get('text', '')}}</textarea>
                                    %if 'text' in errors: <div class="error-message">{{errors['text']}}</div> %end
                                </div>
                                <div class="mb-3">
                                    <label class="form-label">Дата (ДД.ММ.ГГГГ) *</label>
                                    <input type="text" class="form-control" name="date" placeholder="21.05.2026" value="{{form_data.get('date', '')}}">
                                    %if 'date' in errors: <div class="error-message">{{errors['date']}}</div> %end
                                </div>
                                <div class="text-center"><button type="submit" class="btn-submit">📤 Опубликовать</button></div>
                            </form>
                        </div>
                    </div>

                    <div class="mt-4">
                        %if updates_list:
                            %for u in updates_list:
                                <div class="card game-card update-card mb-3">
                                    <div class="row g-0">
                                        <div class="col-md-4">
                                            <img src="{{u['image']}}" class="img-fluid rounded-start update-img" alt="Update">
                                        </div>
                                        <div class="col-md-8">
                                            <div class="card-body">
                                                <div class="update-date">📅 {{u['date']}}</div>
                                                <p class="update-text">{{u['text']}}</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            %end
                        %else:
                            <div class="text-center text-secondary p-4">📭 Нет обновлений</div>
                        %end
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
