# Instrucciones para Realizar el Estudio de Sezgo Educativo por Género

1. Graficar en el eje de las abscisas los años y en el de las ordenadas la columna de biología del grupo de datos.
2. Graficar también el porcentaje de licenciados en biología hombres
3. Ajustar los colores y etiquetas de los datos
4. Poner un título indicativo "Porcentaje de Licenciaturas Otorgadoas por Género"
5. Generar una leyenda de los datos y posicionarla con `loc=...`
6. Remover las contaminación gráfica con `Axes.tick_params()` utilizando los parámetros:
    - "bottom": "off"
    - "top": "off"
    - "left": "off"
    - "right": "off"
7. Continuar mejorando el radio _tinta-información_ removiendo las `spine`s de la gráfica utilizando `Axes.spines["left"].set_visible(False)` 
8. Para incitar comparación, graficaremos `majors = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']`
    1. Crear una figura vacía `fig = plt.figure(figsize=(12,12))`
    2. Iterar por la cantidad de carreras agregando un subplot `ax = fig.add_subplot(2,2,sp+1)`
    3. En cada iteración graficar porcentaje para hombres y mujeres como lo hicimos antes
    4. Para hacer comparaciones justas, limitar en `x` y `y` con `ax.set_xlim(1968,2011)` y `ax.set_ylim(0,100)`
    