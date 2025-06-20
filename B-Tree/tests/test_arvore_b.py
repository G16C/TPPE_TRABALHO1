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

if __name__ == "__main__":
    test_arvore_b()
    test_validacao_estrutural()
    print("Todos os testes passaram!")
