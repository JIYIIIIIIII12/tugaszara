print("Selamat datang di Aplikasi perhitungan nilai Mahasiswa")
Tugas = float(input("Silahkan Masukan Nilai Tugas Anda: "))
UTS = float(input("Silahkan Masukan Nilai UTS Anda: "))
UAS = float(input("Silahkan Masukan Nilai UAS Anda: "))

a = Tugas * 0.25
b = UTS * 0.35
c = UAS * 0.4
Nilai_Akhir = a + b + c


print("Nilai Akhir Anda: ", NA)

if NA > 85:
  print("Dalam Huruf: A")
elif Nilai_Akhir > 80:
  print("Dalam Huruf: A-")
elif Nilai_Akhir > 75:
  print("Dalam Huruf: B+")
elif Nilai_Akhir > 70:
  print("Dalam Huruf: B")
elif Nilai_Akhir > 65:
  print("Dalam Huruf: B-")
elif Nilai_Akhir > 60:
  print("Dalam Huruf: C+")
elif Nilai_Akhir > 55:
  print("Dalam Huruf: C")
elif Nilai_Akhir > 50:
  print("Dalam Huruf: C-")
elif Nilai_Akhir > 30:
  print("Dalam Huruf: D")
elif Nilai_Akhir <= 30:
  print("Dalam Huruf: E")