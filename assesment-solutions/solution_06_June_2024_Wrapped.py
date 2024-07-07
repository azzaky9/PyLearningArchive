age = int(input("Masukkan usia Anda: "))
student_status = input("Apakah Anda seorang mahasiswa? (yes/no): ").strip().lower() == "yes"
income = int(input("Masukkan pendapatan tahunan Anda: "))

# Tentukan apakah pengguna berhak mendapatkan diskon
if age < 18:
    eligible_for_discount = True
elif 18 <= age <= 25 and student_status:
    eligible_for_discount = True
elif age > 25 and income < 30000:
    eligible_for_discount = True
else:
    eligible_for_discount = False

# Cetak pesan yang sesuai
if eligible_for_discount:
    print("Anda berhak mendapatkan diskon.")
else:
    print("Anda tidak berhak mendapatkan diskon.")
