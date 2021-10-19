# Arrays e Listas Encadeadas

## Arrays

Um array armazena items continuamente ou de maneira linear. Podemos armazenar em um array uma quantidade determinada de elementos. No entando, existem cenários que pode nos ocorrer, quando precisamos armazenar os dados.

Vamos criar uma situacao hipotética, imagine que alguns amigos vao ao cinema. Compraram 5 cadeiras, no entanto, quando foram sentar, uma das cadeiras estavam ocupadas. Forcando a todos se moverem para ter espaco livre para as 5 pessoas.

Embora todos se movam, podem cair no mesmo problema de espaco insuficiente, forcando os mesmos a moverem novamente. Logo, chegamos a uma outra solucao. Solicitar para ter mais de 5 espacos reservados, assim, as cadeiras seguintes, poderiam ser preenchidas.

Mas, mesmo assim, caimos em um outro problema, o desperdicio de espaco, pois, pode existir o cenario que todas as cadeiras reservadas, nao sejam ocupadas.

## Listas Encadeadas

Sua grande diferenca comparada aos arrays, e que sua posicao pode ser armazenada em qualquer lugar da memória. Sempre guardando uma referencia da posicao anterior da lista.
Logo, para o cenario do cinema, se existir espaco disponivel no cinema, todos estariam alocados corretamente.

## Arrays vs Listas Encadeadas

Listas Encadeadas sao terriveis para buscar um elemento aleatorio. Por exemplo, caso precise saber qual o elemento do ultimo indice, teriamos que buscar um por um, pois teriamos que ter a referencia do primeiro elemento para chegar no dois, e assim por diante.

Com os arrays, sao diferentes, voce tem acesso facil a todos os indices do array.

### Tempo de execucao

|   | Arrays  | Listas  |
|---|---|---|
| LEITURA  | O (1)  |  O (n) |
| INSERCAO  | O (n)  |  O (1) |
