import pygame
import time
import random
import os

os.system('cls')
pygame.init()
def permainan():
    biru = pygame.Color("blue")
    merah = pygame.Color("red")
    kuning = pygame.Color("yellow")
    hitam = pygame.Color("black")

    mulai = [["WELLCOME TO", "HUNTER SNAKE GAME"],
         [3, 2, 1, "Go!"]]

    layar = {
        "lebar" : 600,
        "tinggi" : 400
        }

    game_over = False
    game_selesai = False

    x1 = layar["lebar"] / 2
    y1 = layar["tinggi"] / 2

    x1_perubahan = 0
    y1_perubahan = 0

    daftar_ular = []
    panjang_ular = 1
    skor = 0
    ukuran_ular = 10
    
    kecepatan_ular = 8
    tampilan = pygame.display.set_mode((layar["lebar"], layar["tinggi"]))
    pygame.display.set_caption('HUNTER SNAKE GAME')
    tulisan = pygame.font.SysFont(None, 30)

    makanan_x = round(random.randrange(0, layar["lebar"] - ukuran_ular) / 10.0) * 10.0
    makanan_y = round(random.randrange(0, layar["tinggi"] - ukuran_ular) / 10.0) * 10.0

    def ular(ukuran_ular, daftar_ular):
            for i in daftar_ular:
                pygame.draw.rect(tampilan, biru, [i[0], i[1], ukuran_ular,ukuran_ular])

    def simpan(skor):
                with open ("skor.txt", "a") as file:
                    file.write(str(skor) + "\n")

    def pesan1(psn, warna):
            isi_pesan = tulisan.render(psn, True, warna)
            x_teks = layar["lebar"] / 2.5
            y_teks = layar["tinggi"] / 3
            tampilan.blit(isi_pesan, [x_teks, y_teks])
    
    def pesan2(psn, warna):
            isi_pesan = tulisan.render(psn, True, warna)
            x_teks = layar["lebar"] / 3.5
            y_teks = layar["tinggi"] / 1.8
            tampilan.blit(isi_pesan, [x_teks, y_teks])
            
    def pesan3(warna):
            isi_pesan = tulisan.render(f"Skor Tertinggi : {skor_tertinggi}", True, warna)
            x_teks = layar["lebar"] / 2.9
            y_teks = layar["tinggi"] / 2.2
            tampilan.blit(isi_pesan, [x_teks, y_teks ])

    def pesan4(psn, warna):
            isi_pesan = tulisan.render(psn, True, warna)
            x_teks = layar["lebar"] / 2.3
            y_teks = layar["tinggi"] / 2.5
            tampilan.blit(isi_pesan, [x_teks, y_teks])
            
    def pesan5(psn, warna):
            isi_pesan = tulisan.render(psn, True, warna)
            x_teks = layar["lebar"] / 3
            y_teks = layar["tinggi"] / 2.5
            tampilan.blit(isi_pesan, [x_teks, y_teks])
            
    tampilan.fill(hitam)
    pesan1(f"{mulai[0][0]}", kuning)
    pesan5(f"{mulai[0][1]}", kuning)
    pygame.display.update()
    time.sleep(3)

    for i in range (4) :
        tampilan.fill(hitam)
        pesan4(f"{mulai[1][i]}", kuning)
        pygame.display.update()
        time.sleep(1)

    while not game_over:
        tampilan.fill(hitam)
        pygame.draw.rect(tampilan, kuning, [makanan_x, makanan_y, ukuran_ular, ukuran_ular])

        kepala_ular = []
        kepala_ular.append(x1)
        kepala_ular.append(y1)
        daftar_ular.append(kepala_ular)
        if len(daftar_ular) > panjang_ular:
            del daftar_ular[0]
            
        ular(ukuran_ular, daftar_ular)
    
        pygame.display.update()
        if x1 == makanan_x and y1 == makanan_y:
            makanan_x = round(random.randrange(0, layar["lebar"] - ukuran_ular) / 10.0) * 10.0
            makanan_y = round(random.randrange(0, layar["tinggi"] - ukuran_ular) / 10.0) * 10.0
            panjang_ular += 1
            skor += 10
        
        pygame.time.Clock().tick(kecepatan_ular)

        if x1 >= layar["lebar"] or x1 < 0 or y1 >= layar["tinggi"] or y1 < 0:
            game_selesai = True
            simpan(skor)

        for x in daftar_ular[:-1]:
            if x == kepala_ular:
                game_selesai = True
                simpan(skor)

        with open('skor.txt', 'r') as file:
                nilai = [int(line.strip()) for line in file]
        skor_tertinggi = max(nilai)

        while game_selesai == True:
            tampilan.fill(hitam)
            pesan1("GAME OVER!", merah)
            pesan2(" 0 (keluar) atau 1 (main lagi)", merah)
            pesan3(merah)
            pesan4(f"Skor : {skor}", merah)
    
            pygame.display.update()
          
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        game_over = True
                        game_selesai = False
                    if event.key == pygame.K_1:
                        permainan()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    x1_perubahan = -ukuran_ular
                    y1_perubahan = 0
                elif event.key == pygame.K_l:
                    x1_perubahan = ukuran_ular
                    y1_perubahan = 0
                elif event.key == pygame.K_i:
                    x1_perubahan = 0
                    y1_perubahan = -ukuran_ular
                elif event.key == pygame.K_k:
                    x1_perubahan = 0
                    y1_perubahan = ukuran_ular
        x1 += x1_perubahan
        y1 += y1_perubahan
    pygame.quit()
    
    quit()

permainan()