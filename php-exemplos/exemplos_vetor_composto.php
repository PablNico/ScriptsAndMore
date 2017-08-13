<?php 
	$v = array("nome"=> array("Pablo",'Carlos', "Nicolas"),
		"idade"=>array("18 anos", '20 anos', "90 anos" ),
		 "peso" => array(59.60, 70.0, 84.99));
	echo 'Nome: '.$v["nome"][0].'<br>Idade:'.$v["idade"][0].'<br>Peso: '.$v["peso"][0];
	echo '<br><br>';

	echo '<br>Nome: '.$v["nome"][1].'<br>Idade:'.$v["idade"][1].'<br>Peso: '.$v["peso"][1];
	echo '<br><br>';


	echo '<br>Nome: '.$v["nome"][2].'<br>Idade:'.$v["idade"][2].'<br>Peso: '.$v["peso"][2];
?>
