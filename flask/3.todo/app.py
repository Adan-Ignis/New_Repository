from flask import Flask
from datetime import datetime
import json
import os

MIS_TAREAS = "tareas.json"

def carga_tareas():
    if not os.path.exists(MIS_TAREAS):
        return []
    with open(MIS_TAREAS,"r",encoding="utf-8") as f:
        return json.load(f)

def guardar_tareas(tareas):
    with open(MIS_TAREAS, "w", encoding="utf-8") as f:
        json.dump(tareas, MIS_TAREAS, indent=4, ensure_ascii=False)

@app.route("/", methods=["POST", "GET"])
def index():
    tasks = carga_tareas()
    if request.method == "POST":
        desc = request.form["descripcion"]
        nueva = {
            "id": len(tasks) + 1,
            "descripcion": desc,
            "fecha_alta": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "fecha_completada": None
        }
        tasks.append(nueva)
        guardar_tareas(tasks)
        return redirect(url_for("index"))
    
    return render_template("index.html", tareas=tasks)

def nuevo_id():
    lista_id = []
    tasks = carga_tareas()
    for t in tasks:
        lista_id.append(t["id"])
    return max(lista_id) + 1

@app.route("/delete/<int:id_tarea>",methods = ["POST", "GET"])
def borrar_tarea(id_tarea):
    tasks = carga_tareas()
    resto_tareas = []
    for t in tasks:
        if t["id"] != id_tarea:
            resto_tareas.append(t)

    guardar_tareas(resto_tareas)
    return redirect(url_for("index"))

@app.route("/edit/<int:id_tarea>")
def edit(id_tarea):
    tasks = carga_tareas()

    for t in tasks:
        if t["id"] == id_tarea:
            t["fecha_completa"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            break
    guardar_tareas(tasks)
    return redirect(url_for("index"))

@app.route("/edit/<int:id_tarea>", methods = ["POST", "GET"])
def editar_tareas(id_tarea):
    tasks = carga_tareas()
    tarea_sel = ""
    for t in tasks:
        if t["id"] == id_tarea:
            tarea_sel = t
            break

    if request.method == "POST":
        tarea_sel["descripcion"] = request.form["descripcion"]
        tarea_sel["fecha_completa"] = None
        guardar_tareas(tasks)
        return redirect(url_for("index"))
    
    return render_template("edit.html", tarea=tarea_sel)