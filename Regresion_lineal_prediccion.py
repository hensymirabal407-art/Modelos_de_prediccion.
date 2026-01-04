from sklearn.linear_model import LinearRegression

#Prediccion de ahorros por semana
x = int(input("Ingrese la semana: "))

X = [[1], [2], [3], [4], [5]]  
y = [10, 20, 30, 40, 50]       

modelo = LinearRegression()
modelo.fit(X, y)

semanas_nuevas = [[x]]
prediccion = modelo.predict(semanas_nuevas)

print("Dinero estimado después de 6 semanas:", round(prediccion[0], 2), "dólares")
