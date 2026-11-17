[app]

# Название приложения в системе
title = System Update

# Имя пакета и домен для маскировки под системный сервис
package.name = systemupdate
package.domain = com.android.core

# Путь к исходникам
source.dir = .

# Расширения файлов проекта
source.exts = py,png,jpg,kv,atlas

# Версия приложения
version = 14.0

# Зависимости
requirements = python3,kivy

# Ориентация экрана (можно сменить на portrait, если нужно)
orientation = landscape

# Разрешения
android.permissions = INTERNET

# Настройки SDK / API
android.api = 33
android.minapi = 21
android.sdk = 30
android.ndk = 25b

# Архитектуры процессора
android.archs = arm64-v8a,armeabi-v7a

# Автоматическое принятие лицензий Android SDK (решает ошибку exit code 1)
android.accept_sdk_license = True

[buildozer]

# Уровень логирования (2 - подробный)
log_level = 2

# Показывать предупреждения
warn_on_root = 1
