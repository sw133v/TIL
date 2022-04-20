# 챕터4 네트워크 계층(Network Layer)

> 세그먼트를 sending host에서 receiving host로 전송 시켜주는 계층
>
> 전송계층이 프로세스-프로세스 서비스 였다면
>
> 네트워크 계층은 호스트-호스트 서비스이다

## 특징

* 선택이 불가능: 전송계층처럼 TCP/UDP를 고를수 있지않고 서비스를 산 회사의 방침대로 서비스를 받음(ex 회사가 데이터그램으로 운영을 한다면 데이터그램으로 받고 vir-cir 방식이면 vir-cir 방식대로 서비스를 받음)



## 기능

> 크게 두가지 기능으로 요약가능

* routing : 경로를 계산하여 포워딩 테이블을 만들어줌, 논리적으로

  라우터들의 정보를 받기위한routing/management control plane(software)

* forwarding : 경로 정보를 받아 input 포트랑 ouput포트를 연결시켜주는, 물리적으로

  받은 패킷을 다음 홉으로 보내는것

  forwarding data plane(hardwrae)



## 구조



![image-20220409172518698](Chapter4_Network_layer.asset\image-20220409172518698.png)

점선 기준 위가 control plane 아래가 data plane



### 인풋 포트

![image-20220409172806762](Chapter4_Network_layer.asset\image-20220409172806762.png)

* line termination 파트 : 비트레벨로 받아오는 부분 (물리계층)
* link later protocol 파트 : 데이터가 잘 들어왔는지 확인하는 부분(데이터링크 계층)
* look up forwarding queueing 파트 : 목적지로 보내기위해 아웃풋 포트를 찾기위해 포워딩 테이블을 찾는 부분 (네트워크 계층)

여기서 헤더를 때는 기능



인풋포트 프로세싱의 목표 : 데이터가 유입되는 속도와 처리되는 속도가 같아지는것

만약 더빨리 정보가 들어오면 queueing이 발생하고 보다 빨리 포워딩 해주는것



switch fabric의 전달 속도가 인풋포트들의 처리량보다 느리다면 인풋포트의 큐가 쌓이고 심한경우는 딜레이나 큐가 오버플로 되서 loss가 생김

Head-of-the-Line(HOL) blocking : 인풋포트에서만 발생하는데 같은 아웃풋 포트를 쓰면 뒤에 들어온 패킷이 막히는데 그 인풋포트 큐의 신호의뒤에 있는 패킷은 아웃풋포트가 안쓰이고 있어도 지연되는 현상

### switching fabrics

처리량은 

n * input / output line rate

![image-20220409175957279](Chapter4_Network_layer.asset\image-20220409175957279.png)

> 목표 : 얼마나 빠르게 인풋포트의 패킷을 아웃풋으로 보낼수 있는지



크게 3가지 형태로 나뉨

![image-20220409180145389](Chapter4_Network_layer.asset\image-20220409180145389.png)

#### via memory

초기 스위칭은 cpu의 직접적인 컨트롤하에 이루어짐

뿐만아니라 메모리에 인풋포트의 패킷이 저장되기 위해 시스템버스를 이용했어야함

즉 인풋 -> 메모리, 메모리 -> 아웃풋 처리를 해야하기때문에 시스템 버스를 두번 탔어야했다

이방식을 타개한것이 but 방식이다(but 하나의 인풋(패킷)만 버스에 접근 가능)

but contentions : 패킷이 서로 버스를 차지하려고 하는현상 bus의 대역폭에 달려있다



#### via interconnection

bus 형식의 단점을 극복하고자 만듦



### 아웃풋 포트

![image-20220409182401276](Chapter4_Network_layer.asset\image-20220409182401276.png)

> 기본적으로 인풋포트랑 비슷함

헤더를 다는 기능?

여기서도 버퍼는 역시 필요한데

보내는 속도보다 들어오는 속도가 더빠를때 이를 처리하기위해 필요함

큐안 내용(패킷)중 무엇을 더 먼저 보낼지 스케줄링도 할 수 있음(버퍼가 있음으로)

여기서 역시 딜레이나 loss가 발생가능



라우터를 디자인할때 이 버퍼링 capacity을 하는것이 중요함







## 서비스 모델

* 개별적인 데이터 그램
  * 특정 지연시간 내에 전달이 보장되는것
* 흐름에 따른 데이터 그램ㅋㅋㅋ
  * 순서대로(in-order) 전달
  * 최소한의 대역폭이 보장



## Packet Switching

> circuit switching과는 다른 도메인 방식

전송계층의 TCP(connection-oriented)와 UDP(connectionless) 방식처럼

비슷하게 연결방식 비연결방식이 존재



### 종류

