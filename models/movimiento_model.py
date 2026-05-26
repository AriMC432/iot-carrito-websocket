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

    # =========================================
    # CREAR DEMO
    # =========================================

    @staticmethod
    def crear_demo(nombre):

        connection = Database.get_connection()

        try:

            with connection.cursor() as cursor:

                sql = """
                CALL sp_crear_demo(%s)
                """

                cursor.execute(sql, (nombre,))

                connection.commit()

                return {
                    "status": True
                }

        except Exception as e:

            return {
                "status": False,
                "error": str(e)
            }

        finally:

            connection.close()

    # =========================================
    # AGREGAR MOVIMIENTO DEMO
    # =========================================

    @staticmethod
    def agregar_movimiento_demo(

        id_demo,
        id_movimiento,
        orden_demo

    ):

        connection = Database.get_connection()

        try:

            with connection.cursor() as cursor:

                sql = """
                CALL sp_agregar_movimiento_demo(
                    %s,
                    %s,
                    %s
                )
                """

                cursor.execute(sql, (

                    id_demo,
                    id_movimiento,
                    orden_demo

                ))

                connection.commit()

                return {
                    "status": True
                }

        except Exception as e:

            return {
                "status": False,
                "error": str(e)
            }

        finally:

            connection.close()

    # =========================================
    # VER DEMOS
    # =========================================

    @staticmethod
    def ver_demos():

        connection = Database.get_connection()

        try:

            with connection.cursor() as cursor:

                sql = "CALL sp_ver_demos()"

                cursor.execute(sql)

                result = cursor.fetchall()

                return result

        except Exception as e:

            return {
                "status": False,
                "error": str(e)
            }

        finally:

            connection.close()

    # =========================================
    # VER DETALLE DEMO
    # =========================================

    @staticmethod
    def ver_demo_detalle(id_demo):

        connection = Database.get_connection()

        try:

            with connection.cursor() as cursor:

                sql = """
                CALL sp_ver_demo_detalle(%s)
                """

                cursor.execute(sql, (id_demo,))

                result = cursor.fetchall()

                return result

        except Exception as e:

            return {
                "status": False,
                "error": str(e)
            }

        finally:

            connection.close()