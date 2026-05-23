<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Dota 2 Guide</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="/static/content/main.css">
</head>
<body>
    <div class="page-wrapper bg-dota">
        <!-- Кнопки навигации -->
        <div class="top-nav-fixed">
            <a href="/" class="nav-btn">Дота</a>
            <a href="/deadlock" class="nav-btn secondary">Дедлок</a>
            <a href="/about" class="nav-btn tertiary">Об авторах</a>
            <a href="/reviews" class="nav-btn reviews">Отзывы</a>
            <a href="/updates" class="nav-btn secondary">Обновления</a>
        </div>

        <div class="container pt-4">
            <!-- Заголовок  -->
            <div class="text-center mb-5">
                <h1 class="main-title dota-title-shift">Dota 2</h1>
                <div class="accent-line line-orange"></div>
            </div>

            <div class="row justify-content-center">
                <div class="col-lg-8">
                    
                    <!-- БЛОК 1: ЦЕЛЬ ИГРЫ -->
                    <div class="card game-card">
                        <div class="card-h-orange">
                            <h4 class="m-0"><strong>🏆</strong> Цель игры</h4>
                        </div>
                        <div class="card-body-p">
                            <p class="desc-text">
                                Ваша главная задача — разрушить <strong class="highlight-orange">Древний (Ancient)</strong> на базе врага. 
                                Это большое здание в центре вражеской базы, защищенное башнями и героями.
                            </p>
                            <div class="text-center mt-4">
                                <ul class="list-unstyled list-style-custom">
                                    <li class="mb-2">✅ <strong>Last Hit:</strong> Добивайте крипов</li>
                                    <li class="mb-2">✅ <strong>Фарм:</strong> Копите золото</li>
                                    <li class="mb-2">✅ <strong>Айтемы:</strong> Покупайте предметы</li>
                                    <li class="mb-2">✅ <strong>Пуш:</strong> Ломайте башни</li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <!-- БЛОК 2: РОЛИ ГЕРОЕВ -->
                    <div class="card game-card">
                        <div class="card-h-dark-orange">
                            <h4 class="m-0"><strong>⚔️</strong> Роли героев</h4>
                        </div>
                        <div class="card-body-p">
                            <p class="desc-text">В команде 5 человек, у каждого своя задача:</p>
                            
                            <div class="role-container role-pos1">
                                <h5 class="highlight-orange role-title">Керри (Pos 1)</h5>
                                <p class="role-text">Главный урон команды. Слаб в начале, но становится машиной для убийств к 40-й минуте.</p>
                            </div>
                            
                            <div class="role-container role-pos2">
                                <h5 class="highlight-cyan role-title">Мидер (Pos 2)</h5>
                                <p class="role-text">Играет на центральной линии. Быстро качается и контролирует темп игры.</p>
                            </div>

                            <div class="role-container role-pos3">
                                <h5 class="highlight-orange role-title">Оффлейнер (Pos 3)</h5>
                                <p class="role-text">Инициатор драк. Часто танкует урон и начинает сражения.</p>
                            </div>

                            <div class="role-container role-pos4">
                                <h5 class="highlight-cyan role-title">Саппорты (4 & 5)</h5>
                                <p class="role-text">Помогают керри, покупают варды, лечат и спасают команду.</p>
                            </div>
                        </div>
                    </div>

                    <!-- БЛОК 3: СОВЕТЫ -->
                    <div class="card game-card">
                        <div class="card-h-dark-cyan">
                            <h4 class="m-0"><strong>💡</strong> Советы для старта</h4>
                        </div>
                        <div class="card-body-p text-start">
                            <ol class="desc-text ps-5">
                                <li class="mb-3"><strong class="highlight-orange">Last Hit:</strong> Старайтесь добивать крипов своим ударом, чтобы получить золото.</li>
                                <li class="mb-3"><strong class="highlight-orange">Мини-карта:</strong> Смотрите на неё каждые 5 секунд! Если не видите врагов — они могут быть рядом.</li>
                                <li class="mb-3"><strong class="highlight-orange">Предметы:</strong> Не выходите из дома без покупки. Всегда тратьте золото на полезные айтемы.</li>
                                <li class="mb-3"><strong class="highlight-orange">Психология:</strong> Не тильтуйте. Ошибаются все. Учитесь на поражениях и mute токсичных игроков.</li>
                            </ol>
                        </div>
                    </div>

                    <!-- БЛОК 4: РЕСУРСЫ (Вертикально как на скрине) -->
                    <div class="card game-card">
                        <div class="card-body-p">
                            <h4 class="highlight-orange mb-4">📚 Полезные ресурсы</h4>
                            <p class="desc-text">Хотите прокачать скилл быстрее? Используйте эти сайты:</p>
                            
                            <a href="https://dotabuff.com" target="_blank" class="text-decoration-none">
                                <div class="resource-box mb-3">
                                    <h5 class="res-title-teal">Dotabuff</h5>
                                    <p class="res-text">Статистика героев</p>
                                </div>
                            </a>
                            
                            <a href="https://ru.wikidota.com" target="_blank" class="text-decoration-none">
                                <div class="resource-box mb-3">
                                    <h5 class="res-title-orange">WikiDota</h5>
                                    <p class="res-text">Энциклопедия игры</p>
                                </div>
                            </a>
                            
                            <a href="https://www.opendota.com" target="_blank" class="text-decoration-none">
                                <div class="resource-box">
                                    <h5 class="res-title-blue">OpenDota</h5>
                                    <p class="res-text">Анализ матчей</p>
                                </div>
                            </a>
                        </div>
                    </div>

                    <!-- ПЕРЕХОДЫ (Вертикально как на скрине) -->
                    <div class="footer-nav-box">
                        <h5 class="desc-text mb-4">Продолжить изучение MOBA игр:</h5>
                        
                        <a href="/deadlock" class="footer-link-card f-card-deadlock mb-3">
                            <div class="display-4 mb-2">🔫</div>
                            <h4 class="highlight-orange">Deadlock</h4>
                            <p class="res-text">Новый шутер от Valve</p>
                        </a>
                        
                        <a href="/about" class="footer-link-card f-card-about">
                            <div class="display-4 mb-2">ℹ️</div>
                            <h4 class="highlight-cyan">Об авторах</h4>
                            <p class="res-text">Кто создал этот гайд</p>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>