* virtual circuit

  * 데이터를 주고받기전 call setup을 무조건 함

    이과정에서 경로와 VC ID를 설정하게됨, 뿐만아니라 얼마나 자원을 할당 받았는지 **상태** 를 저장하게됨

    경로, VC num 을 포워딩 테이블에 저장

  * 주고받기가 끝나면 reardown을 하게됨

  * 라우터간 시그널링 할 프로토콜들이 존재해야함

  * ATM, X.25, frame-relay등에 사용됨 주로 전화회사

  * 오늘날의 인터넷에서는 사용 안하는 방식

  * end 시스템이 주로 멍청함 (전화,)

![vc_forwarding](Chapter3_Transport_layer.asset\vc_forwarding.jpg)

vc방식의 예시



* datagram
  * elastic 서비스가 주로 이루어짐(relaible의 반대말인듯?)
  * end 시스템이 똑똑함 (주로 컴퓨터) - 오류 복구가 좋다



![dg_forwarding](Chapter3_Transport_layer.asset\dg_forwarding.jpg)

헤더 파일로 판단



## 프로토콜

### 라우팅 프로토콜

![image-20220413211634056](Chapter4_Network_layer.asset\image-20220413211634056.png)



> control plane에 관련된 프로토콜
>
> 라우팅 알고리즘과 그것을 필요로하는 네트워크 정보를 주고받는것을 목적으로함
>
> 라우팅 알고리즘이 필요로하는 정보를 모으기위해 존재

Graph abstraction

> graph: G = (N, E)
>
> N = set of routers = {1,2,3,4,5,6....}
>
> E = set of links = {(1,3),(1,4).....}

대역폭은 높을수록 적은코스트로

congestion이나 delay는 고코스트로 측정

라우팅 알고리즘

> 최소비용으로 경로를 만들기위한 목적

* global : 모든 링크를 알고있는 알고리즘

  link state 알고리즘이라고도 함

  * Dijkstra 알고리즘
  * 

* decentralized : 지역적인 정보만앎 -> 이웃 라우터 정도와 비용정도만 앎

  대신 서로의 라우터 끼리 대화(거리 비용을 서로 공유시도)를 함

  distance vector 알고리즘이라고도 함

  * 



static - 링크 코스트가 고정적



dynamic - 링크 코스트가 가변적



#### 실제 라우팅 프로토콜 알고리즘



**Intra-ASes**

* RIP: Routing Information Protocol
  * 가장 기초적인 인트라 as라우팅 프로토콜
  * UDP사용

* OSPF:Open Shortest Path First
  * 다잌스트라 알고리즘을 사용

* IGRP:Interior Gateway Routing Protocol

**inter-ASes**

* BGP : Border Gateway Protocol
  * eBGP : 외부 AS들에게서 reachability를 알아온다
  * iBGP : 내부 라우터들에게 reachability를 전달
  * BGP Message
    * OPEN
    * UPDATE
    * KEEP ALIVE
    * NOTIFICATION



### IP프로토콜

> data plane에 관련된 프로토콜

#### 데이터 그램 포맷

![image-20220409183237924](Chapter4_Network_layer.asset\image-20220409183237924.png)

##### fragmentation

> 감당 못할 큰 데이터를 잘라서 보낸는 행위?
>
> 잘린 데이터그램들은 독립적인 데이터그램들이 된다
>
> 그후 reassemb 되어서 원 데이터 그램을 이룸



![image-20220409184325263](Chapter4_Network_layer.asset\image-20220409184325263.png)



![image-20220409184525715](Chapter4_Network_layer.asset\image-20220409184525715.png)

MTU가 최대 1500이므로 4000짜리는 

![image-20220409184634627](Chapter4_Network_layer.asset\image-20220409184634627.png)

이런식으로 나눌수 있음

이때 마지막 데이터 그램의 길이가 1040인 이유는 위에 데이터그램들이 가지는 헤더가 각 20바이트씩 차지하기때문에 원 4000짜리를 보내기 위해선 나눠질 데이터그램수-1 * 헤더크기 만큼이 더 필요하다

fragflag = 뒤에 들어올 데이터그램이 더 있다 없다는 의미 (즉 0이 마지막 데이터그램)

offset 은 헤더를 제외한 실질 데이터(1480바이트)를 8바이트로 나눈 결과값을 이전 오프셋과 더해서 저장



#### IPv4 addressing

ip address : 32bit(8bit * 4 ) id for host, router interface

interface: host와 router간의 물리적 링크

​	기본적으로 라우터는 여러개의 인터페이스를 가짐

​	host는 하나 혹은 두개(유선, 무선)의 인터페이스를 가짐

스위치, wifi base station은 기본적으로 ip주소를 할당받지 않음(네트워크계층이 없기 때문)



##### subnets

> 라우터의 개입없이 서로 통신할 수 있게끔하는것

