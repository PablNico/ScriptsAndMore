<?php 
$a = 10;
$b = 29;

//soma
$resultado = $a+$b;
echo "O Resultada da soma entre ".$a.' e '.$b. " é: ".$resultado;


//subtração
$resultado = $a-$b;
echo "<br>O Resultada da subtração entre ".$a.' e '.$b. " é: ".$resultado;

//multiplicação
$resultado = $a*$b;
echo "<br>O Resultada da multiplicação entre ".$a.' e '.$b. " é: ".$resultado;

// divisão
$resultado = $a/$b;
echo "<br>O Resultada da divisão entre ".$a.' e '.$b. " é: ".number_format($resultado,2);

?>