from sklearn.neighbors import KNeighborsClassifier

#Clasificacion de frutas
tamano = float(input("Ingrese el tamaño: "))
color = float(input("Ingrese el color (0 o 1): "))

X = [[1,0], [1,0], [2,1], [2,1]]  
y = ["manzana", "manzana", "pera", "pera"] 

modelo = KNeighborsClassifier(n_neighbors=1)
modelo.fit(X, y) 

fruta_nueva = [[tamano,color]]
prediccion = modelo.predict(fruta_nueva)

print("La fruta nueva es:", prediccion[0])
