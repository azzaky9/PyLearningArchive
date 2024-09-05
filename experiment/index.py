
nama_mahasiswa = ["John", "Doe", "Stephen", "Rick"]

def find_mahasiswa(name, list_mahasiswa):
  
  i = 0
  while i < len(nama_mahasiswa):
    if name == list_mahasiswa[i]:
      return list_mahasiswa[i]

  return  ""

result = find_mahasiswa("Clara", nama_mahasiswa)

print(f"Found name: {result}")