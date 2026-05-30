from flask import Blueprint, jsonify

from models.movimiento_model import MovimientoModel
from websocket.ws_server import WebSocketServer

from controllers.telemetria_controller import (
    TelemetriaController
)

telemetria_routes = Blueprint(
    "telemetria_routes",
    __name__
)

# =========================================
# TELEMETRIA
# =========================================

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

    # =========================================
    # ESTADO WEBSOCKET
    # =========================================

    estado_ws = "DESCONECTADO"

    try:

        if WebSocketServer.server.clients:

            estado_ws = "CONECTADO"

    except:

        estado_ws = "DESCONECTADO"

    # =========================================
    # RESPONSE
    # =========================================

    return jsonify({

        "status": True,

        "distancia":
            WebSocketServer.ultima_distancia,

        "ultimo_movimiento":
            nombre_movimiento,

        "obstaculo":
            WebSocketServer.ultimo_obstaculo,

        "websocket":
            estado_ws

    })

# =========================================
# REGISTRAR OBSTACULO
# =========================================

@telemetria_routes.route(
    "/api/obstaculo",
    methods=["POST"]
)
def registrar_obstaculo():

    return TelemetriaController.registrar_obstaculo()

# =========================================
# ULTIMOS OBSTACULOS
# =========================================

@telemetria_routes.route(
    "/api/ultimos_obstaculos",
    methods=["GET"]
)
def ultimos_obstaculos():

    return TelemetriaController.ultimos_obstaculos()