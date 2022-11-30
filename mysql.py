import pymysql
#접속 정보
con = pymysql.connect(host='192.168.228.3', user='seongmun-hwang', password='0920',
                       db='genshin', port = 4567)
 
cur = con.cursor()
 

#quit 입력전까지 mysql과 동일한 명령어 입력해 데이터베이스 사용
while True :
    print("1. 유저 등록")
    print("2. 유저 삭제")
    print("3. 유저 열람")
    print("9. 자유 문법")
    print("10. 종료")
    num=input("원하시는 기능을 선택하세요: ")
    
    if num == '1':
        uid, nickname, gender=input("유아이디, 닉네임, 성별을 입력하세요: ").split()
        sql="INSERT INTO 사용자 (유아이디, 닉네임, 성별) VALUE ("+uid+",'"+nickname+"','"+gender+"');"
        cur.execute(sql)
        rows = cur.fetchall()
        print(rows)
        
    elif num == '2':
        uid=input("삭제하고자 하는 유아이디를 입력하세요: ")
        sql="DELETE FROM 사용자 WHERE 유아이디 =123"
        cur.execute(sql)
        rows = cur.fetchall()
        print(rows)
        
    elif num == '3':
        sql="SELECT * FROM 사용자;"
        cur.execute(sql)
        rows = cur.fetchall()
        print(rows)
        
    elif num == '9':
        sql=input("원하는 쿼리문을 입력하세요: ");
        cur.execute(sql)
        rows = cur.fetchall()
        print(rows)
        
    elif num == '10': break

    con.commit()
    
con.close()


