API Documentation
=================
* **굵은 글씨**로 표시된 값은 필수값

## API 목록

## 관심사(Category) API
### getCategories
> 관심사/사진을 가져오는 API
#### Request <br>
- url
`GET /api/v1/categories`

#### Response <br>
`status: HTTP 200 OK`
```
[
    {
        "id": 1,
        "name": "디자인",
        "img_url": "http://blog.rightbrain.co.kr/CMS1/wp-content/uploads/2016/03/00-Syrup-Character_Titlegw.png"
    },
    {
        "id": 2,
        "name": "스포츠",
        "img_url": "https://sejong.korea.ac.kr/mbshome/mbs/kr/images/sub/hakbu/hakbu_info_2017_030100.jpg"
    },
    {
        "id": 3,
        "name": "뷰티",
        "img_url": "https://post-phinf.pstatic.net/MjAxODAyMDdfMjQz/MDAxNTE3OTY4OTI1MzYy.bLREVpZJN3r_g7VR3021Z_E55IqPT9Sm7cRBk-XcOIUg.6kq-mZe8sAwivyPKrfxyupB1DEm47WuKGQe_8DrlXVQg.JPEG/GettyImages-jv11011817.jpg?type=w1200"
    }
]
```

## 유저(User) API
### user sign up
> 회원가입 API
#### Request <br>
- url
`POST /api/v1/users/signup`
- Body
```
"name": 이미림
"username": leemirim
"password1": a12345
"password2": a12345
```

#### Response <br>
```json
{
    "name": "이미림",
    "username": "leemirim",
    "password1": "admin12345",
    "password2": "admin12345"
}
```
