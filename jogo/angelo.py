import pygame
from random import randint

class Dados:
    def __init__(self):
        self.resultado = (None, None)  # inicializa os dados sem valores definidos

    def calcular_lancamento(self):
        self.resultado = (randint(1, 6), randint(1, 6))  # gera dois números aleatórios entre 1 e 6
        
def main():
    pygame.init()  # inicializa todos os modulos do pygame q fazem o jogo funcionar
    tamanho_tela = (1000, 600) 
    tela = pygame.display.set_mode(tamanho_tela)  # cria a janela do jogo com o tamanho especificado
    pygame.display.set_caption('Cramps - The Gambling Game')  # define o título da janela
    fundoimg = pygame.image.load('fundo.png')  # carrega a imagem de fundo
    fonte = pygame.font.Font(None, 30)  # define a fonte para o texto do jogo

    cores = {
        "branco": (255, 255, 255),
        "preto": (0, 0, 0),
        "vermelho": (255, 0, 0),
        "amarelo": (255, 255, 0),
        "azul": (0, 0, 255),
        "verde": (0, 255, 0)
    } #define cores com dicionario
    
    def desenhar_inicio_jogo():
        tela.blit(fundoimg, (0, 0)) # desenha a imagem de fundo na posição (0,0)
        
    def centralizar_texto(texto, tamanho_tela):
        return texto.get_rect(center=(tamanho_tela[0] // 2, tamanho_tela[1] // 2))
    
    def escrita_fixa():
        fonte_grande = pygame.font.Font(None, 100)  # define uma fonte maior
        
        #renderiza titulo e subtitulo
        texto1 = fonte_grande.render('CRAMPS', True, cores['branco'])
        texto2 = fonte_grande.render('The gambling game', True, cores['branco'])
        
        #centraliza título e subtítulo
        pos_t1 = centralizar_texto(texto1, tamanho_tela)
        pos_t2 = centralizar_texto(texto2, tamanho_tela)
        
        pos_t1[1] = 0  # define a posição do título na parte superior da tela
        pos_t2[1] = 80  # define a posição do subtítulo um pouco abaixo do título
        
        #desenha titulo e subtitulo na tela
        tela.blit(texto1, pos_t1)  
        tela.blit(texto2, pos_t2)  
        
    def desenhar_caixas_texto()->tuple:
        caixa_aposta=pygame.Rect(100, 200, 200, 50) # caixa de "Aposta"
        caixa_numero=pygame.Rect(100, 270, 200, 50) # caixa de "Número"
        
        aposta = fonte.render('Aposta', True, cores['preto'])  # texto "Aposta"
        numero = fonte.render('Número', True, cores['preto'])  # texto "Número"
        
        # exibe o texto dentro da caixa
        tela.blit(aposta, (120, 215))  
        tela.blit(numero, (120, 285))
        return caixa_aposta,caixa_numero  
        
    def desenhar_area_dados(dados):
        pygame.draw.rect(tela, cores['branco'], (500, 200, 350, 200), 3)  # area dos dados
        pygame.draw.rect(tela, cores['branco'], (550, 230, 80, 80))  # primeiro dado
        pygame.draw.rect(tela, cores['branco'], (740, 230, 80, 80))  # segundo dado
        pygame.draw.rect(tela, cores['branco'], (620, 330, 120, 60))  # botao de rolagem
        
        rolar_txt = fonte.render('Rolagem', True, cores['preto'])  # texto do botão
        tela.blit(rolar_txt, (640, 355))  # exibe o texto no botão
        
        # exibe os valores dos dados após a rolagem
        if dados.resultado[0] is not None:
            dado1_txt = fonte.render(str(dados.resultado[0]), True, cores['preto'])
            dado2_txt = fonte.render(str(dados.resultado[1]), True, cores['preto'])
            
            tela.blit(dado1_txt, (560, 260))  # lugar do primeiro dado
            tela.blit(dado2_txt, (750, 260))  # lugar do segundo dado
            
    #loop principal do jogo       
    dados = Dados()
    texto_aposta=''
    texto_numero=''  
    fim_jogo = False 
    

    while not fim_jogo:
        #atualiza funcoes
        desenhar_inicio_jogo()  
        escrita_fixa()  
        desenhar_area_dados(dados)
        caixa_aposta,caixa_numero=desenhar_caixas_texto() #pega a posição das caixas
        
        for evento in pygame.event.get(): 
             
            if evento.type == pygame.QUIT:  
                fim_jogo = True  # sai do loop

            elif evento.type == pygame.MOUSEBUTTONDOWN:

                posicao=pygame.mouse.get_pos()  # obtem a posição do clique

                if caixa_aposta.collidepoint(posicao):#percebe acolisão de aposta
                    pass

                elif pygame.Rect(620, 330, 120, 60).collidepoint(posicao):# identifica o botão de rolagem
                    dados.calcular_lancamento()#rola os dados

                elif caixa_numero.collidepoint(posicao):#percebe a acolisão de número 
                    pass

            elif evento.type==pygame.KEYDOWN:#identifica quando o teclado é usado
                if evento.key == pygame.K_BACKSPACE:#verifica o uso do backspace

                    if caixa_aposta.collidepoint(pygame.mouse.get_pos()):#tira o caracter final de aposta
                        texto_aposta = texto_aposta[:-1]

                    elif caixa_numero.collidepoint(pygame.mouse.get_pos()):#tira oo caracter final de número
                        texto_numero = texto_numero[:-1]

                else:#assimila o texto a aposta do tipo string 
                    if caixa_numero.collidepoint(pygame.mouse.get_pos()):
                        texto_numero+=evento.unicode

                    elif caixa_aposta.collidepoint(pygame.mouse.get_pos()):
                        texto_aposta+=evento.unicode

        #cria o texto a ser renderizado
        superficie_texto_aposta=fonte.render(texto_aposta,True,cores['preto']) 
        superficie_texto_numero=fonte.render(texto_numero,True,cores['preto'])
        #renderiza os textos
        tela.blit(superficie_texto_aposta,caixa_aposta.bottomright)
        tela.blit(superficie_texto_numero,caixa_numero.bottomright)

        pygame.display.flip()  # atualiza a tela
    pygame.quit()  # finaliza o Pygame quando o jogo encerra
        
if __name__ == '__main__':
    main()

