@echo off
chcp 65001 > nul
title Редактор макета квитка тролейбуса

echo ==========================================================
echo  🚎 Запуск веб-додатку «Редактор макета квитка»
echo ==========================================================
echo.

where python >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [OK] Знайдено Python. Запуск локального сервера...
    python server.py
    goto end
)

where py >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [OK] Знайдено Python (py). Запуск локального сервера...
    py server.py
    goto end
)

echo [УВАГА] Python не знайдено у системі.
echo Відкриваємо index.html безпосередньо у веб-браузері...
start "" "index.html"

:end
pause
