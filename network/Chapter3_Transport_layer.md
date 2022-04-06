# 챕터3 전송 계층(Transport Layer)

## services

>  app process 간의 논리적 상호작용



![reliable_data_transfer_mechanism.jpg](Chapter3_Transport_layer.asset\reliable_data_transfer_mechanism.jpg)

![reliable_data_transfer_mechanism2.jpg](Chapter3_Transport_layer.asset\reliable_data_transfer_mechanism2.jpg)

* checksum : 오류 여부 확인용 데이터 (리시버)

* acknowledgement : 무사 송신 여부 개념 (리시버 -> 샌더)

* negative acknowledgement : 특정 패킷에대한 오전송의 데이터 (리시버 -> 샌더)

* timer : 리시버의 반응이 없으면 재전송, 단 위의 두 신호가 안오면 리시버는 데이터를 잘 받았으나 다시 오는경우가 존재

  다만 이경우는 리시버에서 받고 ack만 날려줌 (중복된 데이터는 삭제)

  이 타이머가 너무 짧으면 신호가 오기전에 전송실패로 여겨 다시보내고

  너무 길면 시간낭비가 발생함 그래서 RTT를 참고한느데

  RTT를 사용하는데 예측을 하기 위해 이전 RTT시간들을 사용함 이전 RTT값일 수록 가중치가 줄어듦

* pipelining : ack이나 nack 신호가 안와도 데이터를 보내는 것
* window : pipelining을 할때 적재할 수 있는 최대 패킷의 양
* sequence number : 리시버의 받은적이 있는 패킷의 정보인지 판별



### TCP

> 신뢰성을 갖추고 순서대로 전달하는 방식 

* congestion control - network를 overwahling 하지않는

* flow control - 리시버 버퍼를 overwarming 하지않는

* connection setup

* 바이트 스트림 단위로 전송됨 ex) flow, congestion 컨트롤로 인해 수용가능 데이터가 적을땐

  작은 크기로 여유있으면 크기가 큰 세그먼트로 전송됨, 혹은 장비의 버퍼에 양향

* 파이프라인 개념으로 flow, congestion 콘트롤에 의해 윈도우 사이즈가 결정

* 3-way 핸드쉐이크 연결을 한다(2-way일시 문제 발생 가능성 존재)

샌더측 이벤트

* data rcvd from app
* timeout
* ack rcvd

리시버측

* 배송되어온 세그먼트에 대한 액션
  * 인오더 :  순서대로 잘 올때
    * 딜레이를 주는경우(매번 ack을 보내는 대신 딜레이로 후발 ack을 보냄으로써 잘 받았다는것을 의미)
    * 
  * 아웃오브 오더 : 바로 ack을 보냄
  * 갭 사이 세그먼트를 받은경우 : 바로 ack을 보냄

![tcp_fc.jpg](Chapter3_Transport_layer.asset\tcp_fc.jpg)

링크 계층에서 받은 프레임의 헤더를 땐 데이터그램을 네트워크 계층으로

네트워크 계층에서 ip헤더를 때서 세그먼트를 전송계층으로 주고

그 세그먼트를 소켓 버퍼에 전달

만약 샌드의 속도가 리시버의 프로세스의 처리속도 보다 빠를때 드랍이 발생함(congestion?)

![tcp_fc2.jpg](Chapter3_Transport_layer.asset\tcp_fc2.jpg)

TCP 포멧 세그먼트의 헤더안 rwnd 부분에 free buffer space의 정보를 넣어 보냄으로써 흐름을 제어하여 드랍을 배제

3-way

연결 요청 - 연결 승인 - 연결 확인

연결 - 해제 차이점

연결 요청에 따른 연결은 클라이언트가 서버 보다 먼저 연결을 했다고 판단하고

연결 해제 요청에 따른 해제는 클라이언트가 서버보다 나중에 닫는다

2-way

연결 요청 - 연결 승인

이때 TCP는 연결 승인 받고 요청을 받고 ack을 안받으면 연결을 서버에서는 끉어버릴수 있다

즉 서버입장에서 클라이언트가 살아있는지 여부를 모른다

![cp_fsm.jpg](Chapter3_Transport_layer.asset\tcp_fsm.jpg)

#### congestion control

RWND가 flow 컨트롤을 위한거라면

CWND는 congestion 컨트롤을 위한헤더

