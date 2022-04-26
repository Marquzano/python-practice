def city_country(city, country):
    """Returns a formatted string of the city and its country"""
    cityFormatted = city.title() + ", " + country.title()
    return cityFormatted

cityAndCountry = city_country('chihuahua', 'mexico')
print(cityAndCountry)
cityAndCountry = city_country('barcelona', 'spain')
print(cityAndCountry)
cityAndCountry = city_country('tokyo', 'japan')
print(cityAndCountry)