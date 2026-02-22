# LIBRERÍAS IMPORTADAS ------------------------------------------------
import pandas as pd
import streamlit as st


# ESTILOS ---------------------------------------------------

st.set_page_config(
    page_title="Módulo 1",
    layout="wide")
st.set_page_config(layout="wide")
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #39403A, #2F2F40);
    color: 242424;
    font-family: 'Segoe UI', sans-serif;
}

h1 { color: red; }
h2, h3 { color: blue; }

label, .stMarkdown, .stText {
    color: white !important;
}
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #292929, #292929);
}
section[data-testid="stSidebar"] * {
    color: ligthblue !important;
}

.stButton > button {
    background: linear-gradient(90deg, #2563eb, #3b82f6);
    color: white;
    border-radius: 10px;
    border: none;
    padding: 0.6rem 1rem;
    font-weight: 600;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #1d4ed8, #2563eb);
    transform: scale(1.05);
}

.tarjeta {
    background-color: rgba(0, 0, 0, 0.6);    
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)

# MENU LATERAL ------------------------------------------
st.sidebar.title("📋 Listado de Ejercicios")

opcion = st.sidebar.selectbox(
    "-------------------",
    ["🛖 Home", "✨ Ejercicio 1", "✨ Ejercicio 2", "✨ Ejercicio 3", "✨ Ejercicio 4"]
)

# HOME ------------------------------------------------

if opcion == "🛖 Home":

    st.set_page_config(layout="wide")
    st.image(
    "https://cdn.pixabay.com/photo/2018/02/23/11/35/company-3175300_1280.jpg",
    use_container_width=True
)
    st.title("🐍 💰 Casos Financieros")
    st.markdown("---")

    st.markdown("Desarrollado Por: **Kevin Javier Piscoche Rodriguez**")
    st.markdown("Curso: **Especialización de Python for Analytics**")
    st.markdown("---")
      
    st.markdown("## Conceptos desarrollados:")
    st.markdown("""
    Proyecto nombrado **Sistema de Gestión Financiera Interactivo**, 
    donde se aplican conceptos como: Variables y Condicionales, Listas y Diccionarios, funciones y POO.

    Herramientas utilizadas:
    - 🐍 Python | 🚀 Streamlit | 📊 Pandas
    """)

    st.markdown("""
    <div class="tarjeta">
    ⬅️ En el menú lateral contará con 4 ejercicios donde se aplican los conceptos visto previamente en clase.
    </div>
    """, unsafe_allow_html=True)

# ----------------------------------------------- EJERCICIOS ---------------------------------------------

#EJERCICIO 1 --------------------------------
elif opcion == "✨ Ejercicio 1":

    st.header("1️⃣ Presupuesto vs Gasto")

    presupuesto = st.number_input("💰 Ingrese presupuesto mensual (S/.)", min_value=0.0)
    gasto = st.number_input("💸 Ingrese gasto mensual (S/.)", min_value=0.0)

    if st.button("Evaluar"):
        if gasto > presupuesto:
            st.error(f"❌ Se excedió del presupuesto en S/{gasto - presupuesto:,.2f}")        
        else:
            st.success(f"✅ Se Ahorra S/{presupuesto - gasto:,.2f}")

# EJERCICIO 2 -------------------------------

elif opcion == "✨ Ejercicio 2":

    st.header("2️⃣ Actividades registradas")

    if "lista_actividades" not in st.session_state:
        st.session_state.lista_actividades = []

    nombre = st.text_input("Registre Actividad:")
    tipo = st.selectbox("Tipo:", ["💰 Ingreso", "💸 Gasto", "🐖 Ahorro", "📈 Inversión"])
    presupuesto = st.number_input("Presupuesto (S/.)", min_value=0.0)
    gasto = st.number_input("Gasto Real (S/.)", min_value=0.0)

    if st.button("➕ Agregar"):
        if nombre:
            st.session_state.lista_actividades.append({
                "nombre": nombre,
                "tipo": tipo,
                "presupuesto": presupuesto,
                "gasto": gasto
            })
            st.success("Actividad Agregada")
            st.success("Puede registrar otra Actividad")
            st.rerun()

    if st.session_state.lista_actividades:
        df = pd.DataFrame(st.session_state.lista_actividades)
        df["diferencia"] = df["presupuesto"] - df["gasto"]
        st.dataframe(df)

# EJERCICIO 3 -------------------------------

elif opcion == "✨ Ejercicio 3":

    st.header("3️⃣ Programación Funcional")
    st.subheader("| Sistema de Retorno de Inversión")

    if 'registro_inversiones' not in st.session_state:
        st.session_state.registro_inversiones = []

    def calcular_retorno(monto, tasa, meses):
        return monto * tasa * meses

    nombre = st.text_input("Nombre de la inversión:")

    columna1, columna2, columna3 = st.columns(3)

    with columna1:
        monto = st.number_input("Monto invertido (S/):", min_value=0.0, value=10000.0)

    with columna2:
        tasa = st.number_input("Tasa (%):", min_value=0.0, max_value=100.0, value=5.0) / 100

    with columna3:
        meses = st.number_input("Meses:", min_value=1, max_value=60, value=12)

    if st.button("➕ Agregar inversión"):
        if nombre:
            st.session_state.registro_inversiones.append({
                "nombre": nombre,
                "monto": monto,
                "tasa": tasa,
                "meses": meses
            })
            st.success("Inversión agregada")
            st.rerun()

    if st.session_state.registro_inversiones:

        resultados = list(map(
            lambda inv: {
                "nombre": inv["nombre"],
                "monto": inv["monto"],
                "retorno": calcular_retorno(inv["monto"], inv["tasa"], inv["meses"])
            },
            st.session_state.registro_inversiones
        ))

        for r in resultados:
            st.write(f"**{r['nombre']}** → Inversión: S/{r['monto']:,.0f} | Retorno: S/{r['retorno']:,.0f}")

# EJERCICIO 4 -------------------------------

elif opcion == "✨ Ejercicio 4":

    st.header("4️⃣ Programación Orientada a Objetos")
    st.subheader("|POO")

    class Actividad:

        def __init__(self, nombre, tipo, presupuesto, gasto):
            self.nombre = nombre
            self.tipo = tipo
            self.presupuesto = presupuesto
            self.gasto = gasto

        def esta_en_presupuesto(self):
            return self.gasto <= self.presupuesto

        def mostrar_info(self):
            diferencia = self.presupuesto - self.gasto
            estado = "✅ En presupuesto" if self.esta_en_presupuesto() else "❌ Fuera del presupuesto"
            return f"""
            ### {self.nombre}
            Tipo: {self.tipo}
            Presupuesto: S/{self.presupuesto:,.2f}
            Gasto: S/{self.gasto:,.2f}
            Diferencia: S/{diferencia:,.2f}
            {estado}
            """

    if 'objetos' not in st.session_state:
        st.session_state.objetos = []

    nombre = st.text_input("Ingrese Nombre actividad:")
    tipo = st.selectbox("Seleccione Tipo:", ["💰 Ingreso", "💸 Gasto", "🐖 Ahorro", "📈 Inversión"])
    presupuesto = st.number_input("Presupuesto (S/.)", 0.0)
    gasto = st.number_input("Gasto Real (S/.)", 0.0)

    if st.button("Crear objeto"):
        if nombre:
            st.session_state.objetos.append(
                Actividad(nombre, tipo ,presupuesto, gasto)
            )
            st.rerun()

    for i, obj in enumerate(st.session_state.objetos):
        "---"
        st.markdown(obj.mostrar_info())
        
