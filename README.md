# M07_UF4_P5_Botiga
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