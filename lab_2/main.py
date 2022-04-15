from approximation import Approximate as a
import os


folder = './data'
if not os.path.exists('pic'):
    os.makedirs('pic')
files = next(os.walk(folder))[2]
for file in files:
    aprox = a(file=f'{folder}/{file}')
    aprox.add_data()
    aprox.approximate(1)
    print(f'Якiсть апроксимації степенi {1} для файлу {file} = {aprox.sd()}')
    aprox.add_approx()
    aprox.approximate(2)
    print(f'Якiсть апроксимації степенi {2} для файлу {file} = {aprox.sd()}')
    aprox.add_approx('-r')
    aprox.approximate(3)
    print(f'Якiсть апроксимації степенi {3} для файлу {file} = {aprox.sd()}')
    aprox.add_approx('-b')
    aprox.save_plot(f'pic/pic_{file[:-4]}.png')

