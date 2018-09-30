
# Importar o módulo pygame
# se a execução deste import em Python3 ou Python2 der algum erro
# é porque o pygame não está bem instalado
import pygame, sys
from pygame.locals import *
from math import cos, sin, sqrt


# inicialização do módulo pygame
pygame.init()

# criação de uma janela
largura = 900
altura  = 800
tamanho = (largura, altura)
janela  = pygame.display.set_mode(tamanho)
pygame.display.set_caption('Car Race - Luís') #nome da janela
#Nesta janela o ponto (0,0) é o canto superior esquerdo
#e (532-1,410-1) = (531,410) o canto inferior direito.


# número de imagens por segundo
frame_rate = 30

# relógio para controlo do frame rate
clock = pygame.time.Clock()

#Inicializa o tempo
t = 0.0
v = 0.0
i = 1
k = 23
# ler uma imagem em formato bmp
pista = pygame.image.load('circuit.jpg')
carro = pygame.image.load('carro.png')

pygame.mixer.music.load('car.mp3')
pygame.mixer.music.play(-1)
effect = pygame.mixer.Sound('explosion.wav')
#########################
#Para escrever o tempo:
font_size = 25
font = pygame.font.Font(None, font_size) # fonte pré-definida
antialias = True # suavização
WHITE = (255, 255, 255)# cor (terno com os valores Red, Green, Blue entre 0 e 255)
#######################

#(A) Se descomentar aqui (e comentar B) vejo onde passou/ rasto da trajetória
# Pois neste caso só junta a pista uma vez,
#no outro caso está sempre a juntar/desenhar a pista
janela.blit(pista, (0, 0)) 



##################################
##Exemplo ajustado à pista

def parametrizacao (t):
    x  = 320
    y  = 110
    
    if t == 0:
        resultado = (x,y)

    x1 = x + 60 * t
    y1 = y + 60*((1.15-t)**2 -1.5)

    if 0 < t <= 2.4 :
        resultado = (x1,y1)

    x1 = x+60*2.4
    y1 = y + 60 * ((1.15-2.4)**2 -1.5)
    x2 = x1 + 70*cos(t-4)
    y2 = y1 + 20 + 40*sin(t-4)

    if 2.4 < t <= 5:
        resultado = (x2,y2)

    x2 = x1 + 70*cos(5-4)
    y2 = y1 + 20 + 40*sin(5-4)
    x3 = x2 + 30*cos(t-6.6)
    y3 = y2 + 55 + 30*sin(t-6.6)

    if 5 < t <=8.5:
        resultado = (x3,y3)

    x3 = x2 + 30*cos(8.5 - 6.6)
    y3 = y2 + 40 + 30*sin(8.5 - 6.6)
    x4 = x3 - 30 + 50*cos(t-9)
    y4 = y3 + 35 + 50*sin(t-9)
    
    if 8.5 < t <= 11:
        resultado = (x4,y4)
        
    x4 = x3 - 30 + 40*cos(11-9)
    y4 = y3 + 35 + 40*sin(11-9)
    x5 = x4 + 80 - 100*cos(-t-13.5)
    y5 = y4 + 30 - 30*sin(-t-13.5)

    if 11 < t <= 13.3:
        resultado = (x5,y5)

    x5 = x4 + 80 - 100*cos(-13.3-13.5)
    y5 = y4 + 30 - 30*sin(-13.3-13.5)
    x6 = x5 + 45*(t-13.3)
    y6 = y5 + 20*(t-13.3)

    if 13.3 < t <= 15:
        resultado = (x6,y6)    

    y6 = y5 + 20*(15.2-13.3)
    y7 = - 20*(t-15) + 415 

    if 15 < t <= 17:
        resultado = (x6,y7)  

    x7 = x5 + 45*(17-13.3)
    y7 = - 20*(17-15) + 415 
    x8 = x7 + 40*cos(t)
    y8 = y7 + 40 + 40*sin(t)

    if 17 < t <= 20:
        resultado = (x8,y8)

    x8 = x7 + 40*cos(20)
    y8 = y7 + 40 + 40*sin(20)
    x9 = x8 - 150*(t-20)
    y9 = y8 + 130*(t-20)

    if 20 < t <= 21:
        resultado = (x9,y9)

    x9  = x8 - 150*(21-20)
    y9  = y8 + 130*(21-20)
    x10 = x9 - 90 + 150*cos(2*t - 42.8)
    y10 = y9 + 70 + 70*sin(2*t - 42.8)

    if 21 < t <= 23.7:
        resultado = (x10,y10)

    x10 = x9 - 90 + 150*cos(2*23.7 - 42.8)
    y10 = y9 + 70 + 70*sin(2*23.7 - 42.8)
    x11 = x10 -140 - 20*(4*t - 100)
    y11 = y10 -120 - 20*(4*t- 100)

    if 23.7 < t <= 25:
        resultado = (x11,y11)

    x11 = x10 -140 - 20*(4*25 - 100)
    y11 = y10 -120 - 20*(4*25- 100)
    x12 = x11 - 50 +50*cos(4*t - 150)
    y12 = y11 - 20 +50*sin(4*t - 150)
    if 25 < t <= 26.4:
        resultado = (x12,y12)
        effect.play()
        
    x12 = x11 - 50 +50*cos(4*26.4 - 150)
    y12 = y11 - 20 +50*sin(4*26.4 - 150)
    x13 = x12 + (t - 10)
    
    y13 = y12 - 100*(2*t - 52.5)
    if 26.4 < t <= 27.5:
        resultado = (x13,y13)
        janela.blit(ex, (x13,y13-10))
        

    x13 = x12 + (27.5 - 10)
    y13 = y12 - 100*(2*27.5 - 52.5)
    x14 = x13 - 85 + 100*cos(t-2)
    y14 = y13 + 30 + 100*sin(t-2)
    if 27.5 < t :
        resultado = (x14,y14)
    return resultado
