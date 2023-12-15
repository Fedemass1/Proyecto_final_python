# PROYECTO FINAL CODER HOUSE PYTHON
COMISIÓN: 47785
Alumno: Federico Ezequiel Massone
DNI: 35.674.907
Autor del proyecto: Federico Ezequiel Massone

Link video explicativo del proyecto final en YouTube: https://youtu.be/kZCHvn-lVws

Acceso a la web: http://localhost:8000/

IMPORTANTE: Acceder con el siguiente usuario para tener privilegios de administrador y tener la funcionalidad
completa.
Usuario: admin
Password: admin


#Nombre del Proyecto#
Portal de gestión de productos, ventas y clientes

##Alcance del proyecto
El proyecto está dirigido a todas aquellas personas que estén interesadas en administrar su negocio de manera más
eficiente. Este les permitirá gestionar clientes, ventas y productos. A su vez, podrán tener un feedback constante con
el consumidor, ya que estos tienen la posibilidad de comentar las publicaciones sobre productos.

##Estructura del proyecto
El proyecto tiene dos enfoques distintos, acorde a los permisos del usuario que acceda. Por un lado, los usuarios
con estatus de staff, tendrán acceso al CRUD completo y a las opciones de gestión del negocio. Estos pueden:
-Agregar y consultar clientes
-Agregar y consultar productos
-Editar y eliminar productos
-Comentar y eliminar cualquier comentario
-Agregar y consultar ventas realizadas
-Editar datos propios de usuario
-Editar avatar propio
-Acceso a la biografía del creador del proyecto.

Los usuarios que no son de staff, es decir aquel que sea externo a la entidad tienen acceso más restringido
-Consultar y comentar productos
-Eliminar únicamente los comentarios propios, no así los ajenos
-Editar usuario y avatar propio
-Acceso a la biografía del creador del proyecto

El único que tiene acceso a la consola de administración es aquel que tenga permisos de superusuario, es decir que
son los únicos que pueden asignar el estatus de staff a otros usuarios y realizar el CRUD irrestricto (incluyendo
a cualquier usuario) El acceso a la consola de administrador, este tipo de usuario puede realizarlo directamente desde
su perfil, junto a las opciones de edición de este.

Para poder operar en la web es necesario estar registrado y logueado.

Se han realizado un total de 15 pruebas, todas ellas exitosas, en cuanto al funcionamiento de la página web. El
detalle de los test realizados se encuentra dentro del proyecto en un archivo de excel titulado
"Pruebas Proyecto Final Python CoderHouse"
