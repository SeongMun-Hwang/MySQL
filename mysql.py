import pymysql
#접속 정보
con = pymysql.connect(host='192.168.228.3', user='seongmun-hwang', password='0920',
                       db='genshin', port = 4567)
 
cur = con.cursor()

global uid

#sql문 실행 함수
def execute_sql(str):
    cur.execute(str)
    print(cur.fetchall())
    con.commit()
    print("\n")
    
def cal_status(c_name):
    sql="UPDATE 보유_캐릭터 SET \
    공격력=(SELECT 무기_공격력 FROM 무기 WHERE 무기_이름=보유_캐릭터.무기_이름) \
    + (SELECT 성유물_공격력 FROM 성유물 WHERE 성유물_이름=보유_캐릭터.성유물_이름)\
    + (SELECT 캐릭터_공격력 FROM 캐릭터 WHERE 캐릭터_이름=보유_캐릭터.캐릭터_이름)\
    + (SELECT 성장_공격력 FROM 캐릭터 WHERE 캐릭터_이름=보유_캐릭터.캐릭터_이름)*레벨\
    ,방어력 = (SELECT 성유물_방어력 FROM 성유물 WHERE 성유물_이름=보유_캐릭터.성유물_이름)\
    + (SELECT 캐릭터_방어력 FROM 캐릭터 WHERE 캐릭터_이름=보유_캐릭터.캐릭터_이름)\
    + (SELECT 성장_방어력 FROM 캐릭터 WHERE 캐릭터_이름=보유_캐릭터.캐릭터_이름)*레벨\
    ,체력 = (SELECT 성유물_체력 FROM 성유물 WHERE 성유물_이름=보유_캐릭터.성유물_이름)\
    + (SELECT 캐릭터_체력 FROM 캐릭터 WHERE 캐릭터_이름=보유_캐릭터.캐릭터_이름)\
    + (SELECT 성장_체력 FROM 캐릭터 WHERE 캐릭터_이름=보유_캐릭터.캐릭터_이름)*레벨\
    WHERE 유아이디="+uid+" AND 캐릭터_이름='"+c_name+"';"
    execute_sql(sql)
    
def check_exist(table, attr, what) :
    sql="SELECT * FROM "+table+" WHERE EXISTS(SELECT * FROM "+table+" WHERE "+attr+"='"+what+"');"
    if cur.execute(sql)==0:
        print("등록되지 않은",table,"입니다.\n")
        return 0
    
def check_character_all(name, weapon, relic):
    x=check_exist('캐릭터', '캐릭터_이름', name)
    y=check_exist('무기', '무기_이름', weapon)
    z=check_exist('성유물', '성유물_이름', relic)
    if x==0 or y==0 or z==0:
        return 0
    
