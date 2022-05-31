import pandas as pd
import matplotlib.pyplot as plt
from pycodestyle import tabs_obsolete

url = "" """ Ingrese la URL respectiva de sus datos de COVID 19"""
data = pd.read_csv(url)

# Eliminar columnas del dataSet
data.drop('Código ISO del país', axis = 1, inplace=True)
data.drop('Nombre del país', axis = 1, inplace=True)
data.drop('Pertenencia étnica', axis = 1, inplace=True)
data.drop('Nombre del grupo étnico', axis = 1, inplace=True)
data.drop('Fecha de inicio de síntomas', axis = 1, inplace=True)
data.drop('Unidad de medida de edad', axis = 1, inplace=True)
data.drop('Código DIVIPOLA departamento', axis = 1, inplace=True)
data.drop('Código DIVIPOLA municipio', axis = 1, inplace=True)
data.drop('ID de caso', axis = 1, inplace=True)

# Normalizar la columna de Estado

data.loc[data['Estado'] == 'leve'] = 'Leve'
data.loc[data['Estado'] == 'LEVE'] = 'Leve'

# Normalizar columna sexo

data.loc[data['Sexo'] == 'm'] = 'M'
data.loc[data['Sexo'] == 'f'] = 'F'

# Normalizar columna Estado

data.loc[data['Estado'] == 'M'] = 'Moderado'
data.loc[data['Sexo'] == 'F'] = 'Fallecido'

# Normalizar columna Ubicacion del caso
data.loc[data['Ubicación del caso'] == 'casa'] = 'Casa'
data.loc[data['Ubicación del caso'] == 'CASA'] = 'Casa'

# Normalizar columna de Recuperado
data.loc[data['Recuperado'] == 'fallecido'] = 'Fallecido'


#print(data.columns)

# Número de casos de contagios en el país
#contagiosTotales = data.shape[0]
#print(f"El número de casos totales de COVID-19 son: {contagiosTotales}")

# Número de municipios afectados
#NumeroMunicipiosAfectados = len(data['Nombre municipio'].value_counts())
#print(f"El número de municipios afectados es de: {NumeroMunicipiosAfectados}, de un total de 1103 municipios en todo el país")

# Lista de los municipios afectados
#municipiosAfectados = set(data['Nombre municipio'])
#print(municipiosAfectados)

# Número de personas que se encuentran en atención en casa
#atencionEnCasa = len(data.loc[data['Ubicación del caso'] == 'Casa'])
#print(f"El número de personas que están siendo atendida en casa es de: {atencionEnCasa}")


# Número de personas que se encuentran recuperados
#numeroRecuperados = len(data.loc[data['Recuperado'] == 'Recuperado'])
#print(f"El número de personas que se han recuperado es de: {numeroRecuperados}")

# Número de personas que han fallecido
#numeroFallecidos = len(data.loc[data['Recuperado'] == 'Fallecido'])
#print(f"El número de personas que han fallecido es de: {numeroFallecidos}")


# Ordenar de Mayor a menor por tipo de caso (Importado, en estudio, Relacionado)
#aux = data.loc[(data['Tipo de contagio'] == 'Importado') | (data['Tipo de contagio'] == 'Relacionado') | (data['Tipo de contagio'] == 'En estudio')]
#tipoCasoContagio = aux['Tipo de contagio'].value_counts()
#print(tipoCasoContagio)


# Número de departamentos afectados
#numeroDepartamentosAfectados = len(data['Nombre departamento'].value_counts())
#print(f"El número de departamentos afectados es de {numeroDepartamentosAfectados}")

# Lista de departamentos afectados
#depatamentossAfectados = set(data['Nombre departamento'])
#print(depatamentossAfectados)

# Ordenar de mayor a menor por tipo de recuoperación (Tipo de atención no existe)
#ordenarTipoAtencion = data['Tipo de recuperación'].value_counts()
#print(ordenarTipoAtencion)


# Listar de mayor a menor los 10 departamentos con más casos de contagios
#top10DepartamentosContagiados = data['Nombre departamento'].value_counts().head(10)
#print(top10DepartamentosContagiados)

# Listar de mayor a menor los 10 departamentos con más fallecidos
#aux = data.loc[data['Recuperado'] == 'Fallecido']
#top10DepartamentosConMasFallecidos = aux['Nombre departamento'].value_counts().head(10)
#print(top10DepartamentosConMasFallecidos)


# Listar de mayor a menor los 10 departamentos con más recuperados
#aux = data.loc[data['Recuperado'] == 'Recuperado']
#top10DepartamentosConMasRecuperados = aux['Nombre departamento'].value_counts().head(10)
#print(top10DepartamentosConMasRecuperados)

# Listar de mayor a menor los 10 municipios con más casos de contagios
#top10MunicipiosConMasContagios = data['Nombre de municipio'].value_counts().head(10)
#print(top10MunicipiosConMasContagios)


# Liste de mayor a menor los 10 municipios con mas casos de
# fallecidos
# aux = data.loc[data['Recuperado'] == 'Fallecido']
# municipiosConMasMuertos = aux['Nombre municipio'].value_counts().head(10)
# print(municipiosConMasMuertos)


#Liste de mayor a menor los 10 municipios con mas casos de
#recuperados
#aux = data.loc[data['Recuperado'] == 'Recuperado']
#municipiosConMasRecuperados = aux['Nombre municipio'].value_counts().head(10)
#print(municipiosConMasRecuperados)



#Liste agrupado por departamento y en orden de Mayor a menor las
#ciudades con mas casos de contagiados
#top10Contagiados = data.groupby(['Nombre departamento'])
#print(top10Contagiados['Nombre municipio'].value_counts())



""" Realizado hasta la consulta 17 """