# Fibonacci serisinde her sayı, kendisinden önce gelen iki sayının toplamıdır.
# Bu serinin dört milyondan küçük tüm ÇİFT sayılarının toplamını bulunuz.

ilkSayi = 1
ikinciSayi = 1
sayilarinToplami = 0
mSonuc = 0

while (ilkSayi < 4000000 and ikinciSayi < 4000000):
    sayilarinToplami = ilkSayi + ikinciSayi
    ilkSayi = ikinciSayi
    ikinciSayi = sayilarinToplami
    if(sayilarinToplami % 2 == 0):
        mSonuc += sayilarinToplami

print(mSonuc)
