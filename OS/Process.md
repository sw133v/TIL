### 프로세스 관리

> 프로세스의 개념 : 실행중인 프로그램

프로세스의 문맥(context)

* cpu의 수행상태를 나타내는 하드웨어 문맥()
  * Program Counter - 어디 까지 수행 되었는지
  * 각종 register - 연산에 필요한 정보가 저장된곳
* 프로세스의 주소 공간
  * code, data, stack
* 프로세스 관련 커널 자료 구조
  * PCB(Process Control Block)
  * Kernel stack

![image-20220201143532164](C:\Users\sw133\AppData\Roaming\Typora\typora-user-images\image-20220201143532164.png)

여기서 PC는 CPU의 PC (저장할 정보)

PCB내의 PC는 커널 메모리의 안의 PC (저장된 정보)



### 프로세스의 상태

#### 상태

* Running

  * CPU를 잡고 기계어를 수행중인 상태

* Ready

  * CPU를 기다리는 상태(메모리 등 다른 조건을 모두 만족한)

* Blocked (wait, seleep)

  * CPU를 받아도 당장 기계어를 수행할 수 없는 상태

  * Process 자신이 요청한 event(I/O처리와 같은)가 처리 되지않아 기다리는 상태

    ex:) 디스크에서 파일을 읽어 와야하는 경우

  * 혹은 큐에서 대기하고 있는 상태

* New 
  * 프로세스가 생성중인 상태
* Terminated 
  * 수행이 끝난 상태(덜 지워진 상태)

![image-20220201151118691](C:\Users\sw133\AppData\Roaming\Typora\typora-user-images\image-20220201151118691.png)



![image-20220201151422971](C:\Users\sw133\AppData\Roaming\Typora\typora-user-images\image-20220201151422971.png)

![image-20220201152715304](C:\Users\sw133\AppData\Roaming\Typora\typora-user-images\image-20220201152715304.png)







### PCB ( Process Control Block)

> 운영체제가 각 프로세스를 관리하기 위해 프로세스당 유지하는 정보

구성 요소

* 1)OS가 관리상 사용하는 정보
  * process state, process ID
  * scheduling information, priority



* 2)CPU 수행 관련 하드웨어 값

  * program counter, registers

    

*  3)메모리 관련

  * code, data, stack의 위치 정보

    

* 4)파일 관련

  * open file descriptors

![image-20220201153154007](C:\Users\sw133\AppData\Roaming\Typora\typora-user-images\image-20220201153154007.png)



### 문맥 교환

> CPU를 한 프로세스에서 다른 프로세스로 넘겨주는 과정
>
> CPU가 다른 프로세스에게 넘어갈 때 운영체제는 다음 과정을 수행

* CPU를 내주는 프로세스의 상태를 그 프로세스의 PCB에 저장
* CPU를 새롭게 얻는 프로세스의 상태를 PCB에서 읽어옴

![image-20220201154103215](C:\Users\sw133\AppData\Roaming\Typora\typora-user-images\image-20220201154103215.png)

#### **주의점** 

 ![image-20220201154216681](C:\Users\sw133\AppData\Roaming\Typora\typora-user-images\image-20220201154216681.png)

1번경우 문맥 교환이 아님 

문맥교환은 PCB정보가 다른 프로세스가 들어올떄 일어남 

2번경우 기존 캐시데이터들이 의미가 없기때문에 cache memory flush(싹다 날리는거)가 일어나고 오버헤드가 큰작업



### 프로세스를 스케줄링하기위한 큐

> 프로세스들은 각 큐들을 오가며 수행된다.

* job 큐

  현재 시스템 내에 있는 모든 프로세스의 집합

  

* ready 큐

  현재 메모리 내에 있으면서 CPU를 잡아서 실행되기를 기다리는 프로세스의 집합

  

* device 큐s

  I/O 디바이스의 처리를 기다리는 프로세스의 집합



![image-20220201155249705](C:\Users\sw133\AppData\Roaming\Typora\typora-user-images\image-20220201155249705.png)



![image-20220201155310864](C:\Users\sw133\AppData\Roaming\Typora\typora-user-images\image-20220201155310864.png)

큐의 예시



### 스케줄러

* Long-term scheduler(장기 혹은 job 스케쥴러)

  * 시작 프로세스 중 어떤 것들을 ready 큐에 보낼지 결정

  * new 에서 ready로 가는 admit을 해주는 스케줄러

  * 프로세스에 메모리 및 각종 자원을 주는 문제

  * degree of multiprogramming(메모리에 올라가있는 프로그램수)을 제어

  * **시분할 시스템OS에서는 보통 장기스케줄러가 없고 ready에서 시작됨**

    

