from Student import Student
from Professionals import Professionals
from Admin import Admin

Andi = Student(1000, 'cumanTest', 'Andi', 'andi@mail.com', 800, 'Anxiety')
Budi = Professionals(2000, 'bukanKonsultan', 'Budi',
                     'budi@mail.com', 909, '012-BIN', 'Kamis')
Jono = Admin(301, 'bukanAdmin', 'Admin App 01', 'jono@mail.com')

# Contoh login
Andi.login('cumanTest')
print('Login status:', Andi.verifyLogin(), '\n')

# Konsultasi
Andi.buatForm(['Kurang percaya diri', 'Tidak produktif'])
Andi.mintaKonsultasi('Kamis', 'Konsultasi Biasa')
for key, value in Andi.giveConsultList().items():
    consultID = key
    print(key, "|", value.printDetail())
Budi.berikanKonsultasi(Andi, 1)
Jono.siapkanKonsultasi(Andi, 1)
