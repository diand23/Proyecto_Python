# Instalación de librerias
pip install pandas openpyxl xlrd
%pip install seaborn

# Verificar el directorio de trabajo actual
import os
print(os.getcwd())

# Importar las librerías necesarias
import pandas as pd
import numpy as np 

# Cargar el archivo Excel
df_excel = pd.read_csv('StudentsSocialMediaAddiction_Bruto.csv')  # si existiera
df_excel.head()  # Mostrar las primeras filas del DataFrame

# Para ver el tipo de variable que hay en cada columna
df_excel.dtypes

import numpy as np 

# 1. Limpieza de la columna Age: 
df_excel["Age"] = df_excel["Age"].astype(str)
# strip() elimina los espacios en blanco al principio y al final de la cadena
# lower() convierte la cadena a minúsculas
for i in range(len(df_excel)):
    valor = df_excel.loc[i, "Age"].strip().lower() 
    #.loc es un acceso basado en etiquetas para seleccionar 
    # #y modificar datos en un DataFrame de pandas.

    if valor == "diecinueve":
                df_excel.loc[i, "Age"] = 19
    if valor == "veinte":
                 df_excel.loc[i, "Age"] = 20
    if valor == "veintidos":
        df_excel.loc[i, "Age"] = 22
    if "," in valor:
        valor = valor.replace(",",".")
        try:
            df_excel.loc[i, "Age"] = int(float(valor))
        except:
            df_excel.loc[i, "Age"] = None

#Para esta columna que contiene errores más complejos, combierto el formato de str a int aquí
df_excel["Age"] = pd.to_numeric(df_excel["Age"], errors="raise")  # Convierte str → números
df_excel["Age"] = df_excel["Age"].astype("Int64")                 # Convierte float → Int64

df_excel.head()  # Mostrar las primeras filas del DataFrame

#Para comprobar que en casos donde aparece por ejemplo 20,5 obtenemos 20
df_excel.loc[354]     # Muestra la fila con índice 5 (según etiqueta) 

# 2. Limpieza de la columna Gender:
# Poner todas las palabras con la primera letra en mayúscula
# y cambiar las que tengan un valor mujer o hombre.
df_excel["Gender"] = df_excel["Gender"].astype(str)
# strip() elimina los espacios en blanco al principio y al final de la cadena
# lower() convierte la cadena a minúsculas
for i in range(len(df_excel)):
    valor = df_excel.loc[i, "Gender"].strip().lower()
    
    if valor == 'female' or valor == 'male':
        df_excel.loc[i, "Gender"] = valor.capitalize()
    elif valor == 'mujer':
        df_excel.loc[i, "Gender"] = "Female"
    elif valor == 'hombre':
        df_excel.loc[i, "Gender"] = "Male"

df_excel.head()  # Verificar el tipo de datos después de la conversión

# 3. Limpieza de la columna Academic_Level:
# Poner todas las palabras con la primera letra en mayúscula
df_excel["Academic_Level"] = df_excel["Academic_Level"].astype(str)
# strip() elimina los espacios en blanco al principio y al final de la cadena
# lower() convierte la cadena a minúsculas
for i in range(len(df_excel)):
    valor = df_excel.loc[i, "Academic_Level"].strip().lower()
    df_excel.loc[i, "Academic_Level"] = valor.capitalize()

df_excel.head()  # Verificar el tipo de datos después de la conversión

# 4. Poner todos los países en un mismo formato.
df_excel["Country"] = df_excel["Country"].astype(str)
# strip() elimina los espacios en blanco al principio y al final de la cadena
# lower() convierte la cadena a minúsculas
for i in range(len(df_excel)):
    valor = df_excel.loc[i, "Country"].strip().lower()
    df_excel.loc[i, "Country"] = valor.capitalize()

df_excel.head()  # Verificar el tipo de datos después de la conversión

