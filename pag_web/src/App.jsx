import React from "react";
import { motion } from "framer-motion";
export default function IoTCarDashboard() {

  // =========================================
  // API URL
  // =========================================


    const [apiUrl, setApiUrl] = React.useState(
    "http://10.161.176.154:5000"
  );
  // =========================================
  // CONFIG MOTOR
  // =========================================

  const [movimientoSeleccionado, setMovimientoSeleccionado] =
    React.useState(1);

  const [configMotor, setConfigMotor] = React.useState({

    MIA: "",
    MIB: "",
    MITime: "",

    MDA: "",
    MDB: "",
    MDTime: ""

  });

  // =========================================
  // TELEMETRIA
  // =========================================

  const [telemetria, setTelemetria] = React.useState({

    distancia: 0,

    ultimo_movimiento: "NINGUNO",

    obstaculo: false,

    websocket: "DESCONECTADO"

  });

  // =========================================
  // HISTORIAL
  // =========================================

  const [historialMovimientos, setHistorialMovimientos] =
    React.useState([]);

  const [historialConfig, setHistorialConfig] =
    React.useState([]);

  // =========================================
  // INPUTS MODIFICADOS
  // =========================================

  const [camposModificados, setCamposModificados] =
    React.useState({});

  const [ultimosObstaculos, setUltimosObstaculos] = React.useState([]); 
  // =========================================
// DEMOS
// =========================================

const [nombreDemo, setNombreDemo] =
  React.useState("");

const [secuenciaDemo, setSecuenciaDemo] =
  React.useState("");

const [demosGuardadas, setDemosGuardadas] =
  React.useState([]);
  // =========================================
  // MOVIMIENTOS
  // =========================================
  const movimientos = [

    {
      id: 1,
      nombre: "Adelante",
      icono: "⬆️",
      color: "from-cyan-600 to-cyan-900"
    },

    {
      id: 2,
      nombre: "Atrás",
      icono: "⬇️",
      color: "from-cyan-600 to-cyan-900"
    },

    {
      id: 3,
      nombre: "Detener",
      icono: "🛑",
      color: "from-red-600 to-red-900"
    },

    {
      id: 4,
      nombre: "Vuelta Adelante Derecha",
      icono: "↗️",
      color: "from-cyan-600 to-cyan-900"
    },

    {
      id: 5,
      nombre: "Vuelta Adelante Izquierda",
      icono: "↖️",
      color: "from-cyan-600 to-cyan-900"
    },

    {
      id: 6,
      nombre: "Vuelta Atrás Derecha",
      icono: "↘️",
      color: "from-cyan-600 to-cyan-900"
    },

    {
      id: 7,
      nombre: "Vuelta Atrás Izquierda",
      icono: "↙️",
      color: "from-cyan-600 to-cyan-900"
    },

    {
      id: 8,
      nombre: "Giro 90 Derecha",
      icono: "↻",
      color: "from-cyan-600 to-cyan-900"
    },

    {
      id: 9,
      nombre: "Giro 90 Izquierda",
      icono: "↺",
      color: "from-cyan-600 to-cyan-900"
    },

    {
      id: 10,
      nombre: "Giro 360 Derecha",
      icono: "🌀",
      color: "from-cyan-600 to-cyan-900"
    },

    {
      id: 11,
      nombre: "Giro 360 Izquierda",
      icono: "💫",
      color: "from-cyan-600 to-cyan-900"
    }

  ];

  // =========================================
  // CARGAR CONFIG
  // =========================================

  const cargarConfigMotor = async (idMovimiento) => {

    try {

      const response = await fetch(
        `${apiUrl}/api/config_motor/${idMovimiento}`
      );

      const data = await response.json();

      setConfigMotor({

        MIA: data.MIA || "",
        MIB: data.MIB || "",
        MITime: data.MITime || "",

        MDA: data.MDA || "",
        MDB: data.MDB || "",
        MDTime: data.MDTime || ""

      });

    } catch (error) {

      console.log(error);

    }

  };

  // =========================================
  // GUARDAR CONFIG
  // =========================================

  const guardarConfiguracion = async () => {

    try {

      const response = await fetch(

        `${apiUrl}/api/actualizar_motor`,

        {

          method: "PUT",

          headers: {
            "Content-Type": "application/json"
          },

          body: JSON.stringify({

            id_movimiento: movimientoSeleccionado,

            nuevo_MIA: configMotor.MIA,
            nuevo_MIB: configMotor.MIB,
            nuevo_MITime: configMotor.MITime,

            nuevo_MDA: configMotor.MDA,
            nuevo_MDB: configMotor.MDB,
            nuevo_MDTime: configMotor.MDTime

          })

        }

      );

      await response.json();

      alert("Configuración guardada 😎");

      setCamposModificados({});

    } catch(error) {

      console.log(error);

    }

  };

  // =========================================
  // TELEMETRIA
  // =========================================

  React.useEffect(() => {

    const obtenerTelemetria = async () => {

      try {

        const response = await fetch(
          `${apiUrl}/api/telemetria`
        );

        const data = await response.json();

        setTelemetria(data);

      } catch (error) {

        console.log(error);

      }

    };
    const cargarUltimosObstaculos = async () => {

  try {

    const response = await fetch(

      `${apiUrl}/api/ultimos_obstaculos`

    );

    const data = await response.json();

    if(data.status){

      setUltimosObstaculos(data.data);

    }

  } catch(error){

    console.log(error);

  }

};
    cargarUltimosObstaculos();
    obtenerTelemetria();

    const intervalo = setInterval(() => {

      obtenerTelemetria();
      cargarUltimosObstaculos();

    }, 1000);

    return () => clearInterval(intervalo);

  }, [apiUrl]);

  // =========================================
  // HISTORIAL
  // =========================================

  React.useEffect(() => {

    const cargarHistorial = async () => {

      try {

        const responseMov =
          await fetch(
            `${apiUrl}/api/ultimo_movimiento`
          );

        const dataMov =
          await responseMov.json();

        setHistorialMovimientos([dataMov]);
        const responseConfig =
          await fetch(
            `${apiUrl}/api/historial_config`
          );

        const dataConfig =
          await responseConfig.json();

        setHistorialConfig(dataConfig);

      } catch(error) {

        console.log(error);

      }

    };

    cargarHistorial();

    const intervalo = setInterval(() => {

      cargarHistorial();

    }, 2000);

    return () => clearInterval(intervalo);

  }, [apiUrl]);

  // =========================================
  // USE EFFECT
  // =========================================

  React.useEffect(() => {

    cargarConfigMotor(
      movimientoSeleccionado
    );

  }, [movimientoSeleccionado]);

  // =========================================
// EJECUTAR MOVIMIENTO
// =========================================

const ejecutarMovimiento = async (idMovimiento) => {

  try {

    await fetch(
      `${apiUrl}/api/movimiento`,
      {
        method: "POST",

        headers: {
          "Content-Type": "application/json"
        },

        body: JSON.stringify({
          id_movimiento: idMovimiento,
          id_dispositivo: 1
        })
      }
    );

  } catch (error) {

    console.log(error);

  }

};

// =========================================
// GUARDAR DEMO
// =========================================

const guardarDemo = async () => {

  try {

    if(!nombreDemo || !secuenciaDemo){

      alert("Completa nombre y secuencia");

      return;

    }

    const response = await fetch(

      `${apiUrl}/api/crear_demo`,

      {

        method: "POST",

        headers: {
          "Content-Type": "application/json"
        },

        body: JSON.stringify({

          nombre: nombreDemo,

          secuencia: secuenciaDemo

        })

      }

    );

    const data = await response.json();

    console.log(data);

    alert("Demo guardada en MySQL 😎");

    setNombreDemo("");

    setSecuenciaDemo("");

  } catch(error) {

    console.log(error);

  }

};

// =========================================
// EJECUTAR DEMO
// =========================================
const ejecutarDemo = async () => {

  try {

    // =====================================
    // OBTENER DEMOS
    // =====================================

    const demosResponse = await fetch(

      `${apiUrl}/api/ver_demos`

    );

    const demos = await demosResponse.json();

    if(demos.length === 0){

      alert("No hay demos");

      return;

    }

    // =====================================
    // ULTIMA DEMO
    // =====================================

    const ultimaDemo = demos[0];

    // =====================================
    // DETALLE DEMO
    // =====================================

    const detalleResponse = await fetch(

      `${apiUrl}/api/ver_demo_detalle/${ultimaDemo.id_demo}`

    );

    const detalle = await detalleResponse.json();

    // =====================================
    // EJECUTAR
    // =====================================

    for (const movimiento of detalle) {

      await ejecutarMovimiento(

        movimiento.id_movimiento

      );

      await new Promise(resolve =>
        setTimeout(resolve, 1500)
      );

    }

  } catch(error) {

    console.log(error);

  }

};
    // =========================================
  // RETURN
  // =========================================

  return (

    <div className="min-h-screen bg-black text-white p-6">

      <div className="max-w-7xl mx-auto">

        {/* HEADER */}

        <div className="rounded-3xl border border-cyan-500 bg-gradient-to-r from-cyan-950 to-black p-6 shadow-2xl shadow-cyan-500/20 mb-8">

          <h1 className="text-5xl font-bold text-cyan-400">
            IoT Smart Car Dashboard
          </h1>

          <p className="text-gray-300 mt-4 text-lg">
            Sistema de control ESP8266 + AWS + WebSocket + MySQL
          </p>

        </div>

        {/* TELEMETRIA */}

        <div className="rounded-3xl border border-cyan-500 p-5 mb-6 bg-zinc-950">

          <h2 className="text-2xl text-cyan-400 mb-4">
            Telemetría
          </h2>

          <div className="grid md:grid-cols-4 gap-4">

            <div className="bg-black rounded-2xl p-4 border border-cyan-700">
              <p className="text-gray-400">Distancia</p>

              <p className="text-3xl font-bold text-cyan-300">
                {telemetria.distancia} cm
              </p>
            </div>

            <div className="bg-black rounded-2xl p-4 border border-cyan-700">
              <p className="text-gray-400">
                Último Movimiento
              </p>

              <p className="text-xl font-bold text-cyan-300">
                {telemetria.ultimo_movimiento}
              </p>
            </div>

            <div className="bg-black rounded-2xl p-4 border border-cyan-700">
              <p className="text-gray-400">
                Obstáculo
              </p>

              <p className="text-2xl font-bold text-cyan-300">
                {telemetria.obstaculo ? "SI" : "NO"}
              </p>
            </div>

            <div className="bg-black rounded-2xl p-4 border border-cyan-700">
              <p className="text-gray-400">
                WebSocket
              </p>

              <p className="text-2xl font-bold text-green-400">
                {telemetria.websocket}
              </p>
            </div>

          </div>

        </div>

        {/* GRID PRINCIPAL */}

        <div className="grid lg:grid-cols-4 gap-6">

          {/* BOTONES */}

          <div className="lg:col-span-3">

            <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">

              {movimientos.map((mov) => (

                <motion.button
                  key={mov.id}

                  onClick={() => ejecutarMovimiento(mov.id)}

                  whileHover={{
                    scale: 1.07,
                    rotate: 1,
                  }}

                  whileTap={{
                    scale: 0.95
                  }}

                  animate={{
                    y: [0, -4, 0]
                  }}

                  transition={{
                    duration: 2,
                    repeat: Infinity
                  }}

                  className={`
                    rounded-3xl
                    border
                    border-cyan-300
                    bg-gradient-to-br
                    ${mov.color}
                    transition-all
                    p-6
                    shadow-xl
                    shadow-cyan-500/20
                    hover:shadow-cyan-300/90
                    hover:border-cyan-100
                    text-left
                    overflow-hidden
                    relative
                  `}
                >

                  <div className="absolute inset-0 bg-white/5 opacity-0 hover:opacity-100 transition-all"></div>

                  <motion.div

                    animate={{
                      rotate: [0, 8, -8, 0]
                    }}

                    transition={{
                      duration: 1.5,
                      repeat: Infinity
                    }}

                    className="text-7xl"
                  >
                    {mov.icono}
                  </motion.div>

                  <div className="mt-4 text-5xl font-bold text-white">
                    {mov.id}
                  </div>

                  <div className="mt-4 text-xl font-semibold">
                    {mov.nombre}
                  </div>

                </motion.button>

              ))}
          <motion.button

            onClick={() => ejecutarDemo()}

            whileHover={{
              scale: 1.07
            }}

            whileTap={{
              scale: 0.95
            }}

            className="
              rounded-3xl
              border
              border-yellow-300
              bg-gradient-to-br
              from-yellow-500
              to-orange-700
              transition-all
              p-6
              shadow-xl
              shadow-yellow-500/30
              text-left
            "
          >

            <div className="text-7xl">
              🤖
            </div>

            <div className="mt-4 text-5xl font-bold text-white">
              DEMO
            </div>

            <div className="mt-4 text-xl font-semibold">
              Ejecutar Demo
            </div>

          </motion.button>

            </div>
            {/* CONFIG DEMO */}

<div className="
  rounded-3xl
  border
  border-yellow-400
  p-6
  bg-zinc-950
  shadow-2xl
  shadow-yellow-500/20
  mt-10
">

  <h2 className="
    text-3xl
    font-bold
    text-yellow-300
    mb-6
  ">
    Configuración Demo
  </h2>

  <div className="
    grid
    md:grid-cols-3
    gap-4
  ">

    {/* NOMBRE */}

    <input
      type="text"

      value={nombreDemo}

      onChange={(e) =>
        setNombreDemo(e.target.value)
      }

      placeholder="Nombre demo"

      className="
        bg-black
        border
        border-yellow-500
        rounded-2xl
        p-4
        text-white
      "
    />

    {/* SECUENCIA */}

      <input
      type="text"

      value={secuenciaDemo}

      onChange={(e) =>
        setSecuenciaDemo(e.target.value)
      }

      placeholder="1,1,8,1,3"

      className="
        bg-black
        border
        border-yellow-500
        rounded-2xl
        p-4
        text-white
      "
    />

    {/* BOTON */}

    <button
     onClick={guardarDemo}
      className="
        bg-yellow-500
        hover:bg-yellow-400
        text-black
        font-bold
        rounded-2xl
        p-4
        transition-all
      "
    >
      Guardar Demo
    </button>

  </div>

</div>
                {/* HISTORIALES */}

<div className="mt-10 space-y-10">
  
  {/* HISTORIAL CONFIG */}

  <div className="
    rounded-3xl
    border
    border-cyan-500
    p-6
    bg-zinc-950
    shadow-2xl
    shadow-cyan-500/20
    overflow-x-auto
  ">

    <h2 className="
      text-3xl
      font-bold
      text-cyan-400
      mb-6
    ">
      Historial Configuración
    </h2>

    <table className="w-full min-w-[850px]">

      <thead>

        <tr className="
          text-cyan-300
          border-b
          border-cyan-700
        ">

          <th className="p-3 text-left">
            Movimiento
          </th>

          <th className="p-3 text-left">
            MIA
          </th>

          <th className="p-3 text-left">
            MIB
          </th>

          <th className="p-3 text-left">
            MITime
          </th>

          <th className="p-3 text-left">
            MDA
          </th>

          <th className="p-3 text-left">
            MDB
          </th>

          <th className="p-3 text-left">
            MDTime
          </th>

        </tr>

      </thead>

      <tbody>

        {historialConfig.map((cfg, index) => (

          <tr
            key={index}

            className="
              border-b
              border-cyan-900
              hover:bg-cyan-500/10
              transition-all
            "
          >

            <td className="
              p-3
              text-white
              font-semibold
            ">
              {cfg.nombre_movimiento}
            </td>

            <td className="p-3 text-cyan-100">
              {cfg.MIA}
            </td>

            <td className="p-3 text-cyan-100">
              {cfg.MIB}
            </td>

            <td className="p-3 text-cyan-100">
              {cfg.MITime}
            </td>

            <td className="p-3 text-cyan-100">
              {cfg.MDA}
            </td>

            <td className="p-3 text-cyan-100">
              {cfg.MDB}
            </td>

            <td className="p-3 text-cyan-100">
              {cfg.MDTime}
            </td>

                      </tr>

                    ))}

                  </tbody>

                </table>

              </div>
              

              </div>
          
                   {/* HISTORIAL OBSTACULOS */}

          <div className="
            rounded-3xl
            border
            border-red-500
            p-6
            bg-zinc-950
            shadow-2xl
            shadow-red-500/20
            overflow-x-auto
            mt-10
          ">

            <h2 className="
              text-3xl
              font-bold
              text-red-400
              mb-6
            ">
              Historial Obstáculos
            </h2>

            <table className="w-full">

              <thead>

                <tr className="
                  text-red-300
                  border-b
                  border-red-700
                ">

                  <th className="p-3 text-left">
                    ID
                  </th>

                  <th className="p-3 text-left">
                    Estatus
                  </th>

                  <th className="p-3 text-left">
                    Fecha
                  </th>

                </tr>

              </thead>

              <tbody>

                {ultimosObstaculos.map((obs, index) => (

                  <tr
                    key={index}

                    className="
                      border-b
                      border-red-900
                      hover:bg-red-500/10
                      transition-all
                    "
                  >

                    <td className="p-3">
                      {obs.id_obs}
                    </td>

                    <td className="p-3 text-red-300 font-bold">
                      {obs.estatus}
                    </td>

                    <td className="p-3">
                      {obs.fecha}
                    </td>

                  </tr>

                ))}

              </tbody>

            </table>

            </div>
          </div>
           
          {/* PANEL DERECHO */}

          <div className="space-y-6">

            {/* CONTROL CENTER */}

            <div className="rounded-3xl border border-cyan-500 bg-cyan-950/40 p-6 shadow-2xl shadow-cyan-500/20 h-fit">

              <h2 className="text-3xl font-bold text-cyan-300 mb-6">
                Control Center
              </h2>

              <div className="space-y-4">

                <div>

                  <label className="text-cyan-200 text-sm">
                    API URL
                  </label>

                  <input
                    type="text"
                    value={apiUrl}

                    onChange={(e) =>
                      setApiUrl(e.target.value)
                    }

                    className="
                      w-full
                      mt-2
                      rounded-2xl
                      bg-black
                      border
                      border-cyan-500
                      p-3
                      text-cyan-300
                    "
                  />

                </div>

                <div className="
                  rounded-2xl
                  bg-green-500/20
                  border
                  border-green-400
                  p-4
                  text-green-300
                  font-semibold
                ">
                  ● ONLINE
                </div>

              </div>

            </div>

            {/* CONFIG MOTOR */}

            <div className="rounded-3xl border border-cyan-500 bg-zinc-950 p-5 shadow-2xl shadow-cyan-500/20 h-fit">

              <h2 className="text-2xl font-bold text-cyan-400 mb-5">
                Control de Velocidad y Tiempo
              </h2>
                            {/* MOVIMIENTO */}

              <div className="mb-4">

                <label className="block mb-2 text-sm text-gray-300">
                  Movimiento
                </label>

                <select

                  value={movimientoSeleccionado}

                  onChange={(e) =>
                    setMovimientoSeleccionado(
                      e.target.value
                    )
                  }

                  className="
                    w-full
                    bg-black
                    border
                    border-cyan-500
                    rounded-xl
                    p-3
                    text-white
                  "
                >

                  {movimientos.map((mov) => (
                    <option
                      key={mov.id}
                      value={mov.id}
                    >
                      {mov.id} - {mov.nombre}
                    </option>
                  ))}

                </select>

              </div>

              {/* INPUTS */}

              {Object.keys(configMotor).map((campo) => (

                <div
                  className="mb-4"
                  key={campo}
                >

                  <label className="block mb-2 text-sm text-gray-300">
                    {campo}
                  </label>

                  <input
                    type="number"
                 
                    value={configMotor[campo]}

                    onChange={(e) => {

                      setConfigMotor({

                        ...configMotor,

                        [campo]: e.target.value

                      });

                      setCamposModificados({

                        ...camposModificados,

                        [campo]: true

                      });

                    }}

                    className={`
                      w-full
                      bg-black
                      border-2
                     ${
                      camposModificados[campo]
                        ? "border-green-400 shadow-lg shadow-green-500/40"
                        : "border-cyan-500"
                    }
                      rounded-xl
                      p-3
                      text-white
                    `}
                  />

                </div>

              ))}

              {/* BOTON */}

              <button

                onClick={guardarConfiguracion}

                className="
                  w-full
                  bg-cyan-500
                  hover:bg-cyan-400
                  text-black
                  font-bold
                  py-3
                  rounded-2xl
                  transition-all
                "
              >
                Guardar Configuración
              </button>

            </div>

        

          </div>

        </div>

      </div>

    </div>

  );

}