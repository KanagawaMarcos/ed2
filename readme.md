### Conceitos importantes

#### Primeira Prova
* Algoritmo de *ordenação estável*
	* Um algoritmo de ordenação é considerado estável quando ele não altera a posição relativa de itens com chaves iguais.
* *Ordenação Interna*
	* Quando o arquivo a ser ordenado cabe todo na memória interna.
	* *Simples*
		* Velocidade O(n²)
		* Códigos menores e mais simples de entender
		* Adequados para arquivos pequenos
	* *Eficiente*
		* Velocidade O(n\*Log(n))
		* Códigos com menos comparações
		* Comparações mais complexas nos detalhes
		* Adequado para arquivos grandes
* *Ordenação Externa*
	* Quando o algoritmo a ser ordenado não cabe completamente na memória interna e precisa de memória secundária.
* *Ordenação in Situ*
	* Quando o algoritmo faz as permutações no mesmo vetor.
