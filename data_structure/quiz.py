# 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게됩니다.
# 추첨 프로그램을 작성하시오.

# 조건 1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1-20 이라고 가정한다.
# 조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복은 불가능 하다.
# 조건 3 : random 모듈의 shuffle 과 sample을 활용한다.

from random import *
users = list(range(1,21)) # 20명의 아이디를 리스트로 받는다.
shuffle(users) # shuffle 함수를 통하여 섞는다.
winners = sample(users,4) # 샘플 함수를 통해서 user 변수에서 4개를 고른다
print("치킨 당첨자 : {}".format(winners[0])) # winners 변수에서 첫번째 자리는 치킨 당첨
print("커피 당첨자 : {}".format(winners[1:])) # winners 변수에서 나머지 변수는 커피 당첨


