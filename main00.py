
# Main00.  2개 온습도센서 (AM2302) 모니터 및 저장

import serial
import time
import sys
import keyboard

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
f=open('./data/'+TT+'.txt','w')                 # 폴더 및 파일명 지정        
f.write(firstline)

# No. 변수 
add=0                                  

# Data 읽기 

for i in range(1,5):                   # 측정 Data 길이 
    add=add+1

    if keyboard.is_pressed("q"):        # q 누루고 있으면 출력             
        break

    c='a'
    c=c.encode('utf8')
    Arduino.write(c)                    # 온습도 센서 11 읽기    
    str1=Arduino.readline()
    output11=str1.decode()
    H1=output11[13:18]                  # 습도1 
    T1=output11[37:42]                  # 온도1   


    c='b'                          
    c=c.encode('utf8')
    Arduino.write(c)                    # 온습도 센서 22 읽기 
    str2=Arduino.readline()
    output22=str2.decode()
    H2=output22[13:18]                  #습도2  
    T2=output22[37:42]                  #온도2     

    num=str(add)
    SS='\t'
    TT=time.strftime('%Y-%m-%d %H:%M:%S')


    SUM00=num+SS+TT+SS+H1+SS+T1+SS+H2+SS+T2+'\n'                            # 문자열 합치기 

    print(SUM00)
    f.write(SUM00)

    time.sleep(1)                                                               # 초 

f.close()
 
