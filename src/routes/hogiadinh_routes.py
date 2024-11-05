from flask import Blueprint, jsonify, request
from sqlalchemy import text
from src import db

hogiadinh_bp = Blueprint('HoGiaDinh', __name__)

@hogiadinh_bp.route('/hogiadinh', methods=['GET'])
def get_data_db2():
    try:
        # Lấy tham số truy vấn cho phân trang
        page = request.args.get('page', default=1, type=int)  # Mặc định là trang đầu tiên
        per_page = request.args.get('per_page', default=10, type=int)  # Số bản ghi trên mỗi trang

        # Tạo kết nối tới cơ sở dữ liệu thứ hai
        with db.get_engine('db2').connect() as connection:
            # Sử dụng text() để chỉ định câu lệnh SQL với phân trang
            query = text("""
                SELECT * FROM HoGiaDinh
                ORDER BY HoGiaDinhID  -- Thay đổi 'Id' thành tên cột bạn muốn sắp xếp
                OFFSET :offset ROWS
                FETCH NEXT :per_page ROWS ONLY
            """)
            offset = (page - 1) * per_page  # Tính toán vị trí bắt đầu của trang hiện tại
            result = connection.execute(query, {"offset": offset, "per_page": per_page})
            
            # Chuyển đổi kết quả thành danh sách dictionary
            data = [dict(zip(result.keys(), row)) for row in result]

            # Lấy tổng số bản ghi để tính toán tổng số trang
            total_result = connection.execute(text("SELECT COUNT(*) FROM HoGiaDinh"))
            total = total_result.scalar()

            # Tính toán tổng số trang
            total_pages = (total + per_page - 1) // per_page

        return jsonify({
            "data": data,
            "total": total,
            "page": page,
            "per_page": per_page,
            "total_pages": total_pages
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500