## DeadLock

![image-20220219151537171](.\DeadLock\image-20220219151537171.png)

![image-20220219151958191](.\DeadLock\image-20220219151958191.png)

### **데드락의 발생조건**

> 밑에 모든 조건을 만족해야함

* Mutual Exclusion (상호 배제)

  매 순간 하나의 프로세스만이 자원을 사용가능

* No preemption (비선점)

  프로세스는 자원을 스스로 내어높을  뿐 강제로 빼앗기지 않음

* Hold and wait 

  자원을 가진 프로세스가 다른 자원을 기다릴 때 보유 자원을 놓지 않고 계속해서 가지고 있는것

* Circular wait (환영 대기)

  자원을 기다리는 프로세스간에 사이클이 형성되어야함

  

### **데드락 처리방법**

* Deadlock Prevention

  > 자원 할당시 Deadlock의 4가지 필요 조건 중 어느 하나가 만족 되지 않도록 하는것

  * mutual exclusion

    공유해서는 안되는 자원의 경우 반드시 성립

    

  * hold and wait

    프로세스가 자원을 요철할 때 다른 어떤 자원도 가지고 있지 않아야 한다

    방법1 : 프로세스 시작 시 모든 필요한 자원을 할당 받게 하는방법

    방법2 : 자원이 필요한 경우 보유 자원을 모두 놓고 다시 요청

    

  * No Preemption

    process가 어떤 자원을 기다려야 하는 경우 이미 보유한 자원이 선점됨

    모든 필요한 자원을 얻을 수 있을 때 그 프로세스는 다시 시작된다

    state를 쉽게 save 하고 restore할 수 있는 자원에서 주로 사용한다(cpu, memory)

    

  * Circular Wait

    모든 자원 유형에 할당 순서를 정하여 정해진 순서대로만 자원 할당

    예를 들어 순서가 3인 자원을 R_i를 보유 중인 프로세스가 순서가 1인 자원R_j를 할당받기 위해서는 우선 R_i를 release 해야한다.

  → Utiliztion(자원의 이용률) 저하, throughput 감소, starvation 문제 발생 



* Deadlock Avoidance

  > 자원 요청에 대한 부가적인 정보를 이용해서 deadlock의 가능성이 없는 경우에만
  >
  > 자원을 할당
  >
  > 시스템 state가 원래 state로 돌아올 수 있는 경우에만 할당

  Deadlock Prevention과 비슷해 보이지만 state라는 추가정보를 이용하는것이 차이점

  자원 요청에 대한 부가정보르 이용해서 자원 할당이 deadlock로 부터 안전한지를 동적으로 조사해서 안전한 경우에만 할당

  가장 단순하고 일반적인 모델은 프로세스들이 필요로 하는 각 자원별 **최대 사용량**을 미리 선언하도록 하는 방법 - (최대 사용량을 안다는 가정하에)

  * safe state - 시스템 내의 프로세스들에 대한 safe sequence가 존재하는 상태

  * safe sequence

    프로세스의 시퀀스<P_1 ....P_n>이 safe 하려면 P_i(1<=i<=n)의 자원 요청이 가용자원 + 모드P_j(j<i)의 보유자원 에의해 충족 되야함

    조건을 만족하면 다음 방법으로 모든 프로세스의 수행을 보장

  ex) banker's 알고리즘

![image-20220219170024473](.\DeadLock\image-20220219170024473.png)

banker's 알고리즘은 safe state를 유지하기 위해  

 현재 가용자원(Available)이 Need(점선)보다 클 경우에만 자원을 할당!



* Deadlock Detection and recovery

  > Deadlock발생은 허용하되 그에 대한 detection 루틴을 두어 deadlock 발견시 recover

  * Deadlock detection

    * 자원당 인스턴스가 하나인경우 그래프를 통해서

      ![image-20220219183748003](.\DeadLock\image-20220219183748003.png)

    * 자원당 인스턴스가 여러개면 banker's 알고리즘 처럼

      ![image-20220219184123300](.\DeadLock\image-20220219184123300.png)

      자원을 요구하면 계산할 필요 없이 그냥 주고

      나중에 데드락이 생겼는지 판단

  * Recovery

    * Process Termination

      1. 모든 프로세스들을 죽이는 방법
      2. 프로세스들을 하나씩 죽이면서 확인하는 방법

    * Resource Preemption

      비용을 최소화할 victim의 선정

      ​	safe state로 rollback, process를 restart

      기아 현성을 대비해서

      계속 동일한 프로세스가 victim으로 선정될 경우 cost factor에 rollback 횟수도 같이 고려



* Deadlock Ignorance

  > Deadlock을 시스템이 책임지지 않음
  >
  > UNIX를 포함한 대부분의 OS가 채택

  생기면 사람이 죽이는 형태로 조치 ㅋㅋ



#### Resource-Allocation Graph (자원 할당 그래프)

 ![image-20220219154343585](.\DeadLock\image-20220219154343585.png)

사각형 - 자원

동그라미 - 프로세스



![image-20220219161957627](.\DeadLock\image-20220219161957627.png)

실선 - 자원을 선점하고 있다는 개념

점선 - 프로세스가 해당 자원의 사용 가능성이 있다는 개념 

화살표 방향 

R->P : p가 R을 선점하고 있다는 개념

P->R : p가 R을 요청했다는 개념

프로세스가 자원을 요청하면 실선이되는것

맨 오른쪽 상태에서 P1이 R2를 요청하면 데드락 발생

avoidance는 2번 그림에서 P2에게 R2를 주지않게끔 하는것

![image-20220219170628392](.\DeadLock\image-20220219170628392.png)

  