def angulos (t):
    if t == 0:
        angulo = 0
    if 0 < t <= 2.4:
        angulo = 0
    if 2.4 < t <= 5 :
        angulo = -45
    if  5< t <= 8.5:
        angulo = -90
    if 8.5 < t <= 11:
        angulo = -90
    if 11 < t <= 13.3:
        angulo = 0
    if 13.3 < t <= 15:
        angulo = -45
    if 15 < t <= 17:
        angulo = 45
    if 17 < t <= 21.1:
        angulo = 0
    if 21.1 < t <= 23.7:
        angulo = 90
    if 23.7 < t <= 25.5:
        angulo = 180
    if 25.5 < t <= 27.5:
        angulo = 90
    if 27.5 < t:
        angulo = 0
    return angulo

#################################
#Ciclo principal do jogo
while True:
    
    novo_carro = pygame.transform.rotate(carro, angulos(t))
    if 16 <t <= 23:
        novo_carro = pygame.image.load('carro2.png')
    if 26.3 <t <= 27.5:
        ex = pygame.image.load('(' + str(k) + ').gif')
        k +=1
    if t > 27.5:
            novo_carro = pygame.image.load('(' + str(i) + ').gif')
    if i == 22:
        i = 1
    if k == 28:
        k = 23

    tempo = font.render("t = " + str(t), antialias, WHITE)
    velocidade = font.render("v = " + str(v), antialias, WHITE)
    janela.blit(pista, (0, 0))  #(B) se descomentar aqui (e comentar (A)) vejo movimento
    janela.blit(novo_carro, parametrizacao(t))
    i+=1
    janela.blit(tempo, (8, 5))
    janela.blit(velocidade, (8, 25))
    pygame.display.update()
    clock.tick(frame_rate)
    v1 = parametrizacao(t)[0] + parametrizacao(t)[1]
    t1 = t
    t = t + 0.1
    #t = pygame.time.get_ticks()*0.001
    v2 = parametrizacao(t)[0] + parametrizacao(t)[1]
    v = abs((v2-v1)/(t-t1))
    

   
    for event in pygame.event.get():
        #Para sair...
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #Ao clicar em qualquer local, o tempo recomeça com t=0
        # evento mouse click botão esquerdo (código = 1)
        elif event.type== pygame.MOUSEBUTTONUP and event.button == 3:
            t = 0
                       

##        #Quando queremos saber as coordenadas de um ponto: 
##        # descomentar isto e comentar o "evento mouse click"...
##        #"clicar" nesse ponto... o python print as coordenadas.
##        # evento mouse click botão esquerdo (código = 1)
        elif event.type== pygame.MOUSEBUTTONUP and event.button == 1:
            (x, y) = event.pos
            localizacao = "posicao = (" + str(x) + "," + str(y) + ")"
            print(localizacao)


##FAQs:
##            (1)
##            Quando parametrização (ou velocidade) não está definida
##            para algum valor de t, dá o erro:
##                "local variable "result/resultado" referenced before assignment"
##            
            




