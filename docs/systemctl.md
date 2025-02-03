# Запустить поочередно и обновления будут приняты
- sudo systemctl daemon-reload
- sudo systemctl stop mybot.service
- sudo systemctl start mybot.service
- sudo systemctl status mybot.service
- sudo systemctl enable mybot.service     # автозапуск при перезагрузке

# Конфиг systemctl для перезапуска
- /etc/systemd/system

[Unit]
    Description=My Bot Service
    After=network.target

[Service]
    User=benzin
    WorkingDirectory=/home/benzin/Lexa_bot
    ExecStart=/usr/bin/python3 /home/benzin/Lexa_bot/bot.py
    Restart=always

[Install]
    WantedBy=multi-user.target