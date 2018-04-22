#This Python file uses the following encoding: utf-8 
import utilities

class Quick():

        def sort_array(self,array):
                        end=len(array)
                        self.QuickSort(array,0,end)
                        return array

                        
        def particiona(self, array, begin, end):
                        meio=(begin+end)/2
                        pivo=array[meio]
                        left_index=begin
                        right_index=end-1
                        
                        #Troca o pivÃ´ com o primeiro elemento
                        array[left_index],array[meio] = array[meio],array[left_index]

                        left_index=left_index+1

                        while right_index>left_index:
                                        
                                        #Testa se a palavra em left vem antes da palavra em pivÃ´
                                        
                                        if utilities.this_word_comes_first_than_that(array[left_index],pivo):
                                                        left_index=left_index+1
					
                                        #Testa se a palavra no pivÃ´ vem antes da palavra em right
                                        elif utilities.this_word_comes_first_than_that(pivo,array[right_index]):
                                                        right_index=right_index-1
                                                        
                                        else:
                                                        #Troca as palavras no array nas posiÃ§Ãµes i e j
                                                        array[left_index],array[right_index] = array[right_index],array[left_index]
                                                        
                                                        left_index=left_index+1
                                                        right_index=right_index-1
                                                       
                        #Troca as palavras no array nas posiÃ§Ãµes do começo e right_index
                        array[begin],array[right_index]=array[right_index],array[begin]
                        return right_index                                 


        def QuickSort(self, array, begin, end):
                        
                        if begin<end

                                        #Atribui a variavÃ©l num o valor que serÃ¡ retornado em particiona
                                        split=self.particiona(array, begin, end)
                                        #Usa a variavÃ©l num para determinar um novo fim e comeÃ§o para a funÃ§Ã£o quicksort
                                        self.QuickSort(array, begin, split)
                                        self.QuickSort(array, spli+1, end)
                                        
                                        return array




"""
class QuickSort(AbstractSortClass):
        def sort_array(self,array):
                end = len(array)
                self.quickSort(array,0,end-1)
                return array
        
        def particiona(self, array, begin, end):
    		meio=(begin+end)/2
                pivo=array[meio]
		left_index=begin
		right_index=end-1

		#Troca o pivÃ´ com o primeiro elemento
		array[left_index],array[meio] = array[meio],array[left_index]

		left_index=left_index+1

		while right_index>left_index:

                        #Testa se a palavra em left vem antes da palavra em pivÃ´

                        # Verify if it's a number or a word
                        if type(array[left_index]) is not int:
                                if utilities.this_word_comes_first_than_that(array[left_index],pivo):
                                	left_index=left_index+1
                        	elif utilities.this_word_comes_first_than_that(pivo,array[right_index]):
                                	right_index=right_index-1
                                                        
				else:
					#Troca as palavras no array nas posiÃ§Ãµes i e j
					array[left_index],array[right_index] = array[right_index],array[left_index]

					left_index=left_index+1
					right_index=right_index-1
                                                       
			
                        else:
                                if array[left_index] < pivo :
                                        left_index=left_index+1
                                elif pivo < array[right_index]:
					right_index=right_index+1
                                else:
                                        #Troca as palavras no array nas posiÃ§Ãµes i e j
					array[left_index],array[right_index] = array[right_index],array[left_index]

					left_index=left_index+1
					right_index=right_index-1
		#Troca as palavras no array nas posiÃ§Ãµes do começo e right_index
		array[begin],array[right_index]=array[right_index],array[begin]
		return right_index 

        def quickSort(self, array, begin, end):
                       
               if begin<end
	       
			#Atribui a variavÃ©l split o valor que serÃ¡ retornado em particiona
			split=self.particiona(array, begin, end)
			
			#Usa a variavÃ©l num para determinar um novo fim e comeÃ§o para a funÃ§Ã£o quicksort
			self.QuickSort(array, begin, split)
			self.QuickSort(array, spli+1, end)

			return array
"""

				
