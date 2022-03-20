# 컴퓨터 네트워크

> 컴퓨터 네트워크의 계층적인 ***프로토콜** 구조

프로토콜 : 통신 규약

* 응용 프로그램(app)
* 트랜스포트 프로토콜
* 라우팅 알고리즘



## 챕터1 컴퓨터 네트워크 and 인터넷

### 인터넷 (Internet)

![image](.\Chapter1_Roadmap\roadmap)



> Hosts = end system 
>
> ex PC, Server IOT기기들 등등
>
> 실제로 컴퓨터라고 부를수 있는 객체들
>
> >Packet switches
> >
> >ex router 나 switche
> >
> >네트워크 장비로서 사용자(end system)들의 메시지의 목적지(라우터나 스위치)를 지정하는
> >
> >>Communication links
> >>
> >>bandwidth
> >>
> >>물리적인 연결
> >>
> >>
> >



인터넷 : 네트워크들의 네트워크

프로토콜 : 인터넷에서 메시지를 보내고 받는 규칙들(규약들)

ㄴ 표준화가 중요함!

인터넷 표준기관 

RFC : Request for comments

IETF : **I**nternet **E**ngineering **T**ask **F**orce



### 네트워크의 구조

#### network edge

> 메시지를 직접적으로 보내거나 받는 역할을 하는 부분

* access network

  > bandwidth(transmission rate)
  >
  > 단위 시간당/ 초당 전송가능한 bits (ex Mbps Gbps)

  * shared - 보안이 약함
  * dedicated 

![image](.\Chapter1_Roadmap\DSL)

LGU+나 SKT 같은 회사들(ISP - Internet Service Provider)이 이 access network를(DSL) 제공해주는 회사들임

제공받는 서비스는 dedicated line이다

![image](.\Chapter1_Roadmap\cable_net)

HFC : hyvrid fiber coax

여러 network를 묶어주는 중앙선 ?

제공받는 서비스는 share access network이다

shared access 라서 대역폭을 나눠쓰기 때문에 up to(최대 속도)라고 표현

![image](.\Chapter1_Roadmap\home_net)

home_net - cable / DSL - internet 순으로 연결

![image](.\Chapter1_Roadmap\ethernet)

이런 기관들은 위의 케이블회사나 DSL회사가 제공해주는게 아니라 ISP가 직접 제공해준다고함

![image](.\Chapter1_Roadmap\wirelss)

##### 역할

* host

  > app프로그램을 hosting(app의 메시지를 받아오고) 하고 있어서 host라고 부름

  메시지를 작게 자른 형태가 packet 

  * paket trasmission delay = L(패킷의 길이(bit단위)) / R(대역폭(bits/sec))

  ![image](.\Chapter1_Roadmap\physical media)

  ###### guided

  * twisted pair

    > 랜선(동선)

  * coaxial cable

    > 좀 더 굵은 동선

  * fiber optic cable

    > 광섬유

    높은 대역폭, 빛으로 정보를 주고받음, 빛이기 때문에 손실이 없음

  ###### unguided

  특징

  * 반사 (reflection)
  * 차단(obstruction by objects)
  * 주변의 영향에 민감함(interference)

  종류

  * terrstrial microwave

    >주변에서 잘안씀

  * LAN (wi-fi)

    >근거리용(커버리지가 작음), 대역폭 높음

  * wide-area(cellular)

    > 장거리용(커버리지가 큼), 대역폭이 낮음

  * satellite

    > 초장거리용(커버리지가 엄첨큼), 거리가 긴 만큼 딜레이가 긺

  

#### network core

> 메시지를 목적지에서 목적지로 전달하는 역할을 하는 부분

종류

* Packet switching
* circuit switching
* network structure



##### Circuit switching

![image](.\Chapter1_Roadmap\circuit_switching)

> 주로 전화 네트워크에서 쓰이던 방식
>
> user massage 전달전 call 요청이 있어야만하고
>
> call 요청이 있으면 call set up 과정이 됨

* 경로 설정과 경로상(라우터나 스위치들의) 자원할당이 call setup 과정에서 일어남

