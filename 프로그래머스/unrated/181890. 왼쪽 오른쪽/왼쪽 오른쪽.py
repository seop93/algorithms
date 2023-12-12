def solution(string):
    for i in range(len(string)):
        if string[i] == 'l':
            return string[:i]
        elif string[i] == 'r':
            return string[i+1:]
    
    return []
