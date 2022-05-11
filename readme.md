![휴먼스케이프](https://user-images.githubusercontent.com/88444944/167796009-9b41d165-46e9-4bcc-b82e-7513e81ad8c8.jpg)


# Wanted team_B #3휴먼스케이프 기업과제  

임상정보 open API를 수집하는 WEB Aplication을 설계, 구현, 개발합니다.

## 과제 기한:
* 3 ~ 5인이 2 ~ 3일 이내로 완료하세요  
#
  1일: API분석, 모델링, 수집 스크립트(batch task) 작성

  2일: 임상정보 API 구현, 로컬 테스트 완료, API 문서화 

  3일: 배포 및 문서화, 가산점 구현(기능추가)

## Team process:

### Team 분업  ###  
  
|성명|업무|비고|
|------|---|---|
|최승리|배치스크립트 작성|팀장⭐ |
|하정현|배포(docker,swagger)|.|
|남기윤|데이터 적재 앱구현|.|\

### 중점 point

1. RESTFUL 한 API 구현 (Endpoint URL, HTTP Method , JSON Response)
2. 효율적인 쿼리 구현
3. 요구사항 뿐 아니라 다른 기능이 함게 있는 서버라고 가정하고 폴더, 파일, 코드 스트럭처를 설계

## Directory Info.

```
├─menu                      -menu add 디렉토리
│  ├─migrations
│  │  └─__pycache__
│  └─__pycache__
├─point_of_sale             -프로젝트 main configure
│  ├─settings
│  │  └─__pycache__
│  └─__pycache__
├─pos_log                   -poslog CRUD 및 검색 add 디렉토리
│  ├─migrations    
│  │  └─__pycache__
│  ├─tests                  -unit test 디렉토리
│  │  └─__pycache__
│  └─__pycache__
└─restaurants               -restaurant add 디렉토리
    ├─migrations
    │  └─__pycache__
    └─__pycache__
```
## 실행 안내

**누구나 따라 할 수 있을 정도의 자세한 실행 방법, 가이드대로 실행되지 않을경우 트러블 슈팅 가이드를 함께 제시해야 합니다.**

## 휴먼스케이프 project 요구사항 분석

* 임상시험 정보를 수집하는 batch task 작성
  * open API 참고:"htps://www.data.go.kr/data/3074271/fileData.do#/API목록/GETuddi%3Acfc19dda-6f75-4c57-86a8-bb9c8b103887"
* 출제의도 :
  * open API 스펙을 보고 이해하며 데이터를 주기적으로 적재 하는 기능을 구현, 실제 데이터를 추가하면서 중복 방지에 대한 전략을 세워야함
  * 기존 데이터와 API 데이터간의 수정된 사항을 비교하여 해당 임상시험이 업데이트 된 것인지 새로 추가된 것 인지 구별이 가능해야함
  * 실행이 완료되면 추가된 건 수, 업데이트 된 건 수를 출력하거나 따로 로깅해줘야함
```
요구사항 분석
1. open API데이터를 적재하는 기능을 구현하며 중복을 방지하는 방법
  -여기에 내용을 입력해주세요
  
2.기존 데이터와 수정된 사항을 비교하여 구분하는 방법
  -여기에 내용을 입력해주세요
  
3.실행후 로깅 방법
  -여기에 내용을 입력해주세요
  
```
* 수집한 임상정보에 대한 API
  * 특정 임상정보 읽기(uuid 값은 자유)
* 수집한 임상정보 리스트 API
  * 최근 일주일 내에 업데이트 된 임상정보 리스트
  * pagination 기능
    * offset, limit로 구현
* 직접 API를 호출해서 볼 수 있는 API Document 작성
## 추가 도전과제(v2)

  * 임상시험 정보를 제공하는 다른 API를 스스로 발굴하여 batch task를 추가(가산점)
  * 배포하여 웹에서 사용 할 수 있도록 제공
    * README.md에 배포과정에 대한 가이등화 주소 제공, 설치하지 않고 확인가능한 경우 가산점
  * 임상정보 리스트 API
    * 검색기능 제공
    * pagination 기능: offset, limit구현후 새로운 방식을 제공하면 가산점

## API info.
  **request, response 둘 다 적어야합니다.
## DB info.

## 구현 과정

### 최승리
### 하정현
### 남기윤 (아래는 기본 양식입니다.)
  * 구현 기능 설명(캡쳐 이미지등을 활용해주세요)
  * 구현 방법과 이유 (이론적 설명을 포함해주시면 좋습니다. + ex)사용한 기술을 선정한 이유, 효율성, 확장성에대한 설명 등)
  * 구현과정에서 어려웠던 점 (100~200자 이내로 자유롭게 작성해주세요. 필수사항은 아닙니다.)
  * 구현 기능 설명2(필요 시 추가)
  * 구현 방법과 이유2
  * 구현 과정에서 어려웠던 점2
  * ...



