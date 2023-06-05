# Flask Python API - Lưu trữ dữ liệu từ W3

Đây là một ứng dụng Flask Python API được sử dụng để lưu trữ dữ liệu từ W3 (World Wide Web). Ứng dụng cho phép lưu trữ các tài sản (asset) và người dùng (user) vào cơ sở dữ liệu PostgreSQL.

## Yêu cầu

- Docker
- Docker Compose

## Cài đặt

1. Clone repository:

   ```shell
   git clone <fujitech@fujitech.git.backlog.jp:/PRO_TYPE/web_PRO_TYPE-1.git>
   cd web_PRO_TYPE-1

2.Tạo file .env từ file .env.example và điều chỉnh các giá trị cần thiết:

Copy code
  ```shell
  cp .env.example .env
   ```
Các giá trị cần điều chỉnh bao gồm cấu hình PostgreSQL (POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB) và các cài đặt khác của ứng dụng.

3. Chạy ứng dụng:
- Khởi tại 1 network để kết nối các service lại với nhau
   ```
   docker network create prototype_network1
   ```
- Build và chạy ứng dụng:
   ```shell
   docker-compose up --build
   ```
Đợi cho đến khi ứng dụng được xây dựng và chạy thành công.

Để truy cập vào container sử dụng lệnh:

   ```shell
   docker ps
   docker exec -it <container_name> bash
   ```

Trong đó, <container-name> là tên container đang chạy ứng dụng Flask Python API.
5.Trong terminal của container, chạy lệnh sau để khởi tạo cơ sở dữ liệu:
- Để khởi tạo 1 file migrate mới ta chạy lệnh sau:
   ```shell
   python3 manage.py db init
   python3 manage.py db migrate
   python3 manage.py db upgrade
   ```
- Nếu như đã có sẵn file migrate thì ta chỉ cần chạy lệnh sau:
   ```shell
   python3 manage.py db upgrade
   ```

6.Khi ứng dụng và cơ sở dữ liệu đã được khởi tạo thành công, bạn có thể truy cập vào API qua URL http://localhost:5000 hoặc http://<địa chỉ IP của máy chủ>:5000.

## Tài liệu API

Các endpoint của API được mô tả trong tài liệu sau:
Trên Postman:

https://lively-star-798995.postman.co/workspace/tutorial~d9506442-5fa6-417e-8000-d571842b6e87/collection/18309823-f0536c3f-1fa1-462e-b227-2a29b012f4f1?action=share&creator=18309823
...

## Cấu trúc thư mục

````
├── app
│   ├── __init__.py
│   ├── main
│   │   ├── __init__.py
│   │   ├── controller
│   │   ├── models
│   │   ├── service
│   │   └── util
    test
│   │   ├── __init__.py
│   __init__.py
migration
.env
.env.example
config.py
docker-compose.yml
Dockerfile
manage.py
README.md
requirements.txt
````   # Flask-Scrapy
