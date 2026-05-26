from flask import Blueprint, jsonify

from models.movimiento_model import MovimientoModel

from websocket.ws_server import WebSocketServer

telemetria_routes = Blueprint(
    "telemetria_routes",
    __name__
)

@telemetria_routes.route(
    "/api/telemetria",
    methods=["GET"]
)
def obtener_telemetria():

    movimiento = MovimientoModel.ultimo_movimiento()

    nombre_movimiento = "NINGUNO"

    if movimiento:

        nombre_movimiento = movimiento.get(
            "nombre_movimiento",
            "NINGUNO"
        )

    return jsonify({

        "status": True,

        "distancia":
            WebSocketServer.ultima_distancia,

        "ultimo_movimiento":
            nombre_movimiento,

        "obstaculo":
            WebSocketServer.ultimo_obstaculo,

        "websocket": "CONECTADO"

    })

from controllers.telemetria_controller import TelemetriaController


@telemetria_routes.route(
    "/api/obstaculo",
    methods=["POST"]
)
def registrar_obstaculo():

    return TelemetriaController.registrar_obstaculo()

@telemetria_routes.route(
    "/api/ultimos_obstaculos",
    methods=["GET"]
)
def ultimos_obstaculos():

    return TelemetriaController.ultimos_obstaculos()