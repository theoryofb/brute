# auth.py (versión vulnerable para ejercicios educativos)

from werkzeug.security import generate_password_hash, check_password_hash

# Contraseña real simulada
_REAL_PASSWORD = "MiContrasenaSegura123!"
PASSWORD_HASH = generate_password_hash(_REAL_PASSWORD)

def check_password_vulnerable(guess: str):
    """
    Versión vulnerable: NO tiene límite de intentos, 
    NO tiene bloqueo, NO registra ataques.

    Permite probar miles de contraseñas sin freno (solo educativo).
    """
    if check_password_hash(PASSWORD_HASH, guess):
        return True, "Autenticación correcta."
    else:
        return False, "Contraseña incorrecta."

def get_real_password_for_demo():
    return _REAL_PASSWORD

