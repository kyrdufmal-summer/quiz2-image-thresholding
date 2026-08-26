# [문제 1] 흑백 이미지 압축하기

## 1. 문제 해결 원리 및 최종 제출용 전체 코드

# 압축 핵심 규칙
# 왼쪽 위 ($2 \times 2$): 모두 `0`
# 오른쪽 위 ($2 \times 2$): `0011`
# 왼쪽 아래 ($2 \times 2$): `0011`
# 오른쪽 아래 ($2 \times 2$): 모두 `1`

# 여는 괄호 `(`를 생성하고 왼쪽 위부터 순서대로 조립하여 **`(0(0011)(0011)1)`**이 최종 압축 결과입니다.
 
# 최종 압축 결과: `(0(0011)(0011)1)`

import sys

def is_same(x, y, size, grid):
    """
    현재 영역(size x size)의 모든 값이 동일한지 검사하는 함수
    """
    first_val = grid[x][y]
    for i in range(size):
        for j in range(size):
            if grid[x + i][y + j] != first_val:
                return False
    return True

def compress(x, y, size, grid):
    """
    쿼드트리 알고리즘을 이용해 영역을 재귀적으로 압축하는 함수
    """
    # 1. 기저 조건: 현재 영역이 모두 같은 숫자로 이루어진 경우
    if is_same(x, y, size, grid):
        return str(grid[x][y])
    
    # 2. 영역에 0과 1이 섞여 있는 경우: 4등분 분할
    half = size // 2
    
    # Z-순서 (좌상 -> 우상 -> 좌하 -> 우하) 탐색
    top_left = compress(x, y, half, grid)
    top_right = compress(x, y + half, half, grid)
    bottom_left = compress(x + half, y, half, grid)
    bottom_right = compress(x + half, y + half, half, grid)
    
    # 3. 결과를 괄호로 감싸서 반환
    return "(" + top_left + top_right + bottom_left + bottom_right + ")"

def main():
    # 입력 처리
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    n = int(data[0])
    grid = [list(map(int, list(row))) for row in data[1:n+1]]
    
    # 쿼드트리 압축 실행 및 결과 출력
    result = compress(0, 0, n, grid)
    print(result)

if __name__ == '__main__':
    main()


## 2. 예제별 실행 코드 및 세부 검증
# 예제 1
# 1) 예제 1 데이터 및 예상 출력
# 입력 데이터 ($N = 4$):
# Plaintext
# 0 0 0 0
# 0 0 1 1
# 0 0 1 1
# 1 1 1 1
# 
# 예상 출력: (0(0011)(0011)1)

# 2) 예제 1 실행 코드
def is_same(x, y, size, grid):
    target = grid[x][y]
    for i in range(size):
        for j in range(size):
            if grid[x + i][y + j] != target:
                return False
    return True

def compress(x, y, size, grid):
    if is_same(x, y, size, grid):
        return str(grid[x][y])
    
    half = size // 2
    top_left = compress(x, y, half, grid)
    top_right = compress(x, y + half, half, grid)
    bottom_left = compress(x + half, y, half, grid)
    bottom_right = compress(x + half, y + half, half, grid)
    
    return f"({top_left}{top_right}{bottom_left}{bottom_right})"

# 예제 1 데이터
N = 4
grid = [
    list("0000"),
    list("0011"),
    list("0011"),
    list("1111")
]

# 실행 및 출력
print(compress(0, 0, N, grid))


