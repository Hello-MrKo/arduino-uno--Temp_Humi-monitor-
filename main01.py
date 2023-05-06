
# Main00.  2개 온습도센서 (AM2302) 모니터 및 저장

import serial                # pip install pyserial
import time
import sys
import keyboard              # pip install keyboard


# 통신포트 설정 및 에러처리    
try:
    Arduino=serial.Serial('com4',9600,timeout=2)
    time.sleep(2)
except:
    print("Device can not be found or can not be configured.")
    sys.exit(0)

# 첫번째 Line 출력 
firstline='No.''\t''--- date & time ---''\t''H1''\t''T1''\t''H2''\t''T2''\n'
print(firstline)

# 데이터 저장 
TT=time.strftime('%Y-%m-%d-%H-%M-%S')
f=open('./data/'+TT+'.txt','a')                 # 폴더 및 파일명 지정        
f.write(firstline)

# No. 변수 
add=0                                  

# 함수 
def Daq(c):                              # c 는 a 또는 b   (a:센서1, b:센서2)
    c=c.encode('utf8')
    Arduino.write(c) 
    str1=Arduino.readline()
    output=str1.decode()
    time.sleep(1)    
    return output    

# Data 읽기 
for i in range(1,50):                   # 측정 Data 길이 
    output11=Daq('a')                   # 센서 1 데이터 요청   
    output22=Daq('b')                   # 센서 2 데이터 요청
      
    if keyboard.is_pressed("q"):        # q 누루고 있으면 출력             
        break

    H1=output11[13:18]                  # 습도1 
    T1=output11[37:42]                  # 온도1
    H2=output22[13:18]                  # 습도2  
    T2=output22[37:42]                  # 온도2       

    add=add+1
    num=str(add)
    SS='\t'
    TT=time.strftime('%Y-%m-%d %H:%M:%S')
    SUM00=num+SS+TT+SS+H1+SS+T1+SS+H2+SS+T2+'\n'     

    print(SUM00)
    f.write(SUM00)
                                                                    # 초 
f.close()
 
