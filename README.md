# Nombre del Archivo: exp-regular-php-javascript-python 🏍
Expresiones Regulares 🪂 REGEXps para el manejo de grandes volúmenes de datos, aplicado en los lenguajes de Python, PHP y Javascript, código de ejemplos y trabajo como herramienta. 


# <a name="_nlbsdl4kefta"></a>Expresiones regulares


Mi expresion regular para buscar numero:

+54 388 5377055 

-> **[+]?(\d{2,4}[ ]?){2,4}**

- Caso 1

5556581111
56-58-11-12-34
56\.58.11.12.33

(\d{2,2}[\-\.]?){5,5}$

- Caso 2

302-345-9876
143-457-90-77
096-907-11.12

**(\d{3,3}[\-\.]?){2,2}(\d{2,2}[\-\.]?){2,2}$**

En caso de que quieran tener una expresión que haga match tanto con el primer caso como con el segundo. Necesitan unir la expresión regular utilizando el operador lógico “o” ( | ).

- Caso 3

5556581111
56-58-11-12-34
56\.58.11.12.33
302-345-9876
143-457-90-77
096-907-11.12

(\d**{2,2}[\-\.]?){5,5}$|(\d{3,3}[\-\.]?){2,2}(\d{2,2}[\-\.]?){2,2}$**

### <a name="_6a1vitrnczlv"></a>**Mis apuntes sobre: "Los delimitadores: +,\*,? "**
Resumen hasta hoy#p132:
\w - caracteres de palabras
\d - dígitos
\s - espacios/invisibles en blanco
[0-9] ~ \d
[0-9a-zA-Z\_] ~ \w
\* - greedy - todo cero o más veces
\+ - uno o más
? - cero o uno, en otro contexto (Sean los menos posibles)

- 1. Ejemplo regex:

.\*

-Explicación 1: Encuentra un caracteres y sigue seleccionando hasta el final de la linea.
’
’

- 2. Ejemplo regex:

\d+

-Explicación 2: Encuentra un dígito, luego 1 o más hasta que no haya.
’
’

- \*\*3. Ejemplo regex: \*\*

\d\*[a-z]

-Explicación 3: Encuentra y selecciona: Toda vez que se inicie o no con un dígito,
y siga y termine con una letra de la a a la z.
’
’

- 4. Ejemplo regex:

\d\*[a-z][a-z]?

-Explicación 4: Encuentra y selecciona: Toda vez que haya o no un dígito, luego
haya una letra de la a a la z, y luego haya o no una letra.
’
’

- 5. Ejemplo regex:

\d\*[a-z]?s\d\*

-Explicación 5: Encuentra y selecciona: Cero o muchos dígitos, y cero o una letras de la
a a la z y una letra ‘s’ y cero o muchos dígitos.
’
’

7\. Mis apuntes sobre: “Los contadores {1,4}”
{1,2} -> Los contadores tienen una cota inferior y una superior, indicando el mínimo y máximo
de resultados que se quieren encontrar.

- 1. Ejemplo regex: Contadores

\d{2,2}

-Explicación 1: Encuentra y selecciona [match], mínimo dos y máximo 2 dígitos.
’
’

- 2. Ejemplo regex: Contadores 2

\d{2,10}

-Explicación 2: Encuentra y selecciona [match], mínimo dos y máximo 10 dígitos.
’
’

- 3. Ejemplo regex: Contadores sin límite

\d{4,}

-Explicación 3: Encuentra y selecciona [match], mínimo cuatro y máximo sin límite de dígitos.
’
’

- 4. Ejemplo regex: Contadores seguidos de más patrones

**\d{2,2}-?\d{2,2}-?\d{2,2}-?\d{2,2}-?\d{2,2}**

-Explicación 4: Encuentra y selecciona [match], mínimo 2 y máximo dos dígitos, seguidos
de cero o un guión, luego lo mismo cuatro veces, y finaliza con mínimo dos y máximo dos dígitos.
’
’

- \*4. Ejemplo regex: Combinando contadores

**\d{2,2}[\-\.]?**

-Explicación 4: Encuentra y selecciona [match], mínimo 2 y máximo dos dígitos, seguidos
de cero o un guión(-) o punto(.).
’
’

- 5. Ejemplo regex: Combinando contadores

**\d{2,2}[\-\. ]?\d{2,2}[\-\. ]?\d{2,2}**

-Explicación 5: Encuentra y selecciona [match], mínimo 2 y máximo dos dígitos, seguidos
de cero o un guión(-) o punto(.) o espacio en blanco ( ), tres veces lo mismo.

<a name="_93kkzvml5gax"></a>7. Mis apuntes sobre: “El caso de (?) como delimitador”
? --> modifica el +,\*
-----------------------------------------------------------------------------------
- 1. Ejemplo regex: <?> como modificador débil

**.+?,**

-Explicación 1: Encuentra y selecciona [match], todos los caractares que existan
antes de una coma, haz el match, pero divídelos en los grupos más pequeños posibles,
de igual manera cumpliendo las condiciones.
’
’

