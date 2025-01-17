# GAMEXON API

GAMEXON merupakan bisnis rental game dan warnet dengan cafe yang berbasis teknologi. Project ini dibuat dengan arsitektur berbasis microservice dengan perancangan Domain Driven Design. Project ini dipenuhi untuk kebutuhan mata kuliah II3160 Teknologi Sistem Terintegrasi

## Quick Access

| Resource                                | Link                                                                                           |
|-----------------------------------------|------------------------------------------------------------------------------------------------|
| **Frontend Repository**                 | [Gamexon React.js](https://github.com/tvaldig/gamexon-fe)                                      |
| **Game Recommendation Deployment**      | [Game Recommendation API](https://gamexonrec-gvakbbc8eaekgweq.southeastasia-01.azurewebsites.net/) |
| **Personalized Cafe Payment Deployment**| [Integrated Microservice API](https://gamexoncafe-fxdhfkaudag3eka2.southeastasia-01.azurewebsites.net/) |
| **Game Recommendation Swagger Docs**    | [Game Recommendation API Docs](https://gamexonrec-gvakbbc8eaekgweq.southeastasia-01.azurewebsites.net/docs) |
| **Personalized Cafe Payment Swagger Docs**| [Integrated Recommendation API Docs](https://gamexonrec-gvakbbc8eaekgweq.southeastasia-01.azurewebsites.net/docs) |
| **Final Report**                        | [Final Report TST](https://drive.google.com/file/d/15CC2OXk5bVn7tAFTp_9UE2E6H6pg6Ldg/view?usp=drive_link) |
---

## Struktur Folder
- **`gamexon-rec`**: Microservice untuk rekomendasi game.
- **`gamexon-cafe`**: Microservice untuk pembayaran yang dipersonalisasi (Integrasi microservice dengan teman).

> **Warning:**
> Dibawah ini merupakan panduan untuk menjalankan  **`Game Recommendation API`**!
> untuk melihat panduan  **`Personalized Cafe Payment API`** silahkan akses folder gamexon-cafe.

---
 
# Panduan Game Recommendation API
## Run Local menggunakan Docker

### Pastikan sudah didalam folder gamexon-rec
```bash
cd gamexon-rec
```
### Build docker image dengan command dibawah ini :

```bash
docker build . -t ghcr.io/tvaldig/gamexon-rec
```

### Jalankan backend dengan command dibawah ini :

```bash
docker-compose up
```

---

# Tabel Endpoints

| **Method** | **Endpoint**                               | **Description**                  | **Security** |
|------------|-------------------------------------------|----------------------------------|--------------|
| GET        | `/api/v1/public/`                         | Menampilkan Public Root                        | None         |
| GET        | `/api/v1/public/games`                    | Menampilkan semua Games                   | Bearer Token        |
| GET        | `/api/v1/public/games/{game_id}`          | Menampilkan game melalui id                  | Bearer Token         |
| GET        | `/api/v1/public/games/price/{game_id}`    | Menampilkan harga game melalui id                 | Bearer Token        |
| PUT        | `/api/v1/public/games/price/{game_id}`    | Memodifikasi harga game melalui id              | Bearer Token       |
| GET        | `/api/v1/public/recommendations/{game_id}`| Mendapatkan rekomendasi game berdasarkan id        | Bearer Token        |
| POST       | `/api/v1/auth/login`                      | Login                           | None         |
| GET        | `/api/v1/auth/me`                         | Informasi akun pribadi                  | Bearer Token |
| POST       | `/api/v1/auth/register`                   | Register                        | None         |

# Penggunaan Endpoints
## Authentication

### POST `/api/v1/auth/register`
- **Description:** Register a new user.
- **Request Body:**
  ```json
  {
    "name": "string",
    "email": "string",
    "password": "string"
  }
  ```
- **Success Response (200):**
  ```json
  {
    "status": "success",
    "message": "User registered successfully"
  }
  ```
- **Error Response (400):**
  ```json
  {
    "status": "error",
    "message": "Invalid input"
  }
  ```

### POST `/api/v1/auth/login`
- **Description:** Log in a user.
- **Request Body:**
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```
- **Success Response (200):**
  ```json
  {
    "access_token": "string",
    "token_type": "Bearer"
  }
  ```
- **Error Response (401):**
  ```json
  {
    "detail": "Invalid credentials"
  }
  ```

### GET `/api/v1/auth/me`
- **Description:** Retrieve user details.
- **Headers:**
  ```json
  {
    "Authorization": "Bearer <token>"
  }
  ```
- **Success Response (200):**
  ```json
  {
    "id": "integer",
    "name": "string",
    "email": "string"
  }
  ```
- **Error Response (401):**
  ```json
  {
    "detail": "Not authenticated"
  }
  ```

---

## Games

### GET `/api/v1/public/games`
- **Description:** Retrieve all games.
- **Success Response (200):**
  ```json
  [
    {
      "id": 0,
    "title": "string",
    "genre": "string",
    "release_year": 0,
    "popularity": 0,
    "developer": "string",
    "publisher": "string",
    "price_per_day": 0,
    "rating": "string"
    }
  ]
  ```

### GET `/api/v1/public/games/{game_id}`
- **Description:** Retrieve a specific game by its ID.
- **Success Response (200):**
  ```json
  {
    "id": 0,
    "title": "string",
    "genre": "string",
    "release_year": 0,
    "popularity": 0,
    "developer": "string",
    "publisher": "string",
    "price_per_day": 0,
    "rating": "string"
  }
  ```
- **Error Response (404):**
  ```json
  {
    "detail": "Game not found"
  }
  ```

### PUT `/api/v1/public/games/price/{game_id}`
- **Description:** Update the price of a specific game.
- **Request Body:**
  ```json
  {
    "id": "integer"
  }
  ```
- **Success Response (200):**
  ```json
  {
    "price_per_day": 0
  }
  ```
- **Error Response (400):**
  ```json
  {
    "detail": "Invalid price"
  }
  ```

### GET `/api/v1/public/recommendations/{game_id}`
- **Description:** Get game recommendations based on a specific game.
- **Success Response (200):**
  ```json
  [
    {
      
    "title": "string",
    "similarity_score": 0
  
    }
  ]
  ```
- **Error Response (404):**
  ```json
  {
    "detail": "Game not found"
  }
  ```

