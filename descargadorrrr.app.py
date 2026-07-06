from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tareas = []

@app.route("/")
def inicio():
    return render_template("index.html", tareas=tareas)

@app.route("/agregar", methods=["POST"])
def agregar():
    nombre = request.form["nombre"]

    if nombre:
        tareas.append({
            "nombre": nombre,
            "completada": False
        })

    return redirect(url_for("inicio"))

@app.route("/completar/<int:numero>")
def completar(numero):
    if 0 <= numero < len(tareas):
        tareas[numero]["completada"] = True

    return redirect(url_for("inicio"))

if __name__ == "__main__":
    app.run(debug=True)
