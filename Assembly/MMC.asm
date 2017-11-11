.data 
 	str: .asciiz "Digite um número: "
	quebra: .asciiz "\n"
	
		
.text	
	
	main:
		la $a0, str #carrega texto de str em A0 
		li $v0, 4 #printa a0
		syscall
		
		addi $v0, $zero, 5 #operação read int	
		syscall 
		add $t1, $0, $v0 #adiciona valor de entrada a t1
		
		la $a0, quebra #atribui o texto de quebra em A0 
		li $v0, 4 #printa a0
		syscall
   		
   		la $a0, str #atribui o texto de str em A0 
		li $v0, 4 #printa a0
		syscall
		
		addi $v0, $zero, 5  #operação read int
		syscall 
		add $t2, $0, $v0  #adiciono valor de entrada a t1
   		
   		
		la $a0, quebra #atribui o texto de quebra em A0 
		li $v0, 4 #printa a0
		syscall
   	
   	loop:	beq $t1, $t2, exit #se t1(a) == t2(b) pula para label exit
   		bge $t2, $t1, else #se b > a pula para label else
   		sub $t1, $t1, $t2 #a -= b
   		addi $v0, $0, 1 #printar inteiro
   		add $a0, $zero, $t1 #o valor a ser printado deve estar em a0, nessa linha a0 = 0+t1
   		syscall
   		j loop 
   		
     	
   	else: sub $t2, $t1, $t2 #b-=a
   		addi $v0, $0, 1
   		add $a0, $zero, $t2 #a0 = 0+b
   		syscall 
 
   		
   	exit: nop
   	 
   		
   		
   		
   	