while True :
    print("1. 유저   2. 캐릭터   3.종료 \n4.캐릭터,무기,성유물 조회")
    func=input("사용할 기능을 선택하세요: ")
    #유저 기능 선택
    if func == '1':
        while True :
            print("유저 메뉴")
            print("1. 유저 등록")
            print("2. 유저 정보 수정")
            print("3. 유저 목록 조회")
            print("4. 유저 삭제")
            print("5. 종료")
            print("!입력이 여러 개일시 ,를 사용하세요!")
            user_num=input("원하시는 기능을 선택하세요: ")
            print("\n")
            
            #유저 등록
            if user_num == '1':
                while True:
                    uid, nickname, gender=input("유아이디, 닉네임, 성별을 입력하세요: ").split(",")
                    if check_exist('사용자', '유아이디', uid)==0:
                        break
                    else :
                        print("이미 등록된 사용자입니다")
                
                sql="INSERT INTO 사용자 (유아이디, 닉네임, 성별) VALUE ("+uid+",'"+nickname+"','"+gender+"');"
                execute_sql(sql)
                
            #유저 정보 수정
            elif user_num == '2':                   
                while True:
                    uid=input("수정할 사용자 유아이디를 입력해 주세요: ")
                    if check_exist('사용자', '유아이디', uid) !=0:
                        break
                
                nickname, gender=input("수정할 닉네임과 성별을 입력해주세요: ").split(",")
                sql="UPDATE 사용자 SET 닉네임='"+nickname+"',성별='"+gender+"' WHERE 유아이디='"+uid+"';"
                execute_sql(sql)
                
            #유저 목록 조회
            elif user_num == '3':
                sql="SELECT * FROM 사용자;"
                execute_sql(sql)
                
            #유저 삭제
            elif user_num == '4':
                while True:
                    uid=input("삭제하고자 하는 유아이디를 입력하세요: ")
                    if check_exist('사용자', '유아이디', uid) !=0:
                        break
                
                sql="DELETE FROM 사용자 WHERE 유아이디 ='"+uid+"';"
                execute_sql(sql)
                
            elif user_num == '5':
                break
            
            else :
                print("잘못된 입력입니다.\n")
        
    #캐릭터 기능 선택
    elif func == '2':     
        while True:
            uid=input("본인의 유아이디를 입력해주세요: ")
            if check_exist('사용자','유아이디',uid)!=0:
                break
       
        while True:           
            print("\n현재 유아이디:",uid)
            print("캐릭터 메뉴")
            print("1. 보유 캐릭터 등록")
            print("2. 보유 캐릭터 수정")
            print("3. 보유 캐릭터 조회")
            print("4. 보유 캐릭터 삭제")
            print("5. 종료")
            print("!입력이 여러 개일시 ,를 사용하세요!")
            char_num=input("원하시는 기능을 선택하세요: ")
            print("\n")
            
            #보유 캐릭터 등록
            if char_num == '1':
                while True:
                    character, level, weapon, relic=input("추가하려는 캐릭터, 레벨, 무기, 성유물 이름을 입력해주세요: ").split(',')
                    sql="INSERT 보유_캐릭터 SET 유아이디="+uid+",캐릭터_이름='"+character+"',레벨="+level+",무기_이름='"+weapon+"',성유물_이름='"+relic+"';"
                    if check_character_all(character, weapon, relic)!=0:
                        break              
                execute_sql(sql)
                cal_status(character)
                
            #보유 캐릭터 수정
            elif char_num == '2':
                while True:
                    character, level, weapon, relic=input("수정할 캐릭터, 레벨, 무기, 성유물 이름을 입력해주세요: ").split(',')
                    sql="UPDATE 보유_캐릭터 SET 무기_이름='"+weapon+"',레벨="+level+",성유물_이름='"+relic+"' WHERE 유아이디="+uid+" AND 캐릭터_이름='"+character+"';"
                    if check_character_all(character, weapon, relic)!=0:
                        break
                execute_sql(sql)
                cal_status(character)
                
            #보유 캐릭터 조회
            elif char_num == '3':
                sql="SELECT * FROM 보유_캐릭터 WHERE 유아이디="+uid+";"
                execute_sql(sql)
                
            #보유 캐릭터 삭제
            elif char_num == '4':
                while True:
                    character = input("삭제할 캐릭터 이름을 입력해 주세요: ")
                    sql="SELECT * FROM 보유_캐릭터 WHERE EXISTS(SELECT * FROM 보유_캐릭터 WHERE 캐릭터_이름='"+character+"' AND 유아이디="+uid+");"
                    if cur.execute(sql) != 0:
                        break
                    else :
                        print("해당 유아이디 계정에 존재하지 않는 캐릭터입니다.\n")
                sql="DELETE FROM 보유_캐릭터 WHERE 유아이디="+uid+" AND 캐릭터_이름='"+character+"';"
                execute_sql(sql)                
                
            elif char_num == '5':
                break
            
            else :
                print("잘못된 입력입니다.\n")                
                      
    elif func == '3':
        print("bye")
        break
    
    elif func== '4':
        sql="SELECT 캐릭터_이름 FROM 캐릭터"
        execute_sql(sql)
        sql="SELECT 무기_이름 FROM 무기"
        execute_sql(sql)
        sql="SELECT 성유물_이름 FROM 성유물"
        execute_sql(sql)
                    
con.close()


