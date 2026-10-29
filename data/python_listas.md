# Listas en Python

Una lista en Python es una colección ordenada y mutable que puede almacenar varios elementos. Se crea con corchetes, por ejemplo `numeros = [1, 2, 3]`. Los índices comienzan en cero y permiten acceder a los elementos mediante `numeros[0]`.

El método `append(elemento)` agrega un elemento al final de la lista. Por ejemplo, `numeros.append(4)` deja la lista como `[1, 2, 3, 4]`. El método `extend(iterable)` agrega los elementos de otro iterable. El método `insert(indice, elemento)` inserta un valor en una posición específica. El método `remove(valor)` elimina la primera aparición de un valor. El método `pop()` elimina y devuelve el último elemento, o el elemento del índice indicado.

La función `len(lista)` devuelve la cantidad de elementos. Las listas pueden recorrerse con un bucle `for`. Una lista por comprensión permite construir listas a partir de otra secuencia, por ejemplo `[x * 2 for x in numeros]`.
