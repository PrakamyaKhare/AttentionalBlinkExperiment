"""
Program :- Attentional Blink Experiment
Author:- Prakamya Khare


"""


import pygame
import numpy as np
import sys
import random


pygame.init()
screen = pygame.display.set_mode((1820,820))
#font = pygame.font.SysFont("timesnewroman",30)
font = pygame.font.Font('freesansbold.ttf',32)
clock = pygame.time.Clock()
is_running = 1
key_to_char = {
    pygame.K_a: 'a',
    pygame.K_b: 'b',
    pygame.K_c: 'c',
    pygame.K_d: 'd',
    pygame.K_e: 'e',
    pygame.K_f: 'f',
    pygame.K_g: 'g',
    pygame.K_h: 'h',
    pygame.K_i: 'i',
    pygame.K_j: 'j',
    pygame.K_k: 'k',
    pygame.K_l: 'l',
    pygame.K_m: 'm',
    pygame.K_n: 'n',
    pygame.K_o: 'o',
    pygame.K_p: 'p',
    pygame.K_q: 'q',
    pygame.K_r: 'r',
    pygame.K_s: 's',
    pygame.K_t: 't',
    pygame.K_u: 'u',
    pygame.K_v: 'v',
    pygame.K_w: 'w',
    pygame.K_x: 'x',
    pygame.K_y: 'y',
    pygame.K_z: 'z',
    pygame.K_0: '0',
    pygame.K_1: '1',
    pygame.K_2: '2',
    pygame.K_3: '3',
    pygame.K_4: '4',
    pygame.K_5: '5',
    pygame.K_6: '6',
    pygame.K_7: '7',
    pygame.K_8: '8',
    pygame.K_9: '9'
}


def get_render_array(array) :
    global font
    fonts =  {}
    for element in array :
        key = font.render(element,0,(255,255,255),(0,0,0))
        fonts[key] = element
    return fonts

def get_render(text,c1=(255,255,255),c2=(0,0,0)) :
    global font
    return font.render(text,0,c1,c2)

def get_key(dist,value) :
    for k,v in zip(dist.keys(),dist.values()) :
        if v == value :
            return k

text1 = get_render("Welcome to the experiment :') press space to start the experiment")
text2 = get_render("What was the second number?")
path = "C:\\Attention Blink\\"


pygame.display.set_caption("Attentional Blink")
fonts = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
chars_dist = get_render_array(fonts)
chars = np.array(list(chars_dist.keys()))
numbers_dist = get_render_array('0123456789')
numbers = np.array(list(numbers_dist.keys()))
alphas_dist = get_render_array('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
alphas = np.array(list(alphas_dist.keys()))
flag1 = 1
Data = []
file = open(path+'data.csv','w')
file.write("True Key,Response Key\n")
file.close()
format_data = ""
d = 0
while is_running :
    file = open(path+'data.csv','a')
    screen.fill('black')
    if flag1 :
        rect = text1.get_rect()
        rect.center = (screen.get_width()//2,screen.get_height()//2)
        screen.blit(text1,rect)
        flag1 = 0
        pygame.display.update()
        while 1 :
            event = pygame.event.wait()
            if event.type == pygame.QUIT :
                is_running = 0
                continue
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    break
        pygame.time.wait(900)
        screen.fill('black')
    for event in pygame.event.get() :
        if event == pygame.QUIT :
            is_running = 0
            continue
    np.random.shuffle(chars)
    np.random.shuffle(numbers)
    np.random.shuffle(alphas)
    pos1,pos2 = np.random.randint(0,10,size=(2))
    n1 = numbers[pos1]
    n2 = numbers[pos2]
    Data.append([numbers_dist[numbers[pos2]],0])
    format_data += str(Data[d][0]) +','
    pos1,pos2 = np.random.randint(0,len(alphas)+2,size=(2))
    new_string = []
    insert_pos1 = insert_pos2 = False
    j = 0
    #d = 0
    for i in range(28) :
        if i == pos1 :
            insert_pos1 = True
            new_string.append(n1)
            continue
        if i == pos2 :
            insert_pos2 = True
            new_string.append(n2)
            continue
        if j >= 26 :
            if insert_pos1 == insert_pos2 == True :
                break
            if insert_pos1 :
                new_string.append(n2)
                break
            if insert_pos2 :
                new_string.append(n1)
                break
        new_string.append(alphas[j])
        j = j + 1
    for char in new_string :
        rect = char.get_rect()
        rect.center = (screen.get_width()//2,screen.get_height()//2)
        screen.blit(char,rect)
        pygame.time.wait(200)
        pygame.display.update()
    pygame.time.wait(500)
    screen.fill("black")
    rect = text2.get_rect()
    rect.center = (screen.get_width()//2,screen.get_height()//2)
    screen.blit(text2,rect)
    pygame.display.update()
    while 1 :
            event = pygame.event.wait()
            if event.type == pygame.QUIT :
                is_running = 0
                continue
            elif event.type == pygame.KEYDOWN :
                if event.key in key_to_char :
                   value = key_to_char[event.key]
                   print(numbers_dist[n2],'  ',numbers_dist[get_key(numbers_dist,value)])
                   if n2 == get_key(numbers_dist,value) :
                    print('true')
                   
                   Data[d][1] = int(numbers_dist[n2])
                   format_data += str(Data[d][1]) + '\n'
                   file.write(format_data)
                   format_data = ""
                   file.close()
                   d = d + 1
                   break
    pygame.display.flip()
    clock.tick(60)
    
pygame.display.quit()
pygame.quit()
exit()
