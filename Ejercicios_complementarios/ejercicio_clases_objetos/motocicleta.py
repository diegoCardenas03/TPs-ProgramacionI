class Motocicleta:
    # Atributo de clase
    condition = "Nueva"
    engine = False 

    # Atributos
    def __init__(self, color, license_plate, fuel_liters, wheels, brand, model, manufacture_date, top_speed, weight):
        self.color = color
        self.license_plate = license_plate
        self.fuel_liters = fuel_liters
        self.wheels = wheels
        self.brand = brand
        self.model = model
        self.manufacture_date = manufacture_date
        self.top_speed = top_speed
        self.weight = weight
