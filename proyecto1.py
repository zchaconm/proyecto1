#problema1: Dado un entero, determinar si es par.
def prob_1 (n):
	if n % 2 == 2:
		return True
	else:
		return False 

#problema2: Dado un número real representando una temperatura 
#en grados Farenheit, encontrar su equivalente en grados Celcios.
def prob_2 (n):
	Celsius = (n - 32) * 5/9
	return Celsius

#problema3: Dados dos enteros (base y potencia, en este orden), determinar 
#manualmente el valor que se obtiene al evaluar base^potencia.
def prob_3 (a,b):
	potencia = a ** b
	return potencia

#problema4: Dada una hilera de caracteres y una longitud de párrafo
#(en este orden), devolver una hilera de caracteres que centre 
#la palabra en un párrafo de ancho como el dado, utilizando de 
#relleno asteriscos. 
def prob_4 (a):
	hilera = (("*"*a) + "2013" + ("*"*a))
	return hilera

#Problema5: Dadas dos listas, representando dos vectores, 
#encuentre el vector resultante del producto cruz entre ambos vectores dados.
def prob_5 (a,b):
	
