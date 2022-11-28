import os

def pic_count(file):
    return len(os.listdir(file))

def img_array(file):
    return os.listdir(file)

def div_param(files):
    first, second = "0", "0"
    file = open(files, "r")
    read = file.read()
    div = read.split()
    if(read != ""):
        first = div[0]
        second = div[1]
    file.close()
    return first, second

def div_loc(lat, lon):
    lat_len = len(str(int(lat)))
    lon_len = len(str(int(lon)))

    lat_rounded = round(lat, (12-lat_len))
    lon_rounded = round(lon, (12-lon_len))

    lat1 = int(str(lat_rounded).replace(".", "")[0:5])
    lat2 = int(str(lat_rounded).replace(".", "")[5:9])
    lon1 = int(str(lon_rounded).replace(".", "")[0:5])
    lon2 = int(str(lon_rounded).replace(".", "")[5:9])
    return lat1, lat2, lon1, lon2