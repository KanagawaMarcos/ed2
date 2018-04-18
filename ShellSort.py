import utilities 

class ShellSort():
	
	def shell(self, array):
			
		size=len(array)
		h=1
		
		#Faz com que a variavél H receba o maior valor possível
		for h in range(1,size,(h*3)+1):
			
		while h>0:
			i=0
			j=h
			
			#Percorre a array nas posições i e j, na distância h até o final do vetor
			while j<=h:
				#Testa para ver se a palavra no array[i] vem antes do array[j]
				if self.__this_word_comes_first_than_that(array[i], array[j]):
					
					#Troca as palavras da array
					array[i],array[j]=array[j],array[i]

					#Movimenta as variaveis i e j
					j=+1
					i=+1
			#Atualiza o valor de h
			h=(h-1)/3			

		return array
	
		
	
