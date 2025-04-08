from flask import Flask
import os
from dotenv import load_dotenv
from openai import OpenAI
from app.routes import routes

def create_app():
    load_dotenv(override=True)
    
    app = Flask(__name__, 
                template_folder='../templates',
                static_folder='../static')
    
    app.config['SECRET_KEY'] = os.urandom(24).hex()
    
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key) if api_key else None

    routes.init_app(app, client)
    
    return app, client 