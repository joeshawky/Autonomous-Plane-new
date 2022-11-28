from exif import Image
from PIL import Image
from PIL.ExifTags import TAGS

img_path = 'C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/rp/0.jpeg'#hangi foto alınacak onun yolu girildi


def exif_data(exif_data):
    for tag_id in exif_data:
        # tag = TAGS.get(tag_id, tag_id)
        content = exif_data.get(tag_id)
        # print(tag_id)
        # print(content)
    content = exif_data.get(37510)
    # print(content) 
    return content

with Image.open('C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/samples/rp/0.jpeg') as im:
    exif = im.getexif()
    
    #exif_data(exif)
    print()
    exif_data(exif.get_ifd(0x8769))
    


# with open(img_path, 'rb') as img_file:#yolu verilen dosya okundu 
#     img = Image(img_file)#bu dosya img nesnesine atandı 


# print(img.has_exif)                      #exift var mı yok mu bool
# img.gps_latitude = (40.0, 29.0, 57.48)   #enlem bilgisni giriyoruz 
# img.gps_altitude='70'                    #yükseklik
# img.gps_longitude = (60.0, 41.0, 39.84)  #boylam
# img.Orientation =5                       #fotoğraf rotasyonu 
# img.gps_img_direction= '50'              #açısı

# print(img.user_comment )                      #exift var mı yok mu bool

# with open(f'changed_{img_path}', 'wb') as new_image_file:
#         new_image_file.write(img.get_file())#dosyaya exiftleri ekle ve yeniden kaydet 
# print(sorted(img.list_all()))#değiştirilen bütün exift dosyaşarını göster