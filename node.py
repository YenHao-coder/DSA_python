class Node:
    """節點練習"""
    def __init__(self, video_id):
        self.prev = None
        self.next = None
        self.video_id = video_id

class VideoTracker:
    """影片追蹤"""
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