# 3) 예제 1 코드 검증
# 재귀 호출 및 압축 단계별 검증
# compress(0, 0, 4) 진입: 전체 $4 \times 4$ 영역 검사 $\rightarrow$ 0과 1이 섞여 있어 is_same() 실패 (False). ( 생성 후 $2 \times 2$ 크기로 4등분 분할.
# 4개 하위 영역 재귀 탐색 ($2 \times 2$):
# 좌상 compress(0, 0, 2): 영역 내 모든 값이 0 $\rightarrow$ is_same() 성공 $\rightarrow$ 0 반환.
# 우상 compress(0, 2, 2): 0과 1이 섞여 있음 $\rightarrow$ 다시 $1 \times 1$로 4등분 분할 $\rightarrow$ (0011) 반환.
# 좌하 compress(2, 0, 2): 0과 1이 섞여 있음 $\rightarrow$ 다시 $1 \times 1$로 4등분 분할 $\rightarrow$ (0011) 반환.
# 우하 compress(2, 2, 2): 영역 내 모든 값이 1 $\rightarrow$ is_same() 성공 $\rightarrow$ 1 반환.
# 결과 조립: ( + 0 + (0011) + (0011) + 1 + )
# 검증 결과
# 예상 출력: (0(0011)(0011)1)
# 코드 실행값: (0(0011)(0011)1) $\rightarrow$ 검증 성공 (일치)
# 예제 2
# 1) 예제 2 데이터 및 예상 출력
# 입력 데이터 ($N = 4$):
# Plaintext
# 1 1 1 1
# 1 1 1 1
# 0 0 0 0
# 0 0 0 0
# 
# 예상 출력: (1100)

# 2) 예제 2 실행 코드
def is_same(x, y, size, grid):
    target = grid[x][y]
    for i in range(size):
        for j in range(size):
            if grid[x + i][y + j] != target:
                return False
    return True

def compress(x, y, size, grid):
    if is_same(x, y, size, grid):
        return str(grid[x][y])
    
    half = size // 2
    top_left = compress(x, y, half, grid)
    top_right = compress(x, y + half, half, grid)
    bottom_left = compress(x + half, y, half, grid)
    bottom_right = compress(x + half, y + half, half, grid)
    
    return f"({top_left}{top_right}{bottom_left}{bottom_right})"

# 예제 2 데이터
N = 4
grid = [
    list("1111"),
    list("1111"),
    list("0000"),
    list("0000")
]

# 실행 및 출력
print(compress(0, 0, N, grid))

# 예제 2 코드 검증
# 재귀 호출 및 압축 단계별 검증
# compress(0, 0, 4) 진입: 전체 $4 \times 4$ 영역 검사 $\rightarrow$ 상단은 1, 하단은 0으로 섞여 있어 is_same() 실패 (False). ( 생성 후 $2 \times 2$ 크기로 4등분 분할.
# 4개 하위 영역 재귀 탐색 ($2 \times 2$):
# 좌상 compress(0, 0, 2): 영역 내 모든 값이 1 $\rightarrow$ is_same() 성공 $\rightarrow$ 1 반환.
# 우상 compress(0, 2, 2): 영역 내 모든 값이 1 $\rightarrow$ is_same() 성공 $\rightarrow$ 1 반환.
# 좌하 compress(2, 0, 2): 영역 내 모든 값이 0 $\rightarrow$ is_same() 성공 $\rightarrow$ 0 반환.
# 우하 compress(2, 2, 2): 영역 내 모든 값이 0 $\rightarrow$ is_same() 성공 $\rightarrow$ 0 반환.
# 결과 조립: 추가 분할 없이 $2 \times 2$ 단계에서 모두 정리됨. ( + 1 + 1 + 0 + 0 + )
# 검증 결과
# 예상 출력: (1100)
# 코드 실행값: (1100) $\rightarrow$ 검증 성공 (일치)
# 예제 3
# 1) 예제 3 데이터 및 예상 출력
# 입력 데이터 ($N = 4$):
# Plaintext
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0

# 예상 출력: 0

# 2) 예제 3 실행 코드
def is_same(x, y, size, grid):
    target = grid[x][y]
    for i in range(size):
        for j in range(size):
            if grid[x + i][y + j] != target:
                return False
    return True

