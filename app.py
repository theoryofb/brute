# app.py
from flask import Flask, request
import auth

app = Flask(__name__)

VALID_USER = "admin"   # usuario válido para la demo

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if username != VALID_USER:
            return "FAIL_USER"

        ok, msg = auth.check_password_vulnerable(password)
        if ok:
            return "LOGIN OK"
        else:
            return "FAIL_PASS"
    
    return """
    <h2>Login vulnerable</h2>
    <form method="post">
        Usuario: <input name="username"><br>
        Contraseña: <input type="password" name="password"><br>
        <input type="submit" value="Entrar">
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)
