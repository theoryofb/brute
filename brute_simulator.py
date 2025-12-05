# brute_simulator.py
# Simulador que intenta contraseñas contra la función auth.check_password_with_lock
# Esta simulación NO ataca nada externo: todo es local.

import auth
import time
import random

IDENT = "local-sim"

# Lista de intentos (en la vida real esta lista sería MUCHO más grande;
# aquí reducimos para la demo). Incluimos la contraseña correcta en algún lugar.
guesses = [
    "1234", "password", "letmein", "MiContrasenaSegura123!", "admin", "qwerty"
]

random.shuffle(guesses)  # para simular orden aleatorio

print("Iniciando simulador de fuerza bruta (local y educativo).")
for i, g in enumerate(guesses, 1):
    success, msg = auth.check_password_with_lock(IDENT, g)
    print(f"Intento {i}: '{g}' -> {msg}")
    if success:
        print("Contraseña encontrada por el simulador (solo demo).")
        break
    # Espera pequeña para simular tiempo entre intentos
    time.sleep(0.5)

# Mostrar comportamiento de bloqueo: intentar seguir después del bloqueo
print("\nProbando comportamiento tras bloqueo (si fue bloqueado)...")
for j in range(3):
    success, msg = auth.check_password_with_lock(IDENT, "cualquiercosa")
    print(f"Post-intento {j+1}: {msg}")
    time.sleep(0.5)

# Muestra la contraseña real (solo para la tarea/entrega educativa)
print("\n[Demo] contraseña real (solo para uso educativo):", auth.get_real_password_for_demo())
