import pygame
from random import randint

class Dados:
    def __init__(self):
        self.resultado = (None, None)  # inicializa os dados sem valores definidos

    def calcular_lancamento(self):
        self.resultado = (randint(1, 6), randint(1, 6))  # gera dois números aleatórios entre 1 e 6

def main():
    pygame.init()  # inicializa todos os módulos do pygame
    tamanho_tela = (1000, 600) 
    tela = pygame.display.set_mode(tamanho_tela)  # cria a janela do jogo com o tamanho especificado
    pygame.display.set_caption('Cramps - The Gambling Game')  # define o título da janela
    fundoimg = pygame.image.load('fundo.png')  # carrega a imagem de fundo
    fonte = pygame.font.Font(None, 30)  # define a fonte para o texto do jogo
    orcamento = 0
    cores = {
        "branco": (255, 255, 255),
        "preto": (0, 0, 0),
        "azul": (0, 0, 255),
        "cinza": (200, 200, 200)
    }  # define cores com dicionário
    
    def desenhar_inicio_jogo():
        tela.blit(fundoimg, (0, 0))  # desenha a imagem de fundo na posição (0,0)
        
    def centralizar_texto(texto, tamanho_tela):
        return texto.get_rect(center=(tamanho_tela[0] // 2, tamanho_tela[1] // 2))
    
    def escrita_fixa():
        fonte_grande = pygame.font.Font(None, 100)  # define uma fonte maior
        
        # renderiza título e subtítulo
        texto1 = fonte_grande.render('CRAMPS', True, cores['branco'])
        texto2 = fonte_grande.render('The gambling game', True, cores['branco'])
        
        # centraliza título e subtítulo
        pos_t1 = centralizar_texto(texto1, tamanho_tela)
        pos_t2 = centralizar_texto(texto2, tamanho_tela)
        
        pos_t1.y = 10  # define a posição do título na parte superior da tela
        pos_t2.y = 90  # define a posição do subtítulo um pouco abaixo do título
        
        # desenha título e subtítulo na tela
        tela.blit(texto1, pos_t1)  
        tela.blit(texto2, pos_t2)  

    def desenhar_caixa_texto(retangulo, texto, ativo, legenda, prefixo=None):
        cor_borda = cores['azul'] if ativo else cores['cinza']  # azul se ativa, cinza se inativa
        pygame.draw.rect(tela, cores['branco'], retangulo)  # fundo branco
        pygame.draw.rect(tela, cor_borda, retangulo, 3)  # adiciona borda a caixa

        # renderiza e exibe a legenda acima da caixa
        texto_legenda = fonte.render(legenda, True, cores['branco'])
        tela.blit(texto_legenda, (retangulo.x, retangulo.y - 30))  

        if prefixo:
            # renderiza e exibe o prefixo dentro da caixa, alinhado a esquerda
            texto_prefixo = fonte.render(prefixo, True, cores['preto'])
            tela.blit(texto_prefixo, (retangulo.x + 10, retangulo.y + 15))
            deslocamento_x = 50  # ajuste para nao sobrepor o prefixo
        else:
            deslocamento_x = 10

        # renderiza e exibe o texto digitado
        superficie_texto = fonte.render(texto, True, cores['preto'])
        tela.blit(superficie_texto, (retangulo.x + deslocamento_x, retangulo.y + 15))  
        
    def desenha_botao_rolagem(dados, retangulo, ativo):
        cor_borda = cores['azul'] if ativo else cores['cinza']  # azul se ativa, cinza se inativa
        pygame.draw.rect(tela, cores['branco'], retangulo)  # botão de rolagem
        pygame.draw.rect(tela, cor_borda, retangulo, 3)  # adiciona borda a caixa
        
        rolar_txt = fonte.render('Rolagem', True, cores['preto'])  # texto do botão
        tela.blit(rolar_txt, (640, 355))  # exibe o texto no botão
        
        # exibe os valores dos dados após a rolagem
        if dados.resultado[0] is not None:
            dado1_txt = fonte.render(str(dados.resultado[0]), True, cores['preto'])
            dado2_txt = fonte.render(str(dados.resultado[1]), True, cores['preto'])
            
            tela.blit(dado1_txt, (580, 260))  # lugar do primeiro dado
            tela.blit(dado2_txt, (770, 260))  # lugar do segundo dado

    def desenhar_area_dados(dados):
        desenha_botao_rolagem(dados, botao_rolagem, caixa_ativa == "rolagem")
        pygame.draw.rect(tela, cores['branco'], (500, 200, 350, 200), 3)  # area dos dados
        pygame.draw.rect(tela, cores['branco'], (550, 230, 80, 80))  # primeiro dado
        pygame.draw.rect(tela, cores['branco'], (740, 230, 80, 80))  # segundo dado
        
    def desenhar_orcamento():
        texto_legenda = fonte.render("Orçamento:", True, cores['branco'])
        texto_valor = fonte.render(f"R$: {orcamento}", True, cores['branco'])
        x_legenda = tamanho_tela[0] - 200
        y_legenda = tamanho_tela[1] - 80
        x_valor = tamanho_tela[0] - 200
        y_valor = tamanho_tela[1] - 50
        
        tela.blit(texto_legenda, (x_legenda, y_legenda))
        tela.blit(texto_valor, (x_valor, y_valor))        
        
    # variaveis das caixas de texto
    dados = Dados()
    caixa_aposta = pygame.Rect(100, 200, 200, 50)
    caixa_numero = pygame.Rect(100, 300, 200, 50)
    botao_rolagem = pygame.Rect(620, 330, 120, 60)
    texto_aposta = ''
    texto_numero = ''
    caixa_ativa = None  # variavel para saber em qual caixa o usuário está digitando
    
    fim_jogo = False  # flag para encerrar o jogo

    while not fim_jogo:
        # atualiza funcoes
        desenhar_inicio_jogo()  
        escrita_fixa()  
        desenhar_area_dados(dados)
        desenha_botao_rolagem(dados, botao_rolagem, False)
        desenhar_caixa_texto(caixa_aposta, texto_aposta, caixa_ativa == "aposta", "Dinheiro a ser apostado:", "R$:")  
        desenhar_caixa_texto(caixa_numero, texto_numero, caixa_ativa == "numero", "Apostar valor dos dados:")
        desenhar_orcamento()
        
        for evento in pygame.event.get(): 
            
            if evento.type == pygame.QUIT:  
                fim_jogo = True  
            
            elif evento.type == pygame.MOUSEBUTTONDOWN:  
                if caixa_aposta.collidepoint(evento.pos):  
                    caixa_ativa = "aposta"
                elif caixa_numero.collidepoint(evento.pos):  
                    caixa_ativa = "numero"
                elif botao_rolagem.collidepoint(evento.pos): 
                    dados.calcular_lancamento()  
                else:
                    caixa_ativa = None   
            elif evento.type == pygame.KEYDOWN and caixa_ativa:  # identifica quando o teclado é usado
                if evento.key == pygame.K_BACKSPACE:  # verifica o uso do backspace
                    if caixa_ativa == "aposta":
                        texto_aposta = texto_aposta[:-1]  
                    elif caixa_ativa == "numero":
                        texto_numero = texto_numero[:-1]  
                else:  #assimila o texto a aposta do tipo string 
                    if caixa_ativa == "aposta" and evento.unicode.isdigit():
                        texto_aposta += evento.unicode  
                    elif caixa_ativa == "numero" and evento.unicode.isdigit():# permite apenas números
                        novo_valor = texto_numero + evento.unicode
                        if novo_valor.isdigit():
                            texto_numero = novo_valor
                            
        pygame.display.flip()  # atualiza a tela
    pygame.quit()  # finaliza o pygame quando o jogo encerra

if __name__ == '__main__':
    main()
