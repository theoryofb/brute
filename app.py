# app.py (versión vulnerable)
from flask import Flask, request, render_template_string
import auth

app = Flask(__name__)

LOGIN_PAGE = """
<h2>Login vulnerable (educativo)</h2>
<form method=post>
  Usuario: <input name="username"><br>
  Contraseña: <input name="password" type="password"><br>
  <input type=submit value="Entrar">
</form>
<p>{{ message }}</p>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        password = request.form.get("password", "")
        ok, msg = auth.check_password_vulnerable(password)
        message = msg
        if ok:
            return "<h2>Login exitoso (vulnerable)</h2>"
    return LOGIN_PAGE.replace("{{ message }}", message)

if __name__ == "__main__":
    app.run(debug=True)
