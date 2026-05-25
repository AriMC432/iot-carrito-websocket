from flask import Flask
from flask_cors import CORS
from routes.movimiento_routes import movimiento_routes
from routes.config_motor_routes import config_motor_routes
from websocket.ws_server import WebSocketServer
from routes.telemetria_routes import telemetria_routes
from routes.historial_config_routes import historial_config_routes
import threading

app = Flask(__name__)
CORS(app)
# REGISTRAR RUTAS
app.register_blueprint(movimiento_routes)
app.register_blueprint(config_motor_routes)
app.register_blueprint(telemetria_routes)
app.register_blueprint(historial_config_routes)
# WEBSOCKET
websocket_thread = threading.Thread(
    target=WebSocketServer.start
)
websocket_thread.daemon = True
websocket_thread.start()
# =========================================
# MAIN
# =========================================
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )