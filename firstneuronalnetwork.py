# -*- coding: utf-8 -*-
"""FirstNeuronalNetwork.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I80HzVVKgPaaT6wLRnwkRLFE_QmdCIGu

# **Red neuronal para convertir grados celsius a fahrenheit.**

Importamos las librerias a utilizar:


*   `tensorflow`: libreria para IA de google
*   `numpy`: libreria para arreglos numericos
"""

import tensorflow as tf
import numpy as np

"""Declaramos un arreglo de numeros (celsius) para establecer los valores de los grados celsius y un arreglo (fahrenheit) para los resultados en grados fahrenheit."""

celsius = np.array([-40, -10, 0, 8, 15, 22, 38])
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100])

"""Diseñamos el modelo de red neuronal utilizando el framework Keras.
Especificamos la capa de entrada y salida, inicializamos la primera capa como una capa densa, estas son las que tienen conexiones a todas las neruonas de la siguiente capa.

*   `units`: neuronas de la capa
*   `input_shape`: una entrada con una neurona

El modelo a utilizar es el modelo secuencial, como argumento se coloca la capa que se ha creado.
"""

capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

"""Compilamos, preparamos el modelo a ser entrenado.

*   `optimizer`: permite a la red saber como ajustar los pesos de manera eficiente para que aprenda, el argumento indica la taza de aprendizaje, es decir que tanto ajustar los sesgos y pesos.
*   `loss`: funcion de perdida.
"""

modelo.compile(
    optimizer = tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

"""Entrenamiento del modelo.


1.   Elementos de entrada
2.   Elementos de salida
3.   Numero de epocas o vueltas
4.   estado de entrenamiento (impresion de estado)




"""

print('Comenzando el entrenamiento')
historical = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
print('Modelo entrenado!!!')

"""Se muestra la grafica con la magnitud de error de acuerdo a las epocas de entrenamiento."""

import matplotlib.pyplot as plt
plt.xlabel("# epoca")
plt.ylabel("Magnitud perdida")
plt.plot(historical.history["loss"])

"""Prueba del modelo"""

print("Realizando predicción")
resultado = modelo.predict([100])
print("El resultado es " + str(resultado) + " fahrenheit!!")

"""valores que se asignaron a los pesos y sesgo"""

print("variables internas del modelo")
print(capa.get_weights())