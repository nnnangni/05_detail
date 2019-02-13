### 05_detail project



#### 1. Django Setting

1. Django 프로젝트를 생성
2. detail 이라는 이름의 앱을 생성
3. django 설정 중 언어 를 한국어로 설정
4. ALLOWED_HOSTS 설정에 "*" 를 추가

#### 2. base.html 구성

1. Bootstrap css,js 를 추가
2. <3.페이지 구성> 에 들어가는 링크들이 모두 들어있는 Nav Bar 를 구성
3. MySite를 클릭하면 / 로 이동
4. Q&A를 클릭하면 qna/ 로 이동
5. Mypage를 클릭하면 mypage/ 로 이동
6. SignUp을 클릭하면 signup/ 으로 이동
7. 링크위치정렬
8. favicon 을 추가

#### 3. 페이지 구성

<3.페이지 구성> 에서 사용하는 html 파일들은 base.html 을 extends

1. /
  시맨틱 태그 header 와 footer 를 사용하여 페이지를 구성
  1. Header
    Navigation Bar 바로 아래에 위치
    높이는 350px , 너비는 브라우저 전체 영역
    배경 이미지 설정
    Header 영역의 수직/수평 가운데 정렬 위치 에 h1 태그를 사용하여 작성
  2. Footer
    브라우저 최하단에 위치
    높이는 50px 이상, 너비는 브라우저 전체 영역
    왼쪽에는 닉네임, 오른쪽에는 헤더로 올라가는 링크

2. signup/
  회원가입페이지
  이메일, 이름, 비밀번호, 비밀번호 확인 을 위한 input tag를 사용
  Bootstrap Grid System 을 사용하여 화면 좌측엔 이미지, 우측엔 데이터를 입력할 폼을
  보여줌.

3. mypage/
  유저 정보를 출력하는 페이지
  사용자의 개인정보와 작성 글을 보여줄 페이지
  화면 좌측엔 사용자의 정보, 우측엔 사용자가 작성한 글 목록을 보여줌.
  이미지는 장고 프로젝트 내부의 이미지를 스태틱으로 적용
  사용자의 정보를 보여주는 Card는 .position-fixed 를 사용

4. qna/
  사용자의 질문을 받기 위한 페이지
  Bootstrap Form 을 사용
  제목, 이메일, 내용 을 위한 input tag를 사용

5. <str:not_found>/
  위에서 만든 경로를 제외한 다른 요청이 들어오면 보여줄 404페이지
  variable routing 을 활용하여 사용자가 잘못 입력한 경로를 잘못된 경로라고 표시