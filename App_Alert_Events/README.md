# Aplicación de Alertas de Eventos

La app es para Android y recibe alertas de un servidor, para que la app lance una notificacion al usuario.

La RPi va a monitorizar una serie de eventos que van a ocurrir en el programa y cuando estos ocurran deberan enviar una señal a la app Android para que cree una notificacion.

Ejemplo:

Programa: lanzar mensaje de prueba ---> App: Notificacion: "Prueba"
Programa: time.sleep(60), msg(han pasado 60 segundos) ---> App: Notificacion: "Han pasado 60 segundos"

La app en Android debe correr en segundo plano. Al igual que en la RPi.
