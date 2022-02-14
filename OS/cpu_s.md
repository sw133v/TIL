## CPU 스케쥴링



### 프로세스와 관련된 시스템 콜(복습의 느낌)

- fork() - 자식 프로세스 생성(copy 부모와 똑같은 프로세스)
- exec() - 새로운 작업을 하게끔 덮어씀
- wait() - 자식이 일을 다 할 때 까지 일을 멈춤
- exit() - 해당 프로세스에 할당된 모든 자원(cpu 나 메모리등)을 회수

### 프로세스간 협력

- 독립적 프로세스(Independent process)

  프로세스는 각자의 주소 공간을 가지고 수행되므로 원칙적으로 하나의 프로세스는 다른 프로세스의 수행에 영향이 없음

- 협력 프로세스(Cooperation process)

  프로세스 협력 메커니즘을 통해 하나의 프로세스가 다른 프로세스의 수행에 영향을 미칠 수 있음

- 프로세스간 협력 메커니즘(IPC : Interprocess Communication)

  - 메시지를 전달하는 방법
    - Message passing : 커널을 통해 메시지 전달
  - 주소 공간을 공유하는 방법
    - Shared memory : 서로 다른 프로세스 간에도 일부 주소 공간을 공유 하게 하는 shared momory 메커니즘이 있음
    - Thread : 쓰레드는 사실상 하나의 프로세스 이므로 프로세스 간 협력으로 보기는 어렵지만 동일한 프로세스를 구성하는 쓰레드들 간에는 주소 공간을 공유하므로 협력 가능

### Message Passing

- Message system

  프로세스 사이에 공유 변수(shared variable)를 일체 사용하지 않고 통신하는 시스템![메시지 패싱](\asset\message_passing.png)

  

- Direct Communication

  통신하려는 프로세스의 이름을 명시적으로 표시

  ![메시지 패싱2](\asset\direct.png)

- Indirect Communication

  mailbox(또는 prot)를 통해 메시지를 간접 전달

  ![indirect](\asset\indirect.png)

### Shared Memory

> 서로 신뢰성이 높은 프로세스들 끼리만 공유

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b7f33d5f-5a7c-49e1-a025-24f86cf9afdd/Untitled.png)

### 프로세스의 일생

- CPU burst : CPU로 기계어를 실행하는 단계
- I/O burst : I/O를 기다리는 단계

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0329ce6a-ca5f-4b8f-89bd-cc48f95be226/Untitled.png)

### CPU burst 예측

> 오로지 추정만이 가능함

- how?

  (input data, branch, user...)

- 과거의 cpu burst time을 이용해서 추정 (exponetial averaging)

  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c0dd13b9-7ab2-4c19-95b8-9cf25936e8bf/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8f46f691-4376-4579-af0b-c3d6add26f19/Untitled.png)

### 프로세스의 특성 분류

- I/O-bound process
  - CPU를 잡고 계산하는 시간보다 I/O에 많은 시간이 필요한 job
  - many short CPU bursts
- CPU-bound process
  - 계산 위주의 job
  - few very long CPU bursts

### CPU 스케줄러 & Dispatcher

> 둘다 소프트웨어의 개념,
>
> 프로세스 보단 OS에 가까운 개념

- CPU 스케줄러

  - Ready 상태의 프로세스 중에서 이번에 CPU를 줄 프로세스를 고름

- Dispatcher

  - CPU의 제어권을 CPU 스케줄러에 의해 선택된 프로세스에게 넘긴다.

  - 그 과정을 context switch(문맥 교환)이라고 함.

    PCB나 그런작업을 저장하고 다른 프로세스 PCB를 받아올때 발생하는 것이 문맥교환(인듯?)

### CPU 스케줄링이 필요한 경우

> **n** = Nonpreemptive(자진 반납), **p** = Preemptive(강탈)

