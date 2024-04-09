
# PAQUETES
from tensorflow.keras.models import load_model
import joblib
import datetime
import pandas as pd
import numpy as np
import pickle


# (1) FUNCIÓN DE PREDICCIÓN DEL MODELO DE REDES
def lstm_pred(df, model, scalerm, periodos_pred = 8):

    """
    Forecast recursive prediction using Keras model. 
    
    Parameters
    ---------------
    df: Dataframe object of observed values with index as date and one column with data.
    model: Pretrained model used for predition.
    scalerm: Scaler used during training.
    periodos_pred: number periods (weeks) a predecir
    """

    pronostico_niveles = [df.iloc[-1][0]]
    
    #Pre-procesamiento de los datos
    lags = model.input_shape[1] #numero_lags
    df = df.pct_change()*100
    df = df.dropna()
    Ys_all = scalerm.transform(df) #transformar la serie

    #Reshap de la serie para la lectura del modeo
    Y_ph = Ys_all[-lags:] 
    Y_ph = Y_ph.reshape(1, lags, 1)

    #Rango de fechas (semanas)
    week_1 = df.index[-1] + datetime.timedelta(days=7)
    week_f = week_1 + datetime.timedelta(weeks=periodos_pred)
    range_date = pd.date_range(start= week_1, end= week_f, freq = "W-MON")

    #Predicción
    for i in range(len(range_date)):
        Y_pred = model.predict(Y_ph[:, i : lags+i+1, :], verbose=0)
        Y_ph = np.append(Y_ph, Y_pred).reshape(1, len(Y_ph[0])+1, 1)

    #Re-escalar (traer a cambios porcentuales)
    Y_ph = scalerm.inverse_transform(Y_ph[0][lags:])
    pronostico_variacion = Y_ph.reshape(len(Y_ph))
    

    #Traer a niveles
    for i in range(len(pronostico_variacion)):
        ynsetp = (pronostico_variacion[i]/100 + 1)*pronostico_niveles[i]
        pronostico_niveles.append(ynsetp)

    #Predicciones y eje (fecha)
    predictions = pronostico_niveles[1:]
    prediction_xaxis = []

    for i in range(len(range_date)):
        k = str(range_date[i])[0:10]
        prediction_xaxis.append(k)
        

    return dict(zip(prediction_xaxis[:-1], list(predictions)[:-1]))
    # return predictions


# (2) FUNCIÓN DE PREDICCIÓN DEL MODELO DE SERIES DE TIEMPO
def sarimax_pred(model, periods, last_date):

    # Obtener las fechas de los pasos hacia adelante a pronosticar
    last_date  = last_date + datetime.timedelta(days=7)
    pred_index = pd.date_range(last_date, periods=periods, freq='W-MON')

    # Realizar la predicción de los pasos hacia adelante
    pred = model.predict(n_periods=periods)

    # Crear un diccionario con las fechas de la predicción como llave y la predicción como valor
    pred_dict = {str(date.date()): pred[i] for i, date in enumerate(pred_index)}

    return pred_dict


# (3) FUNCIÓN DE PREDICCIÓN DEL AMBOS MODELOS
def combinacion_pred(df, modelo_red, modelo_arima, scaler, numperiodos):

    #PREPARACIÓN PREVIA DE LOS DATOS
    fecha_final = df["WEEK"].iloc[-1]

    itbmpp = df.copy()
    itbmpp = itbmpp.rename(columns = {"ITMBPP": "q"})
    itbmpp = itbmpp[["WEEK", "q"]]
    itbmpp = itbmpp.set_index("WEEK") 

    #MODELOS
    c1 = lstm_pred(itbmpp, modelo_red, scaler, numperiodos) #MODELO RED
    c2 = sarimax_pred(modelo_arima,  numperiodos, fecha_final) #MODELO 

    resultado = {clave: c1[clave] * c2[clave] for clave in c1.keys()}

    return resultado