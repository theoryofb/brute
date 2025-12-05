# app.py
# Aplicación web educativa. Ejecuta localmente.
from flask import Flask, request, render_template_string, redirect, url_for, flash
import auth

app = Flask(__name__)
app.secret_key = "dev-secret-key-educativo"  # solo para pruebas locales

LOGIN_PAGE = """
<!doctype html>
<title>Login demo</title>
<h2>Login educativo</h2>
<form method=post>
  Usuario: <input name="username" value="student"><br>
  Contraseña: <input name="password" type="password"><br>
  <input type=submit value="Entrar">
</form>
<p>{{ message }}</p>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        # identificador simple por IP (en local suele ser 127.0.0.1)
        identifier = request.remote_addr or "unknown"
        success, msg = auth.check_password_with_lock(identifier, password)
        message = msg
        if success:
            flash("Login OK (educativo).")
            return redirect(url_for("protected"))
        else:
            flash(msg)
    return render_template_string(LOGIN_PAGE, message=message)

@app.route("/protected")
def protected():
    return "<h3>Zona protegida (simulada). Esta es una demo local.</h3>"

if __name__ == "__main__":
    app.run(debug=True)
