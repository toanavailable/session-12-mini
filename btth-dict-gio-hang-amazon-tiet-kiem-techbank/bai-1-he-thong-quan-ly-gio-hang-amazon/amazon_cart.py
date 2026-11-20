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
