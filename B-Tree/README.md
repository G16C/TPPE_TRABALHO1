## Enunciado

Esse trabalho consiste na implementação da estrutura de dados Árvore-B e seus algoritmos, principais e auxiliares, com a utilização das técnicas de programação por contratos (Design by Contracts).

⚠️⚠️⚠️ Toda a estrutura da Árvore-B e suas operações deverão ser implementadas pelos grupos, utilizando o paradigma de orientação por objetos em seu desenvolvimento. Não serão aceitos trabalhos que utilize implementações de Árvore-B já disponibilizadas por bibliotecas.

Os trabalhos deverão ser desenvolvidos em Python3, com a utilização da biblioteca icontract para implementação dos contratos. Os contratos a serem implementados, descritos em termos de invariantes e pré- e pós-condições, estão apresentados na seção Pontuação e critérios de correção, apresentada em seguida.

Os elementos a serem inseridos na árvore são valores inteiros. Os grupos podem usar os valores apresentados no exemplo desse trabalho para que possam avaliar a implementação.

## Pontuação e critérios de correção

Esse trabalho vale 40 pontos no cálculo final de menção. A pontuação está distribuída conforme tabela apresentada abaixo.
| Tipo        | Descrição                                                                                                                                   | Valor     |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Invariante  | Todos os nós folhas estão no mesmo nível?                                                                                                   | 5 pontos  |
| Invariante  | Para os nós internos, as chaves estão em ordem crescente?                                                                                   | 5 pontos  |
| Invariante  | Para os nós folhas, todos os valores estão em ordem crescente?                                                                              | 5 pontos  |
| Pré         | Chave a ser inserida não existe na árvore                                                                                                   | 5 pontos  |
| Pré         | Chave a ser removida existe na árvore                                                                                                       | 5 pontos  |
| Pós         | Para nó-raiz, 1 ≤ numChaves ≤ 2·t; para nós internos, t − 1 ≤ numChaves ≤ 2·t                                                               | 5 pontos  |
| Pós         | Para nó-raiz, o número de filhos é 2 ≤ numFilhos ≤ 2·t; para nós internos, o número de filhos é t ≤ numFilhos ≤ 2·t                        | 5 pontos  |
| Pós         | Para a raiz, após operação de divisão, nível da árvore aumenta em uma unidade; após operação de fusão, nível da árvore diminui em uma unidade | 5 pontos  |
| **TOTAL**   |                                                                                                                                              | **40 pontos** |


⚠️⚠️⚠️ Penalidades: ⚠️⚠️⚠️

- Trabalhos que utilizaram implementações de bibliotecas e não implementaram a estrutura de Arvore-B: -100% da nota.
- Trabalhos que não utilizaram conceitos de orientação por objetos na implementação dos componentes da Árvore-B: -80% da nota.
- Trabalhos que utilizaram outro framework de projeto por contratos, diferente do icontract: -50% da nota.
