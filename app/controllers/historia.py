from app import app
from flask import render_template
from flask import jsonify
from flask import request
from toggl.api_client import TogglClientApi
from app.models.historia import Historias

# configuration= {
# '':
# '':
# '':
# }
# client=TogglClientApi(configuration)
historial = Historias()

@app.route('/',methods = ['GET'])
def index():
    items = historial.listarHistorial()
    return render_template('historial.html')
