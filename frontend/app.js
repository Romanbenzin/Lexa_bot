document.addEventListener('DOMContentLoaded', () => {
    try {
        if (!window.Vue) {
            throw new Error('Vue.js не загружен');
        }

        const { createApp, ref } = Vue;
        
        console.log('Vue detected, version:', Vue.version);
        
        const app = createApp({
            setup() {
                const purchaseCount = ref(null);
                const pingMessage = ref(null);
                const loading = ref(false);
                const error = ref(null);

                async function getPurchaseCount() {
                    try {
                        loading.value = true;
                        error.value = null;
                        const response = await fetch('/api/count_purchases');
                        const data = await response.json();
                        purchaseCount.value = data.purchase_count;
                        pingMessage.value = null;
                    } catch (err) {
                        error.value = err.message;
                    } finally {
                        loading.value = false;
                    }
                }

                async function ping() {
                    try {
                        loading.value = true;
                        error.value = null;
                        const response = await fetch('/api/ping');
                        const data = await response.json();
                        pingMessage.value = data.message;
                        purchaseCount.value = null;
                    } catch (err) {
                        error.value = err.message;
                    } finally {
                        loading.value = false;
                    }
                }

                return {
                    purchaseCount,
                    pingMessage,
                    loading,
                    error,
                    getPurchaseCount,
                    ping
                };
            }
        });

        app.mount('#app');
        console.log('Vue application mounted successfully');
        
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

const soundClick = new Audio('https://assets.mixkit.co/sfx/preview/mixkit-select-click-1109.mp3');

const buttons = document.querySelectorAll('button');
buttons.forEach(btn => {
    btn.addEventListener('click', () => {
        soundClick.currentTime = 0;
        soundClick.play();
    });
});