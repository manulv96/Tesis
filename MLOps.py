import pandas as pd
from joblib import load

model= load('agn_variability_class')

import streamlit as st

#class_dict = {
#    "0": "No Variable",
#    "1": "Variable"
#}

st.title("Clasificación de Blazares")

st.subheader("Esta página utiliza tus datos observacionales de un AGN para clasificarlo en variable o no variable")

st.caption("Escribir a continuacón en los campos que correspondan las siguientes medidas:")

st.caption("* Media")
st.caption("* Varianza")
st.caption("* Sesgo")
st.caption("* Kurtosis")

st.caption("Previamente usted tiene que calibrar los datos del AGN utilizando estrellas de comparación. ")

val1 = st.number_input("Media", value=None, placeholder="Type a number...") 
st.write("El valor ingresado es ", val1)
val2 = st.number_input("Varianza",value=None, placeholder="Type a number..." ) 
st.write("El valor ingresado es ", val2)
val3 = st.number_input("Sesgo", value=None, placeholder="Type a number...") 
st.write("El valor ingresado es ", val3)
val4 = st.number_input("Kurtosis", value=None, placeholder="Type a number...")
st.write("El valor ingresado es ", val4)

X_pred=pd.DataFrame(columns=['mag_mean', 'mag_var', 'mag_skew', 'mag_kurt'])


def pipeline(mean, var, skew, kurt):
    X_pred=pd.DataFrame(columns=['mag_mean', 'mag_var', 'mag_skew', 'mag_kurt'])
    X_pred.loc[0,:]=[mean,var,skew,kurt]
    return model.predict(X_pred)[0]


if st.button("Clasificar"):

    prediction = pipeline(val1,val2,val3,val4)
    if prediction == 1:

        st.write("El Blazar es variable")
    else:

        st.write("El Blazar es no variable")
