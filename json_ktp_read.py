import json

file_json = open("ktp.json")
data = json.loads(file_json.read())

# cetak isi data JSON
print ("\n" * 10)
print("")
print(f"NIK: {data['nik']}")
print(f"NAMA: {data['nama']}")
print("-------:")
print(f"TEMPAT LAHIR: {data['tempat_lahir']}")
print(f"TANGGAL LAHIR: {data['tanggal_lahir']}")
print(f"JENIS KELAMIN: {data['jenis_kelamin']}")
print(f"GOLONGAN DARAH: {data['golongan_darah']}")
print(f"ALAMAT: {data['alamat']}")
print(f"RT: {data['rt']}")
print(f"RW: {data['rw']}")
print(f"KELURAHAN/DESA: {data['kelurahan_atau_desa']}")
print(f"KECAMATAN: {data['kecamatan']}")
print(f"AGAMA: {data['agama']}")
print(f"STATUS KAWIN: {data['status_perkawinan']}")
print(f"PEKERJAAN: {data['pekerjaan']}")
print(f"KEWARGANEGARAAN: {data['kewarganegaraan']}")
print("")


