from car import Car

if __name__ == "__main__":
    print("Hola mundo")
    car = Car()
    car.license = "AMS234"
    car.driver = "Andrés Herrera"
    print(vars(car))

    car2 = Car()
    car2.license = "QWE567"
    car2.driver = "Martha Nielsen"
    print(vars(car2))