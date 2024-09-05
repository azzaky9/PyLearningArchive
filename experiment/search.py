list_mahasiswa = ["John", "Josh", "Doe", "Stephen", "Rick"] 

def filter_mahasiswa(searchTerm, mahasiswas):
  result = []

  for mahasiswa in mahasiswas:
    if mahasiswa.lower().startswith(searchTerm.lower()):
      result.append(mahasiswa)

  return result 
  

cases = filter_mahasiswa("j", list_mahasiswa)

print(cases)