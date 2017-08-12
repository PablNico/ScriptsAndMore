<?php 
$pi = 3.14159;
$raio = 5.2;
$area = $pi*pow($raio,2);
echo 'Área = '.$area;
echo '<br>Área formatada = ' .number_format($area,2);

?>