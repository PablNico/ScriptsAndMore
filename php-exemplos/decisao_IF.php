<?php 
	$nota1 = 5.8;
	$nota2 = 8.5;
	$media = ($nota1+$nota2)/2;
	echo "Média = ".$media;
	if($media>=7.0){
		echo "<br>Aluno Aprovado";
	}
	else if($media<4){
		echo "<br>Aluno Reprovado";
	}
	else{
		echo "<br> Aluno em Exame";

	}

?>