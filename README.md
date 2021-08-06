# python으로 구현한 주민등록번호 유효성 검사기

## 주요기능
### 1. 주요 logic
  - `set_local_name` : 주민등록번호 8 ~ 9번째자리에 해당하는 지역코드를 `if` 조건문으로 정의하는 함수
  - `verify_gender`: 주민등록번호 7번째자리에 해당하는 성별 관련 숫자를 2로 나누었을 때 나누어 떨어지지 않으면 남성, 나누어 떨어지면 여성으로 정의하는 함수
  - `verify_birth_date` : 생년월일 반환 함수
  - `verify_id_number` : 주민등록번호 각 자리수에 대한 가중치를 연산하는 함수
  - `main` : Application의 Body에 해당하는 함수
  
### 2. import한 library
  - `import sys`
  - `from datetime import datetime`

### 3. 순서도는 main branch를 참고하시기 바랍니다.

### 4. 도움을 준 친구
  - hjun-park "Backend Developer"(github "https://github.com/hjun-park")
