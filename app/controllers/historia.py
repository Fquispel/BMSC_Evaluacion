from app import app
from flask import render_template
from flask import jsonify
from flask import request
from toggl.TogglPy import Toggl
from app.models.historia import Detalles


detalle = Detalles()
toggl = Toggl()
#Cambiar de Acuerdo al Token de Usuario
toggl.setAPIKey("8999771c66072b7327a09b5c1f328525")
# Llamando a la API de Toogle
timeEntries = toggl.request("https://api.track.toggl.com/api/v8/time_entries")
workSpace = toggl.request("https://api.track.toggl.com/api/v8/workspaces")
#
@app.route('/', methods = ['GET'])
def index():
    items = detalle.listarHistorial()
    return render_template('historial.html', items=timeEntries)

#Recogiendo Datos de la api en la variable timeEntries
@app.route('/detalle', methods = ['GET'])
def listarHistorial():
    items = detalle.listarHistorialJSON()
    return jsonify(timeEntries),200

#Exportar a Excel
exportExcel = ("https://api.track.toggl.com/reports/api/v2/details?user_agent=ferquispe.l@gmail.com&workspace_id=6723111&since=2022-09-20&until=until=2022-09-24&")
# r1 = toggl.get("https://api.track.toggl.com/reports/api/v8/details?workspace_id=6723111&since=2022-09-20 &until=2022-09-24 &user_agent=api_test")
