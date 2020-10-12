# Readme

Kim-and-Jo  퍼블릭 Ip :13.230.159.83



### 1. 파일구조

```
-LAST_PJT
	-account
		-migrations
		-templates
			-login.html
			-signup.html
		-__init__.py
		-admin.py
		-apps.py
		-forms.py
		-models.py
		-tests.py
		-urls.py
		-views.py
	-Kim_and_Jo
		-settings
			-__init__.py
			-base.pt
			-local.py
			-production.py
		-__init__.py
		-urls.py
		-wsgi.py
	-movies
		-migrations
		-templates
			-detail.html
			-forms.html
			-index.html
			-recommend.html
			-recommend2.html
			-review_detail.html
			-review_forms.html
		-__init__.py
		-admin.py
		-apps.py
		-forms.py
		-models.py
		-tests.py
		-urls.py
		-views.py
	-templates
		-base.html
	-.gitignore
	-db.sqlite3
	-manage.py
	-requirements.txt
```



### 모델링구조



![DB 모델링](C:\Users\han90\Desktop\Kim & Jo\DB 모델링.png)



### 영화 데이터 베이스

- ###### 약 500개정도의 영화정보 json file로 이용

###### 

### 커뮤니티 기능

- ###### Accounts (계정)

  - ###### admin만 영화 수정/삭제/생성 가능

  

- ###### Movies(영화)

- 

  - ###### 성별/연령대 별 관람추이 표시

  - ###### 리뷰 작성/수정/삭제

  - ###### 리뷰 게시판

  - ###### 영화 평점 등록

  - ###### 리뷰 댓글 달기 기능

  - ###### 리뷰 좋아요 싫어요 기능

### 영화 추천 알고리즘

- #### 유저의 리뷰가 없을 경우 

- - ###### 유저의 가입 나이를 고려햐여 해당 장르를 추천

- #### 유저의 리뷰가 있을 경우 

- - ###### 유저가 남긴 리뷰평점의 평균을 구해서 영화 평점이 리뷰평균의 +-1 범위내 영화들만 추천해준다



### 6/11 목요일(1일차)

#### `진행과정`

###### 1. 개요

###### 2. 새로운 기능 아이디어 제안

###### 3. 앞으로 계획짜기

#### `어려웠던 점`

- ###### 처음 구조를 짜다보니 어느정도의 스케일이 되어야 할지 제대로 정하지 못했고 기능에 대한 시간소요가 어느정도 되는지 파악을 하지 못함



### 6/12 금요일(2일차)

#### `진행과정`

###### 1. Account 기본틀 완성(원정)

###### 2. Movies 기본틀 완성(다빈)

#### `어려웠던 점`

- ###### 기존에 배운 내용을 바탕으로 진행하다보니 딱히 어려운 점은 없었습니다.





### 6/13,14 토,일요일(3,4일차)

#### `진행과정`

###### 1. 게시판에서 Review 기능이랑 Review 안에서의 comment 기능 추가 (좋아요, 싫어요 기능) (다빈)

#### `어려웠던 점`

- ###### movie의 pk 값을 가져와서 Review 기능을 만들기 위해 모델링하는 과정이 어려웠으며 좋아요와 싫어요 기능은 똑같았지만 두개 다 눌러서 평가가 되었고 분기를 통해 두개를 동시에 누르지 못하게 해놓음.

### 6/15 월요일(5일차)

#### `진행과정`

###### 1. 추천 알고리즘 제작 (원정, 다빈)

#### `어려웠던 점`

- ###### User class에 age를 넣어서 age를 이용한 추천알고리즘과 User가 쓴 Review의 평균을 기반으로 알고리즘을 짜는 과정에서 User가 쓴 Review 점수를 가져오는 것부터 어려움을 느꼈습니다.



### 6/16 화요일(6일차)

#### `진행과정`

###### 1. User class에 gender를 추가시켜 주어 Review를 남긴 사람들을 기준으로 나이대와 성별 관람추이 제작(원정,다빈)

#### `어려웠던 점`

- ###### pie 그래프랑 막대 그래프를 표현하는 코드에 오픈 소스 활용