# 5. Poner todos los valores con el mismo formato decimal.
df_excel["Avg_Daily_Usage_Hours"] = df_excel["Avg_Daily_Usage_Hours"].astype(str)
# strip() elimina los espacios en blanco al principio y al final de la cadena
for i in range(len(df_excel)):
    valor = df_excel.loc[i, "Avg_Daily_Usage_Hours"].strip()
    
    try:
        df_excel.loc[i, "Avg_Daily_Usage_Hours"] = df_excel.loc[i,"Avg_Daily_Usage_Hours"].replace(",", ".")
    except:
        df_excel.loc[i, "Avg_Daily_Usage_Hours"] = None

df_excel.head()  # Verificar el tipo de datos después de la conversión

# 6. Limpieza de la columna "Most_Used_Platform":
# Poner todas las palabras con la primera letra en mayúscula

df_excel["Most_Used_Platform"] = df_excel["Most_Used_Platform"].astype(str)
# strip() elimina los espacios en blanco al principio y al final de la cadena
# lower() convierte la cadena a minúsculas
for i in range(len(df_excel)):
    valor = df_excel.loc[i, "Most_Used_Platform"].strip().lower()
    try:
        df_excel.loc[i, "Most_Used_Platform"] = valor.capitalize()
    except:
        df_excel.loc[i, "Most_Used_Platform"] = None

df_excel.head()  # Verificar el tipo de datos después de la conversión

# 7. Limpieza de la columna "Affects_Academic_Performance":
# Indicar que solo esté escrito Yes o No
df_excel["Affects_Academic_Performance"] = df_excel["Affects_Academic_Performance"].astype(str)
# strip() elimina los espacios en blanco al principio y al final de la cadena
# lower() convierte la cadena a minúsculas
for i in range(len(df_excel)):
    valor = df_excel.loc[i, "Affects_Academic_Performance"].strip().lower()
    try:
        df_excel.loc[i, "Affects_Academic_Performance"] = valor.capitalize()
    except:
        df_excel.loc[i, "Affects_Academic_Performance"] = None

for i in range(len(df_excel)):
    valor = df_excel.loc[i, "Affects_Academic_Performance"].strip().lower()
    if valor == "Si" or valor == "Sí":
        df_excel.loc[i, "Affects_Academic_Performance"] = valor.replace("Si", "Yes").replace("Sí", "Yes")

df_excel.head()  # Verificar el tipo de datos después de la conversión

# 8. Limpieza de la columna Sleep_Hours_Per_Night:
# Poner todas las celdas en un mismo formato.
df_excel["Sleep_Hours_Per_Night"] = df_excel["Sleep_Hours_Per_Night"].astype(str)
# strip() elimina los espacios en blanco al principio y al final de la cadena
for i in range(len(df_excel)):
    valor = df_excel.loc[i, "Sleep_Hours_Per_Night"].strip()
    
    try:
        df_excel.loc[i, "Sleep_Hours_Per_Night"] = df_excel.loc[i,"Sleep_Hours_Per_Night"].replace(",", ".")
    except:
        df_excel.loc[i, "Sleep_Hours_Per_Night"] = None

df_excel.head()  # Verificar el tipo de datos después de la conversión

# 9. En este apartado vamos a tranformar el formato de columna correspondiente a los valores introducidos. 
# Una vez que se ha limpiado las columnas.
df_excel["Student_ID"] = pd.Series(df_excel["Student_ID"], dtype="Int64")
df_excel["Gender"] = pd.Series(df_excel["Gender"], dtype="str")
df_excel["Academic_Level"] = pd.Series(df_excel["Academic_Level"], dtype="str")
df_excel["Country"] = pd.Series(df_excel["Country"], dtype="str")
df_excel["Avg_Daily_Usage_Hours"] = pd.Series(df_excel["Avg_Daily_Usage_Hours"], dtype="Float64")
df_excel["Most_Used_Platform"] = pd.Series(df_excel["Most_Used_Platform"], dtype="str")
df_excel["Affects_Academic_Performance"] = pd.Series(df_excel["Affects_Academic_Performance"], dtype="str")
df_excel["Sleep_Hours_Per_Night"] = pd.Series(df_excel["Sleep_Hours_Per_Night"], dtype="Float64")
df_excel["Mental_Health_Score"] = pd.Series(df_excel["Mental_Health_Score"], dtype="Int64")
df_excel["Relationship_Status"] = pd.Series(df_excel["Relationship_Status"], dtype="str")
df_excel["Conflicts_Over_Social_Media"] = pd.Series(df_excel["Conflicts_Over_Social_Media"], dtype="Int64")
df_excel["Addicted_Score"] = pd.Series(df_excel["Addicted_Score"], dtype="Int64")

