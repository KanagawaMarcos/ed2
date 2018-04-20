#This Python file uses the following encoding: utf-8 
import utilities 

class ShellSort():
  
                def sort_array(self, array):
                                size=len(array)-1
                                h=1
                                #Faz com que a variavÃ©l H receba o maior valor possÃ­vel
                                while h<size:
                                        h=(h*3)+1

                                while h>=1:
                                                
                                                print h
                                                print '\n'
                                                i=0
                                                j=h
                                                print'entrou'
                                                #Percorre a array nas posiÃ§Ãµes i e j, na distÃ¢ncia h atÃ© o final do vetor
                                                while j<size and h<>0:
                                                                #Testa para ver se a palavra no array[j] vem antes do array[i]
                                                                if utilities.this_word_comes_first_than_that(array[i],array[j])
                                                                                
                                                                                #Troca as palavras da array
                                                                                array[i],array[j]=array[j],array[i]
                            
                                                                #Movimenta as variaveis i e j
                                                                j=j+h
                                                                i=i+h
                                                                print j
                                                #Atualiza o valor de h             
                                                h=(h-1)/3
                                                
                                                            
                                                    
                                return array
                
