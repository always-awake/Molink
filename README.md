API Documentation
=================
* **굵은 글씨**로 표시된 Key는 필수값
* 사용자 인증은 JWT를 이용
    - Header의 Authorization Key에 JWT <your_token>를 추가하여 request
    - ex) JWT eyJ0eXAiOiJKV1QiLCJh
    - 관련 문서: [Django REST framework JWT](http://getblimp.github.io/django-rest-framework-jwt/)
    - 회원 가입, 로그인 API 외에 모든 API는 Authenticate required

## API 목록
* 관심사(Category) API
* 폴더(Folder) API

## 관심사(Category) API
### get Categories
> 관심사/사진 url을 가져오는 API
#### Request
- url <br>
`GET /api/v1/categories`

#### Response
`status: HTTP 200 OK`
```json
[
    {
        "id": 1,
        "name": "개발",
        "img_url": "http://blog.rightbrain.co.kr/CMS1/wp-content/uploads/2016/03/00-Syrup-Character_Titlegw.png"
    },
    {
        "id": 2,
        "name": "디자인",
        "img_url": "https://sejong.korea.ac.kr/mbshome/mbs/kr/images/sub/hakbu/hakbu_info_2017_030100.jpg"
    },
    {
        "id": 3,
        "name": "화장품",
        "img_url": "https://post-phinf.pstatic.net/MjAxODAyMDdfMjQz/MDAxNTE3OTY4OTI1MzYy.bLREVpZJN3r_g7VR3021Z_E55IqPT9Sm7cRBk-XcOIUg.6kq-mZe8sAwivyPKrfxyupB1DEm47WuKGQe_8DrlXVQg.JPEG/GettyImages-jv11011817.jpg?type=w1200"
    }
]
```
#
### create category-based folder
> 선택한 카테고리 기반으로 폴더를 생성해주는 API <br>
> 폴더 컬러는 랜덤
#### Request  
- url <br>
`POST /api/v1/categories/folders`

- Body <br>
    - **category_name_list**: "개발,디자인,화장품" (string)
    
#### Response
`status: HTTP 201 Created`
```json
[
    {
        "id": 1,
        "color": "#53bbb4",
        "name": "개발",
        "created_at": "2019-08-19T18:46:28.083042+09:00"
    },
    {
        "id": 2,
        "color": "#838cc7",
        "name": "디자인",
        "created_at": "2019-08-19T18:46:28.086418+09:00"
    },
    {
        "id": 3,
        "color": "#e15258",
        "name": "화장품",
        "created_at": "2019-08-19T18:46:28.088045+09:00"
    }
]
```
#
## 폴더(Folder) API
### Folder List
> 유저가 생성한 모든 상위폴더(부모 폴더가 없는 폴더) 리스트를 보여주는 API

#### Request  
- url <br>
`GET /api/v1/folders/all`
    
#### Response
`status: HTTP 201 Created`
```json
[
    {
        "id": 1,
        "parent": null,
        "color": "#53bbb4",
        "name": "개발",
        "is_private": false,
        "created_at": "2019-08-19T18:46:28.083042+09:00"
    },
    {
        "id": 2,
        "parent": null,
        "color": "#838cc7",
        "name": "디자인",
        "is_private": false,
        "created_at": "2019-08-19T18:46:28.086418+09:00"
    },
    {
        "id": 3,
        "parent": null,
        "color": "#e15258",
        "name": "화장품",
        "is_private": false,
        "created_at": "2019-08-19T18:46:28.088045+09:00"
    }
]
```
#
### Create Folder
> 폴더를 생성하는 API <br>
> is_pravate 필드는 입력하지 않을 경우 False 로 설정됨 <br>
> 최상위 폴더일 경우 parent_id 필드에 null을 입력하면 된다.

#### Request  
* url
`POST /api/v1/folders/`

* Body
    - **name**: "코딩",
    - **color**: "#A30000",
    - **parent_id**: 2
    - is_private: true,
    
#### Response
`status: HTTP 201 Created`
```json
{
    "id": 4,
    "name": "코딩",
    "color": "#A30000",
    "parent_id": 2,
    "is_private": true
}
```
#
## 링크(Link) API
### Create Link
> 링크를 생성하는 API

#### Request
* url
`POST /api/v1/links/`

* Body
    - **name**: "프로그래머스-코테연습"
    - **url**: "https://programmers.co.kr/learn/challenges"
    - parent_id: 4

#### Response
`status: HTTP 201 Created`
```json
{
    "id": 1,
    "name": "링크1",
    "url": "https://programmers.co.kr/learn/challenges",
    "parent_id": 4
}
```
#
### Update Link
> 링크를 수정하는 API
> 필드 값 중 수정을 원하는 필드만 request body에 담아 요청하면 해당 필드만 수정됨

#### Request
* url
`PUT /api/v1/links/{link_id}`

* Body
    - name: "네이버",
    - url: "https://www.naver.com/",
    - parent_id: 16

#### Response
`status: HTTP 200 OK`
```json
{
"name":"네이버",
"url":"https://www.naver.com/",
"parent_id":16
}
```
#