* 자원의 분할이 필요함

  * FDM

    ![image](.\Chapter1_Roadmap\FDM)

    대역폭을 자원으로서 분할

  * TDM

    ![image](.\Chapter1_Roadmap\TDM)

    할당시간을 자원으로서 분할

##### Packet switching

![image](.\Chapter1_Roadmap\packet_switching)

> circuit switching처럼 **자원예약이 없음** -> call setup이 없고 자원할당이 없음
>
> 필요할때 마다 자원을 할당
>
> 메시지의 단위를 패킷으로 잘라서 보내고 각 패킷의 목적지 주소가 명시되어있음
>
> 목적지 라우터는 패킷을 받으면 받음과 동시에 다음 목적지로 줄수가 없고 다 받은뒤에 메시지를 뽑아서 보냄
>
> ㄴ strore&forqward
>
> 그리고 자원을 보낼때는 모든 대역폭을 사용함(full link capacity)
>
> 패킷의 크기는 고정적이고  데이터 전송중에는 다른 라우터들이 간섭할 수 없기때문에  circuit switching의 TDM방식처럼 이루어짐

###### store-and-forward

![image](.\Chapter1_Roadmap\PS_store_and_forward)

한 링크를 hop이라고 표현하고 hop당 전송에 필요한 시간은 패킷의길이 L / 대역폭 R 단위시간이 걸린다 



![image](.\Chapter1_Roadmap\queueing_delay)

라우터에는 패킷을 stroe할 queue(버퍼)가 있는데 당연히 최대치가 있다 큐가 다 차있고

그 상태에서 패킷을 받게되면 Queueing delay가 발생하면서 packet이 loss되는 상황이 발생함

그런 상황을 congestion 이라고 표현함

##### packet ,circuit 비교

![image](.\Chapter1_Roadmap\sw_vs_circuit)

circuit 방식이 안정적이나 최대 사용자수가 제한적이다

packet 방식은 congestion이 발생할 수 있으나 확률이 적고 훨씬더 많은 사람을 수용할 수 있다(자원관리 효율적)



##### 구조

![image](.\Chapter1_Roadmap\network_of_network)

기본적으로 국가별 지역별로 환경이나 규제가 다르기때문에 global한 ISP가 존재할 수 없고

크게 나라별로 ISP가 여럿 존재하는데 global 하게 인터넷을 접속하기위해(ex ISP A 사용자가 ISP B 사용자랑 통신)

peering-link를 만든다

그리고 IXP는 ISP들의 ISP같은 역할을 한면서

regional net은 일종의 ISP이다

![image](.\Chapter1_Roadmap\Tier_ISP)

POP : customer(소비층 ISP나 access net)들이 접속할 수 있는점이 POP 접속점이라고 한다.

peering : 같은 레벨의 ISP들 끼리 link를 하는 개념

regional net 이 ISP를 거치지 않고 다른 regional net끼리 peering을 할수 있다

이유는 서로 통신을 하려는 regional net 끼리의 통신량이 많으면 상위 ISP를 통해서 통신을 할때 발생하는 비용과

층이 높을수록 발생하는 hop의 갯수에 따른 전송 시간 이 문제가 될 수 있으며

 또 다른 이유는 서로간 통신의 비용을 묻지 않는 settlement-free를 목적으로 둘 수도 있다

Multi-home : 상위 ISP를 여러개 두는것

content provider network : 구글이나 마이크로 소프트 처럼 데이터 센터를 운영한는 회사들이 ISP를 통하게 되면 데이터의 량 접속자수에 따라 비용이 많이 발생하므로 그것을 줄이고자 자체적으로 ISP처럼 제공을 할 수 있는 방식으로 비용을 줄이는 목적

##### 큰그림

![image](.\Chapter1_Roadmap\big_picture)



### 프로토콜 

> 포맷, 순서, 취할 액션 등을 정의해둔것

보통 layering 시스템으로 되어있음

* 장점
  * identification, relationship에 용의
  * maintenance, updating 용이
* 단점
  * 레이어당 고유 목적이 존재 그에따라 동작의 중복성이 존재할 수 있음
  * 다른레이어의 정보가 필요할때 요청하고 얻어오는 오버헤드가 존재할 수 있음

