import pymysql
#접속 정보
con = pymysql.connect(host='192.168.228.3', user='seongmun-hwang', password='0920',
                       db='genshin', port = 4567)
 
cur = con.cursor()

#sql문 실행 함수
def execute_sql(str):
    cur.execute(str)
    rows = cur.fetchall()
    print(rows)
    con.commit()

#quit 입력전까지 mysql과 동일한 명령어 입력해 데이터베이스 사용
while True :
    print("1. 유저 등록         5. 보유 캐릭터 등록")
    print("2. 유저 정보 수정    6. 보유 캐릭터 수정")
    print("3. 유저 목록 조회    7. 보유 캐릭터 조회")
    print("4. 유저 삭제         8. 보유 캐릭터 삭제")
    print("9. 자유 문법")
    print("10. 종료")
    num=input("원하시는 기능을 선택하세요: ")
    
    if num == '1':
        uid, nickname, gender=input("유아이디, 닉네임, 성별을 입력하세요: ").split()
        sql="INSERT INTO 사용자 (유아이디, 닉네임, 성별) VALUE ("+uid+",'"+nickname+"','"+gender+"');"
        execute_sql(sql)
        
    elif num == '2':
        uid=input("사용자 유아이디를 입력해 주세요: ")
        sql="SELECT * FROM 사용자 WHERE 유아이디='"+uid+"';"
        execute_sql(sql)
        nickname, gender=input("수정할 닉네임과 성별을 입력해주세요: ").split()
        sql="UPDATE 사용자 SET 닉네임='"+nickname+"',성별='"+gender+"' WHERE 유아이디='"+uid+"';"
        execute_sql(sql)
        
    elif num == '3':
        sql="SELECT * FROM 사용자;"
        execute_sql(sql)
        
    elif num == '4':
        uid=input("삭제하고자 하는 유아이디를 입력하세요: ")
        sql="DELETE FROM 사용자 WHERE 유아이디 =123"
        execute_sql(sql)
        
    elif num == '5':
        uid=input("사용자 유아이디를 입력해 주세요: ")
        break;
        
    elif num == '6':
        uid=input("사용자 유아이디를 입력해 주세요: ")
        break;
        
    elif num == '7':
        uid=input("사용자 유아이디를 입력해 주세요: ")
        break;
        
    elif num == '8':
        uid=input("사용자 유아이디를 입력해 주세요: ")
        break;
        
    elif num == '9':
        sql=input("원하는 쿼리문을 입력하세요: ");
        execute_sql(sql)
        
    elif num == '10': break
    
con.close()


