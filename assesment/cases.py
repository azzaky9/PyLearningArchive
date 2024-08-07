import random
# Case

# Buatlah sebuah function yang menerima 2 argument dengan nama "search_term"
# dan "items", function tersebut bertanggung jawab untuk mencari text sesuai dengan
# "search_term" yang di input, perhatikan bahwa setiap input terdiri dari huruf kecil,
# huruf besar dan huruf capital

# Results
# jika search_term cocok dengan salah satu item di dalam List tersebut return index item tersebut
# jika tidak ada yang cocok return index -1 untuk mengindikasi bahwa search_term tidak cocok
# dengan value apapun di dalam List pada argument items;

# data types
# @search_term = string;
# @items = string[];

# Selesaikan case di dalam function ini.
def search_item_inside_list(search_term, items):
    # kerjakan body function ini untuk menyelesaikan test case
    return 0

# !! Jangan Edit Test Case Di bawah ✌️
test_case = ["ball", "johnson", "appear", "gigs", "something", "kanji"]
case_items = ["ball", "Joe", "doe", "gigs", "Something", "rollup", "kanji"]

def get_search_term():
    return random.randrange(0, len(test_case))

def run_case():
    terms = get_search_term()
    index = search_item_inside_list(terms, case_items)

    print(f"Melakukan pencarian `{case_items[terms]}` pada List: {case_items}")

    if terms == "ball" or terms == "gigs" or terms == "kanji":
        if index >= 0:
            return print(f"Test case Berhasil ✅")
        else:
            return print(f"Gagal, Pencarian untuk items `ball` `gigs` `kanji` seharusnya tidak menghasilkan index -1. ❌")

    if index < 0:
       return print(f"Test case Berhasil ✅")
    else:
       return print(f"Test case gagal ❌")

run_case()


