# brute_simulator.py
import auth
import time
import itertools

print("Simulador de fuerza bruta (local).")

# ejemplo: ataque alfabético simple (a,b,c,...)
charset = "abcdefghijklmnopqrstuvwxyz0123456789"

# longitudes que queremos probar
max_len = 4  # puedes subirlo si quieres

attempt = 0
for length in range(1, max_len + 1):
    for combo in itertools.product(charset, repeat=length):
        guess = "".join(combo)
        attempt += 1
        
        ok, msg = auth.check_password_vulnerable(guess)
        print(f"Intento {attempt}: {guess}")

        if ok:
            print(f"\n¡Contraseña encontrada!: {guess}")
            exit()

print("\nNo se encontró la contraseña en el rango probado.")

