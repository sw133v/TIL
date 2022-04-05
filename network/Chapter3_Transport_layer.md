# 챕터3 전송 계층(Transport Layer)

## services

>  app process 간의 논리적 상호작용

### TCP

> 신뢰성을 갖추고 순서대로 전달하는 방식 

* congestion control - network를 overwahling 하지않는
* flow control - 리시버 버퍼를 overwarming 하지않는
* connection setup
* 

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
