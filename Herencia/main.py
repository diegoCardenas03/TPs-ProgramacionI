from Car import Car
from Van import Van
from Bike import Bike
from Motorcycle import Motorcycle


def catalog(vehicle_list, wheels=None):
    count = 0
    if wheels is not None:
        for vehicle in vehicle_list:
            if vehicle.wheels == wheels:
                print(vehicle)
                count += 1
            else:
                continue
        print(f'Fueron encontrados {count} vehículos con {wheels} ruedas')


car1 = Car('Rojo', 4, '250 km/h', '200cc')
van1 = Van('Azul', 4, '450 km/h', '250cc', '20KG')
bike1 = Bike('Morado', 2, 'Urbana')
motorcycle1 = Motorcycle('Amarillo', 2, 'Deportiva', '420 km/h', '150cc')
vehicles = [car1, van1, bike1, motorcycle1]

print('Prueba catálogo 0 ruedas: \n')
catalog(vehicles, 0)
print('\nPrueba catálogo 2 ruedas: \n')
catalog(vehicles, 2)
print('\nPrueba catálogo 4 ruedas: \n')
catalog(vehicles, 4)
