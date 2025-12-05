# app.py
from flask import Flask, request
import auth

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form.get("password", "")
        ok, msg = auth.check_password_vulnerable(password)
        if ok:
            return "LOGIN OK"
        else:
            return "FAIL"
    
    return """
    <h2>Login vulnerable</h2>
    <form method="post">
        Contraseña: <input type="password" name="password"><br>
        <input type="submit" value="Entrar">
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)
