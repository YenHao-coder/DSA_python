class Node:
    """節點(實例)"""
    def __init__(self, video_id):
        self.prev = None
        self.next = None
        self.video_id = video_id

class VideoTracker:
    """影片追蹤器"""
    def __init__(self):
        self.lookup = {}
        self.head = None
        self.tail = None
    
    def add_new(self, video_id):
        """增加新的紀錄"""
        new_node = Node(video_id)
        self.lookup[video_id] = new_node
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
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
