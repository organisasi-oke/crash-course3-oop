from geometry.bangun_ruang import BangunRuang
from geometry.persegi_panjang import PersegiPanjang
from geometry.segitiga import Segitiga

print("Menggunakan OOP")

p1 = PersegiPanjang(6,10)
print(p1.info())
print(f'Luas persegi panjang = {p1.hitung_luas()}')

s1 = Segitiga(6,10)
print(s1.info())
print(f'Luas segitiga = {s1.hitung_luas()}')

b1 = BangunRuang()
print(b1.info())
print(b1.hitung_luas())