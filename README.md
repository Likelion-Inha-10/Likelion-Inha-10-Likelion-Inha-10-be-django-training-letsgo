## API 명세서
![image](https://user-images.githubusercontent.com/103047410/176361405-2109d3c6-b07b-4631-aeeb-f71d080c78dc.png)

## DB 도식화
![image](https://user-images.githubusercontent.com/103047410/176361602-fa69091f-b1f7-4d9b-ae5a-2238e93ad4aa.png)

## 회고
1. 파이썬은 대소문자를 구분한다. <br/>
이로 인해 자주 오류를 범하게 되니 항상 신경써야한다.<br/>
A(대문자)에는 상수 를, a(소문자) 는 변수 를 넣어준다<br/>
A = request.POST['']  X
a = request.POST['']  O

2. 현재 로그인한 사용자가 누군지 알아냈어야 했는데 request.user를 통해 해결이 가능했다
