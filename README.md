### 들어가기 전 해야 할 설정들

#### putty

> screen -list or screen -ls : 스크린 목록

> screen -r 아이디 : 해당 스크린에 attached(평소에는 detached라고 표시됨)

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
> ![image-20200515124409584](C:\Users\Yusejeong\AppData\Roaming\Typora\typora-user-images\image-20200515124409584.png)

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

