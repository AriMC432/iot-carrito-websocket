from flask import request, jsonify
from models.movimiento_model import MovimientoModel

class MovimientoController:

    # =========================================
    # AGREGAR MOVIMIENTO
    # =========================================
    @staticmethod
    def agregar_movimiento():

        data = request.json

        response = MovimientoModel.agregar_movimiento(
            data["id_movimiento"],
            data["id_dispositivo"]
        )

        return jsonify(response)

    # =========================================
    # ULTIMO MOVIMIENTO
    # =========================================
    @staticmethod
    def ultimo_movimiento():

        response = MovimientoModel.ultimo_movimiento()

        return jsonify(response)

    # =========================================
    # ACTUALIZAR MOTOR
    # =========================================
    @staticmethod
    def actualizar_motor():

        data = request.json

        response = MovimientoModel.actualizar_motor(
        
        data["id_movimiento"],
        data["nuevo_MIA"],
        data["nuevo_MIB"],
        data["nuevo_MITime"],
        data["nuevo_MDA"],
        data["nuevo_MDB"],
        data["nuevo_MDTime"]
        )

        return jsonify(response)

    # =========================================
    # VER CONFIG MOTOR
    # =========================================
    @staticmethod
    def ver_config_motor(id_movimiento):

        response = MovimientoModel.ver_config_motor(
            id_movimiento
        )

        return jsonify(response)