import math
from dosya import *
import pathes


def geovdeneme(Uav_lat, Uav_lon, Uav_alt, Uav_heading, obj_frm_x, obj_frm_y, rotation, gmbl_pitch, gmbl_roll):
    global lon_basina_metre_degisimi
    global lat_basina_metre_degisimi
    global kisa_rotation
    global hayali_uav_lon1
    global hayali_uav_lat1
    global hayali_uav_lon2
    global hayali_uav_lat2
    global hayali_uav_lon3
    global hayali_uav_lat3
    global hayali_uav_lon4
    global hayali_uav_lat4
    global dikey_aow
    global Obje_lat
    global Obje_lon
    global frame_w
    global frame_h
    global yatay_aow
    obj_frm_x = int(obj_frm_x)
    obj_frm_y = int(obj_frm_y)
    # frame_w = 6000
    # frame_h = 4000
    frame_w = 1024
    frame_h = 768
    dikey_aow = 51
    yatay_aow = 35.3
    kisa_rotation = 0
    hayali_uav_lon1 = 0
    hayali_uav_lat1 = 0
    hayali_uav_lon2 = 0
    hayali_uav_lat2 = 0
    hayali_uav_lon3 = 0
    hayali_uav_lat3 = 0
    hayali_uav_lon4 = 0
    hayali_uav_lat4 = 0
    
    lon_basina_metre_degisimi = 84096.99461752053 #84096.99461752053.   87665.18980050631
    lat_basina_metre_degisimi = 111054.45946465318 #111054.45946465318.   110999.10213126616

    kisa_rotation = rotation

    if (rotation == 90):
            
        
        # frame_w = 4000
        # frame_h = 6000
        # yatay_aow = 51.98 #derece
        # dikey_aow = 72.35 #derece
        # kisa_rotation = rotation # foto merkezinin asil konumu için ayri rotation bilgisi gerekli bu yüzden böyle yaptim.
        rotation = rotation - 90   # rotation - 90 # bu olmazsa rotasyonu fazladan 90 derece döndürüyor. neden öyle oluyor hiçbir fikrim yok.
    
    elif (rotation == 270):
    
        # frame_w = 4000
        # frame_h = 6000
        # yatay_aow = 51.98 #derece
        # dikey_aow = 72.35 #derece
        # kisa_rotation = rotation # foto merkezinin asil konumu için ayri rotation bilgisi gerekli bu yüzden böyle yaptim.
        rotation = rotation + 90   # rotation - 90 # bu olmazsa rotasyonu fazladan 90 derece döndürüyor. neden öyle oluyor hiçbir fikrim yok.
    
    else:
    
        kisa_rotation = rotation
        rotation = 0
    
    #gimbalin pitch açisina göre yamuk fotonun asil orjinin longitude u bulunuyor. headinge göre lat lon paylasiliyor.
    gmbl_roll = gmbl_roll * -1
    if (gmbl_pitch > 0):
    
        pitch_metre = math.tan(math.radians(gmbl_pitch)) * Uav_alt
        ptch_lon = math.sin(math.radians(Uav_heading +  kisa_rotation)) * pitch_metre
        ptch_lat = math.cos(math.radians(Uav_heading +  kisa_rotation)) * pitch_metre
        #hayali_uav_lon1 = ptch_lon / lon_basina_metre_degisimi
        #hayali_uav_lat1 = ptch_lat / lat_basina_metre_degisimi
        hayali_uav_lon1 = ptch_lon / lon_basina_metre_degisimi
        hayali_uav_lat1 = ptch_lat / lat_basina_metre_degisimi
    
    else:
    
        #gmbl_pitch = gmbl_pitch * -1
        pitch_metre = math.tan(math.radians(gmbl_pitch)) * Uav_alt
        ptch_lon = math.sin(math.radians(Uav_heading +  kisa_rotation)) * pitch_metre
        ptch_lat = math.cos(math.radians(Uav_heading +  kisa_rotation)) * pitch_metre
        #hayali_uav_lon2 = ptch_lon / lon_basina_metre_degisimi
        #hayali_uav_lat2 = ptch_lat / lat_basina_metre_degisimi
        hayali_uav_lon2 = ptch_lon / lon_basina_metre_degisimi
        hayali_uav_lat2 = ptch_lat / lat_basina_metre_degisimi
    
    if (gmbl_roll > 0):
    
        roll_metre = math.tan(math.radians(gmbl_roll)) * Uav_alt
        roll_lon = math.sin(math.radians(Uav_heading + 90 +  kisa_rotation)) * roll_metre
        roll_lat = math.cos(math.radians(Uav_heading + 90 +  kisa_rotation)) * roll_metre
        #hayali_uav_lon3 = roll_lon / lon_basina_metre_degisimi
        #hayali_uav_lat3 = roll_lat / lat_basina_metre_degisimi
        hayali_uav_lon3 = roll_lon / lon_basina_metre_degisimi
        hayali_uav_lat3 = roll_lat / lat_basina_metre_degisimi
    
    else:
    
        #gmbl_roll = gmbl_roll * -1
        roll_metre = math.tan(math.radians(gmbl_roll)) * Uav_alt
        roll_lon = math.sin(math.radians(Uav_heading + 90 +  kisa_rotation)) * roll_metre
        roll_lat = math.cos(math.radians(Uav_heading + 90 +  kisa_rotation)) * roll_metre
        #hayali_uav_lon4 = roll_lon / lon_basina_metre_degisimi
        #hayali_uav_lat4 = roll_lat / lat_basina_metre_degisimi
        hayali_uav_lon4 = roll_lon / lon_basina_metre_degisimi
        hayali_uav_lat4 = roll_lat / lat_basina_metre_degisimi
    
    Uav_yeni_lat = Uav_lat +  hayali_uav_lat1 +  hayali_uav_lat2 +  hayali_uav_lat3 +  hayali_uav_lat4
    Uav_yeni_lon =  hayali_uav_lon1 +  hayali_uav_lon2 +  hayali_uav_lon3 +  hayali_uav_lon4 + Uav_lon
    dikey_mesafe = Uav_alt * math.tan(math.radians(dikey_aow / 2))
    dikey_sapma_pixel_başina_mesafe = dikey_mesafe / (frame_h / 2)
    Ym = dikey_sapma_pixel_başina_mesafe * obj_frm_y
    yatay_mesafe = Uav_alt * math.tan(math.radians(yatay_aow / 2))
    yatay_sapma_pixel_başina_mesafe = yatay_mesafe / (frame_w / 2)
    Xm = yatay_sapma_pixel_başina_mesafe * obj_frm_x

    # print("Yeni lon: {}".format(Uav_yeni_lon))
    # print("Yeni lat: {}".format(Uav_yeni_lat))


    #dist = math.Sqrt(Xm * Xm + Ym * Ym)
    #lon_fark_metre = dist * math.sin(Uav_heading + rotation)   
    #lat_fark_metre = dist * math.cos(Uav_heading + rotation)
    lon_fark_metre = Xm * math.sin(math.radians(Uav_heading + rotation + 90)) + Ym * math.sin(math.radians(Uav_heading + rotation))
    lat_fark_metre = Xm * math.cos(math.radians(Uav_heading + rotation + 90)) + Ym * math.cos(math.radians(Uav_heading + rotation))
    #dist = math.Sqrt(lon_fark_metre * lon_fark_metre + lat_fark_metre * lat_fark_metre)

    
    Obje_lat = Uav_yeni_lat + lat_fark_metre / lat_basina_metre_degisimi
    Obje_lon = Uav_yeni_lon + lon_fark_metre / lon_basina_metre_degisimi
    lat1, lat2, lon1, lon2 = div_loc(Obje_lat, Obje_lon)
    file = open(pathes.target_txt_path, "w")
    file.write(str(Obje_lon) + " " + str(Obje_lat))
    file.close()
    # return lat1, lat2, lon1, lon2
    return Obje_lat, Obje_lon
    
    # print("obje_lat : " + str(Obje_lat))
    # print("obje_lon : " + str(Obje_lon))
    #commentprint("lon_fark_metre : " + str(round(lon_fark_metre, 3)))
    #commentprint("lat_fark_metre : " + str(round(lat_fark_metre, 3)))
    # #commentprint("\n")
    

    # return (Obje_lon, Obje_lat)



#alttaki 3 satır sadece test için kullanılıyor.
# x_pixel, y_pixel = div_param("C:/Users/Joe/Desktop/T/Vsc/lagari/Target_identification_python/geo.txt")
# lon_obj, lat_obj = geovdeneme(41.1012643, 28.5519299, 100, 315, x_pixel, y_pixel, 0, 0, -10)
                                                          #heading, x, y, rotation, pitch, roll
# #commentprint("hedefin lon: " + str(lon_obj))
# #commentprint("hedefin lat: " + str(lat_obj))


# geovdeneme()
# print(geovdeneme(28.5463349, 41.1041451, 13.982, 140, 136, 282.72, 0, -3.1435917907340185, 1.1480464769477752))
# geovdeneme    (Uav_lat, Uav_lon, Uav_alt, Uav_heading, obj_frm_x, obj_frm_y, rotation, gmbl_pitch, gmbl_roll):
print(geovdeneme(41.1016767, 28.5512727, 50, 0, 200, 0, 0, 0, -10))
# geovdeneme(-35.3632168, 149.1641711, 5.495, 329.8, 411, 236, 0, -1.874866009714167, 34.176552229262136)
# lat = 41.1012643 - lon = 28.5519299

# 28.5462989   41.1041533