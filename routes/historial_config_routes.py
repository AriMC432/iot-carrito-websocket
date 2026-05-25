from flask import Blueprint, jsonify
from config.database import Database

historial_config_routes = Blueprint(
    "historial_config_routes",
    __name__
)

@historial_config_routes.route(
    "/api/historial_config",
    methods=["GET"]
)
def historial_config():

    conexion = Database.get_connection()

    cursor = conexion.cursor()

    query = """

    SELECT

        cm.nombre_movimiento,

        cmm.MIA,
        cmm.MIB,
        cmm.MITime,

        cmm.MDA,
        cmm.MDB,
        cmm.MDTime

    FROM config_motor_movimiento cmm

    INNER JOIN cat_movimientos cm
    ON cmm.id_movimiento =
       cm.id_movimiento

    ORDER BY cmm.id_config DESC

    """

    cursor.execute(query)

    datos = cursor.fetchall()

    cursor.close()

    conexion.close()

    return jsonify(datos)