#This Python file uses the following encoding: utf-8 
import utilities

class Quick():

        def sort_array(self,array):
                        end=len(array)
                        self.QuickSort(array,0,end)
                        return array

                        
        def particiona(self, array, begin, end):
                        i=begin
                        j=end-1
                        meio = (i+j)/2
                        pivo=array[meio]

                        #Troca o pivÃ´ com o primeiro elemento
                        array[i],array[meio] = array[meio],array[i]
                        i=+1
                        loop_j=0


                        while j>i:

                                        loop_j=0
                                
                                        #Testa se a palavra em left vem antes da palavra em pivÃ´
                                        
                                        if utilities.this_word_comes_first_than_that(array[i],pivo):
                                                        i=i+1
                                        else:
                                                        while loop_j==0:
                                                                        #Atribui a variavÃ©l right a palavra em array[j]
                                                                        
                                                                        #Testa se a palavra no pivÃ´ vem antes da palavra em right
                                                                        if utilities.this_word_comes_first_than_that(pivo,array[j]):
                                                                                        j=j-1
                                                                        else:
                                                                                        #Troca as palavras no array nas posiÃ§Ãµes i e j
                                                                                        array[i],array[j] = array[j],array[i]
                                                                                     
                                                                                        i+1
                                                                                        j-1

                                                                                        #Encerra o Loop
                                                                                        loop_j=loop_j+1
                        if i>j:
                                        #Troca as palavras no array nas posiÃ§Ãµes meio e j
                                        array[begin],array[j]=array[j],array[begin]
                                        
                                        print array[j]
                                        return j
                        return j                                 




        def QuickSort(self, array, begin, end):
                        
                        if 1>=end:
                                        return array

                        elif begin < end :

                                        #Atribui a variavÃ©l num o valor que serÃ¡ retornado em particiona
                                        num=self.particiona(array, begin, end)
                                        #Usa a variavÃ©l num para determinar um novo fim e comeÃ§o para a funÃ§Ã£o quicksort
                                        self.QuickSort(array, begin, num)
                                        self.QuickSort(array, num+1, end)
                                        
                                        return array




"""
class QuickSort(AbstractSortClass):
        def sort_array(self,array):
                end = len(array)
                self.quickSort(array,0,end)
                return array
        
        def particiona(self, array, begin, end):
                i=begin
                j=end-1
                meio = int((i+j)/2)
                pivo=array[meio]

                #Troca o pivÃ´ com o primeiro elemento
                array[i],array[meio] = array[meio],array[i]
                i=+1
                loop_j=0


                while j>i:

                        loop_j=0

                        #Testa se a palavra em left vem antes da palavra em pivÃ´

                        # Verify if it's a number or a word
                        if type(array[i]) is not int:
                                if utilities.this_word_comes_first_than_that(array[i],pivo):
                                        i=i+1
                                else:
                                        while loop_j==0:
                                                #Atribui a variavÃ©l right a palavra em array[j]
                                                #Testa se a palavra no pivÃ´ vem antes da palavra em right
                                                if utilities.this_word_comes_first_than_that(pivo,array[j]):
                                                        j=j-1
                                                else:
                                                        #Troca as palavras no array nas posiÃ§Ãµes i e j
                                                        array[i],array[j] = array[j],array[i]
                                                        i+1
                                                        j-1
                                                        #Encerra o Loop
                                                        loop_j=loop_j+1
                        else:
                                if array[i] < pivo :
                                        i=i+1
                                else:
                                        while loop_j==0:
                                                #Atribui a variavÃ©l right a palavra em array[j]
                                                #Testa se a palavra no pivÃ´ vem antes da palavra em right
                                                if pivo < array[j]:
                                                        j=j-1
                                                else:
                                                        #Troca as palavras no array nas posiÃ§Ãµes i e j
                                                        array[i],array[j] = array[j],array[i]
                                                        i+1
                                                        j-1
                                                        #Encerra o Loop
                                                        loop_j=loop_j+1

                if i>j:
                        #Troca as palavras no array nas posiÃ§Ãµes meio e j
                        array[begin],array[j]=array[j],array[begin]
                                        
                        array[j]
                        return j

                return j

        def quickSort(self, array, begin, end):
                        
                if 1>=end:
                        return array
                elif begin < end :
                        #Atribui a variavÃ©l num o valor que serÃ¡ retornado em particiona
                        num=self.particiona(array, begin, end)
                        #Usa a variavÃ©l num para determinar um novo fim e comeÃ§o para a funÃ§Ã£o quicksort
                        self.quickSort(array, begin, num)
                        self.quickSort(array, num+1, end)
                        return array
"""

				
