import exifread
# Open image file for reading (binary mode)
def metadata(path):
    img = open(path, "rb")
    user_comment = exifread.process_file(img)["EXIF UserComment"]
    info = str(user_comment).split(",")
    long = info[0]
    lat = info[1]
    alt = info[2]
    hdg = info[3]
    pitch = info[4]
    roll = info[5]

    return long, lat, alt, hdg, pitch, roll

# a, b, c, d, e, f = metadata("C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/rp/5.jpeg")