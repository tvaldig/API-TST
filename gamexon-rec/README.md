# Panduan Personalized Cafe Payment API
## Run Local menggunakan Docker

### Pastikan sudah berada di dalam folder `gamexon-cafe`
```bash
cd gamexon-cafe
```

### Build docker image dengan perintah berikut:
```bash
docker build . -t ghcr.io/tvaldig/gamexon-cafe
```

### Jalankan backend dengan perintah berikut:
```bash
docker-compose up
```

---

# Tabel Endpoints

| **Method** | **Endpoint**                                   | **Description**                          | **Security** |
|------------|-----------------------------------------------|------------------------------------------|--------------|
| GET        | `/api/v1/cafe/`                               | Menampilkan root endpoint                | None         |
| GET        | `/api/v1/cafe/menu`                           | Menampilkan semua item menu              | None         |
| POST       | `/api/v1/cafe/menu`                           | Membuat item menu baru                   | Bearer Token |
| GET        | `/api/v1/cafe/menu/{menu_id}`                 | Menampilkan item menu berdasarkan ID     | None         |
| PUT        | `/api/v1/cafe/menu/{menu_id}`                 | Memperbarui item menu berdasarkan ID     | Bearer Token |
| DELETE     | `/api/v1/cafe/menu/{menu_id}`                 | Menghapus item menu berdasarkan ID       | Bearer Token |
| POST       | `/api/v1/cafe/order-details/bulk`             | Membuat order detail secara bulk         | Bearer Token |
| GET        | `/api/v1/cafe/order-details`                  | Menampilkan semua order detail           | Bearer Token |
| GET        | `/api/v1/cafe/order-details/order/{order_id}` | Menampilkan order detail berdasarkan ID  | Bearer Token |
| GET        | `/api/v1/cafe/orders`                         | Menampilkan semua pesanan                | Bearer Token |
| POST       | `/api/v1/cafe/orders`                         | Membuat pesanan baru                     | Bearer Token |
| GET        | `/api/v1/cafe/orders/{id}`                    | Menampilkan pesanan berdasarkan ID       | Bearer Token |
| POST       | `/api/v1/cafe/recommendation`                 | Membuat rekomendasi menu                 | Bearer Token |
| POST       | `/api/v1/cafe/transactions`                   | Membuat transaksi                        | Bearer Token |

---

# Penggunaan Endpoints

## Menu

### GET `/api/v1/cafe/menu`
- **Description:** Retrieve all menu items.
- **Success Response (200):**
  ```json
  [
    {
      "id": "integer",
      "name": "string",
      "price": "float",
      "category": "string"
    }
  ]
  ```

### POST `/api/v1/cafe/menu`
- **Description:** Create a new menu item.
- **Request Body:**
  ```json
  {
    "name": "string",
    "price": "float",
    "category": "string"
  }
  ```
- **Success Response (201):**
  ```json
  {
    "status": "success",
    "message": "Menu item created successfully",
    "data": {
      "id": "integer",
      "name": "string",
      "price": "float",
      "category": "string"
    }
  }
  ```

### GET `/api/v1/cafe/menu/{menu_id}`
- **Description:** Retrieve a menu item by its ID.
- **Success Response (200):**
  ```json
  {
    "id": "integer",
    "name": "string",
    "price": "float",
    "category": "string"
  }
  ```
- **Error Response (404):**
  ```json
  {
    "detail": "Menu item not found"
  }
  ```

### PUT `/api/v1/cafe/menu/{menu_id}`
- **Description:** Update a menu item by its ID.
- **Request Body:**
  ```json
  {
    "name": "string",
    "price": "float",
    "category": "string"
  }
  ```
- **Success Response (200):**
  ```json
  {
    "status": "success",
    "message": "Menu item updated successfully"
  }
  ```

### DELETE `/api/v1/cafe/menu/{menu_id}`
- **Description:** Delete a menu item by its ID.
- **Success Response (200):**
  ```json
  {
    "status": "success",
    "message": "Menu item deleted successfully"
  }
  ```
- **Error Response (404):**
  ```json
  {
    "detail": "Menu item not found"
  }
  ```

