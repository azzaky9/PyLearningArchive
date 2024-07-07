def is_eligible_for_discount(age, student_status, income):
    if age < 18:
        return True
    elif 18 <= age <= 25 and student_status:
        return True
    elif age > 25 and income < 30000:
        return True
    else:
        return False

def main():
    # Ambil input dari pengguna
    age = int(input("Masukkan usia Anda: "))
    student_status = input("Apakah Anda seorang mahasiswa? (yes/no): ").strip().lower() == "yes"
    income = int(input("Masukkan pendapatan tahunan Anda: "))

    # Tentukan apakah pengguna berhak mendapatkan diskon
    eligible_for_discount = is_eligible_for_discount(age, student_status, income)

    # Cetak pesan yang sesuai
    if eligible_for_discount:
        print("Anda berhak mendapatkan diskon.")
    else:
        print("Anda tidak berhak mendapatkan diskon.")

if __name__ == "__main__":
    main()
