#naivaBayes

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from matplotlib.colors import ListedColormap

# Cargar el dataset Iris
iris = load_iris()
X = iris.data[:, :2]  # Usamos solo las dos primeras características (longitud y ancho del sépalo) para graficar
y = iris.target
class_names = iris.target_names

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Crear el modelo Naive Bayes
model = GaussianNB()
model.fit(X_train, y_train)

# Predecir en el conjunto de prueba
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy:.2f}")

# Gráfica de las fronteras de decisión
def plot_decision_boundaries(X, y, model, class_names):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))

    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Colores para las fronteras
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

    plt.figure(figsize=(10, 6))
    plt.contourf(xx, yy, Z, alpha=0.8, cmap=cmap_light)
    scatter = plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor='k', s=30)
    handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) 
               for color in cmap_bold.colors]
    plt.legend(handles, class_names, loc='upper right')
    plt.xlabel('Longitud del Sépalo')
    plt.ylabel('Ancho del Sépalo')
    plt.title('Fronteras de decisión del modelo Naive Bayes')
    plt.grid(True)
    plt.show()

# Mostrar la gráfica
plot_decision_boundaries(X, y, model, class_names)

# Predicciones en el conjunto de prueba
for i in range(len(y_test)):
    print(f"Predicción: {class_names[y_pred[i]]}, Real: {class_names[y_test[i]]}")
