class LUPrefix:
    def __init__(self, n):
        self.uploaded_videos = [False] * n
        self.longest_prefix = 0
    def upload(self, video):
        self.uploaded_videos[video - 1] = True
        while self.longest_prefix < len(self.uploaded_videos) and self.uploaded_videos[self.longest_prefix]:
            self.longest_prefix += 1
    def longest(self):
        return self.longest_prefix

server = LUPrefix(4)
server.upload(3)
print(server.longest())
