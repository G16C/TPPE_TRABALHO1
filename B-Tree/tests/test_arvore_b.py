from src.arvore_b import BTree
import pytest
import icontract.errors

def test_arvore_b():
    t = 2
    arvore = BTree(t)
    chaves = [10, 20, 5, 6, 12, 30, 7, 17]
    
    for chave in chaves:
        arvore.inserir(chave)
  
    with pytest.raises(icontract.errors.ViolationError):
        arvore.inserir(10)
   
    for chave in chaves:
        assert arvore.buscar(chave)
    assert not arvore.buscar(99)
    
    arvore.remover(6)
    assert not arvore.buscar(6)
  
    with pytest.raises(icontract.errors.ViolationError):
        arvore.remover(99)
    
    valido, msg = arvore.valida_arvore()
    assert valido, msg


def test_validacao_estrutural():
    arvore = BTree(t=3)
    chaves = list(range(1, 50))
    for chave in chaves:
        arvore.inserir(chave)
    
    valido, msg = arvore.valida_arvore()
    assert valido, msg
    
    assert arvore.altura >= 2


def test_pos_condicao_chaves():
    """Testa a pós-condição 1: Para nó-raiz, 1 ≤ numChaves ≤ 2·t; para nós internos, t−1 ≤ numChaves ≤ 2·t"""
    arvore = BTree(t=3)
    
    # Teste com árvore vazia (deve falhar na pós-condição)
    with pytest.raises(AssertionError):
        arvore._valida_pos_condicao_chaves()
    
    # Teste com inserções que devem manter a pós-condição
    chaves = [10, 20, 5, 6, 12, 30, 7, 17, 25, 35, 40, 45, 50]
    for chave in chaves:
        arvore.inserir(chave)
        # Após cada inserção, a pós-condição deve ser válida
        assert arvore._valida_pos_condicao_chaves(), f"Pós-condição de chaves violada após inserir {chave}"


if __name__ == "__main__":
    test_arvore_b()
    test_validacao_estrutural()
    test_pos_condicao_chaves()
    print("Todos os testes passaram!")
