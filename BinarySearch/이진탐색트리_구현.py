class Node:                                     # Node 클래스 정의
    def __init__(self, key):                    # 생성자에서 Child Node 인 Left Node 와 Right Node 를 표현
        self.left = None
        self.val = key
        self.right = None

class BinarySearchTree:                         # Binary Search Tree 클래스 정의
    def __init__(self):                         # 초기에 어떠한 Node 도 없는 상태
        self.root = None

    def insert(self, key):
        if not self.root:                       # 루트 Node 가 없다면 새로운 Node 를 루트 노드로 추가
            self.root = Node(key)
            return
        curr = self.root
        while True:
            if key < curr.val:                  # insert 하려는 key 가 현재 Node 의 값보다 작으면 왼쪽 Child Node 로 이동
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(key)       # 현재 Node 의 Left Node 가 없는 경우 새로운 Node 추가
                    break
            else:                               # insert 하려는 key 가 현재 Node 의 값보다 크면 오른쪽 Child Node 로 이동
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(key)      # 현재 Node 의 Right Node 가 없는 경우 새로운 Node 추가
                    break

    def search(self, key) -> Node:              # 이진 탐색 규칙에 따라 특정값이 있는지 확인 (루트 Node 부터 시작)
        curr = self.root
        while curr and curr.val != key:         # 현재 Node 가 존재하고, 찾으려는 값과 현재 Node의 값이 같이 않은 경우 반복
            if key < curr.val:                  # 찾으려는 값이 현재 Node 의 값보다 작은 경우 왼쪽 Child Node 로 이동
                curr = curr.left
            else:                               # 찾으려는 값이 현재 Node 의 값보다 큰 경우 오른쪽 Child NOde 로 이동
                curr = curr.right
        return curr


def solution(lst, search_lst):
    binary_search_tree = BinarySearchTree()
    for key in lst:
        binary_search_tree.insert(key)
    result = []
    for search_val in search_lst:
        if binary_search_tree.search(search_val):
            result.append(True)
        else:
            result.append(False)
    return result

print(solution([5,3,8,4,2,1,7,10], [1,2,5,6]))
print(solution([1,3,5,7,9], [2,4,6,8,10]))
