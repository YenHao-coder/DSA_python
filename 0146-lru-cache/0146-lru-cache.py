class Node:
    def __init__(self, key, val):
        '''初始化節點(key:鍵名, val:內值, prev:上一個, next:下一個)'''
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        """初始化 (cap:容量, cache:追蹤最新, head:最新, tail:最舊)"""
        self.cap = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node):
        '''增加最新節點'''
        h = self.head
        n = self.head.next
        h.next = node
        node.prev = h
        node.next = n
        n.prev = node        

    def _remove(self,node):
        '''斷開一個節點'''
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def get(self, key: int) -> int:
        '''取得快取內容，不存在回傳-1'''
        if key in self.cache:
            self._remove(self.cache[key])
            self._add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        '''寫入快取，超過容量移除舊節點'''
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self._add(self.cache[key])

        if len(self.cache) > self.cap:
            p = self.tail.prev
            self._remove(p)
            del self.cache[p.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)