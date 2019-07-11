## input type="hidden"

input type="hidden"은 숨겨진 input 영역을 정의한다.

주로 사용하는 이유는 http프로토콜의 비연결성 특성 때문이다.
<br><br>
?http프로토콜의 비연결성이란..?<br>
http프로토콜의 비연결성은 클라이언트와 서버가 한 번 연결을 맺은 후
클라이언트 요청에 대해 서버가 응답을 마치면 맺었던 연결을 끊어 버리는 성질을 말한다.

* input type="hidden"
  * 숨겨진 영역은 웹 개발자들이 사용자들이 폼을 제출하였을 때 사용자들이 보거나 수정할 수 없는 데이터들을 포함할 수 있도록 한다. 
  * 숨겨진 영역은 주로 폼이 제출되었을때 업데이트 되어야 할 내용들을 데이터베이스가 기록하는 것을 저장한다.
  * 화면에 출력은 되지 않지만 데이터를 보낼 때 유용하게 사용할 수 있다.
  * 대체적으로 서버에 데이터를 전송할 때 사용
  
[Definition and Usage](https://www.w3schools.com/tags/att_input_type_hidden.asp) <br>
[Http Connectionless](https://victorydntmd.tistory.com/286) <br>
[Example](https://blog.shovelman.dev/818)