df_excel.dtypes  # Verificar el tipo de datos después de la conversión

# Verificar si hay valores nulos. En este caso comprobamos que no hay.
df_excel.isnull().sum()

# Descargar el archivo limpio
df_excel.to_csv('StudentsSocialMediaAddiction_Clean.csv', index=False)  # Guardar el DataFrame limpio en un nuevo archivo CSV

# Análisis exploratorio de datos
df_excel[
    ['Age', 'Avg_Daily_Usage_Hours', 'Sleep_Hours_Per_Night',
     'Mental_Health_Score', 'Conflicts_Over_Social_Media', 'Addicted_Score']
].describe()

# Representación gráfica de los datos

import seaborn as sns
import matplotlib.pyplot as plt

#Ignorar los warnings de seaborn
import warnings
warnings.filterwarnings("ignore")

# Gráfico de líneas con horas de sueño por grupo de edad y género
sns.lineplot(data=df_excel, x="Age", y="Mental_Health_Score", hue="Gender", marker="o",
                          palette={"Female":"#C71585","Male": "orange"})


plt.title("Salud mental promedio por grupo de edad y género")
plt.xlabel("Grupo de edad")
plt.ylabel("Horas promedio de sueño")
plt.grid(True)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Agrupar por edad y género y calcular el promedio
grouped = df_excel.groupby(["Age", "Gender"])["Mental_Health_Score"].mean()

# Convertir el índice para que cada género sea una columna
pivoted = grouped.unstack()  # Ahora tienes: Age como índice, Gender como columnas

# Graficar
pivoted.plot(kind="bar", figsize=(10, 6))
plt.title("Salud mental promedio por edad y género")
plt.xlabel("Grupo de edad")
plt.ylabel("Puntaje de Salud Mental")
plt.legend(title="Género")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

#Ignorar los warnings de seaborn
import warnings
warnings.filterwarnings("ignore")

# Gráfico de líneas con horas de sueño por grupo de edad y género
sns.lineplot(data=df_excel, x="Age", y="Avg_Daily_Usage_Hours", hue="Gender", marker="o",
             palette={"Female":"#C71585","Male": "blue"})

plt.title("Horas medias de sueño por grupo de edad y género")
plt.xlabel("Grupo de edad")
plt.ylabel("Horas de uso medio")
plt.grid(True)
plt.tight_layout()
plt.show()

# Agrupar por edad y género y calcular el promedio
grouped = df_excel.groupby(["Age", "Gender"])["Avg_Daily_Usage_Hours"].mean()

# Convertir el índice para que cada género sea una columna
pivoted = grouped.unstack()  # Ahora tienes: Age como índice, Gender como columnas

# Graficar
colores = ["#1fb4b2", "#56ff0e"]
pivoted.plot(kind="bar", figsize=(10, 6), color=colores)
plt.title("Uso medio de las redes por edad y género")
plt.xlabel("Grupo de edad")
plt.ylabel("Horas de uso medio")
plt.legend(title="Género")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

#Ignorar los warnings de seaborn
import warnings
warnings.filterwarnings("ignore")

# Gráfico de líneas con horas de sueño por grupo de edad y género
sns.lineplot(data=df_excel, x="Age", y="Addicted_Score", hue="Gender", marker="o",
                          palette={"Female":"#C71585","Male": "blue"})

plt.title("Calificación de adicción por grupo de edad y género")
plt.xlabel("Grupo de edad")
plt.ylabel("Horas promedio de sueño")
plt.grid(True)
plt.tight_layout()
plt.show()

