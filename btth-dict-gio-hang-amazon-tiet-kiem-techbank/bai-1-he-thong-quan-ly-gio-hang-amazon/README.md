# Bài 1 - Hệ thống quản lý giỏ hàng Amazon

## Đề bài

Trên các nền tảng thương mại điện tử như Amazon, "Giỏ hàng" (Cart) là một trong những tính năng cốt lõi. Dữ liệu giỏ hàng lưu dưới dạng danh sách các sản phẩm; mỗi sản phẩm là một dictionary con chứa các thông tin: ID sản phẩm, Tên sản phẩm, Số lượng, Đơn giá.

Trước khi thanh toán (Checkout), hệ thống cần thêm sản phẩm mới, cập nhật số lượng, xóa sản phẩm và tính tổng tiền. Tính toán sai sẽ gây thiệt hại doanh thu và uy tín, nên đội ngũ sinh viên được giao xây dựng module "Cart Management CLI". Dữ liệu mẫu ban đầu: cart_items = [{"id": "P001", "name": "Dien thoai iPhone 15", "number": 1, "price": 25000000}, {"id": "P002", "name": "Op lung Silicon", "number": 2, "price": 150000}].

### Yêu cầu nghiệp vụ

Menu chương trình:

```
====================================================================
                   SHOPEE CART MANAGEMENT SYSTEM                    
====================================================================
[1] Xem chi tiết giỏ hàng & Tính tổng tiền
[2] Thêm sản phẩm mới / Cộng dồn số lượng
[3] Cập nhật số lượng của một sản phẩm
[4] Xóa sản phẩm khỏi giỏ hàng
[5] Thoát chương trình
====================================================================
Mời bạn chọn chức năng (1-5): 
```

- **Chức năng 1 - Xem chi tiết giỏ hàng & Tổng tiền:** In danh sách sản phẩm dạng bảng trực quan; tính và hiển thị tổng số lượng tất cả sản phẩm và tổng tiền của toàn bộ giỏ hàng.
- **Chức năng 2 - Thêm sản phẩm mới / Tăng số lượng:** Nhập mã, tên, số lượng, đơn giá. Nếu mã đã tồn tại thì cộng dồn số lượng mới vào số lượng cũ (không tạo dòng mới); nếu chưa có thì thêm sản phẩm mới vào cuối danh sách.
- **Chức năng 3 - Cập nhật số lượng:** Nhập mã sản phẩm và số lượng mới; tìm theo mã, nếu thấy thì cập nhật lại số lượng bằng số lượng mới.
- **Chức năng 4 - Xóa sản phẩm:** Nhập mã sản phẩm muốn xóa; tìm và xóa hoàn toàn sản phẩm đó.
- **Chức năng 5 - Thoát chương trình:** Dừng chương trình.

### Edge cases (bẫy dữ liệu)

| Bẫy | Mô tả |
|---|---|
| Bẫy 1 | Nhập số lượng <= 0 hoặc đơn giá < 0 khi thêm / sửa → báo lỗi và không thực hiện thao tác |
| Bẫy 2 | Cập nhật / xóa mã không có trong giỏ → "Mã sản phẩm không tồn tại trong giỏ hàng." |
| Bẫy 3 | Lựa chọn menu không phải số 1-5 hoặc nhập chữ → báo lỗi, hiện lại menu |

## (1) Phân tích và thiết kế giải pháp

### Phân tích Input / Output

| Dữ liệu | Biến | Kiểu | Xử lý |
|---|---|---|---|
| Giỏ hàng | `cart_items` | `list[dict]` | Mỗi phần tử có các key id, name, number, price |
| Lựa chọn menu | `choice` | `str` | So sánh "1"…"5" |
| Mã sản phẩm | `product_id` | `str` | strip().upper() |
| Số lượng | `quantity_text → quantity` | `str → int` | isdigit() và > 0 |
| Đơn giá | `price_text` | `str → int` | isdigit() (chặn số âm và chữ) |
| Sản phẩm tìm thấy | `found_item` | `dict / None` | None nếu không có trong giỏ |
| Tổng số lượng / tổng tiền | `total_quantity, total_amount` | `int` | Cộng dồn khi duyệt giỏ |

### Đề xuất giải pháp

