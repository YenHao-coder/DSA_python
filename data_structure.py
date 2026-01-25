from collections import deque

"""Stack 實作 (list)"""
stack = []
stack.append("Page_A")
stack.append("Page_B")
top_item = stack.pop()
print(f"Stack Pop:{top_item}")

"""Queue 實作 (deque)"""
queue = deque()
queue.append("Customer_1")
queue.append("Customer_2")
first_item = queue.popleft()
print(f"Queue Dequeue: {first_item}")

'''觀看紀錄設計'''
class VideoHistory:
    def __init__(self,capacity=10):
        self.capacity = capacity
        self.history = deque()
        self.lookup = set()
    
    def watch_video(self,video_id):
        '''功能:累加觀看紀錄'''
        if video_id in self.lookup:
            self.history.remove(video_id)

        elif len(self.history) >= self.capacity:
            oldest = self.history.popleft()
            self.lookup.remove(oldest)
        
        self.history.append(video_id)
        self.lookup.add(video_id)

        self.read()
    
    def read(self):
        """顯示紀錄"""
        print(f"目前有{len(self.history)}條紀錄: {list(self.history)}")
yt = VideoHistory(3)
yt.watch_video("A")
yt.watch_video("B")
yt.watch_video("C")
yt.watch_video("D")
