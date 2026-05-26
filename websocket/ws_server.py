from websocket_server import WebsocketServer
import json

from models.movimiento_model import MovimientoModel

class WebSocketServer:

    server = None

    # =========================================
    # TELEMETRIA
    # =========================================

    ultima_distancia = 0
    ultimo_obstaculo = False

    # =========================================
    # NUEVO CLIENTE
    # =========================================

    @staticmethod
    def new_client(client, server):

        print("")
        print("=================================")
        print("ESP8266 CONECTADO")
        print(client)
        print("=================================")

    # =========================================
    # MENSAJES RECIBIDOS
    # =========================================

    @staticmethod
    def message_received(client, server, message):

        print("")
        print("=================================")
        print("MENSAJE RECIBIDO")
        print(message)
        print("=================================")

        try:

            data = json.loads(message)

            WebSocketServer.ultima_distancia = data.get(
                "distancia",
                0
            )

            WebSocketServer.ultimo_obstaculo = data.get(
                "obstaculo",
                False
            )

            # =========================================
            # GUARDAR OBSTACULO
            # =========================================

            if WebSocketServer.ultimo_obstaculo:

                from config.database import Database

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

                            1,
                            "DETECTADO"

                        ))

                        connection.commit()

                except Exception as e:

                    print(e)

                finally:

                    connection.close()

        except Exception as e:

            print(e)

    # =========================================
    # START SERVER
    # =========================================

    @staticmethod
    def start():

        WebSocketServer.server = WebsocketServer(

            host='0.0.0.0',
            port=5050

        )

        # =========================================
        # EVENTOS
        # =========================================

        WebSocketServer.server.set_fn_new_client(

            WebSocketServer.new_client

        )

        WebSocketServer.server.set_fn_message_received(

            WebSocketServer.message_received

        )

        print("")
        print("=================================")
        print("WEBSOCKET INICIADO 5050")
        print("=================================")

        ultimo_movimiento = None

        import threading
        import time

        # =========================================
        # ENVIAR MOVIMIENTOS
        # =========================================

        def enviar_movimientos():

            nonlocal ultimo_movimiento

            while True:

                movimiento = MovimientoModel.ultimo_movimiento()

                if movimiento:

                    movimiento_actual = json.dumps(

                        movimiento,
                        default=str

                    )

                    if movimiento_actual != ultimo_movimiento:

                        print("")
                        print("=================================")
                        print("MOVIMIENTO ENVIADO")
                        print(movimiento_actual)
                        print("=================================")

                        WebSocketServer.server.send_message_to_all(

                            movimiento_actual

                        )

                        ultimo_movimiento = movimiento_actual

                time.sleep(0.1)

        hilo = threading.Thread(

            target=enviar_movimientos

        )

        hilo.daemon = True

        hilo.start()

        WebSocketServer.server.run_forever()