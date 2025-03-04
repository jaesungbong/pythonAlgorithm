# 민준이는 뒤늦게 정보 과목의 중요성을 깨닫고 학습실에서 공부를 하고 있습니다.
# 기초적인 공부가 부족하여 아주 쉬운 문제부터 어려움을 겪은 민준이는 친구에게 물어보려고 합니다.
# 가장 잘 하는 친구에게 물어보기는 질문의 내용이 너무 부끄러워서 n명의 친구들 중 정보 성적이 세 번째로 높은 친구에게 묻고자 합니다.
# 친구들의 성적은 모두 다릅니다.
# n명의 친구들의 이름과 정보 성적이 주어졌을 때, 성적이 세 번째로 높은 학생의 이름을 출력해 주세요.
#
# 입력
# 1) 첫째 줄에 n이 입력된다. (3<=n<=50)
# 2) 둘째 줄부터 n명의 데이터가 입력된다.
# 3) 데이터는 영문 이름과 정보 점수가 공백으로 구분되어 입력된다.
#
# 출력
# 세 번째로 높은 학생의 이름을 출력한다.
#
# 입력 예시
# 5
# minsu 78
# gunho 64
# sumin 84
# jiwon 96
# woosung 55
#
# 출력 예시
# minsu

n = int(input())
student = []
for i in range(n):
    name, score = input().split()
    student.append((str(name), int(score)))

student.sort(key=lambda x:x[1],reverse=True)
print(student[2][0])


