#This Python file uses the following encoding: utf-8 
import utilities 

class ShellSort():
        def sort_array(self, array):
                size=len(array)-1
                gap=1
                
                #Faz com que a variavÃ©l H receba o maior valor possÃ­vel
                while gap<size:
                        gap=(gap*3)+1
                while gap>=1:
                        i=0
                        j=gap
                        #Percorre a array nas posiÃ§Ãµes i e j, na distÃ¢ncia h atÃ© o final do vetor
                        while j<size and gap>0:
                                #Testa para ver se a palavra no array[j] vem antes do array[i]
                                if utilities.this_word_comes_first_than_that(array[j],array[i])
                                        #Troca as palavras da array
                                        array[i],array[j]=array[j],array[i]
                                        #Movimenta as variaveis i e j
                                        j=j+gap
                                        i=i+gap
                                #Atualiza o valor de h             
                                gap=(gap-1)/3
        return array
