# BoliviaImporta

Esta es una simple calculadora de impuestos a productos importados en Bolivia. Mi idea es que puede ayudar a los compradores online a tener una mejor idea de los costos que pueden esperar al realizar compras por internet (por ejemplo de Aliexpress u otros sitios).

La calculadora en su primera versión es basada en la explicación de Eduardo Gamón en su [video de YouTube](https://www.youtube.com/watch?v=9Scw_Unk92w). El video es del 2017 por lo que puede estar desactualizado. Voy a buscar mas información cuando pueda para mejorarlo y actualizar cosas.

## Propósito
El propósito como fue mencionado arriba es de facilitar la vida a los compradores de cosas online desde el exterior.

Hay que tomar en cuenta que los valores son aproximados y deben ser usados solo como referencia para tener una mejor idea de cuanto va a costar una compra.

Esta información puede ser usada para decidir si vale la pena comprar afuera teniendo en cuenta el costo aproximado final.

## Cómo Utilizar
Para calcular el impuesto a pagar simplemente hay que ejecutar el script "calculator.py" de Python con los parámetros deseados en la terminal.

Por ejemplo, si traemos un celular con costo de $500 y envío de $10, podemos poner lo siguiente:

```sh
python calculator.py -p 500 -s 10
```

y como resultado veremos algo como:

```
Impuesto final          : bs 940.30
Producto + impuesto     : bs 4489.90
Porcentaje de impuesto  : 27.02%

Costo final en Moneda original : 645.10 USD
```
Hay varios parámetros que se pueden modificar, como la moneda original (si no fue en USD), la tasa de cambio a bolivianos, la taza de impuestos IVA, etc.

Para ver las opciones disponibles, usar:

```sh
python calculator.py --help
```

## Que Sigue

Cuando tenga tiempo quiero hacer una interfaz gráfica simple para que sea mas fácil de usar para otras personas.

Si alguien quiere aportar algo, usen Python 3.7 (o al menos de 3.x) con documentación de que es lo que se implementa. Mejor si el código es escrito en inglés.
