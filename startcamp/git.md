## git(hub)



![image-20220113163759901](git.assets/image-20220113163759901.png)

​																																				**기본적인 순서**

### 기본적인 용어

* #### local

  * 작업 디렉토리(working directory) : 실제 파일이 존재하여 말그대로 작업이 일어나는 공간
    * Untracked : 비추적, 관리x
    * Tracked : 추적 or 관리중
      * Unmodified : 수정하지않아 add, commit를 할필요도 없고 적용 대상도 아님
      * Modified : 수정을 하여 add 및 commit을 할 필요성이 있는 상태
      * Staged : add를 하여 추가적인 add는 할 필요 없이 commit만 하면 되는 상태
  * staging area : Tracked된 상태의 파일들을 관리 및 임시로 저장하는 공간
    * Staged : Tracked상태의 파일들에 git add 명령어를 사용하여 가져지는 상태
    * Unstaged : stage 밖으로 나가진 상태의 파일
  * commits : 코드의 의미있는 변경 작업들을 저장소에 기록하는 곳
    * 

* #### remote

  * commits

* 



###  사용



**처음일시 앞에 `*`가 붙으면 필요한 작업**

1. `*` git init : 새로운 레포지토리 생성후 폴더에서 git을 사용하기 위한 초기화 작업
2. `*` git config --global user.email : 사용자 정보중 email 정보를 저장
3. `*` git config --global user.name : 사용자 정보중 이름 정보를 저장
4. `*` git remote add name : name이라는 이름의 리모트 추가

​	

#### 기본적인 흐름

1. git status : 기본적으로 commit 가능한 상태인지 판단이 가능한 정보 출력
2. git add : commit을 위하여 파일들을 관리하게 만듦(**working directory -> staging area**)
3. git status : 다시한번 확인
4. git commit : 코드의 변화를 기록하는 코드 (**staging area -> commits**)
   * git commit 후 변경사항을 적어넣는 방식 나올때는 :wq 엔터
   * git commit -m "변경 사항" 으로 하는 방식
5. git log : 커밋이 잘 되었는지 알 수 있는 정보 출력



#### 기타

git remote -v : 현재 등록된 리모트 정보

git remote remove 이름 : 존재하는 리모트 제거









