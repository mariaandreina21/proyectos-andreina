import streamlit as st
import pandas as pd
st.title('Mi Primera Aplicación en Streamlit')
st.title('Maria Andreina Castro')
with st.form(key="mi_formulario"):
    st.sidebar.text_input('Mostrar nombre')
    nombre = st.text_input("Nombre")
    if nombre:
        st.write(f"Hola, {nombre}!")
    number = st.number_input("Inserte su edad", min_value=0, max_value=100, value=0)
    st.write("Su edad es ", number)
    mes = st.slider("seleccione un mes", min_value=1, max_value=12, value=1)
    st.write("El mes seleccionado es ", mes)
    st.sidebar.slider("Seleccione mes", min_value=1, max_value=12, value=1)
    agree = st.checkbox("Acepto los terminos y condiciones")
    if agree:
        st.write("Gracias por aceptar los terminos y condiciones!")
    genre = st.radio(
    "Genero con el que se identifica",
    ["Femenino", "Masculino", "Otro"],
        )
    if genre == "Femenino":
        st.write("Usted es una mujer")
    elif genre == "Masculino":
        st.write("Usted es un hombre")
    else:
        st.write("selecciono otro genero")
    option = st.selectbox(
        "seleccione un Pais",
        ("Colombia", "Peru", "Chile", "Brasil", "Argentina", "Venezuela", "Ecuador", "Uruguay", "Paraguay", "Bolivia", "Costa Rica", "Honduras", "Nicaragua", "El Salvador", "Guatemala", "Panama", "Cuba", "Haiti", "Dominica", "Republica Dominicana", "Puerto Rico", "Belize", "Jamaica", "Trinidad y Tobago", "Bahamas", "Barbados", "Grenada", "San Cristobal y Nieves", "Santa Lucia", "Saint Vincent y las Granadinas", "Antigua y Barbuda", "Cayman", "Islas Caiman", "Islas Turcas y Caicos", "Islas Vírgenes Británicas", "Islas Vírgenes de los Estados Unidos", "Islas Caiman", "Islas Vírgenes Británicas", "Islas Vírgenes de los Estados Unidos", "Islas Caiman", "Islas Vírgenes Británicas", "Islas Vírgenes de los Estados Unidos"),
        )
    st.write("Usted selecciono el pais de ", option)
    import pandas as pd
    from io import StringIO

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)

        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)

        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)
    import datetime
    d = st.date_input("cuando es su cumpleaños", value=None)
    st.write("su cumpleaños es:", d)
    submit_button = st.form_submit_button(label="enviar")
t = st.time_input("inserte la hora de la alarma", value=None)
st.write("la alarma es a las:", t)
st.title("Terminado")