# no_arvore_b.py
from typing import List, Optional

class BTreeNode:
    def __init__(self, folha: bool):
        self.chaves: List[int] = []
        self.filhos: List['BTreeNode'] = []
        self.folha = folha

    def __repr__(self):
        return f"BTreeNode(chaves={self.chaves}, folha={self.folha})"

    def esta_cheio(self, t: int) -> bool:
        return len(self.chaves) >= (2 * t - 1)
    
    def esta_abaixo(self, t: int) -> bool:
        return len(self.chaves) < (t - 1)
    
    def adicionar_chave(self, chave: int):
        if not self.chaves:
            self.chaves.append(chave)
            return
        
        i = 0
        while i < len(self.chaves) and chave > self.chaves[i]:
            i += 1
        self.chaves.insert(i, chave)
    
    def remover_chave(self, indice: int) -> int:
        return self.chaves.pop(indice)
    
    def adicionar_filho(self, filho: 'BTreeNode', indice: int):
        self.filhos.insert(indice, filho)
    
    def remover_filho(self, indice: int) -> 'BTreeNode':
        return self.filhos.pop(indice)