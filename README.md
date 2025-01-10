# API TST Deployment

API untuk bisnis GameXon, cloud cafe kitchen untuk internet cafe. API ini disertakan dengan API endpoints dan contohnya serta Swagger docs yang dapat diakses dibawah

## 🚀 Swagger Docs
- Swagger Documentation: [API TST Deployment Docs](https://api-tst-deployment.vercel.app/docs)

---

## 📖 Features
- **User Authentication:** Secure login and API key retrieval.
- **Menu API:** Public access to the café menu.
- **API Key Validation:** Access control for private routes.
- **Built-in Documentation:** Swagger and ReDoc available for testing and exploration.

---

## Autentikasi

API GameXon menggunakan **API Key Authentication** dan **OAuth2 Bearer Tokens**

### API Key Authentication
- Untuk mengakses secured endpoints dengan mengisi `API-Key` pada header.
- Contoh:
  ```
  API-Key: e54d4431-5dab-474e-b71a-0db1fcb9e659
  ```

### OAuth2 Bearer Tokens
- `/api/v1/auth/login` akan memberikan token.
- Masukan token pada header `Authorization`:
  ```
  Authorization: Bearer <token>
  ```

## Endpoint

### 1. Endpoint Publik
Endpoint publik dapat diakses tanpa autentikasi terdapat route, test, dan juga menu yang dapat diakses

#### GET `/api/v1/public/`
- **Deskripsi**: Mengembalikan pesan publik.
- **Respons**:
  ```json
  "PUBLIC ROUTE"
  ```

#### GET `/api/v1/public/menu`
- **Deskripsi**: Mendapatkan daftar menu yang terdapat pada sistem
- **Respons**:
  ```json
  {
    "menu": [
        {
            "id": 1,
            "name": "Indomie Goreng",
            "price": 12000
        },
        {
            "id": 2,
            "name": "Toppoki",
            "price": 25000
        },
        {
            "id": 3,
            "name": "Milkis",
            "price": 16000
        },
        {
            "id": 4,
            "name": "Magelangan Rendang",
            "price": 50000
        },
        {
            "id": 5,
            "name": "Eh Teh",
            "price": 5000
        }
    ]
}
### 2. Endpoint Autentikasi
Endpoint untuk login dan registrasi pengguna.

#### POST `/api/v1/auth/login`
- **Deskripsi**: Untuk Login pengguna dan token autentikasi
- **Body Permintaan**:
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```
- **Respons**:
  ```json
  {
    "message": "Login successful",
    "user": {
      "name": "string",
      "email": "string",
      "password": "string"
    }
  }
  ```


#### POST `/api/v1/auth/register`
- **Deskripsi**: Registrasi pengguna baru.
- **Body Permintaan**:
  ```json
  {
    "name": "string",
    "email": "string",
    "password": "string"
  }
  ```
- **Respons**:
  ```json
  {
    "message": "User registered successfully",
    "user": {
      "name": "string",
      "email": "string",
      "password": "string"
    }
  }
  ```

### 3. Endpoint Secure
Endpoint ini memerlukan autentikasi yang valid.

#### GET `/api/v1/secure/`
- **Deskripsi**: Mengembalikan detail pengguna yang sudah diautentikasi.
- **Headers**:
  ```
  API-Key: <api-key>
  ```
- **Respons**:
  ```json
  {
    "name": "string",
    "message": "string",
    "email": "string",
    "password": "string"
  }
  ```

#### GET `/api/v1/secure/userid`
- **Deskripsi**: Mengembalikan ID user yang sudah diautentikasi.
- **Headers**:
  ```
  API-Key: <api-key>
  ```
- **Respons**:
  ```json
  {
    "user_id": "string"
  }
  ```

  #### GET `/api/v1/secure/get-api-key`
- **Deskripsi**: Mengembalikan api key user saat ini
- **Headers**:
  ```
  API-Key: <api-key>
  ```
- **Respons**:
  ```json
  {
    "API KEY": <api-key>
  }
  ```


## Contoh Permintaan

### 1. Login
**Permintaan**:
```http
POST /api/v1/auth/login HTTP/1.1
Host: https://api-tst-deployment.vercel.app
Content-Type: application/json

{
  "email": "timotiusvivaldi@gmail.com",
  "password": "securepassword"
}
```
**Respons**:
```json
{
  "message": "Login successful",
  "user": {
    "name": "Valdi",
    "email": "timotiusvivaldi@gmail.com",
    "password": "$2a$13$..."
  }
}
```

### 2. Akses Endpoint Secure
**Permintaan**:
```http
GET /api/v1/secure/userid HTTP/1.1
Host: https://api-tst-deployment.vercel.app
API-Key: e54d4431-5dab-474e-b71a-0db1fcb9e659
```
**Respons**:
```json
{
  "user_id": "Valdi"
}
```
**Permintaan**:
```http
GET /api/v1/secure/get-api-key HTTP/1.1
Host: https://api-tst-deployment.vercel.app
API-Key: e54d4431-5dab-474e-b71a-0db1fcb9e659
```
**Respons**:
```json
{
  "API KEY": "e54d4431-5dab-474e-b71a-0db1fcb9e659"
}
```
