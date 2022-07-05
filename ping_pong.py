from pygame import*

class Karakter(sprite.Sprite):
    def __init__(self, krk_image, krk_x, krk_y, krk_hiz, genislik, yukseklik):
        super().__init__()
        self.image = transform.scale(image.load(krk_image),(genislik,yukseklik))
        self.hiz = krk_hiz

        self.rect = self.image.get_rect()
        self.rect.x = krk_x
        self.rect.y = krk_y

    def ciz(self):
        pencere.blit(self.image,(self.rect.x,self.rect.y))

class Oyuncu(Karakter):
    def update_r(self):
        basilan_tuslar = key.get_pressed()
        if basilan_tuslar[K_UP] and self.rect.y >5:
            self.rect.y -= self.hiz
        if basilan_tuslar[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.hiz
    
    def update_l(self):
        basilan_tuslar = key.get_pressed()
        if basilan_tuslar[K_w] and self.rect.y >5:
            self.rect.y -= self.hiz
        if basilan_tuslar[K_s] and self.rect.y < 420:
            self.rect.y += self.hiz


pencere = display.set_mode((600,500))
pencere.fill((200,255,255))


raket_sol = Oyuncu("racket.jpg",30,200,4,50,150)
raket_sag = Oyuncu("racket.jpg",520,200,4,50,150)

top = Karakter("tennis_ball.jpg",200,200,4,50,50)


game = True
FPS = 60
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    pencere.fill((200, 255, 255))
    raket_sag.ciz()
    raket_sol.ciz()
    top.ciz()

    display.update()
    clock.tick(FPS)
