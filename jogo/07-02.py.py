import pygame
from random import randint

class Dados:
    def __init__(self):
        self.resultado = (None, None)  # inicializa os dados sem valores definidos

    def calcular_lancamento(self):
        self.resultado = (randint(1, 6), randint(1, 6))  # gera dois números aleatórios entre 1 e 6

def main():
    pygame.init()  # inicializa todos os módulos do pygame
    #config janela
    tamanho_tela = (1000, 600) 
    tela = pygame.display.set_mode(tamanho_tela) 
    pygame.display.set_caption('Cramps - The Gambling Game')

    #fundo e fonte
    fundoimg = pygame.image.load('fundo.png') 
    fonte = pygame.font.Font(None, 30)

    # variáveis do jogo
    orcamento = 100  
    mensagem = ""  

    cores = {
        "branco": (255, 255, 255),
        "preto": (0, 0, 0),
        "azul": (0, 0, 255),
        "cinza": (200, 200, 200),
        "vermelho": (255, 0, 0),
        "verde": (0, 255, 0)
    }
    
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
        cor_borda = cores['azul'] if ativo else cores['cinza']
        pygame.draw.rect(tela, cores['branco'], retangulo)
        pygame.draw.rect(tela, cor_borda, retangulo, 3)

        texto_legenda = fonte.render(legenda, True, cores['branco'])
        tela.blit(texto_legenda, (retangulo.x, retangulo.y - 30))

        deslocamento_x = 50 if prefixo else 10
        
        if prefixo:
            texto_prefixo = fonte.render(prefixo, True, cores['preto'])
            tela.blit(texto_prefixo, (retangulo.x + 10, retangulo.y + 15))

        superficie_texto = fonte.render(texto, True, cores['preto'])
        tela.blit(superficie_texto, (retangulo.x + deslocamento_x, retangulo.y + 15))
        
    def desenha_botao_rolagem(dados, retangulo, ativo):
        cor_borda = cores['azul'] if ativo else cores['cinza']  # azul se ativa, cinza se inativa
        pygame.draw.rect(tela, cores['branco'], retangulo)  # botão de rolagem
        pygame.draw.rect(tela, cor_borda, retangulo, 3)  # adiciona borda a caixa
        texto_botao = fonte.render("Rolagem", True, cores['preto'])  # texto do botão
        tela.blit(texto_botao, (retangulo.x + 20, retangulo.y + 15)) # exibe o texto no botão
        
        # exibe os valores dos dados após a rolagem
        if dados.resultado[0] is not None:
            dado1_txt = fonte.render(str(dados.resultado[0]), True, cores['preto'])
            dado2_txt = fonte.render(str(dados.resultado[1]), True, cores['preto'])
            
            tela.blit(dado1_txt, (580, 260))  # lugar do primeiro dado
            tela.blit(dado2_txt, (770, 260))  # lugar do segundo dado

    def desenhar_area_dados(dados):
        desenha_botao_rolagem(dados, botao_rolagem, False)
        pygame.draw.rect(tela, cores['branco'], (500, 200, 350, 200), 3)  # area dos dados
        pygame.draw.rect(tela, cores['branco'], (550, 230, 80, 80))  # primeiro dado
        pygame.draw.rect(tela, cores['branco'], (740, 230, 80, 80))  # segundo dado
        

    def desenhar_orcamento():
        texto_legenda = fonte.render("Orçamento:", True, cores['branco'])
        texto_valor = fonte.render(f"R$: {orcamento}", True, cores['branco'])
        tela.blit(texto_legenda, (tamanho_tela[0] - 200, tamanho_tela[1] - 80))
        tela.blit(texto_valor, (tamanho_tela[0] - 200, tamanho_tela[1] - 50))

    def desenhar_mensagem():
        if mensagem:
            cor_msg = cores['verde'] if "GANHOU" in mensagem else cores['vermelho']
            texto_msg = fonte.render(mensagem, True, cor_msg)
            tela.blit(texto_msg, (500, 420))

    # variaveis das caixas de texto
    dados = Dados()
    caixa_aposta = pygame.Rect(100, 200, 200, 50)
    caixa_numero = pygame.Rect(100, 300, 200, 50)
    botao_rolagem = pygame.Rect(620, 330, 120, 60)
    texto_aposta = ''
    texto_numero = ''
    caixa_ativa = None # variavel para saber em qual caixa o usuário está digitando

    fim_jogo = False

    while not fim_jogo:
        #atualiza funcoes
        
        tela.blit(fundoimg, (0, 0))
        desenhar_inicio_jogo()
        escrita_fixa()
        desenhar_area_dados(dados)
        desenha_botao_rolagem(dados, botao_rolagem, False)
        desenhar_caixa_texto(caixa_aposta, texto_aposta, caixa_ativa == "aposta", "Dinheiro a ser apostado:", "R$:")  
        desenhar_caixa_texto(caixa_numero, texto_numero, caixa_ativa == "numero", "Apostar valor dos dados:")
        desenhar_orcamento()
        desenhar_mensagem()

        for evento in pygame.event.get():  
            
            if evento.type == pygame.QUIT:  
                fim_jogo = True  
                
            elif evento.type == pygame.MOUSEBUTTONDOWN:  
                if caixa_aposta.collidepoint(evento.pos):  
                    caixa_ativa = "aposta"
                elif caixa_numero.collidepoint(evento.pos):  
                    caixa_ativa = "numero"
                elif botao_rolagem.collidepoint(evento.pos): 
                    if texto_aposta.isdigit() and texto_numero.isdigit():
                        aposta = int(texto_aposta)
                        numero_apostado = int(texto_numero)
                        if aposta > 0 and aposta <= orcamento:  
                            dados.calcular_lancamento()
                            soma_dados = sum(dados.resultado)
                            if soma_dados == numero_apostado:
                                orcamento += aposta
                                mensagem = "VOCÊ GANHOU! +" + str(aposta)
                            else:
                                orcamento -= aposta
                                mensagem = "VOCÊ PERDEU! -" + str(aposta)
                        else:
                            mensagem = "Aposta inválida!"
                    else:
                        mensagem = "Digite valores válidos!"
                else:
                    caixa_ativa = None   
            elif evento.type == pygame.KEYDOWN and caixa_ativa:
                if evento.key == pygame.K_BACKSPACE:
                    if caixa_ativa == "aposta":
                        texto_aposta = texto_aposta[:-1]  
                    elif caixa_ativa == "numero":
                        texto_numero = texto_numero[:-1]  
                else:
                    if caixa_ativa == "aposta" and evento.unicode.isdigit():
                        texto_aposta += evento.unicode  
                    elif caixa_ativa == "numero" and evento.unicode.isdigit():
                        texto_numero += evento.unicode
                            
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()
