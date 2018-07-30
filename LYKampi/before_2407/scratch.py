

#vize=int(input("vize notunuzu girin: "))

#final=int(input("final notunuzu girin: "))


def ortalama_hesapla(tmpvize, tmpfinal):
	if type(tmpvize) == int and type(tmpfinal) == int:
		if 0 < tmpvize < 100 and 0 < tmpfinal < 100 :
			kul_not = tmpvize * 0.4 + tmpfinal * 0.6

			if 0 < kul_not <= 40:
				print("notunuz dc")
			elif 41 < kul_not <= 60:
				print("notunuz cb")
			elif 61 < kul_not <= 80:
				print("notunuz bb")
			elif 81 < kul_not <= 100:
				print("notunuz aa")
			else:
				print("tanımsız")
	else:
		print("lütfen sayı giriniz")


ogr_1_vize=int(input(" ilk ogrencinin vizesini girin:"))
ogr_1_final=int(input(" ilk ogrencinin finalini girin:"))
ortalama_hesapla(ogr_1_vize, ogr_1_final)