- Giỏ hàng là list các dictionary. Duyệt bằng enumerate(cart_items, start=1) và lấy giá trị theo key: item["number"], item["price"]... Dùng key thay cho chỉ số giúp code dễ đọc hơn so với list lồng nhau.
- Thành tiền = item["number"] × item["price"]; tổng số lượng và tổng tiền là biến tích lũy khởi tạo 0 trước vòng lặp. Định dạng tiền bằng f-string {:,} và thêm hậu tố đ.
- Chức năng 2, 3, 4 dùng chung bước tìm sản phẩm theo mã: duyệt list, so item["id"] với mã đã chuẩn hóa, lưu dictionary tìm được vào found_item và break.
- Vì found_item trỏ tới chính dictionary nằm trong list, nên found_item["number"] += quantity sửa thẳng vào giỏ hàng. Khi mã đã tồn tại, chương trình chỉ hỏi số lượng muốn thêm, không hỏi lại tên và đơn giá.
- Thêm mới: tạo dictionary new_item với đủ 4 key rồi append() vào cuối list. Xóa: cart_items.remove(found_item).
- Bẫy 1: kiểm tra isdigit() trước khi int() nên số âm, số 0, chữ hay ô trống đều bị chặn mà không crash. Bẫy 2: found_item is None thì báo mã không tồn tại. Bẫy 3: nhánh else cuối của menu.

### Thiết kế thuật toán (Pseudocode)

```
cart_items ← dữ liệu mẫu (list các dict)
LẶP MÃI:
    IN menu; NHẬP choice
    NẾU choice == "1":
        giỏ rỗng → "Giỏ hàng đang trống."
        tổng_SL ← 0; tổng_tiền ← 0
        VỚI MỖI (stt, item): thành_tiền ← item["number"] × item["price"]; cộng dồn; IN 1 dòng bảng
        IN tổng số lượng và TỔNG TIỀN THANH TOÁN
    NẾU choice ∈ {"2","3","4"}:
        NHẬP product_id → strip().upper(); found_item ← dict có "id" trùng (None nếu không có)
        NẾU "2":
            chưa có → NHẬP tên
            NHẬP số lượng; không phải số nguyên > 0 → báo lỗi, bỏ qua
            đã có → found_item["number"] += số lượng
            chưa có → NHẬP đơn giá (số nguyên ≥ 0) → append({id, name, number, price})
        NẾU "3" hoặc "4" mà found_item là None → "Mã sản phẩm không tồn tại trong giỏ hàng."
        NẾU "3": NHẬP số lượng mới (> 0) → found_item["number"] ← số lượng mới
        NẾU "4": cart_items.remove(found_item)
    NẾU choice == "5": IN lời chào; THOÁT
    NGƯỢC LẠI: "Lựa chọn không hợp lệ"
```

## (2) Triển khai code

File: [`amazon_cart.py`](amazon_cart.py)