* Short-term scheduler(단기 혹은 CPU 스케쥴러)

  * 어떤 프로세스를 다음번에 running 시킬지 결정

  * 프로세스에 CPU를 주는 문제

  * 충분히 빨라야함(ms 단위)

     

* Medium-term scheduler(중기 혹은 Swapper)

  * 여유 공간 마련을 위해 프로세스를 통째로 메모리에서 디스크로 쫓아냄

  * 프로세스에게서 메모리를 뺏는 문제

  * degree of multiprogramming을 제어

  * 이 스케줄러가 들어가면서 추가되는 프로세스의 상태

    * Suspended(stopped)

      외부적인 이유로 프로세스의 수행이 정지된 상태

      프로세스는 통째로 디스크에 sawp out 된다

      ex) 사용자가 프로그램을 일시 정지시킨 경우(break key)

      시스템이 여러이유로 프로세스를 잠시 중단시킨경우

      (메모리에 너무 많은 프로세스가 올라와 있을 때)

      

` blocked : 자신이 요청한 event가 만족되면 Ready 상태로 

` Suspended : 외부에서 resume해 주어야 Active

![image-20220201165429253](C:\Users\sw133\AppData\Roaming\Typora\typora-user-images\image-20220201165429253.png)

suspended 상태는 메모리에 할당되어있지않은 상태

메모리를 할당받는걸 swap in, 빼앗기는걸 swap out이라고 함



러닝(모드에따른 )의 차이

* 러닝 user mode

  * 프로세스가 자기 코드를 수행중일 경우에 지칭

* 러닝 moniutor mode

  * 프로세스가 본인 코드 이외의 코드를 수행중일 경우 CPU를 빼앗긴게 아니라 처리 요청을해 양도를 한경우

    ex:시스템 콜, 트랩 등

  * 혹은 타이머 인터럽트가 아닌 다른 디바이스 컨트롤러에게 인터럽트를 받은경우

    ex: 현재 프로그램A가 실행 될때 프로그램B가 요청한 데이터가 처리되어 인터럽트를 받아 OS가 cpu를 받는경우



### 특이사항

I/O는 트랩, 인터럽트 모두 해당됨

CPU가 디바이스 컨트롤러에게 요청 하는것 (트랩)

디바이스 컨트롤러가 CPU에게 수행이 끝났음을 알림(인터럽트)





![image-20220201141647737](C:\Users\sw133\AppData\Roaming\Typora\typora-user-images\image-20220201141647737.png)

실행전 프로그램 (실행파일), 실행중인 프로그램(프로세스)

실행에 당장 필요한부분 -> 메모리

당장은 필요없는 부분 -> 스왑 에어리어



![image-20220201142731489](C:\Users\sw133\AppData\Roaming\Typora\typora-user-images\image-20220201142731489.png)



#### 가상메모리 구성

* ㄴ코드 : 실행 파일의 cpu가 수행할 명령어 모음

  * 시스템콜, 인터럽트 처리코드

  * 자원 관리를 위한 코드

  * 편리한 서비스 제공을 위한 코드

    

* 데이터 : 프로그램이 필요한 전역변수적인 데이터 모음, 즉 프로그램이 죽기전까지 남아있음

  *  모든 하드웨어 들을 관리하기 위한 자료구조,

  *  모든 소프트웨어들을 관리하기 위한 자료구조(PCB) 

    

* 스택 : 함수안에서 쓰는 지역적인 데이터 모음, 그때그때 모았다가 그때그때 없앰

  * 각 프로세스당 각각 커널 스택(커널 함수를 사용하기위한)을 가짐





![image-20220201143006226](C:\Users\sw133\AppData\Roaming\Typora\typora-user-images\image-20220201143006226.png)

사용자 프로그램이 사용하는 함수

* 사용자 정의 함수
  * 사용자가 프로그램에서 정의한 함수
* 라이브러리 함수
  * 사용자가 프로그램에서 정의하지 않고 갖다 쓴 함수
  * 자신의 프로그램의 실행 파일에 포함됨
* 커널 함수
  * 운영체제 프로그램의 함수
  * 커널 함수의 호출 = 시스템 콜



![image-20220201143224803](C:\Users\sw133\AppData\Roaming\Typora\typora-user-images\image-20220201143224803.png)





