# APIs REST

Una API es una interfaz que permite que dos programas se comuniquen. REST es un estilo arquitectónico común para diseñar APIs web que exponen recursos mediante URLs y utilizan el protocolo HTTP. Una API REST suele representar recursos como usuarios, productos o pedidos, y responde con formatos como JSON.

Los métodos HTTP describen la operación solicitada. GET consulta o recupera un recurso. POST suele crear un recurso o iniciar una operación. PUT reemplaza un recurso completo y PATCH modifica parte de un recurso. DELETE solicita eliminar un recurso. Las respuestas usan códigos HTTP para indicar el resultado.

Una API debería mantener una interfaz coherente y aprovechar los códigos de estado apropiados. La autenticación puede implementarse mediante tokens, por ejemplo JWT, enviados en el encabezado Authorization. La validación de datos de entrada ayuda a prevenir errores y solicitudes inválidas. La documentación de endpoints debe explicar rutas, parámetros, cuerpos de solicitud, respuestas y errores posibles.