```python
"""Hệ thống quản lý giỏ hàng Amazon (Cart Management CLI)."""

# =====================================================================
# KHỞI TẠO: giỏ hàng là list, mỗi sản phẩm là một dictionary
#   {"id": mã, "name": tên, "number": số lượng, "price": đơn giá}
# =====================================================================
cart_items = [
    {
        "id": "P001",
        "name": "Dien thoai iPhone 15",
        "number": 1,
        "price": 25000000
    },
    {
        "id": "P002",
        "name": "Op lung Silicon",
        "number": 2,
        "price": 150000
    }
]
line_width = 68

while True:
    print("\n" + "=" * line_width)
    print(f"{'SHOPEE CART MANAGEMENT SYSTEM':^{line_width}}")
    print("=" * line_width)
    print("[1] Xem chi tiết giỏ hàng & Tính tổng tiền")
    print("[2] Thêm sản phẩm mới / Cộng dồn số lượng")
    print("[3] Cập nhật số lượng của một sản phẩm")
    print("[4] Xóa sản phẩm khỏi giỏ hàng")
    print("[5] Thoát chương trình")
    print("=" * line_width)
    choice = input("Mời bạn chọn chức năng (1-5): ").strip()

    # =================================================================
    # Chức năng 1: Xem chi tiết giỏ hàng và tổng tiền
    # =================================================================
    if choice == "1":
        if len(cart_items) == 0:
            print("\nGiỏ hàng đang trống.")
            continue

        print("\n── CHI TIẾT GIỎ HÀNG ──")
        print(f"{'STT':<4}| {'Mã SP':<6}| {'Tên Sản Phẩm':<22}| {'SL':<4}| {'Đơn Giá':<13}| Thành Tiền")
        print("-" * line_width)
        total_quantity = 0
        total_amount = 0
        for stt, item in enumerate(cart_items, start=1):
            # Lấy giá trị theo key của dictionary
            line_total = item["number"] * item["price"]
            price_display = f"{item['price']:,}đ"
            total_quantity += item["number"]
            total_amount += line_total
            print(f"{stt:<4}| {item['id']:<6}| {item['name']:<22}| {item['number']:<4}| "
                  f"{price_display:<13}| {line_total:,}đ")
        print("-" * line_width)
        print(f"⇒ Tổng số lượng sản phẩm trong giỏ: {total_quantity}")
        print(f"⇒ TỔNG TIỀN THANH TOÁN: {total_amount:,}đ")

    # =================================================================
    # Chức năng 2, 3, 4: đều bắt đầu bằng việc nhập mã sản phẩm
    # =================================================================
    elif choice == "2" or choice == "3" or choice == "4":
        product_id = input("Nhập mã sản phẩm: ").strip().upper()
        if product_id == "":
            print("Mã sản phẩm không được để trống.")
            continue

        # Tìm dictionary sản phẩm có "id" trùng mã (None nếu không có)
        found_item = None
        for item in cart_items:
            if item["id"] == product_id:
                found_item = item
                break

        # ---------- Chức năng 2: Thêm mới / Cộng dồn ----------
        if choice == "2":
            if found_item is None:
                product_name = input("Nhập tên sản phẩm: ").strip()
                if product_name == "":
                    print("Tên sản phẩm không được để trống.")
                    continue

            quantity_text = input("Nhập số lượng: ").strip()
            # Bẫy 1: số lượng phải là số nguyên > 0 (isdigit chặn cả số âm và chữ)
            if not quantity_text.isdigit() or int(quantity_text) <= 0:
                print("Số lượng không hợp lệ (phải là số nguyên lớn hơn 0). Không thực hiện thao tác.")
                continue
            quantity = int(quantity_text)

            if found_item is not None:
                # Mã đã tồn tại -> cộng dồn vào key "number", không tạo dòng mới
                found_item["number"] += quantity
                print(f"Sản phẩm {product_id} đã có trong giỏ. "
                      f"Đã cộng dồn, số lượng mới: {found_item['number']}")
            else:
                price_text = input("Nhập đơn giá: ").strip()
                # Bẫy 1: đơn giá phải là số nguyên >= 0
                if not price_text.isdigit():
                    print("Đơn giá không hợp lệ (phải là số nguyên không âm). Không thực hiện thao tác.")
                    continue
                new_item = {
                    "id": product_id,
                    "name": product_name,
                    "number": quantity,
                    "price": int(price_text)
                }
                cart_items.append(new_item)
                print(f"Đã thêm sản phẩm {product_id} - {product_name} vào cuối giỏ hàng.")

        # ---------- Chức năng 3, 4: sản phẩm phải tồn tại ----------
        elif found_item is None:
            print("Mã sản phẩm không tồn tại trong giỏ hàng.")          # Bẫy 2

        elif choice == "3":
            quantity_text = input("Nhập số lượng mới: ").strip()
            if not quantity_text.isdigit() or int(quantity_text) <= 0:   # Bẫy 1
                print("Số lượng không hợp lệ (phải là số nguyên lớn hơn 0). Không thực hiện thao tác.")
                continue
            found_item["number"] = int(quantity_text)
            print(f"Đã cập nhật số lượng {product_id} thành {found_item['number']}.")

        else:
            cart_items.remove(found_item)
            print(f"Đã xóa sản phẩm {found_item['id']} - {found_item['name']} khỏi giỏ hàng.")

    # =================================================================
    # Chức năng 5: Thoát
    # =================================================================
    elif choice == "5":
        print("Thoát chương trình. Cảm ơn bạn đã mua sắm!")
        break

    # Bẫy 3: lựa chọn không phải số 1-5 hoặc nhập chữ
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1 đến 5!")
```

## Kết quả

Chạy thử toàn bộ chức năng và bẫy dữ liệu *(ẩn menu lặp lại cho gọn)*:

