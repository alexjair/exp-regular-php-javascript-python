<?php
$file = fopen("../files/results.csv","r");

$match   = 0;
$nomatch = 0;

while(!feof($file)) {
    $line = fgets($file);
    if(preg_match(
        '/^2018\-01\-(\d\d),.*$/',
        $line,
        $m
      )
    ) {
        //print_r($m); 
        echo('<pre>');
        var_dump($m);
        echo('</pre>');
        $match++;
    } else {
        $nomatch++;
    }
}
fclose($file);

printf("\n\nmatch: %d\nnomatch: %d\n", $match, $nomatch);