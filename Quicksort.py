# Estou usando array, mas, é possível alterar pra hash 

Class Quick(object){
	

	def particiona(self, array, begin, end):
				i=begin
				j=end
				meio = (i+j)/2
				pivo=array[meio]

				#Troca o pivô com o primeiro elemento
				array[i],array[meio] = array[meio],array[i]
				i=+1

				while i<j

							loop_j =0

							#Atribui a variavél left a palavra em array[i]
							left=array[i]
						
							
							#Testa se a palavra em left vem antes da palavra em pivô
							if self.__this_word_comes_first_than_that(left, pivo):
							
									pivo=pivo
									i=+1

							else:

								while not lopp_j:

										#Atribui a variavél right a palavra em array[j]
										right=array[j]

										#Testa se a palavra no pivô vem antes da palavra em right
										if self.__this_word_comes_first_than_that(pivo, right):

												j=-1

										else:

											#Troca as palavras no array nas posições i e j
											array[i],array[j] = array[j],array[i]
											
											i+1
											j+1

											#Encerra o Loop
											loop_j=1

				if i>j:

					#Troca as palavras no array nas posições meio e j
					array[meio],array[j]=array[j],array[meio]

					return meio


	def quicksort(self, array, begin, end):
			if end =1
					return array

			elif begin < end

					#Atribui a variavél num o valor que será retornado em particiona
					num=self.particiona(array, begin, end)

					#Usa a variavél num para determinar um novo fim e começo para a função quicksort

					self.quicksort(array, begin, num)
					self.quicksort(array, num+1, end)

					
					return array




