
# 🌳 Implementação da Árvore-B com Design by Contract

**Universidade de Brasília (UnB)**  
**FCTE - Faculdade de Ciência e Tecnologia em Engenharias**  
**FGA0242 - Técnicas de Programação para Plataformas Emergentes**  
**Professor: André Lanna**  

## 👥 Integrantes do Grupo

| Nome completo                          |
|----------------------------------------|
| Gabriel Campello Marques               |
| Mateus Fidelis Marinho Maia            |
| Cainã Valença de Freitas               |
| Pedro Augusto Dourado Izarias          |

## 📌 Descrição

Este repositório contém a implementação da estrutura de dados **Árvore-B** utilizando o paradigma de **programação por contratos (Design by Contract)** com a biblioteca [`icontract`](https://icontract.readthedocs.io/en/latest/introduction.html).

A estrutura foi desenvolvida do zero com **orientação a objetos** e atende aos critérios de correção especificados pelo professor, incluindo invariantes, pré-condições e pós-condições.

## 📁 Estrutura do Projeto

```text
B-Tree/
├── src/
│   ├── __init__.py
│   ├── arvore_b.py         # Implementação da Árvore-B
│   └── no_arvore_b.py      # Classe Nó da Árvore-B
├── tests/
│   ├── __init__.py
│   └── test_arvore_b.py    # Casos de teste
├── requirements.txt
├── README.md
```

## 🔧 Ambiente Virtual (venv)

1. **Crie o ambiente virtual:**

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

2. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

3. **Execute os testes:**

```bash
pytest
```

## ✅ Critérios atendidos

| Categoria  | Descrição                                                                 | Status |
|------------|---------------------------------------------------------------------------|--------|
| Invariante | Todos os nós folhas estão no mesmo nível                                 | ✔️     |
| Invariante | Chaves internas estão em ordem crescente                                 | ✔️     |
| Invariante | Valores nas folhas estão em ordem crescente                              | ✔️     |
| Pré-cond.  | Chave a ser inserida não existe na árvore                                | ✔️     |
| Pré-cond.  | Chave a ser removida existe na árvore                                    | ✔️     |
| Pós-cond.  | Número de chaves por nó está dentro do intervalo permitido               | ✔️     |
| Pós-cond.  | Número de filhos por nó está dentro do intervalo permitido               | ✔️     |
| Pós-cond.  | Altura aumenta/diminui corretamente após divisão/fusão                   | ✔️     |

✅ **Total: 40/40 pontos atendidos**

## 📚 Referências

- [Icontract Documentation](https://icontract.readthedocs.io/en/latest/introduction.html)
- Cormen et al. **Algoritmos**, 4ª ed. GEN LTC, 2024.
- Szwarcfiter & Markenzon. **Estruturas de Dados e seus Algoritmos**, LTC, 2010.
- Ziviani, Nivio. **Projeto de Algoritmos**, 3ª ed. +A Educação, 2018.

## 📅 Entrega

Trabalho entregue em conformidade com os requisitos da disciplina.  
Prazo final: **23/06/2025 às 18:00h**

---

Desenvolvido com ❤ para a disciplina FGA0242
