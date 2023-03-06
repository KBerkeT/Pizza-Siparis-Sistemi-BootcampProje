import csv
import datetime
from Pizzas import *
 
# Menuden saçilen pizzaya göre sınıf seçimi yapılması.
def select_pizza(n):
	"""
	Menuden seçilen Pizza nesnesini oluşturmak için bu fonksiyon kullanılır.
		n: Menude bulunan pizza numarası
	"""
	if n == 1:
		return Margherita()
	elif n == 2:
		return MixPizza()
	elif n == 3:
		return TurkPizza()
	elif n == 4:
		return MushroomPizza()
	elif n == 5:
		return SausagePizza()

# Menuden seçiler sosa göre sınıf seçimi yapılması.
def select_sauce(n, pizza):
	"""
	Menuden seçilen Sauce nesnesini oluşturmak için bu fonksiyon kullanılır.
		n: Menude bulunan sos numarası 
		pizza: Pizza nesnesi 
	"""
	if n == 1:
		return Ketchup(pizza)
	elif n == 2:
		return Mayonnaise(pizza)
	elif n == 3:
		return BBQ(pizza)
	elif n == 4:
		return Mustard(pizza)
	elif n == 5:
		return HotSauce(pizza)
	elif n == 6:
		return RanchSauce(pizza)
	elif n == 7:
		return Spice(pizza)


# csv dosyası oluşturmak ve içine verileri yazmak için oluşturulan fonksiyon.
def write_csv(information_list):
	"""
	Csv dosyasına veri yazdırmak için fonksiyon.
		information_list: Yazdırılacak satır liste şeklinde verilir.
	"""
	# Orders_Database.csv dosyasına veri eklemek için açılır,
	csv_file = open("Orders_Database.csv", "a")

	# Oluşturulan csv dosyasına verilerin yazılacağı dosyayı seçiyoruz ve
	# kuralları belirliyoruz. writerow() işlevi ile satır olarak yazdırılıyor.
	writer = csv.writer(csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)  
	writer.writerow(information_list)
	csv_file.close()


def main():
	# Menuyu dosyasını açıp menuyü değişkene atamak
	with open("Menu.txt", "r") as file:
		menu = file.read()

	# Dosyanın olup olmadığını kontrol ediyoruz. Dosya yoksa Kolon adlarını yazarak
	# oluşturuyoruz.
	try:
		file = open("Orders_Database.csv", "r")
		file.close()
	except:
		column_name = ["Isim", "TC Kimlik", "Kredi Karti No", "Pizza Tanimi", "Ucret", "Zaman", "Kredi Karti Sifresi"]
		write_csv(column_name)

	print(menu)

	while True:
		# Kullanıcıdan bir pizza numarası ve bir sos numarası isteniyor.
		# Try except bloğu ile bu girdinin bir sayı olması kontrol ediliyor.
		try:
			selectP = input("Lütfen pizza no seçiniz (Çıkmak için 'q' ya basınız.): ")
			selectS = input("Lütfen sos no seçiniz (Çıkmak için 'q' ya basınız.): ")
			if selectP == "q" or selectS == "q":
				break
			selectP = int(selectP)
			selectS = int(selectS)
		except:
			print("Hatalı giriş! Lütfen menüdeki sayılardan birini giriniz!")
			continue
		
		pizza = select_pizza(selectP)
		

		if selectS == 0:
			try:
				description = pizza.get_description()
				cost = pizza.get_cost()
			except:
				print("Hatalı giriş! Lütfen doğru pizza numarası seçiniz.")
				continue

		else:
			try:
				sos = select_sauce(selectS, pizza)
				description = sos.get_description()
				cost = sos.get_cost()
			except:
				print("Hatalı giriş! Lütfen doğru pizza ve sos numarası seçiniz.")
				continue
		
		print(f"Seçtiğiniz Pizza: {pizza.name}-{description}")
		print(f"Ücret: {cost}")
		
		# Kullanıcıdan bilgileri isteniyor.
		
		# Kullanıcıdan isim bilgisi isteniyor, bu bilginin doğruluğu kontrol ediliyor. Düzgün formata getiriliyor.
		while True:
			name = input("Adınız: ")
			name = name.split()
			x = 0 # Kontrol değişkeni
			for i in range(len(name)):
				name[i] = name[i].capitalize()
				if name[i].isalpha() == False:
					print("Hatalı giriş. Tekrar deneyiniz!")
					x = 1
			if x == 1:
				continue
			isim = " ".join(name)
			break

		# Tc kimlik bilgisi isteniyor. Bilginin doğru formatta olması kontrol ediliyor.
		while True:
			tc = input("TC kimlik: ")
			if tc.isdigit() == True and len(tc) == 11:
				break
			print("Hatalı giriş. Tekrar deneyiniz!")
		
		# Kullanıcıdan kredi kartı numarası isteniyor. Bilginin formatının doğruluğu kontrol ediliyor.
		while True:
			credit_card_no = input("Kredi kartı no: ")
			if credit_card_no.isdigit() == True and len(credit_card_no) == 16:
				break
			print("Hatalı giriş. Tekrar deneyiniz!")

		# Kullanıcıdan kredi kartı şifresi isteniyor. Bilginin formatının doğruluğu kontrol ediliyor.
		while True:
			credit_card_pass = input("Kredi kartı şifresi: ") 
			if credit_card_pass.isdigit() == True and len(credit_card_pass) == 4:
				break
			print("Hatalı giriş. Tekrar deneyiniz!")		
		
		an = datetime.datetime.now() # Zaman bilgisi alınıyor.
		t = datetime.datetime.strftime(an, "%c") # gün adı-ay-gün-saat-yıl formatına getiriliyor.
  
		information_list = [isim, tc, credit_card_no, description, cost, t, credit_card_pass]
		write_csv(information_list) # csv dosyasına bilgiler yazdırılıyor.
