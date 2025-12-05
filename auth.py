# auth.py
# Módulo educativo: maneja verificación de contraseña y bloqueo por intentos.
# NO ataca servidores externos — todo ocurre en memoria local.

from werkzeug.security import generate_password_hash, check_password_hash
import time

# Contraseña "real" (la guardamos como hash). Cambia esto para pruebas.
_REAL_PASSWORD = "MiContrasenaSegura123!"
PASSWORD_HASH = generate_password_hash(_REAL_PASSWORD)  # hashed

# Parámetros de seguridad educativos
MAX_ATTEMPTS = 5
LOCK_SECONDS = 60  # bloqueo temporal después de MAX_ATTEMPTS

# Estructura en memoria para contar intentos por "identificador"
# En una app real se usaría IP, usuario o DB persitente.
_attempt_store = {}  # id -> {"count":int, "locked_until":ts}

def _now():
    return int(time.time())

def check_password_with_lock(identifier: str, guess: str):
    """
    Verifica una contraseña simulada con control de intentos.
    Devuelve (success: bool, message: str).
    identifier: cadena que identifica al atacante/cliente (p.ej. 'local-sim' o IP).
    """
    data = _attempt_store.get(identifier, {"count": 0, "locked_until": 0})
    if data["locked_until"] > _now():
        remaining = data["locked_until"] - _now()
        return False, f"Cuenta temporalmente bloqueada. Intenta en {remaining}s."

    # comprobación segura usando hash
    if check_password_hash(PASSWORD_HASH, guess):
        # éxito -> resetear contador
        _attempt_store.pop(identifier, None)
        return True, "Autenticación correcta."

    # fallo -> incrementar contador
    data["count"] += 1
    if data["count"] >= MAX_ATTEMPTS:
        data["locked_until"] = _now() + LOCK_SECONDS
        data["count"] = 0  # opcional: resetear después de bloqueo
        _attempt_store[identifier] = data
        return False, f"Demasiados intentos. Bloqueado por {LOCK_SECONDS}s."
    else:
        _attempt_store[identifier] = data
        attempts_left = MAX_ATTEMPTS - data["count"]
        return False, f"Contraseña incorrecta. Te quedan {attempts_left} intentos."

# Función para tests / depuración
def get_real_password_for_demo():
    """Solo para fines educativos: devuelve la contraseña real.
    En una situación real NUNCA se expone."""
    return _REAL_PASSWORD
