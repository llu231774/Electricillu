# Aplicació de càlcul d'energia elèctrica

Aquesta és una aplicació de Python que utilitza el framework Flask per calcular el cost total de l'electricitat per a diversos electrodomèstics. L'aplicació utilitza una llista d'electrodomèstics predefinida, però també permet afegir nous electrodomèstics mitjançant un formulari web.

## Funcionament

Quan obriu l'aplicació al vostre navegador, veureu una llista d'electrodomèstics predefinida, el cost total de l'electricitat per a tots els electrodomèstics i un formulari per afegir nous electrodomèstics.

Per afegir un nou electrodomèstic, introduïu el nom, la potència i les hores d'ús del nou electrodomèstic al formulari i feu clic al botó "Afegir". Si el nou electrodomèstic és vàlid, apareixerà a la llista d'electrodomèstics i el cost total de l'electricitat es recalcularà.

Per eliminar un electrodomèstic de la llista, feu clic al botó "Eliminar" al costat del nom de l'electrodomèstic.

Per buidar completament la llista d'electrodomèstics, feu clic al botó "Reiniciar".

## Requisits

Per a executar aquesta aplicació, necessiteu Python 3 i les següents llibreries de Python:

- Flask

Podeu instal·lar les llibreries de Python necessàries executant la següent comanda:

```
pip install -r requirements.txt
```

## Configuració

L'aplicació té la següent configuració:

- **appliances**: una llista d'electrodomèstics predefinida
- **electricity_cost**: el cost de l'electricitat per kilowatt hora
- **currency**: la moneda actual per a l'aplicació

Podeu configurar aquests valors a l'inici del fitxer **app.py**.

## Execució

Per a executar l'aplicació, executeu la següent comanda a la línia de comandes:

```
python app.py
```

A continuació, obriu el vostre navegador web i aneu a la següent adreça:

```
http://localhost:5000/
```
