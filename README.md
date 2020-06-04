
### 개요

> 우리는 종종 메뉴를 선택할 때 개인의 취향과 식성에 따른 불편함을 겪는다. 타인과 함께 식사를 하게 될 때에는 타인의 식성까지 고려해야 하기 때문에 메뉴 선택 시간이 더욱 길어진다. 이러한 불편함을 해소해주기 위해 이를 메뉴 추천 웹으로 만들어 해결하였다. 

### 주요 기능

1. 개인 맞춤형 메뉴 추천

   > 회원가입 시 입력받은 사용자의 정보를 기반으로 추천 알고리즘을 사용하여 메뉴를 추천해주는 기능이다. 무작위 추천이 아닌 협업 필터링 알고리즘과 컨텐츠 기반 알고리즘을 이용하여 신빙성 있는 추천을 한다. 메뉴 추천 뿐만 아니라 사용자의 현재 위치 정보를 받아 주변의 해당 메뉴 판매 식당 위치 및 간단한 정보까지 사용자에게 알려준다.

2. 그룹 메뉴 추천

   >식사를 같이 할 친구를 추가하게 되면 사용자와 상대방의 정보까지 고려하여 여러 명의 취향 및 선호를 만족시키는 메뉴를 추천해주는 기능이다. 먼저, 마이페이지의 친구 목록 화면에서 수동검색 필터에 타인의 이름을 검색한 후, 특정 친구를 추가해야 한다. 그 후, 그룹 메뉴 추천 기능에서 식사를 같이 할 친구를 추가하면 해당 기능을 쉽게 이용할 수 있다. 

### 알고리즘

* 협업 필터링 알고리즘

  > 유사한 성향들을 가진 사람들을 구분하고, 해당 성향의 사람들이 좋아하는 것을 이용하여 추천해주는 방법이다. 

* 컨텐츠 기반 필터링 알고리즘

  > 항목 자체를 분석한 결과를 기반으로 추천하는 방법이다. 예를 들어, 영화 컨텐츠의 경우라면 스토리나 등장인물을, 상품이라면 상세 페이지의 상품 설명을 분석한다. 항목을 분석한 프로필과 사용자의 선호도를 분석한 프로필을 추출해 유사성을 계산한다. 

### 개발 환경

* Language : Python, JavaScript, CSS, HTML
* Framework : Django
* Library : Jquery
* Cloud Server : AWS EC2
* OS : Ubuntu 14.1
* DB : AWS RDS
* Web Server : Nginx


### 들어가기 전 해야 할 설정들

#### putty

* 스크린 설치

  ```bash
  $ sudo apt-get install screen
  ```

* 스크린 만들기

  ```bash
  $ screen -S build1
  ```
  
* 스크린 목록 보기

  ```bash
  $ screen -list 
  $ screen -ls
  ```

* 스크린 실행

  > 해당 스크린에 attached(평소에는 detached라고 표시된다.)

  ```bash
  $ screen -r 아이디
  ```

  

> python manage.py runserver를 했을 떄 zsh :  command not found 에러가 뜬다면 가상환경을 설정해 줘야함.

> source venv/bin/activate : 가상환경 설정
>
> 해당 프로젝트에 들어가서 python manage.py runserver 0:8000 실행

> python manage.py makemigrations를 했을 때 에러가 뜨거나 작동하지 않는다면 인스턴스의 보안 그룹을 다시 생성 후 RDS 인스턴스를 해당 보안 그룹과 다시 연결
>
> 이 때, 인바운드 규칙은 
>
> 유형 : PostgreSQL 
>
> 포트 범위 : RDS를 만들 때 적었던 포트 이름 
>
> 소스 :  내IP 추가 
>
> 그 후, 아래 포트들도 추가
>
> ![image-20200515124409584](image-20200515124409584.png)

> makemigrations를 성공적으로 수행했다면, python manage.py migrate 실행
>
> 이 때, 에러가 뜬다면 python manage.py --fake 앱이름 실행

> DB반영이 끝났으므로 python manage.py runserver 8000 실행 후, ec2 인스턴스의 public ip로 접속 ex) http://12.12.12.12:8000
>
> 위 주소로 접속이 안되는 경우는 127.0.0.1은 localhost주소이고, 이는 서버 내부에서만 접근할 수 있는 주소이기 때문이므로 runserver를 종료시키고 다음과 같이 다시 입력한다.
>
> python manage.py runserver 0:8000
>
> 이 때, port already in user라는 에러가 뜨게 된다면, 
>
> ```python
> >netstat -ntlp
> 
> Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
> tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -
> tcp        0      0 127.0.0.1:8000          0.0.0.0:*               LISTEN      6810/python
> tcp6       0      0 :::22                   :::*                    LISTEN  
> ```
>
> ```python
> > kill -9 PID
> #여기서는 kill -9 6810
> ```
>
> 


