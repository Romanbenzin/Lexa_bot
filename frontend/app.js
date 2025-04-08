document.addEventListener('DOMContentLoaded', () => {
    try {
        if (!window.Vue || !window.VueRouter) {
            throw new Error('Vue.js или Vue Router не загружены');
        }

        const { createApp } = Vue;
        const { createRouter, createWebHistory } = VueRouter;

        // Компонент для отображения страницы 404
        const NotFoundPage = {
            template: `
                <div>
                    <div class="darksouls-separator"></div>
                    <h1>404 - Страница не найдена</h1>
                    <div class="darksouls-separator"></div>
                    <p>К сожалению, запрашиваемая страница не существует.</p>
                    <router-link to="/main" class="darksouls-flame">Вернуться на главную</router-link>
                </div>
            `,
        };

        // Главная страница
        const MainPage = {
            template: `
                <div>
                    <div class="darksouls-separator"></div>
                    <h1>Lexa_bot</h1>
                    <div class="darksouls-separator"></div>
                    <button @click="getPurchaseCount" class="darksouls-flame">Получить количество покупок</button>
                    <button @click="ping" class="darksouls-flame">Проверить работу API (ping)</button>
                    <div class="darksouls-separator"></div>
                    <div id="result">
                        <p v-if="loading">Загрузка...</p>
                        <p v-else-if="error" style="color: red">{{ error }}</p>
                        <div v-else>
                            <p v-if="purchaseCount !== null">Количество покупок: <strong>{{ purchaseCount }}</strong></p>
                            <p v-if="pingMessage !== null">Ответ сервера: <strong>{{ pingMessage }}</strong></p>
                        </div>
                    </div>
                </div>
            `,
            data() {
                return {
                    purchaseCount: null,
                    pingMessage: null,
                    loading: false,
                    error: null,
                };
            },
            methods: {
                async getPurchaseCount() {
                    this.loading = true;
                    this.error = null;
                    try {
                        const response = await fetch('/api/count_purchases');
                        const data = await response.json();
                        this.purchaseCount = data.purchase_count;
                    } catch (err) {
                        this.error = err.message;
                    } finally {
                        this.loading = false;
                    }
                },
                async ping() {
                    this.loading = true;
                    this.error = null;
                    try {
                        const response = await fetch('/api/ping');
                        const data = await response.json();
                        this.pingMessage = data.message;
                    } catch (err) {
                        this.error = err.message;
                    } finally {
                        this.loading = false;
                    }
                },
            },
        };

        // Страница списка игр
        const GetGamePage = {
            template: `
                <div>
                    <div class="darksouls-separator"></div>
                    <h1>Список игр</h1>
                    <div class="darksouls-separator"></div>
                    <input v-model="userName" placeholder="Введите имя пользователя" />
                    <button @click="getGames" class="darksouls-flame">Получить список игр</button>
                    <div id="result">
                        <p v-if="loading">Загрузка...</p>
                        <p v-else-if="error" style="color: red">{{ error }}</p>
                        <ul v-else>
                            <li v-for="(game, index) in games" :key="index">
                                <a :href="game.game_link" target="_blank">{{ game.game_name }}</a> ({{ game.purchase_date }})
                            </li>
                        </ul>
                    </div>
                </div>
            `,
            data() {
                return {
                    games: [],
                    userName: '',
                    loading: false,
                    error: null,
                };
            },
            methods: {
                async getGames() {
                    if (!this.userName) {
                        this.error = 'Введите имя пользователя';
                        return;
                    }
                    this.loading = true;
                    this.error = null;
                    try {
                        const response = await fetch(`/api/get_game?user_name=${encodeURIComponent(this.userName)}`);
                        const data = await response.json();
                        if (Array.isArray(data)) {
                            this.games = data;
                        } else if (data.message) {
                            this.games = [];
                            this.error = data.message;
                        } else {
                            throw new Error('Неизвестный формат ответа');
                        }
                    } catch (err) {
                        this.error = err.message;
                    } finally {
                        this.loading = false;
                    }
                },
            },
        };

        // Корневой компонент с боковым меню
        const App = {
            template: `
                <div>
                    <!-- Кнопка для открытия меню -->
                    <button class="menu-toggle" @click="toggleMenu">☰</button>
                    <!-- Боковое меню -->
                    <div id="sidebar" :class="{ active: isMenuOpen }">
                        <div class="menu-content">
                            <router-link to="/main" class="menu-link" @click="closeMenu">Главная</router-link>
                            <router-link to="/get_game" class="menu-link" @click="closeMenu">Список игр</router-link>
                        </div>
                    </div>
                    <!-- Основной контент -->
                    <div id="main-content">
                        <router-view></router-view>
                    </div>
                </div>
            `,
            data() {
                return {
                    isMenuOpen: false,
                };
            },
            methods: {
                toggleMenu() {
                    this.isMenuOpen = !this.isMenuOpen;
                },
                closeMenu() {
                    this.isMenuOpen = false;
                },
            },
        };

        // Настройка маршрутов
        const routes = [
            { path: '/', redirect: '/main' },
            { path: '/main', component: MainPage },
            { path: '/get_game', component: GetGamePage },
            { path: '/:pathMatch(.*)*', component: NotFoundPage },
        ];

        const router = createRouter({
            history: createWebHistory(),
            routes,
        });

        const app = createApp(App);
        app.use(router);
        app.mount('#app');
    } catch (error) {
        console.error('Vue initialization error:', error);
        document.getElementById('app').innerHTML = `
            <div style="color: red; padding: 20px;">
                Ошибка приложения: ${error.message}
                <br><br>
                <button onclick="window.location.reload()">Перезагрузить</button>
            </div>
        `;
    }
});
