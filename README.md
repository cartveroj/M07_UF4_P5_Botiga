# M07_UF4_P5_Botiga

<h2> Enlace video  </h2>

[link_carpeta_videos_Ejercicio_Botiga](https://drive.google.com/drive/folders/1pimc6uB7hOOn-VYYomya7N910kRowEcn?usp=sharing)



<h2> Model Entitat-Relació </h2>

En aquest model vam partir de la idea de que hi hauria un Login i la api de Pagaments gestionaria el pagament mirant la targeta i l'usuari, al final es va decidir que Pagaments només gestionaria que el carretó sortís com a pagat.

![model](imatges/modelentitatrelacio.png)

Aquesta es la versió final: 

![modelv2](imatges/versio2bbdd.png)

<h2>API CATALEG </h2>

Conté el model de Catàleg i Productes juntament amb els seus serializers per a realitzar les consultes:
<h3> GET PRODUCTE </h3>

![get_producte](imatges/get_productes.png)

<h3> GET PRODUCTES </h3>

![get_productes](imatges/get_all_productes.png)

<h3> CREATE PRODUCTE </h3>

![create del producte](imatges/create_producte.png)

<h3> UPDATE PRODUCTE </h3>

![update_del producte](imatges/update_producte.png)

<h3> DELETE PRODUCTE </h3>

![delete del producte](imatges/delete_producte.png)
![confirma_delete del producte](imatges/producte_eliminat.png)

<h3> GET CATALEG </h3>

![get_cataleg](imatges/get_cataleg.png)

<h3> AFEGIR PRODUCTE AL CATALEG </h3>

![afegir_producte_cataleg](imatges/create_producte_cataleg.png)
![afegit_producte_cataleg](imatges/producte_afegit_cataleg.png)


<h3> ELIMINAR PRODUCTE AL CATALEG </h3>

![eliminar_producte_cataleg](imatges/delete_producte_cataleg.png)
![eliminat_producte_cataleg](imatges/producte_cataleg_eliminat.png)


<h2> API PAGAMENTS </h2>

Conté el model de Pagaments amb la view que permet modificar el estat de Carreto en el camp pagat a True

<h3> PAGAR CARRETO </h3>

![carreto_pagat](imatges/carreto_pagat.png)
![carreto_pagat_bbdd](imatges/carreto_pagat_bbdd.png)

En cas de que el carreto estigui pagat mostrarà el següent missatge: 

![carreto_pagat_error](imatges/control_errors_pagaments.png)

<h2> CARRETO </h2>

Aplicacion que se encarga de la gestion de los carritos, los articulos de compra, en si es la principal aplicacion que lleva la logica de la aplicación. 

Se describe desde la creacion y eliminacion de un carrito, añadir productos, eliminar el producto y modificar la cantidad.

<h3> Crear carrito</h3>

![carreto_crear](imatges/add_carreto_0.png)
![carreto_crear](imatges/add_carreto_1.png)

<h3> Añadir productos al carrito</h3>

![añadir productos carreto](imatges/add_productoAlcarreto_0.png)

<h3> Leer productos del carrito</h3>

![read_productos_carreto](imatges/read_productoAlcarreto_0.png)

<h3> Modificar cantidad de productos del carrito</h3>

![update_cantidad_productos_carreto](imatges/update_cantidad_productoAlcarreto_0.png)

![update_cantidad_productos_carreto](imatges/update_cantidad_productoAlcarreto_1.png)

<h3> Eliminar producto del carrito</h3>

![eliminar_productos_carreto](imatges/eliminar_productoAlcarreto_0.png)

![eliminar_productos_carreto](imatges/eliminar_productoAlcarreto_1.png)

<h3> Eliminar carrito</h3>


![eliminar__carreto](imatges/delete_carreto_0.png)

<h2> COMANDAS</h2>

La aplicación comanda nos brinda una vision amplia del estado de los carritos, tanto los pagados y pendientes de pago.

<h3> Read comandas </h3>

![read_comanda](imatges/comandas_0.png)

<h3> Read historico de carritos pagados</h3>

![read_comanda](imatges/comandas_historico_carritos.png)

<h3> Read carritos pendientes</h3>

![read_comanda](imatges/comandas_pendientes_carritos.png)