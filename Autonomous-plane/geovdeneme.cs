using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FPV_Player
{
    class geovdeneme
    {
        #region sabitler
        double yatay_aow = 72.35; //derece
        double dikey_aow = 51.98; //derece

        double lon_basina_metre_degisimi = 84096.99461752053; //84096.99461752053.   87665.18980050631
        double lat_basina_metre_degisimi = 111054.45946465318; //111054.45946465318.   110999.10213126616

        int frame_w = 6000;
        int frame_h = 4000;
        #endregion

        public double Obje_lat;
        public double Obje_lon;
        class globalvariable
        {
            public static double hayali_uav_lon1;
            public static double hayali_uav_lon2;
            public static double hayali_uav_lon3;
            public static double hayali_uav_lon4;
            public static double hayali_uav_lat1;
            public static double hayali_uav_lat2;
            public static double hayali_uav_lat3;
            public static double hayali_uav_lat4;
            public static double kısa_rotation;
        }
        public geovdeneme(double Uav_lat, double Uav_lon, double Uav_alt, double Uav_heading, int obj_frm_x, int obj_frm_y, int rotation, double gmbl_pitch, double gmbl_roll)
        {

            if (rotation == 90 )//|| rotation == 270)
            {
                frame_w = 4000;
                frame_h = 6000;
                yatay_aow = 51.98; //derece
                dikey_aow = 72.35; //derece
                globalvariable.kısa_rotation = rotation; // foto merkezinin asıl konumu için ayrı rotation bilgisi gerekli bu yüzden böyle yaptım.
                rotation = rotation - 90;   // rotation - 90; // bu olmazsa rotasyonu fazladan 90 derece döndürüyor. neden öyle oluyor hiçbir fikrim yok.
            }
            else if (rotation == 270)
            {
                frame_w = 4000;
                frame_h = 6000;
                yatay_aow = 51.98; //derece
                dikey_aow = 72.35; //derece
                globalvariable.kısa_rotation = rotation; // foto merkezinin asıl konumu için ayrı rotation bilgisi gerekli bu yüzden böyle yaptım.
                rotation = rotation + 90;   // rotation - 90; // bu olmazsa rotasyonu fazladan 90 derece döndürüyor. neden öyle oluyor hiçbir fikrim yok.
            }
            else
            {
                globalvariable.kısa_rotation = rotation;
                rotation = 0;
            }
            //gimbalin pitch açısına göre yamuk fotonun asıl orjinin longitude u bulunuyor. headinge göre lat lon paylasılıyor.
            gmbl_roll = gmbl_roll * -1;
            if (gmbl_pitch > 0)
            {
                double pitch_metre = Math.Tan(D2R(gmbl_pitch)) * Uav_alt;
                double ptch_lon = Math.Sin(D2R(Uav_heading + globalvariable.kısa_rotation)) * pitch_metre;
                double ptch_lat = Math.Cos(D2R(Uav_heading + globalvariable.kısa_rotation)) * pitch_metre;
                //double hayali_uav_lon1 = ptch_lon / lon_basina_metre_degisimi;
                //double hayali_uav_lat1 = ptch_lat / lat_basina_metre_degisimi;
                globalvariable.hayali_uav_lon1 = ptch_lon / lon_basina_metre_degisimi;
                globalvariable.hayali_uav_lat1 = ptch_lat / lat_basina_metre_degisimi;
            }
            else
            {
                //gmbl_pitch = gmbl_pitch * -1;
                double pitch_metre = Math.Tan(D2R(gmbl_pitch)) * Uav_alt;
                double ptch_lon = Math.Sin(D2R(Uav_heading + globalvariable.kısa_rotation)) * pitch_metre;
                double ptch_lat = Math.Cos(D2R(Uav_heading + globalvariable.kısa_rotation)) * pitch_metre;
                //double hayali_uav_lon2 = ptch_lon / lon_basina_metre_degisimi;
                //double hayali_uav_lat2 = ptch_lat / lat_basina_metre_degisimi;
                globalvariable.hayali_uav_lon2 = ptch_lon / lon_basina_metre_degisimi;
                globalvariable.hayali_uav_lat2 = ptch_lat / lat_basina_metre_degisimi;
            }
            if (gmbl_roll > 0)
            {
                double roll_metre = Math.Tan(D2R(gmbl_roll)) * Uav_alt;
                double roll_lon = Math.Sin(D2R(Uav_heading + 90 + globalvariable.kısa_rotation)) * roll_metre;
                double roll_lat = Math.Cos(D2R(Uav_heading + 90 + globalvariable.kısa_rotation)) * roll_metre;
                //double hayali_uav_lon3 = roll_lon / lon_basina_metre_degisimi;
                //double hayali_uav_lat3 = roll_lat / lat_basina_metre_degisimi;
                globalvariable.hayali_uav_lon3 = roll_lon / lon_basina_metre_degisimi;
                globalvariable.hayali_uav_lat3 = roll_lat / lat_basina_metre_degisimi;
            }
            else
            {
                //gmbl_roll = gmbl_roll * -1;
                double roll_metre = Math.Tan(D2R(gmbl_roll)) * Uav_alt;
                double roll_lon = Math.Sin(D2R(Uav_heading + 90 + globalvariable.kısa_rotation)) * roll_metre;
                double roll_lat = Math.Cos(D2R(Uav_heading + 90 + globalvariable.kısa_rotation)) * roll_metre;
                //double hayali_uav_lon4 = roll_lon / lon_basina_metre_degisimi;
                //double hayali_uav_lat4 = roll_lat / lat_basina_metre_degisimi;
                globalvariable.hayali_uav_lon4 = roll_lon / lon_basina_metre_degisimi;
                globalvariable.hayali_uav_lat4 = roll_lat / lat_basina_metre_degisimi;
            }

            double Uav_yeni_lat = Uav_lat + globalvariable.hayali_uav_lat1 + globalvariable.hayali_uav_lat2 + globalvariable.hayali_uav_lat3 + globalvariable.hayali_uav_lat4;
            double Uav_yeni_lon = globalvariable.hayali_uav_lon1 + globalvariable.hayali_uav_lon2 + globalvariable.hayali_uav_lon3 + globalvariable.hayali_uav_lon4 + Uav_lon;

            double dikey_mesafe = Uav_alt * Math.Tan(D2R(dikey_aow / 2));
            double dikey_sapma_pixel_başına_mesafe = dikey_mesafe / (frame_h / 2);
            double Ym = dikey_sapma_pixel_başına_mesafe * obj_frm_y;

            double yatay_mesafe = Uav_alt * Math.Tan(D2R(yatay_aow / 2));
            double yatay_sapma_pixel_başına_mesafe = yatay_mesafe / (frame_w / 2);
            double Xm = yatay_sapma_pixel_başına_mesafe * obj_frm_x;


            //double dist = Math.Sqrt(Xm * Xm + Ym * Ym);
            //double lon_fark_metre = dist * Math.Sin(Uav_heading + rotation);
            //double lat_fark_metre = dist * Math.Cos(Uav_heading + rotation);

            double lon_fark_metre = Xm * Math.Sin(D2R(Uav_heading + rotation + 90)) + Ym * Math.Sin(D2R(Uav_heading + rotation));
            double lat_fark_metre = Xm * Math.Cos(D2R(Uav_heading + rotation + 90)) + Ym * Math.Cos(D2R(Uav_heading + rotation));

            //double dist = Math.Sqrt(lon_fark_metre * lon_fark_metre + lat_fark_metre * lat_fark_metre);
            Obje_lat = Uav_yeni_lat + lat_fark_metre / lat_basina_metre_degisimi;
            Obje_lon = Uav_yeni_lon + lon_fark_metre / lon_basina_metre_degisimi;
        }
        private double D2R(double angle)
        {
            return Math.PI * angle / 180.0;
        }
    }
}
