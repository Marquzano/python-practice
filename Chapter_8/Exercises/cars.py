def buildCar(manufacturer, model_name, **car_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model_name
    for key, value in car_info.items():
        car[key] = value
    return car

car = buildCar('subaru', 'outback', color='blue', tow_package=True)
print(car)