1. (**n)** Running → Blocked (ex : i/o 요청하는 시스템 콜)
2. (**p)** Running → Ready (ex : 할당시간 만료로 타이머 인터럽트)
3. (**p)** Blocked → Ready (ex : I/O 완료후 인터럽트)
4. (**n)** Terminate

### CPU 스케줄링의 성능 척도(다양한 영어로 불림)

> **h** - 높을 수록 좋음, **L** - 낮을 수록 좋음

- (**h)** CPU utilization (이용률)

  > 전체 시간중 CPU가 놀지 않고 일한 비율

- (**h)** Throughput (처리량)

  > 시간당 CPU가 처리한 작업의 양

- (**L)** Turnaround time (소요 시간, 반환 시간)

  > 프로세스가 실행에 소요한 양

- (**L)** Waiting time (대기 시간)

  > 큐에서 프로세스가 기다린 시간 총량

- (**L)** Response time (응답 시간)

  > 최초로 CPU를 쓰려고 들어와서 CPU를 쓰기까지의 시간

### 스케줄링 알고리즘

> **n** = Nonpreemptive(자진 반납), **p** = Preemptive(강탈)

- **FCFS** (First-Come First-Served) - **n**

  작업 시간이 긴 process가 앞에 오면 뒤의 짧은 process들의 대기 시간이 길어짐 → convoy effect

- **SJF** (Shortest-Job-First) - **n, p**

  > 각 프로세스의 다음번 cpu burst time을 가지고 스케줄링에 활용
  >
  > cpu burst time이 가장 짧은 프로세스를 제일 먼저 스케줄

  대기 시간의 평균으로만 보면 최적의 알고리즘

  - **n -** 작업 도중에 짧은 포로세스가 들어와도 cpu를 빼앗지 않는 방법
  - **p -** 작업 도중에 짧은 포로세스가 들어오면 cpu를 빼앗는 방법 (이 방법이 SRTF)

  문제점

  - 긴 프로세스는 영영 cpu를 못 얻는 기아 현상이 생김

- **SRTF** (Shortest-Remaining-Time-First)

- **Priority Scheduling** - **n, p**

  > 높은 우선순위를 가진 프로세스에게 CPU 할당

  - SJF 도 작업시간이 짧은 프로세스를 우선적으로 처리를 하기 때문에

    일종의 priority scheduling 이다.

  문제점

  - 우선 순위가 낮은 프로세스는 영영 cpu를 못 얻는 기아 현상이 생김

  해결법

  - aging : 기다린 시간 만큼 우선순위를 조금식 높이는 방식

- **RR** (Round Robin) - **p**

  주로 사용하는 방식 (앞선 알고리즘에 비해 형평성이 좋음.)

  > 각 프로세스를 동일한 크기의 할당 시간(quantum)을 가짐 - 일반적으로 10-100ms
  >
  > 할당 시간이 지나면 프로세스는 ready 큐 제일 뒤에 가서 다시 줄을 섬

  - 할당 시간 크기의 차이

    - 할당 시간이 지나치게 긴 경우 - FCFS 방식처럼 동작
    - 할당 시간이 지나치게 짧은 경우 - context switch가 빈번히 발생한다 (오버헤드가 커진다

  - 일반적으로 SJF 보다 평균 반환 시간(average turnaround time)이 길지만

    응답 시간(response time)은 더 짧다

- **Multilevel Queue -**

  > Ready queue를 여러 개로 분할 ****

  - foreground(interactive)
  - background (batch - no human interaction)

  > 각 큐는 독립적인 스케줄링 알고리즘을 가짐

  - foreground - RR
  - background - FCFS

  > 큐에 대한 스케줄링이 필요

  - FIxed priority scheduling
    - 백그라운드 큐는 모든 포그라운드 큐 작업이 끝난 후 실행
    - 기아 현상이 발생 가능
  - time slice
    - 각 큐에 cpu time을 적ㅈ절한 비율로 할당
    - ex) 80% 포그라운드, 20% 백그라운드

