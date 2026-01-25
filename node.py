from collections import deque
class Node:
    """節點(實例)"""
    def __init__(self, video_id):
        self.prev = None
        self.next = None
        self.video_id = video_id

class VideoTracker:
    """影片追蹤器"""
    def __init__(self,capacity =10):
        """追蹤器初始化: (capacity:長度, history:歷史, lookup:紀錄索引, head:最新, tail:最舊)"""
        self.lookup = {}
        self.capacity = capacity
        self.history = deque()
        self.head = None
        self.tail = None
    
    def add_new(self, video_id):
        """累加新的紀錄"""
        new_node = Node(video_id)
        self.lookup[video_id] = new_node
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.read()

    def pin_top(self, video_id):
        """移動到最新紀錄"""
        if video_id not in self.lookup: return
        node = self.lookup[video_id]
        if node is self.head: return
        if node.prev: node.prev.next = node.next
        if node.next: node.next.prev = node.prev
        else: self.tail = node.prev

        node.next = self.head
        node.prev = None
        if self.head: self.head.prev = node
        self.head = node
    
    def newest_one_displace(self, video_id):
        """新節點替換舊節點"""
        if video_id in self.lookup:
            self.pin_top(video_id=video_id)
            return
        
        if len(self.lookup) >= self.capacity:
            old_one = self.tail
            del self.lookup[old_one.video_id]
            self.tail = old_one.prev
            if self.tail: self.tail.next = None
            else: self.head = None
        
        new_node = Node(video_id)
        self.lookup[video_id] = new_node

        if not self.head: self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def read(self):
        """讀取歷史紀錄"""
        print(f"目前有{len(self.history)}條紀錄: {list(self.history)}")
