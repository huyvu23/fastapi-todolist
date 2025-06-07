## uvicorn

uvicorn là một ASGI server (Asynchronous Server Gateway Interface) dùng để chạy các ứng dụng web viết bằng Python, đặc biệt là các framework asynchronous như:

FastAPI

Starlette

Quart

## Comma Create a virtual environment

MAC
source venv/bin/activate
Windows:
venv\Scripts\activate

## deactivate

- Sử dụng để thoat ra khỏi môi trường ảo của project

## Tại sao phải có file **init**.py

Trong Python, file **init**.py biến một thư mục thành một package, cho phép bạn import module trong thư mục đó. Đây là một phần quan trọng trong việc tổ chức mã nguồn thành các module và package.

Khi bạn có một thư mục, nếu bạn không có **init**.py, Python sẽ không coi thư mục đó là một package hợp lệ (trước Python 3.3). Dù Python 3.3+ hỗ trợ implicit namespace packages, nhưng trong thực tế, bạn nên luôn có file **init**.py để tránh lỗi không rõ ràng.

📌 Tóm lại:
Xác định package => Giúp Python biết đó là một package
Quản lý import => Cho phép quản lý import trong package rõ ràng
Chạy code khi package được import => Có thể dùng để import sẵn module, khởi tạo cấu hình

## requirements.txt

- File này chứa danh sách tất cả các dependencies (phụ thuộc) cần thiết để chạy project
- Giúp cài đặt tất cả thư viện dễ dàng chạy lệnh : pip3 install -r requirements.txt
- Tạo requirements.txt như thế nào ? => pip3 freeze > requirements.txt (Lệnh này sẽ ghi toàn bộ dependency hiện tại trong virtualenv vào file requirements.txt.)

## Tác dụng của đặt kiểu dữ liệu cho params trong FastAPI:

🛡 Tự động kiểm tra kiểu dữ liệu: FastAPI sẽ validate tham số và trả lỗi nếu sai kiểu (HTTP 422).

🔄 Chuyển đổi dữ liệu tự động: Tự ép kiểu (ví dụ: "123" → 123 nếu khai báo là int).

🧾 Tự sinh tài liệu API: Swagger UI (/docs) hiển thị rõ kiểu dữ liệu, required/optional.

🤖 Tạo schema OpenAPI: Hỗ trợ sinh API schema để dùng với client, SDK.

💡 Gợi ý thông minh khi viết code: IDE sẽ hiểu được kiểu và hỗ trợ autocomplete, giảm bug.

📦 Kết hợp với Pydantic để kiểm tra sâu hơn: Dễ dàng validate dữ liệu phức tạp như object/json.

🧠 Giúp code rõ ràng, dễ đọc, dễ bảo trì: Dễ biết được API yêu cầu dữ liệu gì.

## Tác dụng chính của Pydantic trong FastAPI:

🛡 Validate dữ liệu đầu vào (body, query, form,...): Kiểm tra kiểu dữ liệu, giá trị hợp lệ tự động.

🔄 Tự động chuyển đổi kiểu dữ liệu: Ví dụ: "25" (string) → 25 (int) nếu cần.

📦 Định nghĩa schema đầu vào và đầu ra: Thông qua các class BaseModel.

🧾 Sinh tài liệu API tự động: Kết hợp OpenAPI để tạo Swagger UI chuẩn.

🧠 Giúp code rõ ràng, dễ bảo trì: Định nghĩa dữ liệu kiểu tường minh, dễ mở rộng.

🔁 Tái sử dụng cấu trúc dữ liệu: Viết 1 lần, dùng nhiều nơi (request, response, DB...).
