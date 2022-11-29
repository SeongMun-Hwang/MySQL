import pymysql
#접속 정보
con = pymysql.connect(host='192.168.228.3', user='seongmun-hwang', password='0920',
                       db='genshin', port = 4567)
 
cur = con.cursor()
 

#quit 입력전까지 mysql과 동일한 명령어 입력해 데이터베이스 사용
while True :
    sql = input("MySQL 명령어를 입력하세요: ")
    if sql == 'quit': break
    cur.execute(sql)
    rows = cur.fetchall()
    print(rows)
    
con.close()

