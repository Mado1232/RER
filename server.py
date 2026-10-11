"""
Локальний веб-сервер для додатку «Редактор макета квитка тролейбуса».
Автоматично визначає локальну IP-адресу для підключення зі смартфона по Wi-Fi.
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import socket

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

def get_local_ip():
    """Визначає локальну IP-адресу комп'ютера у домашній мережі Wi-Fi."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Не надсилає реальних пакетів, просто визначає маршрутний інтерфейс
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        sys.stderr.write(f"[{self.log_date_time_string()}] {args[0]} {args[1]}\n")

def find_available_port(start_port=3000, max_attempts=10):
    for port in range(start_port, start_port + max_attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('0.0.0.0', port))
                return port
            except OSError:
                continue
    return start_port

def main():
    port = find_available_port(PORT)
    local_ip = get_local_ip()
    local_url = f"http://localhost:{port}"
    phone_url = f"http://{local_ip}:{port}"

    print("=" * 64)
    print(" 🚎 Редактор макета квитка тролейбуса (Live View)")
    print("=" * 64)
    print(f" 💻 На комп'ютері: {local_url}")
    print(f" 📱 НА ТЕЛЕФОНІ:   {phone_url}")
    print("=" * 64)
    print(f" Підключіть телефон до тієї ж мережі Wi-Fi та відкрийте:")
    print(f" 👉 {phone_url}")
    print("=" * 64)
    print(" Натисніть Ctrl+C для зупинки сервера.")

    # Відкриваємо браузер на ПК
    try:
        webbrowser.open(local_url)
    except Exception:
        pass

    with socketserver.TCPServer(("0.0.0.0", port), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n Сервер зупинено.")

if __name__ == "__main__":
    main()
