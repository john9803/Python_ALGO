import heapq as hq
import sys

input = sys.stdin.readline() # 항상 빠른입출력을 사용하기
N = int(input())

ab_arr = []

for i in range(1,N+1):
    cand = int(input())

    if cand == 0:
        # 절댓값 제일작은 수 찾기
        # 절댓값이 제일 작은수가 복수면 그중 음수빼기 -> min 쓰면 자동 아님?
        if len(ab_arr) >= 1:
            print(hq.heappop(ab_arr)[-1])
        else:
            print(0)
    else:
        hq.heappush(ab_arr, (abs(cand), cand)) ### 이게 존나 핵심!!!! or max_heap, min_heap을 이용해서 푸는 풀이도 존재함.
    # print(ab_arr)


# 빠른입출력 속도비교
# from datetime import datetime
# start_time = datetime.now()
# input = input() # 항상 빠른입출력을 사용하기
# time_elapsed = datetime.now() - start_time
#
# print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))
#
# start_time = datetime.now()
# input = sys.stdin.readline() # 항상 빠른입출력을 사용하기
# time_elapsed = datetime.now() - start_time
#
# print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))

