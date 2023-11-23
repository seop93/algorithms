class ListNode(object):
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory(object):
    def __init__(self, homepage):
        self.head = self.current = ListNode(val=homepage)  # 형식상 head 정의

    def visit(self, url):
        self.current.next = ListNode(val=url, prev=self.current)  # LinkedList 장점 추가삭제 용이
        self.current = self.current.next
        return None

    def back(self, steps):
        while steps > 0 and self.current.prev is not None:
            steps -= 1
            self.current = self.current.prev
        return self.current.val

    def forward(self, steps):
        while steps > 0 and self.current.next is not None:
            steps -= 1
            self.current = self.current.next
        return self.current.val



browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("youtube.com")
browserHistory.visit("facebook.com")
browserHistory.back(1)
browserHistory.back(1)
browserHistory.forward(1)
browserHistory.visit("linkedin.com")
browserHistory.forward(2)
browserHistory.back(2)
print(browserHistory.back(7))