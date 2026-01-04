from sklearn.linear_model import LogisticRegression

#Prediccion de aprobacion en base a horas de estudio
x = int(input("Ingrese del 1 al 5 las horas de estudio: "))

X = [[1], [2], [3], [4], [5]]
y = [0, 0, 0, 1, 1]

modelo = LogisticRegression()
modelo.fit(X, y)

horas_nuevas = [[x]]
prediccion = modelo.predict(horas_nuevas)

print("¿Aprueba el examen?", "Sí" if prediccion[0] == 1 else "No")
