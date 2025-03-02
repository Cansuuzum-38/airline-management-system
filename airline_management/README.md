# ✈️ Airline Management System

##  Proje Açıklaması

Bu proje, bir havayolu şirketinin uçaklarını, uçuşlarını ve rezervasyonlarını yönetmesini sağlayan bir **REST API** geliştirmektedir. **Django Rest Framework (DRF)** kullanılarak geliştirilmiştir.

## Kurulum

### 1) Depoyu Klonla ve Sanal Ortamı Başlat

```bash
git clone <repo_link>
cd airline_management
python -m venv venv
venv\Scripts\activate  # MAC için:source venv/bin/activate
```

### 2️) Gerekli Kütüphaneleri Yükle

```bash
pip install -r requirements.txt
```

### 3️) Veritabanını Ayarla

```bash
python manage.py makemigrations api
python manage.py migrate
```

### 4️)  Admin Kullanıcısı Oluştur

```bash
python manage.py createsuperuser
```

### 5️)  Sunucuyu Çalıştır

```bash
python manage.py runserver
```

---

## API Kullanımı

###  **Airplane Endpoints**

| Metot  | URL                    | Açıklama                             |
| ------ | ---------------------- | ------------------------------------ |
| GET    | `/api/airplanes/`      | Tüm uçakları listele                 |
| POST   | `/api/airplanes/`      | Yeni uçak ekle                       |
| GET    | `/api/airplanes/{id}/` | Belirli bir uçağın detaylarını getir |
| PATCH  | `/api/airplanes/{id}/` | Belirli bir uçağı güncelle           |
| DELETE | `/api/airplanes/{id}/` | Belirli bir uçağı sil                |

###  **Flight Endpoints**

| Metot  | URL                  | Açıklama                             |
| ------ | -------------------- | ------------------------------------ |
| GET    | `/api/flights/`      | Tüm uçuşları listele                 |
| POST   | `/api/flights/`      | Yeni uçuş ekle                       |
| GET    | `/api/flights/{id}/` | Belirli bir uçuşun detaylarını getir |
| PATCH  | `/api/flights/{id}/` | Belirli bir uçuşu güncelle           |
| DELETE | `/api/flights/{id}/` | Belirli bir uçuşu sil                |

###  **Reservation Endpoints**

| Metot  | URL                       | Açıklama                          |
| ------ | ------------------------- | --------------------------------- |
| GET    | `/api/reservations/`      | Tüm rezervasyonları listele       |
| POST   | `/api/reservations/`      | Yeni rezervasyon ekle             |
| GET    | `/api/reservations/{id}/` | Belirli bir rezervasyonu getir    |
| PATCH  | `/api/reservations/{id}/` | Belirli bir rezervasyonu güncelle |
| DELETE | `/api/reservations/{id}/` | Belirli bir rezervasyonu sil      |

---

## Özellikler

**Uçuş Çakışma Kontrolü:** Aynı uçak için uçuş saatleri çakışamaz.\
**Kapasite Kontrolü:** Uçuş dolu olduğunda rezervasyon yapılamaz.\
**Benzersiz Rezervasyon Kodu:** 8 karakterli rezervasyon kodu otomatik oluşturulur.\
**Postman Collection Dahil**

---

## Postman API Test Dosyası

📌 **Postman Collection dosyasını kullanarak API'yi test edebilirsin.**\
📌 Dosya: `Airline_Management.postman_collection.json`\


## ** Proje Linkleri**

- **Postman Collection:** [Download Here](Airline_Management.postman_collection.json)

