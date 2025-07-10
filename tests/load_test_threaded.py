
import threading
import requests

def request_average_page():
    session = requests.Session()
    login_data = {"username": "user", "password": "user123"}
    session.post("http://127.0.0.1:5000/auth/login", data=login_data)
    response = session.get("http://127.0.0.1:5000/notes/averages")
    print(f"Status Code: {response.status_code}")

threads = []
for i in range(100):  # Simuler 50 utilisateurs simultanés
    t = threading.Thread(target=request_average_page)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
