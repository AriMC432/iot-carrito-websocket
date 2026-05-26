from flask import request, jsonify

from models.movimiento_model import MovimientoModel

class MovimientoController:

    # =========================================
    # AGREGAR MOVIMIENTO
    # =========================================

    @staticmethod
    def agregar_movimiento():

        data = request.get_json()

        id_movimiento = data.get(
            "id_movimiento"
        )

        id_dispositivo = data.get(
            "id_dispositivo"
        )

        result = MovimientoModel.agregar_movimiento(

            id_movimiento,

            id_dispositivo

        )

        return jsonify(result)

    # =========================================
    # ULTIMO MOVIMIENTO
    # =========================================

    @staticmethod
    def ultimo_movimiento():

        result = MovimientoModel.ultimo_movimiento()

        return jsonify(result)

    # =========================================
    # ACTUALIZAR MOTOR
    # =========================================

    @staticmethod
    def actualizar_motor():

        data = request.get_json()

        result = MovimientoModel.actualizar_motor(

            data.get("id_movimiento"),

            data.get("nuevo_MIA"),
            data.get("nuevo_MIB"),
            data.get("nuevo_MITime"),

            data.get("nuevo_MDA"),
            data.get("nuevo_MDB"),
            data.get("nuevo_MDTime")

        )

        return jsonify(result)

    # =========================================
    # VER CONFIG MOTOR
    # =========================================

    @staticmethod
    def ver_config_motor(id_movimiento):

        result = MovimientoModel.ver_config_motor(
            id_movimiento
        )

        return jsonify(result)

    # =========================================
    # CREAR DEMO
    # =========================================

    @staticmethod
    def crear_demo():

        data = request.get_json()

        nombre = data.get("nombre")

        secuencia = data.get("secuencia")

        # CREAR DEMO

        MovimientoModel.crear_demo(nombre)

        demos = MovimientoModel.ver_demos()

        ultimo_demo = demos[0]

        id_demo = ultimo_demo["id_demo"]

        movimientos = secuencia.split(",")

        orden = 1

        for mov in movimientos:

            MovimientoModel.agregar_movimiento_demo(

                id_demo,

                int(mov),

                orden

            )

            orden += 1

        return jsonify({

            "status": True,

            "message": "Demo creada"

        })

    # =========================================
    # VER DEMOS
    # =========================================

    @staticmethod
    def ver_demos():

        result = MovimientoModel.ver_demos()

        return jsonify(result)

    # =========================================
    # VER DETALLE DEMO
    # =========================================

    @staticmethod
    def ver_demo_detalle(id_demo):

        result = MovimientoModel.ver_demo_detalle(
            id_demo
        )

        return jsonify(result)