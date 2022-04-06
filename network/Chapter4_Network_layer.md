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

* forwarding : 경로 정보를 받아 input 포트랑 ouput포트를 연결시켜주는, 물리적으로
* routing : 경로를 계산하여 포워딩 테이블을 만들어줌, 논리적으로

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



## EX

host의 네트워크 계층과 router의 네트워크계층의 역할을 살짝 다름

host의 네트워크 계층이 라우팅 능력이 약간 떨어짐

