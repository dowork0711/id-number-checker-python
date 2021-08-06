# 컴퓨팅적 사고력 기말고사 과제
# 사범대학 일어교육과 20151314 황두일

## 도입
print(f"**************************** 주민등록번호(Identify Number) 유효성 검사 도구 Ver.1.0. ***************************")
print(f"이 검사 도구의 저작권은 제작자에게 있습니다. \n검사 도구 사용간 주민등록번호가 저장되지 않으며 프로그램 종료시 바로 폐기됩니다.")
print(f"이 검사 도구에 입력한 주민등록번호를 통해 생년월일, 성별, 출생지역, 주민등록번호의 유효성을 파악할 수 있습니다.")
print(f"*"*112)
input("계속 진행 하시려면 Enter키를 누르십시오.")

## 시스템 종료 exit 사용하기 위해서 import
import sys

## datetime 모듈에 있는 모든 것을 가져오기
from datetime import datetime

## 특정 자리값의 지역코드 범위 산정하기
def set_local_name(location_num):
    local_name = None
    if 0 <= location_num <= 8:
        local_name = "서울"
    elif 9 <= location_num <= 12:
        local_name = "부산"
    elif 13 <= location_num <= 15:
        local_name = "인천"
    elif 16 <= location_num <= 25:
        local_name = "경기"
    elif 26 <= location_num <= 34:
        local_name = "강원"
    elif 35 <= location_num <= 39:
        local_name = "충북"
    elif location_num == 40:
        local_name = "대전"
    elif (41 <= location_num <= 43) or (45 <= location_num <= 47):
        local_name = "충남"
    elif (location_num == 44) or (location_num == 96):
        local_name = "세종"
    elif 48 <= location_num <= 54:
        local_name = "전북"
    elif 55 <= location_num <= 64:
        local_name = "전남"
    elif (location_num == 55) or (location_num == 56) or (location_num == 65) or (location_num == 66):
        local_name = "광주"
    elif 67 <= location_num <= 70:
        local_name = "대구"
    elif 71 <= location_num <= 81:
        local_name = "경북"
    elif (82 <= location_num <= 84) or (86 <= location_num <= 91):
        local_name = "경남"
    elif (location_num == 85) or (location_num == 90):
        local_name = "울산"
    elif 92 <= location_num <= 95:
        local_name = "제주"
    else:
        pass

    return local_name


## 주민등록번호에서 7번째 자릿수 짝수/홀수 따라 성별이 나뉨
def verify_gender(gender_num):
    if gender_num % 2 == 1:
        print('[+] 성별 : 남성')
        return 0
    elif gender_num % 2 == 0:
        print('[+] 성별 : 여성')
        return 0
    else:
        print("[-] 유효하지 않는 성별번호")
        return -1


## 주민등록번호 앞자리 검증
def verify_birth_date(birth_date):
    system_date_format = "%y%m%d"
    try:
        input_date = datetime.strptime(birth_date, system_date_format)
    except ValueError:
        print("[-] 생년월일이 유효하지 않습니다.")
        input_date = None

    return input_date


## 주민등록번호 각 자리수에 가중치를 연산하기
def verify_id_number(id_num):
    if len(id_num) == 13:
        verify_value = 0
        weight = 2
        for i in range(len(id_num) - 1):
            if weight == 10:
                weight = 2
            temp = int(id_num[i]) * int(weight)
            weight += 1
            verify_value += temp

        # 위 결과에서 11로 나눈 나머지를 계산후 11에서 뺀다 => 결과가 2자리 숫자면 10의 자리를 버린다.
        verify_value = (11 - (verify_value % 11)) % 10

        if int(id_num[12]) == verify_value:
            return 0

        else:
            print('[-] 유효하지 않는 주민등록번호입니다.')
            return -1
    else:
        print('[-] 주민등록번호를 다시 한번 확인해주세요.')
        return -1


## 유효성 검사하기
def main():
    while True:
        id_num = input('[+] 주민등록번호를 입력하세요(13자리 "-" 제외) : ')
        print('')

        ### 주민등록번호 연도 검증
        birth_date = id_num[0:6]
        if verify_birth_date(birth_date) is not None:
            print("[+] 생년월일 : {}".format(birth_date))
        else:
            continue

        ### 주민등록번호가 유효하지 않다면 주민등록번호 다시 입력
        if verify_id_number(id_num):
            continue

        ### 성별코드가 유효하지 않다면 종료
        gender_num = int(id_num[6:7])
        if verify_gender(gender_num):
            break

        ### 지역코드 정의
        location_num = int(id_num[7:9])
        local_name = set_local_name(location_num)

        ### 지역코드 출력
        if local_name is not None:
            print("[+] 출생지역 : {}".format(local_name))

        ### 지역코드가 없다면 종료
        else:
            print("[-] 출생지역 구분코드에 문제가 발생하였습니다. 프로그램을 다시 실행합니다.")
            break

        print("[+] 정상 확인된 주민등록번호입니다. 프로그램을 종료합니다.")
        break


if __name__ == '__main__':
    main()
    sys.exit()

input()

## 끝.