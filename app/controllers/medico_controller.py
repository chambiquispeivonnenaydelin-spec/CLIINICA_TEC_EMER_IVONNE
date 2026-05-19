from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models.medico import Medico

medico_bp = Blueprint("medico", __name__, url_prefix="/medicos")

@medico_bp.route("/")
def listar_medicos():
    medicos = Medico.query.all()
    return render_template("medicos/lista.html", medicos=medicos)

@medico_bp.route("/crear", methods=["GET", "POST"])
def crear_medico():
    if request.method == "POST":
        medico = Medico(
            nombre=request.form["nombre"],
            especialidad=request.form["especialidad"],
            telefono=request.form["telefono"],
            correo=request.form["correo"]
        )
        db.session.add(medico)
        db.session.commit()
        return redirect(url_for("medico.listar_medicos"))

    return render_template("medicos/crear.html")

@medico_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_medico(id):
    medico = Medico.query.get_or_404(id)

    if request.method == "POST":
        medico.nombre = request.form["nombre"]
        medico.especialidad = request.form["especialidad"]
        medico.telefono = request.form["telefono"]
        medico.correo = request.form["correo"]
        db.session.commit()
        return redirect(url_for("medico.listar_medicos"))

    return render_template("medicos/editar.html", medico=medico)

@medico_bp.route("/eliminar/<int:id>", methods=["POST"])
def eliminar_medico(id):
    medico = Medico.query.get_or_404(id)
    db.session.delete(medico)
    db.session.commit()
    return redirect(url_for("medico.listar_medicos"))