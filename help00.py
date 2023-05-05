import time
import keyboard

add=0

firstline='No.''\t''---------일시---------''\t''H1''\t''T1''\t''H2''\t''T2''\n'
print(firstline)

TT=time.strftime('%Y-%m-%d-%H-%M-%S')

f=open('./data/'+TT+'.txt','w')
f.write(firstline)


for i in range(1,10):
    add=add+1

    if keyboard.is_pressed("q"):                                    # q 입력시 while 빠져 나오기 
        break

    str1 =b'Humidity 11: 44.70 %\tTemperature 11: 29.30 *C\r\n'
    output11=str1.decode()
    s11=output11[13:18]
    s12=output11[37:42]
  
    str2=b'Humidity 22: 37.70 %\tTemperature 22: 29.80 *C\r\n'
    output22=str2.decode()
    s21=output11[13:18]
    s22=output11[37:42]

    num=str(add)
    SS='\t'
    TT=time.strftime('%Y-%m-%d %H:%M:%S')


    SUM00=num+SS+TT+SS+s11+SS+s12+SS+s21+SS+s22+'\n'                            # 문자열 합치기 

    print(SUM00)
    f.write(SUM00)

    time.sleep(1)                                                   # 초 

f.close()