* end-end congestion

  * 주로 네트워크에서 발생하여 피드백을 받을수 없는데

  * loss나 delay로 암시하는정도

  * TCP에서는 이방식을 채택

* network-assited congestion
  * 라우터에서 신호를 end시스템 쪽으로 피드백을 제공
    * 싱글 비트로(SNA, DECbit, TCP/IP ECN, ATM)등 있고 없고만 알려주거나
    * explicit rate로 알려주면서 congestion을 없애는 방법을 알려주는 방법이 존재

* TCP slow start 
  * 초기 rate가 느리지만 증가폭이 굉장히 빠름

* congestion avoidance start

  * cwnd < 임계치 일경우에는 

    cwnd를 RTT마다 2배로 증가

  * 그 반대일 경우RTT 마다 1개씩(MSS/cwnd) 

* loss를 발견했을시에

  > cwnd를 줄여 나가야함 

  * 타임 아웃시 : 도착이 안될때
    * 무조건 cwnd를 최소값(1)로 셋
  * 3 duplicate ack : 도착은 해서 반응은 하지만 모두 오지는 않을때
    * TCP RENO : cwnd를 반으로 셋
    * TCP Tahoe : cwnd를 최솟값(1)로 셋

![cwnd](Chapter3_Transport_layer.asset\cwnd.jpg)



다만 특정 시점(cwnd가 충분히 커지면)이 되면 무작정 늘리면 안됨

ssthresh(임계치)이고 OS가 디폴트 값을 정함, 단 loss가 발생하면 cwnd 값이 많다는것이니 줄여나감

loss가 발생하면 ssthresh = loss가 발생한 시점 cwnd /2 으로 설정 



TCP throughput(성능 척도)

W : loss가 발생하는곳 즉 window

  throughput는 W와 W/2 을 평균적으로 가질것 이기때문에

TCP throughput(avg)는 3W/4RTT bytes/sec 으로 볼수 있다



TCP Fairness(성능 척도)

공정성 = 기아현상이 적은정도

R이 bandwidth K가 이용자

R/K

![tcp_fair](Chapter3_Transport_layer.asset\tcp_fair)



![tcp_fair2](Chapter3_Transport_layer.asset\tcp_fair2.jpg)

rhroughput이 파란선 미만이면 각각 1씩 증가시키다가 파란선을 넘으면 반토막을 반복하다가

점점 equal bandwidth share에 가까워짐



### UDP

> 비신뢰적이고 순서없이 전달

* 핸드쉐이킹(연결작업)이 없다
* 각 세그먼트들을 독립적으로 받음(순서가 없음)
*  16비트의 checksum으로 센더에서 보낸것과 리시버가 받은것을 비교하여 전송오류가 있는지 체크
  * 단 모든 오류를 검출해내지는 않음



장점

* 메시지를 보낼때 금방보내짐 딜레이가 적음
* 간단함(연결이 없기때문에 denderm receiver가 없어도됨)
* 헤더사이즈가 작음

주요 사용app들

* 스트리밍 멀티미디어 앱
* DNS
* SNMP (네트워크 관리 프로토콜)





![format](Chapter3_Transport_layer.asset\format)

![udp_seg](Chapter3_Transport_layer.asset\udp_seg)

![tcp_seg](Chapter3_Transport_layer.asset\tcp_seg)

### * Multiplexing

> 보내는 곳에서 신호를 묶는 개념



### * Demultiplexing

> 받는곳에서 신호를 여러가닥으로 나누는개념?

![demul.jpg](Chapter3_Transport_layer.asset\demul.jpg)

대충 모양새는 요렇고

![demul2_2.jpg](Chapter3_Transport_layer.asset\demul2_2.jpg)

app(프로세스)마다 같은 포트을 쓰기때문에 source ip정보를 알아야한다

![demul2.jpg](Chapter3_Transport_layer.asset\demul2.jpg)

그렇지만 같은 포트를 사용하게 되면 다른 소켓으로 demultiplexed 해줘야하므로 관리 오버헤드가 발생한다

각기 다른 app들의 소켓을 관리하는 threaded server를 두면 이문제를 해결?



TCP soket identified by 4-tuple

* source IP : 보내는곳의 주소
* source Port num : 보내는 곳의 앱이 뭔지(소켓번호을 통해서)
* dest IP : 받는 곳의 주소
* dest Port : 어느 앱에서 받을것인지



* * 
