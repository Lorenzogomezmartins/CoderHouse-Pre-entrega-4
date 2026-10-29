# Bases de datos relacionales y SQL

SQL es un lenguaje usado para consultar y modificar datos en sistemas de bases de datos relacionales. Una tabla organiza datos en filas y columnas. Cada fila representa un registro y cada columna una propiedad del registro.

Una clave primaria o PRIMARY KEY identifica de forma única cada fila de una tabla. No debe repetirse y no puede ser NULL. Una clave foránea o FOREIGN KEY relaciona una tabla con la clave de otra tabla y ayuda a mantener la integridad referencial.

SELECT consulta datos; WHERE filtra filas; ORDER BY ordena resultados; INSERT INTO agrega registros; UPDATE modifica registros existentes; DELETE elimina registros. JOIN permite combinar filas de dos o más tablas mediante una condición de relación. GROUP BY agrupa filas y se usa habitualmente con funciones como COUNT, SUM y AVG.

Los índices pueden acelerar consultas sobre columnas utilizadas frecuentemente, aunque ocupan almacenamiento y pueden aumentar el costo de las escrituras. Las transacciones agrupan operaciones y permiten mantener propiedades de consistencia cuando se confirman o revierten correctamente.
