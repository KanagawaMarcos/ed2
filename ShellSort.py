Class ShellSort(object){
	
		def shell(self, array):
				
				size=len(array)
				h=1

				for h in range(1,size,(h*3)+1):
					
				while h>0:
							i=0
							j=h

							while j<=h:

									if self.__this_word_comes_first_than_that(array[i], array[j]):
										array[i],array[j]=array[j],array[i]
											j=+1
											i=+1

	}