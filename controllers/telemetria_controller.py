from flask import request, jsonify
from config.database import Database


class TelemetriaController:

    # =========================================
    # REGISTRAR OBSTACULO
    # =========================================

    @staticmethod
    def registrar_obstaculo():

        data = request.json

        connection = Database.get_connection()

        try:

            with connection.cursor() as cursor:

                sql = """
                CALL sp_registrar_obstaculo(
                    %s,
                    %s
                )
                """

                cursor.execute(sql, (

                    data["id_dispositivo"],
                    data["estatus"]

                ))

                connection.commit()

                return jsonify({

                    "status": True,
                    "message": "Obstaculo registrado"

                })

        except Exception as e:

            return jsonify({

                "status": False,
                "error": str(e)

            })

        finally:

            connection.close()

        # =========================================
    # ULTIMOS OBSTACULOS
    # =========================================

    @staticmethod
    def ultimos_obstaculos():

        connection = Database.get_connection()

        try:

            with connection.cursor() as cursor:

                sql = "CALL sp_ultimos_obstaculos()"

                cursor.execute(sql)

                result = cursor.fetchall()

                return jsonify({

                    "status": True,
                    "data": result

                })

        except Exception as e:

            return jsonify({

                "status": False,
                "error": str(e)

            })

        finally:

            connection.close()