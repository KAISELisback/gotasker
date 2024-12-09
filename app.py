from flask import Flask
import os
from dotenv import load_dotenv
from src.database.db import iniciar_banco_de_dados
from src.routes.tarefa_route import tarefa_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    
    app.register_blueprint(tarefa_bp)

    iniciar_banco_de_dados()
    
    return app

if __name__=='__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=3000, debug=True)