#%%
def retornar_item_por_css(html, lista_seletores=["selec q nao existe","","h1.product_title.entry-title"]):
    """
    Função que encontra um item HTML por meio de seletor CSS

    Parâmetros: 
        html (str): cópia do elemento body do html da página
        lista_seletores (list): seletores definidos para fazer a busca

    Retorno:
        item_encontrado (str): conteudo do item encontrado por um dos seletores da lista
    """    
    # essa função serve pra fazer a busca dos possiveis seletores
    def encontrar_seletor():
        for seletor in lista_seletores:
            if seletor != "":
                seletor_encontrado = html.select(seletor)
                if seletor_encontrado != []:
                    return seletor_encontrado

    seletor_encontrado = encontrar_seletor()
    # filtro de validação do None
    # quando o seletor é None, ele não tem index, retornando erro de NoneType
    if seletor_encontrado != None:
        # filtra o conteudo do item do seletor
        item_encontrado = seletor_encontrado[0].text
        return item_encontrado

def retornar_imagem_por_css(html, seletor_css="img.wp-post-image", atributo="src"):
    """
    Função que encontra o link de uma imagem HTML por meio de seletor CSS

    Parâmetros: 
        html (str): cópia do elemento body do html da página
        seletor_css (list): seletor definidos para fazer a busca

    Retorno:
        img_encontrada (str): imagem encontrado pelo seletor
    """    
    # busca dos possiveis seletores

    if seletor_css != "":
        seletor_encontrado = html.select(seletor_css)
        # filtro de validação do None e do nao encontrado (vazio)
        # quando o seletor é None, ele não tem index, retornando erro de NoneType
        if seletor_encontrado != [] or seletor_encontrado != None:
            # filtra o conteudo do item do seletor
            imagem_encontrada = seletor_encontrado[0]
            return imagem_encontrada.get(atributo)
                    
