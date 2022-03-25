# 챕터2 응용 계층(application Layer)

## conceptual

### Client-Server 구조

> C <---> S

* 서버
  * 항상 호스트
  * 영구적인 ip 주소 할당
  * 데이터 센터형 스케일
* 클라이언트(s)
  * 서버와만 통신
  * 연결은 그때그때
  * 동적 ip주소 할당

### P2P(peer to peer)

> P <-----> P

* 항상 서버가 켜져있지는 않다
* peer들은 host도 되고 clients도 된다.
* 관리가 복잡하다.



## protocols

### app-layer protocol

#### defines

##### type of messages exchanged

* request
* response

##### message syntax



##### message semantics



##### rules



##### open protocols



##### proprietary protocols



#### Web and HTTP(TCP port:80)

HTTP: HyperText Transfer Protocol 

> 웹페이지는 여러 객체(이미지, 오디오, 템플릿등)를 포함하는데 base html파일은 역시 여러 객체들에 의해 참조 되어진다

각각의 객체는 rul을 토대로 접근될 수 있다

ex:

(www. someschool.edu)/(someDept/pic.gif)

host name								path name

* clent : 브라우저의 request나 receives, and displays of  웹 객체
* server : 요청에 의한 반응



Non-persisternt HTTP (옛방식)

![image](.\Chapter2_application_layer.asset\RTT)

Round Trip Time(RTT)

요청에 대한 결과물만 주고 연결을 끉음

persistent HTTP(현대)

요청에 대한 결과물을 주고 대기(연결 유지) 



![image](.\Chapter2_application_layer.asset\http_request_message)

![image](.\Chapter2_application_layer.asset\http_request_message_format)



![image](.\Chapter2_application_layer.asset\http_response_message)

![image](.\Chapter2_application_layer.asset\http_status)







![image](.\Chapter2_application_layer.asset\uploading_form_input)

![image](.\Chapter2_application_layer.asset\http_method_types)

head에게 url요청에 의한 object는 보내지말라는 의미(아마 통신이 되는지 확인용 메서드인듯?)



## Sockets

![image](.\Chapter1_Roadmap\sockets)

전송 계층과 응용 계층간 통로

### addressing processes

>통신은 hosts 간 통신이 아닌 process 끼리의 통신이다.

host의 ip 주소 만으로는 통신이 불가능하고 port 번호를 알아야함



### 서비스 4종류

#### data intefrity

* file sransfer - 데이터값이 바뀌면 큰일나는 파일 ex 엑셀파일이나 문서
* web treansactions - 비디오나 오디오같이 값이 바뀌어도 크게 지장이 없는

#### timing

* low delay

#### throughput

* 비디오나 오디오의 스트리밍 같은경우 최소 처리량이 중료
* elastic app 같은경우 크게 상관없음

#### security 



### TCP / IP

#### TCP

* 신뢰성 있는 전송
* flow control 전송되는 데이터 량을 조절 RTCP 의 버퍼가 차지 않게끔
* congestion control - 중간 라우터의 버퍼가 차지 않게끔 조절
* connection-oriented - hand shake 과정이 필요함

ex

SMTP (email)

Telnet

HTTP

FTP



#### UDP

* 신뢰성이 떨어지는 전송
* TCP에서 필요한 hand shake, control이 없기때문에 그에 따른 오버헤드가 없으므로 속도가 빠름

ex

HTTP

RTP

SIP, RTP, proprietanry

## app 



