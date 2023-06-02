# leetcode - 1472
[문제 링크](https://leetcode.com/problems/design-browser-history/)

### 분류
LinkedList 자료구조

### 문제 설명
한 개의 탭을 가진 브라우저가 있습니다. 이 브라우저는 홈페이지에서 시작하고, 다른 URL을 방문하거나, 히스토리에서 일정한 단계만큼 뒤로 이동하거나 앞으로 이동할 수 있습니다.

BrowserHistory 클래스를 구현하세요:

- BrowserHistory(string homepage): 브라우저의 홈페이지로 객체를 초기화합니다.
- void visit(string url): 현재 페이지에서 url을 방문합니다. 앞으로의 히스토리를 모두 지웁니다.
- string back(int steps): 히스토리에서 steps만큼 뒤로 이동합니다. 히스토리에서 x 단계만큼만 이동할 수 있고, steps > x인 경우, 최대 x 단계만큼만 이동합니다. 이동한 후의현재 URL을 반환합니다.
- string forward(int steps): 히스토리에서 steps만큼 앞으로 이동합니다. 히스토리에서 x 단계만큼만 앞으로 이동할 수 있고, steps > x인 경우, 최대 x 단계만큼만 이동합니다. 이동한 후의 현재 URL을 반환합니다.

### 입력

```python
BrowserHistory browserHistory = new BrowserHistory("leetcode.com"); // 현재 페이지는 "leetcode.com" 입니다.
browserHistory.visit("google.com"); // 현재 페이지는 "google.com" 입니다.
browserHistory.visit("facebook.com"); // 현재 페이지는 "facebook.com" 입니다.
browserHistory.visit("youtube.com"); // 현재 페이지는 "youtube.com" 입니다.
browserHistory.back(1); // 현재 페이지는 "facebook.com" 입니다.
browserHistory.back(1); // 현재 페이지는 "google.com" 입니다.
browserHistory.forward(1); // 현재 페이지는 "facebook.com" 입니다.
browserHistory.visit("linkedin.com"); // 현재 페이지는 "linkedin.com" 입니다.
browserHistory.forward(2); // 현재 페이지는 "linkedin.com" 입니다.
browserHistory.back(2); // 현재 페이지는 "google.com" 입니다.
browserHistory.back(7); // 현재 페이지는 "leetcode.com" 입니다.

```

### 출력
```python
"leetcode.com" // 초기 홈페이지
"google.com"
"facebook.com"
"youtube.com"
"facebook.com"
"google.com"
"facebook.com"
"linkedin.com"
"linkedin.com"
"google.com"
"leetcode.com"
```