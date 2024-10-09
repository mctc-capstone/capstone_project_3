import geocoder

def main():
    location = input('Please enter location you would like data on (city, state): ')
    get_coordinates = getCoordinates(location)


def getCoordinates(location):
    get_data = geocoder.arcgis(location)
    coordinates = get_data.latlng
    return coordinates
















if __name__ == '__main__':
    main()