import exiftool

file = "C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/backup/i00.jpeg"
with exiftool.ExifToolHelper() as et:

    metadata = et.get_metadata(file)

print("{:20.20} {:20.20}".format(["SourceFile"],
                                     ["EXIF:DateTimeOriginal"]))