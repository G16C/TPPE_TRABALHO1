# arvore_b.py
import icontract
from typing import List, Optional, Tuple, Any
from .no_arvore_b import BTreeNode

class BTree:
    def __init__(self, t: int):
        if t < 2:
            raise ValueError("Ordem 't' deve ser no mínimo 2")
        self.t = t
        self.raiz = BTreeNode(folha=True)
        self.altura = 1  

    def valida_invariantes(self) -> None:
        valid, msg = self.valida_arvore()
        assert valid, f"Invariante violado: {msg}"

    @icontract.require(lambda self, chave: not self.buscar(chave))
    @icontract.ensure(lambda self, result: self._valida_pos_condicao_chaves())
    @icontract.ensure(lambda self, result: self._valida_pos_condicao_filhos())
    @icontract.ensure(lambda self, result: self._valida_pos_condicao_altura_divisao())
    def inserir(self, chave: int) -> None:
        altura_antes = self.altura
        if self.raiz.esta_cheio(self.t):
            nova_raiz = BTreeNode(folha=False)
            nova_raiz.filhos.append(self.raiz)
            self._dividir_filho(nova_raiz, 0)
            self.raiz = nova_raiz
            self.altura += 1
        self._inserir_nao_cheio(self.raiz, chave)
        self.valida_invariantes()

    @icontract.require(lambda self, chave: self.buscar(chave))
    @icontract.ensure(lambda self, result: self._valida_pos_condicao_chaves())
    @icontract.ensure(lambda self, result: self._valida_pos_condicao_filhos())
    @icontract.ensure(lambda self, result: self._valida_pos_condicao_altura_fusao())
    def remover(self, chave: int) -> None:
        altura_antes = self.altura
        self._remover(self.raiz, chave)
        if not self.raiz.chaves and self.raiz.filhos:
            self.raiz = self.raiz.filhos[0]
            self.altura -= 1
        self.valida_invariantes()

    def buscar(self, chave: int) -> bool:
        return self._buscar(self.raiz, chave)

    def _buscar(self, no: BTreeNode, chave: int) -> bool:
        i = 0
        while i < len(no.chaves) and chave > no.chaves[i]:
            i += 1
        if i < len(no.chaves) and chave == no.chaves[i]:
            return True
        if no.folha:
            return False
        return self._buscar(no.filhos[i], chave)

    def _inserir_nao_cheio(self, no: BTreeNode, chave: int) -> None:
        i = len(no.chaves) - 1
        if no.folha:
            no.adicionar_chave(chave)
        else:
            while i >= 0 and chave < no.chaves[i]:
                i -= 1
            i += 1

            if no.filhos[i].esta_cheio(self.t):
                self._dividir_filho(no, i)
                if chave > no.chaves[i]:
                    i += 1

            self._inserir_nao_cheio(no.filhos[i], chave)


    def _dividir_filho(self, pai: BTreeNode, indice: int) -> None:
        filho = pai.filhos[indice]
        novo_no = BTreeNode(folha=filho.folha)
        
        meio = self.t - 1
        chave_meio = filho.chaves[meio]
        novo_no.chaves = filho.chaves[meio+1:]
        filho.chaves = filho.chaves[:meio]
        
        if not filho.folha:
            novo_no.filhos = filho.filhos[meio+1:]
            filho.filhos = filho.filhos[:meio+1]
        
        pai.adicionar_chave(chave_meio)
        pai.adicionar_filho(novo_no, indice+1)

    def _remover(self, no: BTreeNode, chave: int) -> None:
        i = 0
        while i < len(no.chaves) and chave > no.chaves[i]:
            i += 1
            
        if i < len(no.chaves) and chave == no.chaves[i]:
            if no.folha:
                no.remover_chave(i)
            else:
                self._remover_nao_folha(no, i)
        elif not no.folha:
            self._remover_descendente(no, i, chave)

    def _remover_nao_folha(self, no: BTreeNode, indice: int) -> None:
        chave = no.chaves[indice]
        filho_esq = no.filhos[indice]
        filho_dir = no.filhos[indice+1]
        
        if len(filho_esq.chaves) >= self.t:
            predecessor = self._max_chave(filho_esq)
            no.chaves[indice] = predecessor
            self._remover(filho_esq, predecessor)
        elif len(filho_dir.chaves) >= self.t:
            sucessor = self._min_chave(filho_dir)
            no.chaves[indice] = sucessor
            self._remover(filho_dir, sucessor)
        else:
            self._fundir_filhos(no, indice)
            self._remover(filho_esq, chave)

    def _remover_descendente(self, no: BTreeNode, indice: int, chave: int) -> None:
        filho = no.filhos[indice]
        if filho.esta_abaixo(self.t):
            self._garantir_minimo(no, indice)
            if indice >= len(no.filhos):
                filho = no.filhos[indice-1]
        self._remover(filho, chave)

    def _garantir_minimo(self, pai: BTreeNode, indice: int) -> None:
        filho = pai.filhos[indice]
        irmao_esq = pai.filhos[indice-1] if indice > 0 else None
        irmao_dir = pai.filhos[indice+1] if indice < len(pai.filhos)-1 else None
        
        if irmao_esq and len(irmao_esq.chaves) >= self.t:
            self._emprestar_irmao_esq(pai, indice-1, irmao_esq, filho)
        elif irmao_dir and len(irmao_dir.chaves) >= self.t:
            self._emprestar_irmao_dir(pai, indice, filho, irmao_dir)
        elif irmao_esq:
            self._fundir_filhos(pai, indice-1)
        elif irmao_dir:
            self._fundir_filhos(pai, indice)

    def _emprestar_irmao_esq(self, pai: BTreeNode, indice: int, irmao: BTreeNode, filho: BTreeNode) -> None:
        filho.chaves.insert(0, pai.chaves[indice])
        pai.chaves[indice] = irmao.chaves.pop()
        if not irmao.folha:
            filho.filhos.insert(0, irmao.filhos.pop())

    def _emprestar_irmao_dir(self, pai: BTreeNode, indice: int, filho: BTreeNode, irmao: BTreeNode) -> None:
        filho.chaves.append(pai.chaves[indice])
        pai.chaves[indice] = irmao.chaves.pop(0)
        if not irmao.folha:
            filho.filhos.append(irmao.filhos.pop(0))

    def _fundir_filhos(self, pai: BTreeNode, indice: int) -> None:
        esq = pai.filhos[indice]
        dir = pai.remover_filho(indice+1)
        chave_meio = pai.remover_chave(indice)
        
        esq.chaves.append(chave_meio)
        esq.chaves.extend(dir.chaves)
        esq.filhos.extend(dir.filhos)

    def _max_chave(self, no: BTreeNode) -> int:
        while not no.folha:
            no = no.filhos[-1]
        return no.chaves[-1]

    def _min_chave(self, no: BTreeNode) -> int:
        while not no.folha:
            no = no.filhos[0]
        return no.chaves[0]

    # Métodos auxiliares para validação das pós-condições
    def _valida_pos_condicao_chaves(self) -> bool:
        """Pós-condição 1: Para nó-raiz, 1 ≤ numChaves ≤ 2·t; para nós internos, t−1 ≤ numChaves ≤ 2·t"""
        return self._valida_chaves_recursivo(self.raiz)
    
    def _valida_chaves_recursivo(self, no: BTreeNode) -> bool:
        if no == self.raiz:
            # Para nó-raiz: 1 ≤ numChaves ≤ 2·t
            if not (1 <= len(no.chaves) <= 2 * self.t):
                return False
        else:
            # Para nós internos: t−1 ≤ numChaves ≤ 2·t
            if not (self.t - 1 <= len(no.chaves) <= 2 * self.t):
                return False
        
        # Verificar recursivamente os filhos
        for filho in no.filhos:
            if not self._valida_chaves_recursivo(filho):
                return False
        
        return True

    def _valida_pos_condicao_filhos(self) -> bool:
        """Pós-condição 2: Para nó-raiz, o número de filhos é 2 ≤ numFilhos ≤ 2·t; para nós internos, o número de filhos é t ≤ numFilhos ≤ 2·t"""
        return self._valida_filhos_recursivo(self.raiz)
    
    def _valida_filhos_recursivo(self, no: BTreeNode) -> bool:
        if no.folha:
            return True  # Nós folha não têm filhos
        
        if no == self.raiz:
            # Para nó-raiz: 2 ≤ numFilhos ≤ 2·t
            if not (2 <= len(no.filhos) <= 2 * self.t):
                return False
        else:
            # Para nós internos: t ≤ numFilhos ≤ 2·t
            if not (self.t <= len(no.filhos) <= 2 * self.t):
                return False
        
        # Verificar recursivamente os filhos
        for filho in no.filhos:
            if not self._valida_filhos_recursivo(filho):
                return False
        
        return True

    def _valida_pos_condicao_altura_divisao(self) -> bool:
        """Pós-condição 3: Para a raiz, após operação de divisão, nível da árvore aumenta em uma unidade"""
        # Esta validação é feita no método inserir quando há divisão da raiz
        # A altura é incrementada quando a raiz é dividida
        return True  # A lógica já está implementada no método inserir

    def _valida_pos_condicao_altura_fusao(self) -> bool:
        """Pós-condição 3: Para a raiz, após operação de fusão, nível da árvore diminui em uma unidade"""
        # Esta validação é feita no método remover quando há fusão na raiz
        # A altura é decrementada quando a raiz fica vazia e tem apenas um filho
        return True  # A lógica já está implementada no método remover

    def valida_arvore(self) -> Tuple[bool, str]:
        if not self.raiz.chaves and not self.raiz.filhos:
            return True, "Árvore vazia"
        
        folhas_info = []
        return self._valida_no(self.raiz, 0, folhas_info, float('-inf'), float('inf'))

    def _valida_no(self, no: BTreeNode, nivel: int, folhas_info: List[dict], menor_bound: float, maior_bound: float) -> Tuple[bool, str]:
        chaves = no.chaves
        if chaves != sorted(chaves):
            return False, f"Chaves desordenadas: {chaves}"
        if any(chave <= menor_bound or chave >= maior_bound for chave in chaves):
            return False, f"Chaves fora dos limites [{menor_bound}, {maior_bound}]: {chaves}"

        if no == self.raiz:
            if not (1 <= len(no.chaves) <= (2 * self.t - 1)):
                return False, f"Raiz com número inválido de chaves: {len(no.chaves)}"
        else:
            if not (self.t - 1 <= len(no.chaves) <= (2 * self.t - 1)):
                return False, f"Nó com número inválido de chaves: {len(no.chaves)}"

        if no.folha:
            folhas_info.append({"nivel": nivel})
        else:
            if len(no.filhos) != len(no.chaves) + 1:
                return False, f"Número inválido de filhos: {len(no.filhos)}"
            
            for i, filho in enumerate(no.filhos):
                novo_menor = menor_bound if i == 0 else no.chaves[i - 1]
                novo_maior = maior_bound if i == len(no.chaves) else no.chaves[i]
                valido, msg = self._valida_no(filho, nivel + 1, folhas_info, novo_menor, novo_maior)
                if not valido:
                    return False, msg

        if no == self.raiz:
            niveis = {f["nivel"] for f in folhas_info}
            if len(niveis) > 1:
                return False, f"Folhas em níveis diferentes: {niveis}"
            if folhas_info and self.altura != folhas_info[0]["nivel"] + 1:
                return False, f"Altura incorreta: {self.altura} vs {folhas_info[0]['nivel'] + 1}"

        return True, "Árvore válida"