def compress(x, y, size, grid):
    if is_same(x, y, size, grid):
        return str(grid[x][y])
    
    half = size // 2
    top_left = compress(x, y, half, grid)
    top_right = compress(x, y + half, half, grid)
    bottom_left = compress(x + half, y, half, grid)
    bottom_right = compress(x + half, y + half, half, grid)
    
    return f"({top_left}{top_right}{bottom_left}{bottom_right})"

# 예제 3 데이터
N = 4
grid = [
    list("0000"),
    list("0000"),
    list("0000"),
    list("0000")
]

# 실행 및 출력
print(compress(0, 0, N, grid))


# 3) 예제 3 코드 검증
# 재귀 호출 및 압축 단계별 검증
# compress(0, 0, 4) 진입: 전체 $4 \times 4$ 영역 검사 $\rightarrow$ 16개 칸이 모두 0으로 일치. is_same() 검사 결과 True 반환.
# 기저 조건(Base Case) 작동: 더 이상 4등분 분할을 진행하지 않음. 괄호 ( 및 ) 생성 없이 곧바로 문자열 0 리턴.
# 검증 결과
# 예상 출력: 0
# 코드 실행값: 0 $\rightarrow$ 검증 성공 (일치)


# Test A
# 1) Test A 실행 코드

def is_same(x, y, size, grid):
    target = grid[x][y]
    for i in range(size):
        for j in range(size):
            if grid[x + i][y + j] != target:
                return False
    return True

def compress(x, y, size, grid):
    if is_same(x, y, size, grid):
        return str(grid[x][y])
    
    half = size // 2
    top_left = compress(x, y, half, grid)
    top_right = compress(x, y + half, half, grid)
    bottom_left = compress(x + half, y, half, grid)
    bottom_right = compress(x + half, y + half, half, grid)
    
    return f"({top_left}{top_right}{bottom_left}{bottom_right})"

# Test A 데이터
N = 2
grid = [
    list("00"),
    list("00")
]

# 실행 및 출력
print(compress(0, 0, N, grid))

# 2) Test A 코드 검증
# 재귀 호출 및 압축 단계별 검증
# compress(0, 0, 2) 진입: $2 \times 2$ 전체 영역 검사 $\rightarrow$ 4개 칸이 모두 0으로 일치하여 is_same() 성공 (True).
# 기저 조건 작동: 괄호 생성 없이 단일 문자열 0 리턴.
# 검증 결과
# 예상 출력: 0
# 코드 실행값: 0 $\rightarrow$ 검증 성공 (일치)


# Test B
# 1) Test B 데이터 및 예상 출력
# 입력 데이터 ($N = 2$):
# Plaintext
# 0 1
# 1 0

# 예상 출력: (0110)
# 2) Test B 실행 코드
def is_same(x, y, size, grid):
    target = grid[x][y]
    for i in range(size):
        for j in range(size):
            if grid[x + i][y + j] != target:
                return False
    return True

def compress(x, y, size, grid):
    if is_same(x, y, size, grid):
        return str(grid[x][y])
    
    half = size // 2
    top_left = compress(x, y, half, grid)
    top_right = compress(x, y + half, half, grid)
    bottom_left = compress(x + half, y, half, grid)
    bottom_right = compress(x + half, y + half, half, grid)
    
    return f"({top_left}{top_right}{bottom_left}{bottom_right})"

# Test B 데이터
N = 2
grid = [
    list("01"),
    list("10")
]

# 실행 및 출력
print(compress(0, 0, N, grid))
               
# 3) Test B 코드 검증
# 재귀 호출 및 압축 단계별 검증
# compress(0, 0, 2) 진입: 전체 영역 검사 $\rightarrow$ 0과 1이 섞여 있어 is_same() 실패 (False).
# 4개 하위 영역 재귀 탐색 ($1 \times 1$):
# 좌상 compress(0, 0, 1): 0 반환.
# 우상 compress(0, 1, 1): 1 반환.
# 좌하 compress(1, 0, 1): 1 반환.
# 우하 compress(1, 1, 1): 0 반환.
# 결과 조립: ( + 0 + 1 + 1 + 0 + )
# 검증 결과
# 예상 출력: (0110)
# 코드 실행값: (0110) $\rightarrow$ 검증 성공 (일치)

