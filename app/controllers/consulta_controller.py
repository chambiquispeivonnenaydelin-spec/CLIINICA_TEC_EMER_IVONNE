from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models.consulta import Consulta
from app.models.medico import Medico
from app.models.paciente import Paciente
from datetime import datetime

consulta_bp = Blueprint("consulta", __name__, url_prefix="/consultas")

@consulta_bp.route("/")
def listar_consultas():
    fecha = request.args.get("fecha")
    query = Consulta.query

    if fecha:
        query = query.filter(Consulta.fecha == datetime.strptime(fecha, "%Y-%m-%d").date())

    consultas = query.all()
    return render_template("consultas/lista.html", consultas=consultas, fecha=fecha)

from datetime import datetime

@consulta_bp.route("/crear", methods=["GET", "POST"])
def crear_consulta():
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()

    if request.method == "POST":
        consulta = Consulta(
            fecha=datetime.strptime(request.form["fecha"], "%Y-%m-%d").date(),
            diagnostico=request.form["diagnostico"],
            tratamiento=request.form["tratamiento"],
            medico_id=request.form["medico_id"],
            paciente_id=request.form["paciente_id"]
        )
        db.session.add(consulta)
        db.session.commit()
        return redirect(url_for("consulta.listar_consultas"))

    return render_template("consultas/crear.html", medicos=medicos, pacientes=pacientes)
@consulta_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_consulta(id):
    consulta = Consulta.query.get_or_404(id)
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()

    if request.method == "POST":
        consulta.fecha = datetime.strptime(request.form["fecha"], "%Y-%m-%d").date()        
        consulta.diagnostico = request.form["diagnostico"]
        consulta.tratamiento = request.form["tratamiento"]
        consulta.medico_id = request.form["medico_id"]
        consulta.paciente_id = request.form["paciente_id"]
        db.session.commit()
        return redirect(url_for("consulta.listar_consultas"))

    return render_template("consultas/editar.html", consulta=consulta, medicos=medicos, pacientes=pacientes)

@consulta_bp.route("/eliminar/<int:id>", methods=["POST"])
def eliminar_consulta(id):
    consulta = Consulta.query.get_or_404(id)
    db.session.delete(consulta)
    db.session.commit()
    return redirect(url_for("consulta.listar_consultas"))