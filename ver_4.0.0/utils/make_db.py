import sqlite3

# 데이터베이스 연결
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# 데이터베이스에서 테이블 생성
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = """
    CREATE TABLE IF NOT EXISTS conversation (
        id INTEGER PRIMARY KEY,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        context TEXT,
        utt_label TEXT
    )
    """
    cursor.execute(sql)
    conn.commit()
    conn.close()
    
# 데이터베이스에 기록 업데이트 
def add_log(context, context_utt_label):
    conn = get_db_connection()
    cursor = conn.cursor()
    for i in range(len(context)):
        sql = "INSERT INTO conversation (context, utt_label) VALUES (?, ?)"
        cursor.execute(sql, (context[i], context_utt_label[i]))
        conn.commit()
    conn.close()
    print("db 기록이 완료되었습니다.")