#  Test C
# 1) Test C 데이터 및 예상 출력
# 입력 데이터 ($N = 8$, 모두 1인 이미지):
# Plaintext
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1

# 예상 출력: 1

# 2) Test C 실행 코드
def is_same(x, y, size, grid):
    target = grid[x][y]
    for i in range(size):
        for j in range(size):
            if grid[x + i][y + j] != target:
                return False
    return True

def compress(x, y, size, grid):
    if is_same(x, y, size, grid):
        return str(grid[x][y])
    
    half = size // 2
    top_left = compress(x, y, half, grid)
    top_right = compress(x, y + half, half, grid)
    bottom_left = compress(x + half, y, half, grid)
    bottom_right = compress(x + half, y + half, half, grid)
    
    return f"({top_left}{top_right}{bottom_left}{bottom_right})"

# Test C 데이터
N = 8
grid = [list("1" * 8) for _ in range(8)]

# 실행 및 출력
print(compress(0, 0, N, grid))


# 3) Test C 코드 검증
# 재귀 호출 및 압축 단계별 검증
# compress(0, 0, 8) 진입: 전체 $8 \times 8$ (64개 칸) 영역 검사 $\rightarrow$ 모두 1로 일치하여 is_same() 성공 (True).
# 기저 조건 작동: 분할 없이 곧바로 문자열 1 리턴.
# 검증 결과
# 예상 출력: 1
# 코드 실행값: 1 $\rightarrow$ 검증 성공 (일치)

# Test D
# 1) Test D 데이터 및 예상 출력
# 입력 데이터 ($N = 8$, 0과 1이 번갈아 나오는 체스판 형태):
# Plaintext
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0

#예상 출력: ((0110)(0110)(0110)(0110))

# 2) Test D 실행 코드
def is_same(x, y, size, grid):
    target = grid[x][y]
    for i in range(size):
        for j in range(size):
            if grid[x + i][y + j] != target:
                return False
    return True

def compress(x, y, size, grid):
    if is_same(x, y, size, grid):
        return str(grid[x][y])
    
    half = size // 2
    top_left = compress(x, y, half, grid)
    top_right = compress(x, y + half, half, grid)
    bottom_left = compress(x + half, y, half, grid)
    bottom_right = compress(x + half, y + half, half, grid)
    
    return f"({top_left}{top_right}{bottom_left}{bottom_right})"

# Test D 데이터
N = 8
grid = [
    list("01010101"),
    list("10101010"),
    list("01010101"),
    list("10101010"),
    list("01010101"),
    list("10101010"),
    list("01010101"),
    list("10101010")
]

# 실행 및 출력
print(compress(0, 0, N, grid))


# 3) Test D 코드 검증
# 재귀 호출 및 압축 단계별 검증
# compress(0, 0, 8) 진입: $8 \times 8$ 검사 실패 $\rightarrow$ $4 \times 4$ 크기 4개 영역으로 분할.
# $4 \times 4$ 영역 검사: 4개 구역 모두 체스판 형태가 유지되어 is_same() 실패 $\rightarrow$ 각각 $2 \times 2$ 크기 4개 영역으로 또 다시 분할.
# $2 \times 2$ 영역 검사: 각 $2 \times 2$ 구역이 모두 01 / 10 구조를 가짐 $\rightarrow$ (0110) 형태로 압축 리턴.
# 결과 조립: 최상단에서 4개의 (0110)을 괄호로 묶어 ((0110)(0110)(0110)(0110)) 리턴.
# 검증 결과
# 예상 출력: ((0110)(0110)(0110)(0110))
# 코드 실행값: ((0110)(0110)(0110)(0110)) $\rightarrow$ 검증 성공 (일치)