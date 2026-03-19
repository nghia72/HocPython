so_xe = 100
cho_ngoi_moi_xe = 4.0
tai_xe = 30
hanh_khach = 90

xe_khong_chay = so_xe - tai_xe
xe_dang_chay = tai_xe
suc_chua = xe_dang_chay * cho_ngoi_moi_xe
trung_binh_khach = hanh_khach / xe_dang_chay

print("Hien co", so_xe, "chiec xe.")
print("Chi co", tai_xe, "tai xe lam viec.")
print("Se co", xe_khong_chay, "chiec xe bi bo trong.")
print("Chung ta co the cho", suc_chua, "nguoi.")
print("Co", hanh_khach, "hanh khach can di.")
print("Moi xe can cho khoang", trung_binh_khach, "nguoi.")
