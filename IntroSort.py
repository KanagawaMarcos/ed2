#This Python file uses the following encoding: utf-8 
import utilities,Quicksort,math

class IntroSort():

    def sort_array(self,array):
        end=len(array)
        depthlimit = 2*math.log(end,10)
        print depthlimit
        
        self.real_IntroSort(array,0,end,depthlimit)
        return array

    def real_IntroSort(self,array,begin,end,depthlimit):
            size = end - begin;
 
            print 'entrou\n'
            if 16>=size:
                    print 'entrou\n'
                    self.InsertionSort(array, begin, end)
                    return array;
          
       
            print 'passou\n'
            
            if 0>=depthlimit :
          
                    self.heapSort(array,end,begin)

                    return array


            else:
            
                    print 'passou_parti\n'
                    partitionPoint=self.particiona(array, begin, end)
                    self.real_IntroSort(array, begin, partitionPoint-1, depthlimit - 1)
                    self.real_IntroSort(array, partitionPoint + 1, end, depthlimit - 1)

                    return array


    # Sort an array using Selection Sort
    def InsertionSort(self, array,begin,end):
            print 'funciona\n'
            # Loop through the entire array
            for current_foward in range( begin, end ):

                    # Go on each element before the current

                    current_backwards = current_foward
                    # Check which word comes first in alphabetic order

                    this = array[current_backwards-1]
                    that = array[current_backwards]

                    # Do it whithout going out of the array boundery
                    while current_backwards > 0 and that<this:
                            
                            # Swap the words

                            i = current_backwards
                            j = (current_backwards - 1)

                            array[i],array[j] = array[j],array[i]

                            # Update their indexes to go even futher in the array
                            current_backwards -= 1

                            this = array[current_backwards-1]
                            that = array[current_backwards]
            return array
            


        # Python program for implementation of heap Sort
     
    # To heapify subtree rooted at index i.
    # n is size of heap
    def heapify(self,array, end, i):
            largest = i  # Initialize largest as root
            l = 2 * i + 1     # left = 2*i + 1
            r = 2 * i + 2     # right = 2*i + 2
            
            print 'passou_heap\n'
            # See if left child of root exists and is
            # greater than root
            if l < end and array[i] < array[l]:
                    largest = l
         
            # See if right child of root exists and is
            # greater than root
            if r < end and array[largest] < array[r]:
                    largest = r
         
            # Change root, if needed
            if largest != i:
                    array[i],array[largest] = array[largest],array[i]  # swap
         
                # Heapify the root.
                    self.heapify(array, end, largest)
     
    # The main function to sort an array of given size
    def heapSort(self, array,end,begin):
     
        # Build a maxheap.
            for i in range(end, begin, -1):
                    print 'passou_heap_1\n'
                    self.heapify(array, end, i)
     
        # One by one extract elements
            for i in range(end-1, begin, -1):
                    print 'passou_heap_2\n'
                    array[i], array[0] = array[0], array[i]   # swap
                    self.heapify(array, i, 0)
            print 'FUNFOU\n'
            return array



    def particiona(self, array, begin, end):
                        i=begin
                        j=end-1
                        meio = (i+j)/2
                        pivo=array[meio]
                        print 'passou_PARTI\n'
                        #Troca o pivÃ´ com o primeiro elemento
                        array[i],array[meio] = array[meio],array[i]
                        i=+1
                        loop_j=0


                        while j>i:

                                        loop_j=0
                                
                                        #Testa se a palavra em left vem antes da palavra em pivÃ´
                                        print 'NO_LOOP\n'
                                        print i
                                        if array[i]<pivo:
                                                        i=i+1
                                        else:
                                                        while loop_j==0:
                                                                        #Atribui a variavÃ©l right a palavra em array[j]
                                                                        print '\n'
                                                                        print j
                                                                        #Testa se a palavra no pivÃ´ vem antes da palavra em right
                                                                        if pivo>array[j]:
                                                                                        j=j-1
                                                                        else:
                                                                                        #Troca as palavras no array nas posiÃ§Ãµes i e j
                                                                                        array[i],array[j] = array[j],array[i]
                                                                                     
                                                                                        i=i+1
                                                                                        j=j-1

                                                                                        print 'NO_LOOP_2\n'
                                                                                        #Encerra o Loop
                                                                                        loop_j=loop_j+1
                        if i>j:
                                        #Troca as palavras no array nas posiÃ§Ãµes meio e j
                                        array[begin],array[j]=array[j],array[begin]
                                        print 'SAINDO\n'
                                        print j
                          
                                        return j
                        return j
