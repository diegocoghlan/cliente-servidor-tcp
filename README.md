# Cliente y Servidor TCP en Python

Este proyecto implementa un cliente y un servidor TCP que se comunican entre sí utilizando localhost y el puerto 5000.

## Cómo ejecutar

1. Abrir una terminal y ejecutar el servidor con:
   python server.py

2. En otra terminal, ejecutar el cliente con:
   python client.py

Ambos archivos deben estar en la misma carpeta.

## Pruebas manuales

1. Enviar un mensaje cualquiera desde el cliente, por ejemplo: "hola".
   El servidor debe responder con el mismo mensaje en mayúsculas: "HOLA".

2. Enviar el mensaje "DESCONEXION" desde el cliente (en mayúsculas).
   El cliente debe cerrar la conexión.
   El servidor debe cerrar la sesión de ese cliente, pero seguir funcionando para nuevas conexiones.
