
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

