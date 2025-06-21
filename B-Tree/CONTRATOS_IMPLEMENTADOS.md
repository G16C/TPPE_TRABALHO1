# Contratos Implementados - Árvore B

Este documento descreve as implementações dos contratos (Design by Contracts) para a estrutura de dados Árvore B.

## Contratos Implementados

### Pré-condições (5 pontos cada)

#### 1. Chave a ser inserida não existe na árvore
```python
@icontract.require(lambda self, chave: not self.buscar(chave))
def inserir(self, chave: int) -> None:
```
**Arquivo**: `src/arvore_b.py` - linha 18

#### 2. Chave a ser removida existe na árvore
```python
@icontract.require(lambda self, chave: self.buscar(chave))
def remover(self, chave: int) -> None:
```
**Arquivo**: `src/arvore_b.py` - linha 30

### Pós-condições (5 pontos cada)

#### 1. Validação do número de chaves
```python
@icontract.ensure(lambda self, result: self._valida_pos_condicao_chaves())
```
**Arquivo**: `src/arvore_b.py` - linhas 19 e 31

**Implementação**: Método `_valida_pos_condicao_chaves()` nas linhas 150-165

**Regras**:
- Para nó-raiz: 1 ≤ numChaves ≤ 2·t
- Para nós internos: t−1 ≤ numChaves ≤ 2·t

#### 2. Validação do número de filhos
```python
@icontract.ensure(lambda self, result: self._valida_pos_condicao_filhos())
```
**Arquivo**: `src/arvore_b.py` - linhas 20 e 32

**Implementação**: Método `_valida_pos_condicao_filhos()` nas linhas 167-185

**Regras**:
- Para nó-raiz: 2 ≤ numFilhos ≤ 2·t
- Para nós internos: t ≤ numFilhos ≤ 2·t

#### 3. Validação da altura após operações
```python
# Para inserção (divisão)
@icontract.ensure(lambda self, result: self._valida_pos_condicao_altura_divisao())

# Para remoção (fusão)
@icontract.ensure(lambda self, result: self._valida_pos_condicao_altura_fusao())
```
**Arquivo**: `src/arvore_b.py` - linhas 21 e 33

**Implementação**: Métodos `_valida_pos_condicao_altura_divisao()` e `_valida_pos_condicao_altura_fusao()` nas linhas 187-195

**Regras**:
- Após divisão da raiz: nível da árvore aumenta em uma unidade
- Após fusão na raiz: nível da árvore diminui em uma unidade

## Invariantes (5 pontos cada)

### 1. Todos os nós folhas estão no mesmo nível
**Arquivo**: `src/arvore_b.py` - método `_valida_no()` linhas 220-225

### 2. Para os nós internos, as chaves estão em ordem crescente
**Arquivo**: `src/arvore_b.py` - método `_valida_no()` linha 200

### 3. Para os nós folhas, todos os valores estão em ordem crescente
**Arquivo**: `src/arvore_b.py` - método `_valida_no()` linha 200

## Testes Implementados

### Arquivo: `tests/test_arvore_b.py`

1. **`test_arvore_b()`** - Teste básico das operações principais
2. **`test_validacao_estrutural()`** - Teste de validação estrutural da árvore
3. **`test_pos_condicao_chaves()`** - Testa a pós-condição 1

## Testes Pendentes para Implementação

### Arquivo: `tests/test_arvore_b.py`

1. **`test_pos_condicao_filhos()`** - Testa a pós-condição 2
2. **`test_pos_condicao_altura_divisao()`** - Testa a pós-condição 3 (divisão)
3. **`test_pos_condicao_altura_fusao()`** - Testa a pós-condição 3 (fusão)
4. **`test_contratos_completos()`** - Testa todos os contratos
5. **`test_casos_extremos()`** - Testa casos extremos

## Como Executar os Testes

```bash
cd B-Tree
python -m pytest tests/test_arvore_b.py -v
```

## Pontuação Total

- **Invariantes**: 15 pontos (3 × 5 pontos)
- **Pré-condições**: 10 pontos (2 × 5 pontos)
- **Pós-condições**: 15 pontos (3 × 5 pontos)
- **Total**: 40 pontos

## Observações

1. **Biblioteca icontract**: Utilizada conforme especificado no enunciado
2. **Orientação a objetos**: Implementação completa usando classes Python
3. **Implementação própria**: Não utiliza bibliotecas externas de árvore B
4. **Validação automática**: Contratos são verificados automaticamente durante execução
5. **Testes pendentes**: Alguns testes específicos das pós-condições ainda precisam ser implementados 