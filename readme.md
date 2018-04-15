### Conceitos importantes


#### Primeira Prova
* **Selection Sort**
	* O(n²)
	* Não é estável
	* Seleciona o menor elemento após o atual e troca ambos de lugar.
	* A ordenação inicial do vetor não altera o custo de execução.
* **Insetion Sort**
	* O(n²)
	* É estável
	* Pega o menor item após o atual e o insere na posição correta antes do atual.
	* Recomendado para arquivos semi ordenados
* **Shell Sort**
	* O(??)
	* Não é estável
	* É uma variação do Insertion Sort
	* Define uma distancia inicial sendo metade do arquivo, compara e troca elementos com essa distancia, por fim divide a distancia pela metade recomeça. 
	* Quando a distancia é igual à 1 o algoritmo executa um Insetion Sort
	* Não é estável
	* Recomendado para arquivos de tamanhos moderados
	* Implementação dele é simples
	* Sensivel à ordem original do arquivo
* **Merge Sort**
	* O(n\*Log(n))
	* É estável
	* Out place
* **Quick Sort**
	* Melhor/Médio caso O(n\*Log(n))
	* Não é estável
	* Pior caso O(n²)
	* O custo é igual O(n\*Log(n)), independente da entrada.
	* Precisa de pouca memória
	* Out place
* **Heap Sort**
	* O custo é igual O(n\*Log(n)), independente da entrada.

* **Ordenação estável**
	* Um algoritmo de ordenação é considerado estável quando ele não altera a posição relativa de itens com chaves iguais.
	* Insertion Sort
* **Ordenação Interna**
	* Quando o arquivo a ser ordenado cabe todo na memória interna.
	* **Simples**
		* Velocidade O(n²)
		* Códigos menores e mais simples de entender
		* Adequados para arquivos pequenos
	* **Eficiente**
		* Velocidade O(n\*Log(n))
		* Códigos com menos comparações
		* Comparações mais complexas nos detalhes
		* Adequado para arquivos grandes
* **Ordenação Externa**
	* Quando o algoritmo a ser ordenado não cabe completamente na memória interna e precisa de memória secundária.
* **Ordenação in Situ**
	* Quando o algoritmo faz as permutações no mesmo vetor.