![image](.\Chapter1_Roadmap\internet_protocal_stack)

application 계층 프로토콜 : web app 지원, user app에서 발생한 데이터를 메시지로 만든뒤 전달 계층 으로 전달

단위 : 메시지



transport 계층 프로토콜 : application 프로토콜에서 발생한 메시지를(source process에서 발생한 메시지)를 목적지 프로세스에 전달해주는 프로토콜 host(컴퓨터)-host(컴퓨터) 를 하기위해 네트워크 계층에 요청

단위 : 세그먼트 = H_t flag + 메시지

 

network 계층 프로토콜 : 라우팅을 통해 소스 에서 목적지로 전달하게 해주는 역할, 목적지 까지 가기위해선 hop을 거쳐야하는데 hop by hop 으로 보내기위해 다시 링크 계층으로 요청

단위 : datagram = H_n flag + 세그먼트



link 계층 프로토콜 : hop by hop 으로 보내기위해 물리적인 신호를 bit를 실어보내야하기때문에 물리계층에 요청

단위 : frame = H_l flag + datagram



physical 계층 프로토콜 : bits를 보냄

단위 : packet?

![image](.\Chapter1_Roadmap\source_to_des)

#### 네트워크 보안

* 악성코드(malware)

  * viris : 받아서 execute 되어야만 동작
  * worm : 받기만 해도 동작

* spyware

  받은 사용자의 키 입력, 웹사이트 방문내력 업로드 등 기록하여 collection site 에 모두 업로드

* botnet

  스팸이나 DDos어택에의해 오염된 컴퓨터들의 집합

* Dos

  ![image](.\Chapter1_Roadmap\dos)

  1. select target
  2. break into hosts around the network(see botnet)
  3. send packets to target from compromised hosts

* sniffing

  > 주위 네트워크의 패킷들의 정보를 탈취하는 공격법

  ![image](.\Chapter1_Roadmap\sniff)

  * broadcast media(shared ethernet, wireless)에서 발생함

* spoofing

  > 남인척 하는 공격법

  ![image](.\Chapter1_Roadmap\sfooping)





네트워크의 성능지표 : delay, loss, trubble

#### Delay

![image](.\Chapter1_Roadmap\packet_delay)



* 홉을 지나게 되면서 겪게될 4가지 delay
  * processing delay : err체킹, 목적지 주소처리, 일반적으로 msec보다 작음
    * 거의 고정적
  * queueing delay :
    * 거치는 라우터의 level에 따라 달라짐
  * transmission delay : 링크에 밀어넣을때 발생하는 delay
    * 패킷의 크기L , 링크의 대역폭R에 영향을 받음
    * d_trans = L / R
  * propagation delay : 
    * 링크의 물리적 길이 d
    * 전파의 속도 s
    * d_prop = d / s

##### Queueing delay

![image](.\Chapter1_Roadmap\queueing_delay_detail)

a = 단위시간당 도착하는 packet의 평균 (한순간 클수도 있음)

traffic intensity = 단위시간당 유입되는 트래픽의 양

La/R이 0에 가까울수록 지연이 없고 

La/R이 1에 가까울수록 큐에 쌓여간다고 생각하면 좋다



#### Loss

##### packet loss

> La/R이 1에 가까울수록 큐가 쌓여가는데 큐의 크기를 넘어가는 순간 발생하는 loss

loss가 발생하면 메시지를 정상적으로 보내기위해 재전송 해야한다!(재전송 하는 패킷만큼의 delay)

ㄴ 그렇게되면 사용자 입장에서는 느려지고 컴퓨터 입장에서는 자원낭비를 하게된다



#### throughput : 단위 시간당 소스 에서 부터 목적지까지의 걸린 rate (bits/time)

대역폭이 가장 작은 링크가 기준이 됨

ㄴ bottleneck link(병목)

* instantaneous :
* average : 



## 챕터2 응용 계층(Application Layer)



## 챕터3 전송 계층(Transport Layer)







## 챕터4 네트워크 계층(Network Layer)



## 챕터5 ARP

### 데이터 센터 네트워킹



## 챕터6 모바일 네트워크





