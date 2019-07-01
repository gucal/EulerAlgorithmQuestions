#3’ün veya 5’in katı olan 10’dan küçük tüm doğal sayıları listelersek, 3, 5, 6, ve 9’u elde ederiz.
# Bu katların toplamı 23’tür. 3’ün veya 5’in 1000’den küçük tüm katlarının toplamını bulunuz.

Sayac = 1
SayiToplami = 0

while Sayac < 1000:
    if (Sayac % 3 == 0 or Sayac % 5 == 0):
        SayiToplami += Sayac
    Sayac += 1

print(SayiToplami)