```
Mời bạn chọn chức năng (1-5): 1

── CHI TIẾT GIỎ HÀNG ──
STT | Mã SP | Tên Sản Phẩm          | SL  | Đơn Giá      | Thành Tiền
--------------------------------------------------------------------
1   | P001  | Dien thoai iPhone 15  | 1   | 25,000,000đ  | 25,000,000đ
2   | P002  | Op lung Silicon       | 2   | 150,000đ     | 300,000đ
--------------------------------------------------------------------
⇒ Tổng số lượng sản phẩm trong giỏ: 3
⇒ TỔNG TIỀN THANH TOÁN: 25,300,000đ

Mời bạn chọn chức năng (1-5): 2
Nhập mã sản phẩm:  p001 
Nhập số lượng: 2
Sản phẩm P001 đã có trong giỏ. Đã cộng dồn, số lượng mới: 3

Mời bạn chọn chức năng (1-5): 2
Nhập mã sản phẩm: p003
Nhập tên sản phẩm: Sac nhanh 20W
Nhập số lượng: 1
Nhập đơn giá: 350000
Đã thêm sản phẩm P003 - Sac nhanh 20W vào cuối giỏ hàng.

Mời bạn chọn chức năng (1-5): 2
Nhập mã sản phẩm: P004
Nhập tên sản phẩm: Cap
Nhập số lượng: 0
Số lượng không hợp lệ (phải là số nguyên lớn hơn 0). Không thực hiện thao tác.

Mời bạn chọn chức năng (1-5): 2
Nhập mã sản phẩm: P004
Nhập tên sản phẩm: Cap
Nhập số lượng: 2
Nhập đơn giá: -5
Đơn giá không hợp lệ (phải là số nguyên không âm). Không thực hiện thao tác.

Mời bạn chọn chức năng (1-5): 2
Nhập mã sản phẩm: P004
Nhập tên sản phẩm: Cap
Nhập số lượng: abc
Số lượng không hợp lệ (phải là số nguyên lớn hơn 0). Không thực hiện thao tác.

Mời bạn chọn chức năng (1-5): 3
Nhập mã sản phẩm: P002
Nhập số lượng mới: 5
Đã cập nhật số lượng P002 thành 5.

Mời bạn chọn chức năng (1-5): 3
Nhập mã sản phẩm: P009
Mã sản phẩm không tồn tại trong giỏ hàng.

Mời bạn chọn chức năng (1-5): 3
Nhập mã sản phẩm: P001
Nhập số lượng mới: -1
Số lượng không hợp lệ (phải là số nguyên lớn hơn 0). Không thực hiện thao tác.

Mời bạn chọn chức năng (1-5): 4
Nhập mã sản phẩm: P002
Đã xóa sản phẩm P002 - Op lung Silicon khỏi giỏ hàng.

Mời bạn chọn chức năng (1-5): 4
Nhập mã sản phẩm: P002
Mã sản phẩm không tồn tại trong giỏ hàng.

Mời bạn chọn chức năng (1-5): 1

── CHI TIẾT GIỎ HÀNG ──
STT | Mã SP | Tên Sản Phẩm          | SL  | Đơn Giá      | Thành Tiền
--------------------------------------------------------------------
1   | P001  | Dien thoai iPhone 15  | 3   | 25,000,000đ  | 75,000,000đ
2   | P003  | Sac nhanh 20W         | 1   | 350,000đ     | 350,000đ
--------------------------------------------------------------------
⇒ Tổng số lượng sản phẩm trong giỏ: 4
⇒ TỔNG TIỀN THANH TOÁN: 75,350,000đ

Mời bạn chọn chức năng (1-5): abc
Lựa chọn không hợp lệ, vui lòng nhập số từ 1 đến 5!

Mời bạn chọn chức năng (1-5): 0
Lựa chọn không hợp lệ, vui lòng nhập số từ 1 đến 5!

Mời bạn chọn chức năng (1-5):  
Lựa chọn không hợp lệ, vui lòng nhập số từ 1 đến 5!

Mời bạn chọn chức năng (1-5): 5
Thoát chương trình. Cảm ơn bạn đã mua sắm!
```

### Bảng kiểm thử

| Kịch bản | Dữ liệu | Kết quả |
|---|---|---|
| Xem giỏ hàng mẫu | Chọn 1 | Tổng SL 3, tổng tiền 25,300,000đ (khớp đề) |
| Cộng dồn mã đã có (chữ thường, thừa khoảng trắng) | " p001 ", SL 2 | P001 số lượng 3, không tạo dòng mới |
| Thêm sản phẩm mới | p003, Sac nhanh 20W, 1, 350000 | Thêm dict P003 vào cuối giỏ |
| Bẫy 1 - số lượng 0 / chữ | 0, abc | Báo lỗi, không thêm |
| Bẫy 1 - đơn giá âm | -5 | Báo lỗi, không thêm |
| Cập nhật số lượng | P002 → 5 | Số lượng P002 = 5 |
| Bẫy 1 - cập nhật số âm | P001 → -1 | Báo lỗi, giữ nguyên |
| Bẫy 2 - cập nhật / xóa mã không có | P009; P002 (đã xóa) | Mã sản phẩm không tồn tại trong giỏ hàng. |
| Xóa sản phẩm | P002 | Xóa khỏi giỏ; giỏ còn P001 (3) và P003, tổng 75,350,000đ |
| Bẫy 3 - menu sai | abc, 0, rỗng | Báo lỗi, hiện lại menu |
| Thoát | 5 | Kết thúc chương trình |

## Ghi chú

Khung menu mẫu trong đề ghi tiêu đề "SHOPEE CART MANAGEMENT SYSTEM" (dù bối cảnh là Amazon), nên chương trình giữ nguyên tiêu đề này cho khớp với output mẫu.

## Cách chạy

```bash
python amazon_cart.py
```
