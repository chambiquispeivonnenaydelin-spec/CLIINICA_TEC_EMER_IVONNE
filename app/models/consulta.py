from app import db
from datetime import date

class Consulta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    diagnostico = db.Column(db.String(200), nullable=False)
    tratamiento = db.Column(db.String(200), nullable=False)
    medico_id = db.Column(db.Integer, db.ForeignKey("medico.id"), nullable=False)
    paciente_id = db.Column(db.Integer, db.ForeignKey("paciente.id"), nullable=False)

    medico = db.relationship("Medico", back_populates="consultas")
    paciente = db.relationship("Paciente", back_populates="consultas")