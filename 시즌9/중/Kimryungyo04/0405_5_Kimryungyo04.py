# [ 알고리즘 ]
# k번을 움직여 n개의 계단을 움직이는 경우를 보다 쉽게 찾기 위해
# 0번째 계단부터 오르는 것이 아닌 역으로 n번째 계단에서 0번째 계단으로 내려온다고 생각한다

# 현재 위치가 텔레포트를 통해 올 수 없는 계단인 경우 1칸 아래로 내려가고
# 텔레포트를 통해 올 수 있는 계단인 경우 2/3 지점으로 텔레포트한다
# 이 과정을 반복해 남아있는 이동 횟수가 1회 이상 남아있을 때 1번째 계단에 도착하면
# K번을 이동해 N번째 계단을 전부 내려올 수 있다는 것이므로 minigimbob을 출력한다
# 반대로 이동 횟수를 다 소진했음에도 1번째 계단에 도달하지 못했다면 water를 출력한다

# 텔레포트를 통해 올 수 없는 계단 : 3n + 2번째 계단 (n은 0 이상의 정수)

def main():
    """씨부엉 난이도 중 5일차 알고리즘 함수"""

    # 정보 입력
    n, k = map(int, input().split())

    # k-1번 움직이는 시뮬레이션
    for i in range(k - 1):
        # 현재 위치를 3으로 나누기
        remainder = n % 3

        # 텔레포트를 통해 올 수 없는 위치인 경우 한 칸 내려가기
        if remainder == 2: n -= 1
        
        # 텔레포트를 통해 올 수 있는 위치이나 나머지가 있는 경우 2/3 지점 한칸 위로 이동
        elif remainder == 1: n = int(n * 2/3) + 1

        # 나머지가 없는 경우 2/3 지점으로 이동
        else: n = n * 2/3

        # 1번째 계단에 도달한 경우 루프 종료
        if n == 1: break

    # 결과 출력
    if n == 1: print("minigimbob")
    else: print("water")

main()
