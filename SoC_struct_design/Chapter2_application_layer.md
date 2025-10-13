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

![image](Chapter2_application_layer.asset\RTT)

Round Trip Time(RTT)

요청에 대한 결과물만 주고 연결을 끉음

persistent HTTP(현대)

요청에 대한 결과물을 주고 대기(연결 유지) 



![image](Chapter2_application_layer.asset\http_request_message)

![image](Chapter2_application_layer.asset\http_request_message_format)



![image](Chapter2_application_layer.asset\http_response_message)

![image](Chapter2_application_layer.asset\http_status)







![image](Chapter2_application_layer.asset\uploading_form_input)

![image](Chapter2_application_layer.asset\http_method_types)

head에게 url요청에 의한 object는 보내지말라는 의미(아마 통신이 되는지 확인용 메서드인듯?)

##### cookies

> 트랜잭션의 히스토리를 모아둔것
>
> 웹사이트에 의해 사용자 컴퓨터에 저장되는 정보

![cookies](Chapter2_application_layer.asset\cookies.png)



4가지 필수사항

* 쿠키 헤더 라인을 HTTP response에다 추가
* 쿠키 헤더 라인을 다음 HTTP request message 에다가도 추가
* 브라우저에서 쿠키 파일 유지
* 웹사이트에서는 백엔드 DB를 유지



주요 쓰임새

* 유저 세션 유지(web e-mail) ex) 로그인

  예를 들면 장바구니를 나갈때마다 새로 로그인을 안하는 그런거

* 장바구니

* 제품 추천



##### Web caches(proxy server)

데이터를 요청할때 기본적으로 캐시데이터가 저장된 프록시 서버(서버같은 역할을 한다해서 프록시임)에 요청을 하고 

없으면 오리지널 서버에 요청을 하여 requset에 대한 object를 받아옴



예시

![web_caching](Chapter2_application_layer.asset\web_caching)

하지만 갱신 되지 않은 데이터를 계속 캐시서버에서 줄수 있으므로 

Conditional GET 메서드를 사용



#### E-mail(electronic mail)

![Email](Chapter2_application_layer.asset\Email)



![Email2](Chapter2_application_layer.asset\Email2)

![mail_acess_protocols](Chapter2_application_layer.asset\mail_acess_protocols)

telnet

>  telnet hostname port# 형태로 사용됨



![SMTP](Chapter2_application_layer.asset\SMTP)

![SMTP_port](Chapter2_application_layer.asset\SMTP_port)

![pull_push](Chapter2_application_layer.asset\pull_push)

##### POP3 protocol

![POP3_protocol](Chapter2_application_layer.asset\POP3_protocol)

해당 방식은 download-delete 방식

![pop3_more](Chapter2_application_layer.asset\pop3_more)

##### IMAP

> POP3을 보완하고자 나옴

pop방식이 로커(컴퓨터)에 저장되는 방식이라면

pop 방식에는 delete는 서버메일박스에 bob이 받으면 삭제

keep은 bob이 받아도 유지

IMAP방식은 서버에 저장 -> 서버메일박스에서 들고옴

동기화됨



여기까지는 C-S 형태



## Sockets

![image](Chapter1_Roadmap\sockets)

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

### DNS: domain name system

![DNS](Chapter2_application_layer.asset\DNS)

어떤 사이트에 접근하기위해

hostname 에 접근을 하는데 얘가 domain name이다



![DNS_struct](Chapter2_application_layer.asset\DNS_struct)



> hostname -> IP주소 변환
>
> hostname의 별명 설정
>
> 여러 복사된 서버를 사용



![DNS_distrib](Chapter2_application_layer.asset\DNS_distrib)

yahoo.com 같은걸 authoritive 주소라고 함



+알파(DNS hierarchichical 에는 속하지 않음)

![Local_DNS](Chapter2_application_layer.asset\Local_DNS)

#### TLD: top-level domain

![TLD](Chapter2_application_layer.asset\TLD)

TLD = DNS hierarchichical 에서 두번째 그거인듯?

TLD서버는 관리하는 기관이 따로 있음

authoritative DNS server = DNS hierarchichical 에서 3번째?

#### iterated query

![iterated_query](Chapter2_application_layer.asset\iterated_query)

request 받은 서버가 어디로 가면 되는지만 알려줌

즉 response 받은 서버는 그 주소의 서버에 request

그래서 그 주소로 다시 접근

#### recursive query

![recursive_query](Chapter2_application_layer.asset\recursive_query)

requst 받은 서버는 그 주소를 찾아주려고 다른 서버에 request를 함



#### cache

![DNS_cache](Chapter2_application_layer.asset\DNS_cache)

request하는 서버에서 cahe를 사용할 수 있다.(TLD 레벨 수준의 주소를 캐시저장함)

즉 root DNS서버를 안 거쳐도 됨

out-of-date 정보를 배제하기 위해 TTL(expire되면 해당 정보를 버리게끔) 정보를 고려함



#### DNS 프로토콜 메시지 구조

![DNS_message_str](Chapter2_application_layer.asset\DNS_message_str)

##### records

![DNS_records](Chapter2_application_layer.asset\DNS_records)

#### 요약

![DNS_Summerize](Chapter2_application_layer.asset\DNS_Summerize)





### P2P: peer to peer

![p2p](Chapter2_application_layer.asset\p2p)

장점 

* 확장성(scalability)
* 



사용 예시

* file distruibution (ex: 토렌트)
* streaming
* Voip(ex: skype)



C-S 와의 차이점

![p2p_upload](Chapter2_application_layer.asset\p2p_upload)

