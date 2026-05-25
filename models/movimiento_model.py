from config.database import Database

class MovimientoModel:

    # =========================================
    # AGREGAR MOVIMIENTO
    # =========================================

    @staticmethod
    def agregar_movimiento(id_movimiento, id_dispositivo):

        connection = Database.get_connection()

        try:

            with connection.cursor() as cursor:

                sql = "CALL sp_agregar_movimiento(%s,%s)"

                cursor.execute(sql, (
                    id_movimiento,
                    id_dispositivo
                ))

                connection.commit()

                return {
                    "status": True,
                    "message": "Movimiento agregado"
                }

        except Exception as e:

            return {
                "status": False,
                "error": str(e)
            }

        finally:

            connection.close()


    # =========================================
    # ULTIMO MOVIMIENTO
    # =========================================

    @staticmethod
    def ultimo_movimiento():

        connection = Database.get_connection()

        try:

            with connection.cursor() as cursor:

                sql = "CALL sp_ultimo_movimiento()"

                cursor.execute(sql)

                result = cursor.fetchone()

                return result

        except Exception as e:

            return {
                "status": False,
                "error": str(e)
            }

        finally:

            connection.close()


    # =========================================
    # ACTUALIZAR MOTOR
    # =========================================

    @staticmethod
    def actualizar_motor(

        id_movimiento,

        nuevo_MIA,
        nuevo_MIB,
        nuevo_MITime,

        nuevo_MDA,
        nuevo_MDB,
        nuevo_MDTime

    ):

        connection = Database.get_connection()

        try:

            with connection.cursor() as cursor:

                sql = """
                CALL sp_actualizar_motor(
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                )
                """

                cursor.execute(sql, (

                    id_movimiento,

                    nuevo_MIA,
                    nuevo_MIB,
                    nuevo_MITime,

                    nuevo_MDA,
                    nuevo_MDB,
                    nuevo_MDTime

                ))

                connection.commit()

                return {
                    "status": True,
                    "message": "Motor actualizado"
                }

        except Exception as e:

            return {
                "status": False,
                "error": str(e)
            }

        finally:

            connection.close()


    # =========================================
    # VER CONFIG MOTOR
    # =========================================

    @staticmethod
    def ver_config_motor(id_movimiento):

        connection = Database.get_connection()

        try:

            with connection.cursor() as cursor:

                sql = "CALL sp_ver_config_motor(%s)"

                cursor.execute(sql, (id_movimiento,))

                result = cursor.fetchone()

                return result

        except Exception as e:

            return {
                "status": False,
                "error": str(e)
            }

        finally:

            connection.close()


    # =========================================
    # ACTUALIZAR CONFIG MOTOR
    # =========================================

    @staticmethod
    def actualizar_config_motor(

        id_movimiento,

        MIA,
        MIB,
        MITime,

        MDA,
        MDB,
        MDTime

    ):

        connection = Database.get_connection()

        try:

            with connection.cursor() as cursor:

                sql = """
                    CALL sp_actualizar_config_motor(
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                    )
                """

                cursor.execute(
                    sql,
                    (

                        id_movimiento,

                        MIA,
                        MIB,
                        MITime,

                        MDA,
                        MDB,
                        MDTime

                    )
                )

                connection.commit()

                return {
                    "status": True,
                    "message": "Configuración actualizada"
                }

        except Exception as e:

            return {
                "status": False,
                "error": str(e)
            }

        finally:

            connection.close()