ip address

* subnet part - high order bits
* host part - low order bits

범위는 뒤에 서브넷.0/서브넷 마스크 방식으로 표현

ex) 223.1.3.0/24(범위 즉 1부터 24까지)



#### CIDR: Classless InterDomain Routing

> 기존 방식은 class (a(8bit) - 24bit, b(16bit)- 16bit, c(24bit)-8bit 으로되는데)  방식인데
>
> 이 방식은 subnet과 host비율의 조절이 유연하지 못함 -> 비효율적임

CIDR notation : a.b.c.d / x

방식으로 표시되고 x값이 subnet부분의 비트수를 나타냄



#### DHCP : Dynamic Host Configuration Protocol

> 말 그대로 고정된 IP주소를 사용하는것 ex 회사나 연구실에서 사용하는 컴퓨터 -> ip주소가 바뀔일이 드뭄
>
> 해당 ip를 사용하는 host가 종료하면 그것을 회수해서 다른 host에게 쥐어줌(주소의 재사용) -> 동시사용이 아니라면 더 많은 host를 수용가능 주소의 활용도가 높음

overview

* DHCP discover msg[opt]
* DHCP offer msg[opt]
* DHCP request
* DHCP ack

ip할당 제외하고도

first-hop 라우터를 알려줌



**hierarchical addressing**



**Longest prefix matching**



**NAT:network address translation**

공유기 처럼 한 ip를 사용하여 subnet을 구성하는것 사설 ip라고도 표현함

![image-20220413060045555](Chapter4_Network_layer.asset\image-20220413060045555.png)

실제로 NAT라우터가  할당 받은 ip는 10.0.0.4이고 이것을 오른쪽과 같이 사용을 하지만 밖에서 보는 ip는 10.0.0.4이다

16-bit port-num field 이기에 6만여개의 LAN-side 주소를 만들어줄 수 있음

발생할 수 있는 문제점

* server을 둘 수 있는가? - 보여지는 곳에 server가 있어야하는데 nat라우터 서브넷 안에 있으면 클라이언트가 server에 request함에 문제가 발생(즉 클라이언트가 server의 위치를 몰라서 contact를 할 수 없음)

  * 이를 해결하기위한 방법

    * 수동적으로 static하게 포워딩 하는 하는방법(port를 서버에 함께주면서 request를 하는?)

    * 이것을 자동적으로 해주는 upnp(universal plug and play) IGD(internet gateway device) Protocol 

      public ip주소를 기억, port를 맵핑하며(add/remove)





### ICMP:internet control message protocol

> 에러 및 시그널링 관련 프로토콜 즉 라우팅 프로토콜과 IP프로토콜은 라우터-라우터, 라우터-호스트 간의 데이터 전송에 관련된 프로토콜

![image-20220413064106029](\Chapter4_Network_layer.asset\image-20220413064106029.png)

ICMP가 IP보다 위에 있음 -> 인캡슐레이션 할때 ICMP가 먼저 함





### IPv6

> 2^32 개의 주소를 가질수 있는 IPv4가 점점 주소가 고갈되감에 CIDR, DHCP, NAT를 개념을 점점 도입하다가 결국에 수용이 불가능 하기때문에 새로운 모델을 만듦
>
> 2^128개의 주소를 가질수 있음

40 byte의 고정적인 헤더를 사용함으로 프로세싱 속도를 빠르게 만듦

but optinoal header를 추가로 달면서 

40바이트 고정적인 헤더안에 NH(next header)를 넣어줌

마지막 NH에는 UDP/TCP인지의 값이 저장됨

데이터그램이 너무 크면 드랍시켜서 전송을 포기함

그래서 소스에다가 프래그먼트해서 보내게끔 만듦

![image-20220413071231065](\Chapter4_Network_layer.asset\image-20220413071231065.png)

priority 와 flow Label가 QoS(quality of service)를 위한 헤더



IPv4와의 차이점

checksum(최신의 장비들이 거의 bit오류가 없다는것을 가정) 과 options헤더가 없음(보다 빠른 프로세싱을 위해 가변적인 포맷대신 고정적인 크기의 포맷을 사용)대신에 Next Header 필드를 사용.

ICMPv6를 사용

#### IPv4 -> IPv6

IPv6 장비들은 IPv4장비들의 데이터 포맷(헤더)을 이용및 이해가 가능하지만 반대의경우x

그래서 터널링이라는 개념이 필요

IPv4 페이로드에 IPv6의 데이터를 저장

![image-20220413072231065](Chapter4_Network_layer.asset\image-20220413072231065.png)

밑이 실제 형태,





## EX

host의 네트워크 계층과 router의 네트워크계층의 역할을 살짝 다름

host의 네트워크 계층이 라우팅 능력이 약간 떨어짐