[0-9a-z]+?[,.:;]
### <a name="_qee4d62syfs9"></a>Not (^), su uso y sus peligros
- \D -> Encuentra todo lo que no sea un dígito
- \S -> Encuentra todo lo que no sea un espacio
- \W -> Encuentra todo lo que no sea una palabra
- ^ -> Sirve para negar SOLAMENTE dentro los corchetes. Por ejemplo: [^0-5a-c] significa que tomará del 6 al 9 y de la ‘d’ a la ‘z’

<h5>Otros caracteres</h5>

- \t — Representa un tabulador.
- \r — Representa el “retorno de carro” o “regreso al inicio” o sea el lugar en que la línea vuelve a iniciar.
- \n — Representa la “nueva línea” el carácter por medio del cual una línea da inicio. Es necesario recordar que en Windows es necesaria una combinación de \r\n para comenzar una nueva línea, mientras que en Unix solamente se usa \n y en Mac\_OS clásico se usa solamente \r.
- \a — Representa una “campana” o “beep” que se produce al imprimir este carácter.
- \e — Representa la tecla “Esc” o “Escape”
- \f — Representa un salto de página
- \v — Representa un tabulador vertical
- \x — Se utiliza para representar caracteres ASCII o ANSI si conoce su código. De esta forma, si se busca el símbolo de derechos de autor y la fuente en la que se busca utiliza el conjunto de caracteres Latin-1 es posible encontrarlo utilizando “\xA9”.
- \u — Se utiliza para representar caracteres Unicode si se conoce su código. “\u00A2” representa el símbolo de centavos. No todos los motores de Expresiones Regulares soportan Unicode. El .Net Framework lo hace, pero el EditPad Pro no, por ejemplo.
- \d — Representa un dígito del 0 al 9.
- \w — Representa cualquier carácter alfanumérico.
- \s — Representa un espacio en blanco.
- \D — Representa cualquier carácter que no sea un dígito del 0 al 9.
- \W — Representa cualquier carácter no alfanumérico.
- \S — Representa cualquier carácter que no sea un espacio en blanco.
- \A — Representa el inicio de la cadena. No un carácter sino una posición.
- \Z — Representa el final de la cadena. No un carácter sino una posición.
- \b — Marca la posición de una palabra limitada por espacios en blanco, puntuación o el inicio/final de una cadena.
- \B — Marca la posición entre dos caracteres alfanuméricos o dos no-alfanuméricos.


En el texto siguiente:

555658

56-58-11

56\.58.11

56\.78-98

65 09 87

76y87r98

Definir un patrón que haga match a todas las líneas excepto a la la última, la que tiene letras.

Es decir, seleccionar todas sin importar el caracter de separación, excepto cuando los números están separados entre sí por letras.

mio

**[0-9]{2,2}[^a-zA-Z]+**

ok 

**\d\d\W?\d\d\W?\d\d**

**(\d{2}\W?){3}**

**\d{2,}[^a-z]+**

\----------------------------------------------- 
### <a name="_fx9y2cedo2kp"></a>**url**
ejemplo: URL 

url: https://www.go-ogle.com

url: http://www.google.com.pe

url: http://www.fulldominio.google.com.pe?pgp=3

url: http://fulldominio.google.com.pe?pgp=3

https://www.fulldominio.google.com.pe?pgp=3

http://www.fulldo-minio.google.com.pe?pgp=3

https://www.fulldominio.google.com.pe?pgp=3

https://fulldominio.google.com.pe?pgp=3   ddd ddd // \*\*f.. 

resp

**https?:\/\/((www)+\.)?[\w\-]+\.\w{2,6}(\/?)\S\***

\--------------------------------------------------- 
### <a name="_8v458h15bp1b"></a>**correo**

` `- esto.es.un.mail+gmail@mail.com sdsd sd @sd sd sd

esto.es\_un.mail@mail.com

1 esto.es\_un.mail+complejo@mail.com

dominio.com

rodr-igo.jimenez@yahoo.com.mx

ruben@starbucks.com

esto\_no$es\_email@dominio.com.pe

no\_se\_de\_internet3@hotmail.com.cl

Patron

alumonos

**[\w\.\_]{3,30}\+?\w{0,10}@[\w\-\.]{3,}\.\w{2,5}**

clase

**[\w\.\_]{3,30}\+?[\w]{0,10}@[\w\.\-]{3,}\.\w{2,5}**              ok

mode

**[\w\.\-\_]{3,30}\+?[\w]{0,10}@[\w\.\-]{3,}\.\w{2,5}**

mod1

**[\w\.\-\_]{3,30}\+?[\w]{0,10}@[\w\.\-]{3,}\.\w{2,5}**

solo chile

**[\w\.\_]{3,30}\+?[\w]{0,10}@[\w\.\-]{3,}\.cl**

### <a name="_qss2wlct2w18"></a>GIS

\s? si hay espacio o no

-99.205646,19.429707,2275.10

-99.205581, 19.429652,2275.10