- **Multilevel Feedback Queue -**

  > 프로세스들의 큐(우선 순위)가 바뀌는 형식
  >
  > ageing 을 이와 같은 방식으로 구현 가능

  주요 파라미터들

  - Queue의 갯수
  - 각 큐들의 알고리즘
  - 프로세스를 상위 큐로 보내는 기준
  - 프로세스를 하위 큐로 보내는 기준
  - 프로세스가 CPU서비스를 받으려 할 때 들어갈 큐를 결정하는 기준

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c8e43a96-25ae-4bba-bd52-06a3f59e8a05/Untitled.png)

멀티레벨 피드백 큐 방식의 예시

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/67b06f72-8728-4c39-85c6-55e0dfd7d346/Untitled.png)

### Multiple-Processor Scheduling

> CPU가 여러 개인 경우 스케줄링은 더욱 복잡해짐

- Homogeneous Processor
  - 큐에 한줄로 세워서 각 프로세서가 알아서 꺼내가게 할 수 있다
  - 반드시 특정 프로세서에서 수행되어야 하는 프로세스가 있는 경우에는 문제가 더 복잡해짐
- Load Sharing
  - 일부 프로세서에서  job이 몰리지 않도록 부하를 적절히 공유하는 메커니즘 필요
  - 별개의 큐를 두는 방법 vs. 공동 큐를 사용하는 방법
- Symmetric Multiprocessing (SMP)
  - 각 프로세서가 각자 알아서 스케줄링 결정
- Asymmetric Multiprocessing
  - 하나의 프로세서가 시스템 데이터의 접근과 공유를 책임지고 나머지 프로세서는 거기에 따름

### **Real-Time Scheduling**

- deadline이 추가로 붙어서 이를 만족시키는 것이 중요
- Hard real-time systems :
  - Hard real-time task는 정해진 시간 안에 반드시 끝내도록 스케줄링해야 함
  - 오프라인으로 미리 스케줄링을 시켜놓고 따라가게하는 경우도 많다
- Soft real-time systems :
  - Soft real-time task는 일반 프로세스에 비해 높은 priority를 갖도록 해야함
  - 주기적으로 일해야하는 경우가 많다
  - deadline을 지키는 것이 중요하지만 반드시 보장하지 않을 수 있다

### **Thread Scheduling**

- Local Scheduling : User level thread의 경우 사용자 수준의 thread library에 의해 어떤 thread를 스케줄할지 결정
- Global Scheduling : kernel level thread의 경우 일반 프로세스와 마찬가지로 커널의 단기 스케줄러가 어떤 thread를 스케줄할지 결정

### 스케줄링 알고리즘 평가 방법

![image-20220206220225382.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/694b46a4-3879-4e22-924e-084ed63a47a9/image-20220206220225382.png)

- Queueing models : 대단히 이론적인 방법, job의 도착율과 cpu처리율이 확률분포로 주어진다
- 실제 구현은 대단히 어려워서 Simulation을 사용하기도 한다
- trace : Simulation에서 input이 되는 데이터(실제 포로그램에서 뽑아서 사용 혹은 임의로 만들어서 사용)



* #### Queueing models

  > 확률 분포로 주어지는 arrival rate와 service rate 등을 통해 각종 
  >
  > perfomance index값을 계산

* #### Implementation(구현) & Measurement(성능 측정)

  > 실제 시스템에 알고리즘을 구현하여 실제 작업(workload)에 대해서
  >
  > 성능을 측정 비교

  이 방법은 알고리즘을 사용해봤을때 오류가 있으면 시스템이 멈춰서 디버깅이 쉽지안흥ㅁ

  이 방법의 대안이 simulation 방식임 

* #### Simulation(모의 실험)

  > 알고리즘을 모의 프로그램으로 작성후 trace를 입력으로 하여 결과 비교



