# Python_3ra_entrega
Recomentación: Primer acceso realizarlo desde /app/show/

Para la presente entrega se ha creado un portal de clientes destinado a la administración de ventas y la gestión del negocio. Por tal motivo el desarrollo de la página web,
se realizó teniendo en cuenta como usuario final al administrador de una unidad comercial.

En el proyecto que se presenta a continuación pueden identificarse por un lado las funciones destinadas a almacenar información en la base de datos, mientras que el otro grupo se encarga de mostrar dicha información por pantalla.

Las funciones que almacenan información consisten en formularios web que el usuario deberá completar con los datos solicitados y que se desean ingresar. Entre estas tenemos:

Agregar cliente: Se accede desde /app/clientes/ y permite dar de alta clientes de la empresa. Los campos a completar son 'Nombre', 'Dni', 'Email'. Si la empresa es una persona jurídica se debe poner aquí la
clave tributaria o análoga.

Agregar producto:Se accede desde /app/productos/ y permite la carga de 'Id producto', 'Nombre producto' y 'Precio venta' de cada producto que se desee agregar al listado de artículos disponibles para la venta.

Agregar venta: Se accede desde /app/ventas/ y permite cargar las ventas realizadas. Los campos a completar son 'Dni' del cliente al cual le vendimos, 'Nombre producto' que se vendió y ' Cantidad vendida'

Por otra parte el segundo grupo de funciones que se encarga de mostrar la información almacenada en la base de datos se compone de:

Clientes: Se accede desde /app/mostrar_clientes/ Muestra por pantalla el nombre, número de documento y correo electrónico de cada cliente ingresado por la empresa. Además admite la opción de BÚSQUEDA por el Dni del cliente.

Productos: Se accede desde /app/mostrar_productos/ y muestra el nombre del producto, su ID y su precio de venta de cada producto, uno debajo del otro.

Ventas: Se accede desde /app/mostrar_ventas/ y muestra las ventas realizadas, es decir: nombre del producto vendido, DNI del cliente y cantidad de esos objetos vendidos en la misma transacción a ese cliente.

PASOS PARA LA PUESTA EN FUNCIONAMIENTO DEL PORTAL DE VENTAS Y CLIENTES

1) Descargarse el reposiorio Python_3ra_entrega de la rama principal 'master'. Una vez hecho esto descomprimir el archivo y cargarlo en un IDE python.
2) Si es que no se tiene uno, instalar un nuevo entorno virtual. Si fuera necesario instalar django también en el entorno virtual.
3) Dar de alta la base de datos dentro del IDE con los siguientes comandos: python manage.py makemigrations (se hace por única vez), python manage.py migrate (se hace por única vez), python manage.py runserver (se hace cada vez que se quiera poner en funcionamiento el servidor. Se puede automatizar en el IDE si se configura la ejecución mediante el modulo 'manage' y el comando'runserver'
4) Una vez que se ejecute runserver, y si ha salido todo bien debería aparecer en la consola una dirección parecida o igual a esta 'http://127.0.0.1:8000/' Por medio de esta usar un navegador para acceder a esta y agregarle al final app/show/ Es decir, quedaría la ruta completa del ejemplo 'http://127.0.0.1:8000/app/show/' Al ingresar esta dirección en el navegador web se abrirá el portal de compras en la pantalla de inicio. Esta pantalla sólo es a los efectos de dar la bienvenida al usuario, luego no se usará más ya que no cumple ninguna otra funcionalidad.
5) Las funcionalidades que le sirven al usuario se encuentran todas en el navbar (franja superior de la pantalla) pudiéndose hallar de izquierda a derecha las opciones ya mencionadas al comienzo de este texto: Agregar cliente, Clientes, Agregar producto, Productos, Agregar venta, Ventas. La funcionalidad de cada una y la url que conduce directamente a ellas ya ha sido mencionada arriba.








