import subprocess
import time

print("Bắt đầu nè")
# Danh sách các file script cần chạy với đường dẫn đầy đủ
scripts = [
    "./thethao/phukienthethao/crawl-product-id-tiki.py",
    "./thethao/thethaochoivot/crawl-product-id-tiki.py",
    "./thethao/thethaodongdoi/crawl-product-id-tiki.py",
    "./thethao/trangphucthethao/crawl-product-id-tiki.py",
    "./nhacua/giatgiu/crawl-product-id-tiki.py",
    "./nhacua/vesinhnhabep/crawl-product-id-tiki.py",
    "./nhacua/vesinhnhacua/crawl-product-id-tiki.py",
    "./nhacua/vesinhnhatam/crawl-product-id-tiki.py",
    "./maytinh/laptop/crawl-product-id-tiki.py",
    "./maytinh/linhkien/crawl-product-id-tiki.py",
    "./maytinh/pc/crawl-product-id-tiki.py",
    "./sach/sachtienganh/crawl-product-id-tiki.py",
    "./sach/sachtiengviet/crawl-product-id-tiki.py",
    "./sach/vanphongpham/crawl-product-id-tiki.py",
    "./xeco/oto/crawl-product-id-tiki.py",
    "./xeco/phukienxe/crawl-product-id-tiki.py",
    "./xeco/xemay/crawl-product-id-tiki.py",
    "./xeco/xedap/crawl-product-id-tiki.py",
    "./thietbidien/maygiat/crawl-product-id-tiki.py",
    "./thietbidien/maylanh/crawl-product-id-tiki.py",
    "./thietbidien/tivi/crawl-product-id-tiki.py",
    "./thietbidien/tulanh/crawl-product-id-tiki.py",

]


# Hàm để chạy một script và chờ nó hoàn thành
def run_script(script_path):
    start_time = time.time()
    print(f"Đang chạy script {script_path}")
    result = subprocess.run(["python", script_path], capture_output=True, text=True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    if result.returncode == 0:
        print(f"Script {script_path} chạy thành công.")
    else:
        print(f"Script {script_path} gặp lỗi:\n{result.stderr}")
    
    print(f"Thời gian chạy: {elapsed_time:.2f} giây")
    print("=====================================")


# Chạy từng script một cách tuần tự
for script in scripts:
    run_script(script)