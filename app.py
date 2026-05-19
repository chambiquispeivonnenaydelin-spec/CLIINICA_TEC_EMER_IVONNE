from app import create_app, db
from app.models.medico import Medico
from app.models.paciente import Paciente
from app.models.consulta import Consulta
from app.models.user import User


app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Medico": Medico,
        "Paciente": Paciente,
        "Consulta": Consulta,
        "User": User,
    }

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)