# Agrupar por edad y género y calcular el promedio
grouped = df_excel.groupby(["Age", "Gender"])["Addicted_Score"].mean()

# Convertir el índice para que cada género sea una columna
pivoted = grouped.unstack()  # Ahora tienes: Age como índice, Gender como columnas

# Graficar
colores = ["#b41fa3", "#0e0eff"]
pivoted.plot(kind="bar", figsize=(10, 6), color=colores)
plt.title("Calificación de adicción a las redes por edad y género")
plt.xlabel("Grupo de edad")
plt.ylabel("Nota de adicción")
plt.legend(title="Género")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Cuenta de estudiantes por país
df_excel['Country'].value_counts()[df_excel['Country'].value_counts() > 10]

# Promedios por país
promedios = df_excel.groupby('Country')[[
    'Age', 
    'Avg_Daily_Usage_Hours', 
    'Sleep_Hours_Per_Night', 
    'Mental_Health_Score', 
    'Conflicts_Over_Social_Media', 
    'Addicted_Score'
]].mean().round(2)
promedios

promedios.loc[promedios['Addicted_Score'].idxmax()]

# Plataforma más usada por los estudiantes
df_excel['Most_Used_Platform'].agg(lambda x: x.value_counts().index[0])

# Plataformas más usadas por estudiantes y genero
df_excel.groupby('Gender')['Most_Used_Platform'].agg(lambda x: x.value_counts().index[0])

df_excel.groupby('Gender')['Most_Used_Platform'].value_counts()

df_excel['Affects_Academic_Performance'].value_counts()

# Calcular el porcentaje de estudiantes que creen que las redes sociales afectan su rendimiento académico
porcentaje = df_excel['Affects_Academic_Performance'].value_counts(normalize=True) * 100
porcentaje

# Graficamos la representación de los valores por porcentaje
df_excel['Affects_Academic_Performance'].value_counts().plot(kind='bar', color=['salmon', 'skyblue'])
plt.title("¿Las redes sociales afectan el rendimiento académico?")
plt.xlabel("Respuesta")
plt.ylabel("Número de estudiantes")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Agrupar por nivel académico y calcular el promedio del puntaje de adicción
avg_addiction_by_level = df_excel.groupby("Academic_Level")["Addicted_Score"].mean().sort_values()
avg_addiction_by_level

import matplotlib.pyplot as plt

# Agrupar y calcular la media de adicción
avg_addiction_by_level = df_excel.groupby("Academic_Level")["Addicted_Score"].mean()

# Graficar
avg_addiction_by_level.plot(kind="bar", color="red")
plt.title("Nivel de adicción por nivel académico")
plt.xlabel("Nivel académico")
plt.ylabel("Puntaje promedio de adicción")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Si hay espacios en los nombres, hay que corregirlos
df_excel.columns = df_excel.columns.str.strip().str.replace(" ", "_")

# Crear gráfico de barras agrupadas sobre el estado sentimental y la plataforma más usada
plt.figure(figsize=(10, 6))
sns.countplot(data=df_excel, x='Relationship_Status', hue='Most_Used_Platform')

plt.title('Relación entre Estado Sentimental y Plataforma Más Usada')
plt.xlabel('Estado Sentimental')
plt.ylabel('Cantidad de Personas')
plt.legend(title='Plataforma Más Usada', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Clasificar el nivel de conflicto en redes sociales
def clasificar_conflicto(valor):
    if valor <= 2:
        return 'Bajo (0–2)'
    else:
        return 'Alto (3–5)'

df_excel['Nivel_Conflicto'] = df_excel['Conflicts_Over_Social_Media'].apply(clasificar_conflicto)

plt.figure(figsize=(10, 6))
sns.countplot(data=df_excel, x='Most_Used_Platform', hue='Nivel_Conflicto')
plt.title('Niveles de Conflicto según Plataforma Más Usada')
plt.xlabel('Plataforma Más Usada')
plt.ylabel('Cantidad de Personas')
plt.legend(title='Nivel de Conflicto')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Matriz de correlación
sns.heatmap(df_excel.corr(numeric_only=True), cmap="coolwarm")