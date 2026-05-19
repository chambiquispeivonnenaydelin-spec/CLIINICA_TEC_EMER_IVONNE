from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models.paciente import Paciente

paciente_bp = Blueprint("paciente", __name__, url_prefix="/pacientes")

@paciente_bp.route("/")
def listar_pacientes():
    pacientes = Paciente.query.all()
    return render_template("pacientes/lista.html", pacientes=pacientes)
@paciente_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_paciente(id):
    paciente = Paciente.query.get_or_404(id)

    if request.method == "POST":
        paciente.nombre = request.form["nombre"]
        paciente.edad = request.form["edad"]
        paciente.direccion = request.form["direccion"]
        paciente.telefono = request.form["telefono"]
        db.session.commit()
        return redirect(url_for("paciente.listar_pacientes"))

    return render_template("pacientes/editar.html", paciente=paciente)


@paciente_bp.route("/eliminar/<int:id>", methods=["POST"])
def eliminar_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    db.session.delete(paciente)
    db.session.commit()
    return redirect(url_for("paciente.listar_pacientes"))



@paciente_bp.route("/crear", methods=["GET", "POST"])
def crear_paciente():
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = request.form["edad"]
        direccion = request.form["direccion"]
        telefono = request.form["telefono"]

        paciente = Paciente(
            nombre=nombre,
            edad=edad,
            direccion=direccion,
            telefono=telefono
        )

        db.session.add(paciente)
        db.session.commit()
        return redirect(url_for("paciente.listar_pacientes"))

    return render_template("pacientes/crear.html")