# Análisis del Top 500 de Forbes: Instrucciones
1. Encontrar qué compañías subieron y bajaron más de lugar
    1. Crear la `series` `rank_change`
    2. Encontrar el valor máximo de la columna `rank_change`
    3. Encontrar el valor mínimo de la columna `rank_change`
2. Descrbir la columan `rank` y `prev_rank`
    1. Utilizar el método `series.describe` en la columna `rank`
    2. Hacerlo ahora en la columna `prev_rank`
3. Encontrar valores sin sentido
    1. Utilizar _method chaining_ para encontrar cuántas filas con `previous_rank` == 0 (data[idx].value_counts().loc[0])
4. Encontrar los valores numéricos máximos de cada columna
    1. Utilizar el método `max(numeric_only=True, axis='index')`
5. Describir todo el `dataframe`
6. Al parecer "Dow Chemical" cambió de CEO, ahora es Jim Fitterling
7. Encontrar las compañías que se dedican a vehículos de motor y partes
    1. Crear una `series` booleana que checa la columna `industry` con el valor `Motor Vehicles and Parts
    2. Utilizar la `series` creada para ver qué compañías hay
8. Actualizar los valores erroneos encontrados en el punto 3.
    1. Utilizar indexado booleano para actualizar la columna `previous_rank`
        1. Donde había un valor `0`, ahora debe haber `np.nan` (`bidx = data['previous_rank'] == 0; data.loc[bidx, "previous_rank"] = np.nan`). Podemos comparar los cambios con `prev_rank_before = f500["previous_rank"].value_counts(dropna=False).head()` y uno para _after_
9. Agregar una nueva columna `rank_change` en el `dataframe` que sea la resta (ya corregida) de los ranking previos y actuales