-99.204654,19.428952,2275.58

mio

**-?(\d{1,3}\.\d{1,6},\s?){2}\d{1,5}.\***

-99 12' 34.08"W, 19 34' 56.98"N

-34 54' 32.00"E, -3 21' 67.00"S

clase

**^-?\d{1,3}\s\d{1,2}' \d{1,2}\.\d{2,2}"[WE],\s?-?\d{1,3}\s\d{1,2}' \d{1,2}\.\d{2,2}"[SN]$**


### <a name="_ieyfp4s6zfop"></a>**ESCAPE como aki:** 
**\w**

**\s  (Espacio)**

**\d**

**\-**

**\.**

**\)**

**\(**

**.\*   (todo lo que falta.. va la final)**

**?   (vacio o 1 valor)**

**+   (1valor o muchos valores)**

**\*   (muchos valores)**

### <a name="_h1bmtrmpfuq0"></a> REEMPLACE GO!! CON SQL Y JSON


CLASE

**^\d+::(.\*)\s\((\d{4})\)::.\*$**

**^\d{1,4}::([[A-Z]?\w?.\*)?\(([\d]{4,4})\)::([\w?'\-\|]+)?$**

GRUPOS

**^\d{1,5}+::([\w\s:,\)\(\.\'\-\&\!\/?]+)\s\(\d\d\d\d\)::.\*$**

PROFF

**^\d+::([\w\s:,\(\)'\.\-&!\/]+)\s\((\d\d\d\d)\)::.\*$**

REEMPLACE 

**{\n  movie: '$1', \n  year: $2, \n},**

1::Toy Story (1995)::Adventure|Animation|Children|Comedy|Fantasy

2::Jumanji (1995)::Adventure|Children|Fantasy

3::Grumpier Old Men (1995)::Comedy|Romance

4::Waiting to Exhale (1995)::Comedy|Drama|Romance

5::Father of the Bride Part II (1995)::Comedy

6::Heat (1995)::Action|Crime|Thriller

7::Sabrina (1995)::Comedy|Romance

8::Tom and Huck (1995)::Adventure|Children

9::Sudden Death (1995)::Action

10::GoldenEye (1995)::Action|Adventure|Thriller

11::American President, The (1995)::Comedy|Drama|Romance

12::Dracula: Dead and Loving It (1995)::Comedy|Horror

13::Balto (1995)::Animation|Children

14::Nixon (1995)::Drama

15::Cutthroat Island (1995)::Action|Adventure|Romance

16::Casino (1995)::Crime|Drama

17::Sense and Sensibility (1995)::Comedy|Drama|Romance

18::Four Rooms (1995)::Comedy|Drama|Thriller

19::Ace Ventura: When Nature Calls (1995)::Comedy

### <a name="_h7qdmfvub57e"></a>**BÚSQUEDAS  romper query:**


**Find: [\?&](\w+)=([^&\n]+)**

**Replace: \n - $1=$2**

https://b3co.com/?s=fotografia&mode=search&module=blog

https://www.google.com/search?q=regex+platzi&oq=regex+platzi&aqs=chrome..69i57j69i60.6885j0j9&sourceid=chrome&ie=UTF-8

https://co.search.yahoo.com/search?p=flickr&fr=yfp-t&fp=1&toggle=1&cop=mss&ie=UTF-8

resp

https://b3co.com/ 

` `- s=fotografia 

` `- mode=search 

` `- module=blog

https://www.google.com/search 

` `- q=regex+platzi 

` `- oq=regex+platzi 

` `- aqs=chrome..69i57j69i60.6885j0j9 

` `- sourceid=chrome 

` `- ie=UTF-8

https://co.search.yahoo.com/search 

` `- p=flickr 

` `- fr=yfp-t 

` `- fp=1 

` `- toggle=1 

` `- cop=mss 

` `- ie=UTF-8

\-------------------------------------------------------------------------------------
### <a name="_cv4cmjvf4yzj"></a>**PHP**

preg\_match( '/regex/',

`		`$line,

`		`$m)

donde:

- regex: es la expresion regular.
- $line: cadena de caracteres (cada línea del archivo).
- $m: arreglo en donde cada match va a ir en cada uno de los lugares. En el script, este arreglo tiene dos elementos donde el elemento [0] es la cadena de caracteres de prueba y el elemento [1] es el grupo de caracteres que hace match.
- Expresión regular para obtener partidos jugados en enero del 2018:

^2018\-01\-(\d\d),.\*$

Código:

<?php

$file = fopen("../files/results.csv","r");

$match   = 0;

$nomatch = 0;

while(!feof($file)) {

`    `$line = fgets($file);

`    `if(preg\_match(

`        `'/^2018\-01\-(\d\d),.\*$/',

`        `$line,

`        `$m

`      `)

`    `) {

`        `print\_r($m); 

`        `$match++;

`    `} else {

`        `$nomatch++;

`    `}

}

fclose($file);

printf("\n\nmatch: %d\nnomatch: %d\n", $match







