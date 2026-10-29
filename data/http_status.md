# Códigos de estado HTTP

Los códigos HTTP informan el resultado de una solicitud entre un cliente y un servidor. La familia 2xx representa solicitudes procesadas correctamente.

El código HTTP 200 OK indica que la solicitud tuvo éxito. El código 201 Created indica que la solicitud se completó y se creó un recurso nuevo; suele aparecer luego de una solicitud POST que crea un registro. El código 204 No Content indica que la solicitud tuvo éxito, pero la respuesta no incluye contenido.

La familia 4xx representa errores atribuidos a la solicitud del cliente. El código 400 Bad Request indica que el servidor no pudo interpretar la solicitud. El código 401 Unauthorized señala que falta autenticación válida. El código 403 Forbidden indica que el cliente no tiene permiso para acceder al recurso. El código 404 Not Found significa que el recurso solicitado no fue encontrado.

La familia 5xx representa errores del servidor. El código 500 Internal Server Error indica un fallo inesperado. El código 503 Service Unavailable indica que el servicio no está disponible temporalmente.
