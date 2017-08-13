<?php 
$a = 10;
$b = 29;

//soma
$resultado = $a+$b;
echo "O Resultado da soma entre ".$a.' e '.$b. " é: ".$resultado;


//subtração
$resultado = $a-$b;
echo "<br>O Resultado da subtração entre ".$a.' e '.$b. " é: ".$resultado;

//multiplicação
$resultado = $a*$b;
echo "<br>O Resultado da multiplicação entre ".$a.' e '.$b. " é: ".$resultado;

// divisão
$resultado = $a/$b;
echo "<br>O Resultado da divisão entre ".$a.' e '.$b. " é: ".number_format($resultado,2);

?>
