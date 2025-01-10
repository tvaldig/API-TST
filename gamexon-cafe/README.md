# Panduan Personalized Payment API
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
    "id": 0,
    "item_name": "string",
    "description": "string",
    "price": 0,
    "category": "string",
    "available": true
    }
  ]
  ```

### POST `/api/v1/cafe/menu`
- **Description:** Create a new menu item.
- **Request Body:**
  ```json
  {
    "item_name": "string",
  "description": "string",
  "price": 0,
  "category": "string",
  "available": true
  }
  ```
- **Success Response (201):**
  ```json
  {
    "id": 0,
  "item_name": "string",
  "description": "string",
  "price": 0,
  "category": "string",
  "available": true
  }
  ```

### GET `/api/v1/cafe/menu/{menu_id}`
- **Description:** Retrieve a menu item by its ID.
- **Success Response (200):**
  ```json
  {
     "id": 0,
  "item_name": "string",
  "description": "string",
  "price": 0,
  "category": "string",
  "available": true
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
    "item_name": "string",
  "description": "string",
  "price": 0,
  "category": "string",
  "available": true
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
    "message": "Menu item deleted successfully"
  }
  ```
- **Error Response (404):**
  ```json
  {
    "detail": "Menu item not found"
  }
  ```

## Orders

### GET `/api/v1/cafe/orders`
- **Description:** Retrieve all orders.
- **Success Response (200):**
  ```json
  [
    {
      "total_amount": 0,
    "id": 0,
    "order_date": "2025-01-10T16:11:55.641Z"
    }
  ]
  ```

### POST `/api/v1/cafe/orders`
- **Description:** Create a new order.
- **Request Body:**
  ```json
  {
    "total_amount": 0
  }
  ```
- **Success Response (201):**
  ```json
  {
    "total_amount": 0,
  "id": 0,
  "order_date": "2025-01-10T16:12:08.488Z"
  }
  ```

### GET `/api/v1/cafe/orders/{id}`
- **Description:** Retrieve an order by its ID.
- **Success Response (200):**
  ```json
  {
     "total_amount": 0,
    "id": 0,
    "order_date": "2025-01-10T16:12:36.950Z"
  }
  ```
- **Error Response (404):**
  ```json
  {
    "detail": "Order not found"
  }
  ```

## Payments

### POST `/api/v1/cafe/transactions`
- **Description:** Create a transaction for an order.
- **Success Response (201):**
  ```json
  {
    
    "message": "Transaction completed successfully",
  }
  
  ```
- **Error Response (400):**
  ```json
  {
    "detail": "Invalid payment details"
  }
  ```

