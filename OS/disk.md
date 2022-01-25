## 디스크 스케줄링

seek time의 최소화를 위한것이 목표



* 탐색 시간 Seek time

  헤드를 해당 트랙으로 움직이는데 걸리는 시간

  이게 가장 많은 시간을 소요 => 헤드가 최소로 움직이면 가장 적은 시간을 소요

* 회전 지연 Rotational latency

  헤드가 원하는 섹터에 도달하기까지 걸리는 시간



* 전송 시간 Transfer time

  실제 데이터의 전송 시간



### 주요 알고리즘

* FCFS(First-Come First-Served) 

  굉장히 비효율적인 알고리즘



* SSTF(Shortest Seek Time First)

  현재위치에서 가장 가까운곳 부터 탐색

  기아현상 발생 가능

  

* SCAN 

  헤드는 반복적으로 왔다갔다 하면서 대기열에 헤당 트랙이 있으면 처리

  

   