### Thread

> CPU의 수행단위
>
> 프로세스를 여러개 만들면(여러개의 주소공간, 여러개의 pcb) 비효율적.
>
> 프로세스를 여러개 두더라도 주소공간을 한군데로 두는개념

구성

* PC(program counter)
* register set
* satck space

thread 가 동료 thread와 공유하는 부분(= task)

* code section
* data section
* OS resources

-- 전통적인 개념의 heavyweight process는 하나의 쓰레드를 가지고 있는 task로 볼 수 있다



장점 

* 다중 스레드로 구성된 태스크 구조에서는 하나의 서버 스레드가 blocked(waiting)상태인 동안에도 동일한 태스크 내의 다른 스레드가 실행(running)되어 빠른 처리를 할 수 있다.
* 동일한 일을 수행하는 다중 스레드가 협력하여 높은 처리율(throughtput)과 성능 향상을 얻을 수 있다
* 스레드를 사용하면 병렬성을 높일 수 있다



간략화

* Responsiveness - 높은 응답성
* Resource Sharing - 자원 공유가능
* Economy - 경제성
* Utiliztion of MP Architectures - 병렬성을 추구가능 



구현방법

* 운영체제가 쓰레드를 지원할 경우

  > --> 커널 - 커널 쓰레드

  * windows 유닉스 등등

* 운영체제가 쓰레드를 지원하지 않는 경우

  > --> 라이브러리 - user 쓰레드

  * posix p쓰레드
  * mach C-쓰레드
  * 솔라리스 쓰레드

  



![image-20220201202036865](C:\Users\sw133\AppData\Roaming\Typora\typora-user-images\image-20220201202036865.png)



![image-20220201202051173](C:\Users\sw133\AppData\Roaming\Typora\typora-user-images\image-20220201202051173.png)

 

![image-20220201173446379](C:\Users\sw133\AppData\Roaming\Typora\typora-user-images\image-20220201173446379.png)

↓

![image-20220201172723012](C:\Users\sw133\AppData\Roaming\Typora\typora-user-images\image-20220201172723012.png)



### 프로세스 생성

> 부모 프로세스가 자식 프로세스를 생성(직접은 불가능)
>
> OS한테 요청(시스템 콜)하여 생성
>
> 사실상 별개의 프로세스  

* 프로세스의 트리(계층 구조)형성
* 프로세스는 자원을 필요로함
  * 운영체제로 부터 할당 받는 경우
  * 부모와 공유하는 경우
* 자원의 공유
  * 부모와 자식이 모든 자원을 공유하는 모델
  * 일부를 공유하는 모델
  * 전혀 공유하지 않는 모델
* 수행
  * 부모와 자식이 공존하며 수행하는 모델
  * 자식이 종료(terminate)될 때 까지 부모가 기다리는(wait) 모델

* 주소 공간

  * 자식은 부모의 공간을 복사함(binary and OS data)
  * 자식은 그 공간에 새로운 프로그램을 올림

* 유닉스의 예

  * fork() - 복제 생성 

    > 시스템 콜이 새로운 프로세스를 생성

    * 부모를 그대로 복사 (OS data except PID + binary)
    * 주소 공간 할당

  * exec() - 메모리 할당

    > 새로운 프로그램을 메모리에 올림
    >
    > 사실상 부모와 다른 태스크를 진행시키기 위해 fork 후 사용

​	

### 프로세스 종료

* exit - 프로세스가 마지막 명령을 수행한 후 OS에게 이를 알려줌

  * via **wait**자식이 부모에게 output data를 보냄
  * 프로세스의 각종 자원들이 OS에게 반납됨

* abort - 부모 프로세스가 자식의 수행을 종료시킴

  * 자식이 할당 자원의 한계치를 넘어섬

  * 자식에게 할당된 태스크가 더 이상 필요하지 않음

  * 부모가 종료(exit)하는 경우

    > 부모에게 exit가 와도 자식먼저 종료후 부모가 마지막으로 종료

    * OS는 부모가 죽으면 자식이 활동하는것을 두지 않음
    * 단계적인 종료

![image-20220202151443988](C:\Users\sw133\AppData\Roaming\Typora\typora-user-images\image-20220202151443988.png)

부모와 자식의 구분하는 방법

부모의 경우 양수를 리턴 시키고 

자식의 경우 0을 리턴시킴





![image-20220202151902663](C:\Users\sw133\AppData\Roaming\Typora\typora-user-images\image-20220202151902663.png)    







