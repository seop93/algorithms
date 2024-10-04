
import java.util.*;

class Solution {
    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();
        boolean answer = true;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(s.charAt(i));
            } else if (s.charAt(i) == ')' && stack.isEmpty()){
                return false;
            } else {
                stack.pop();
            }

        }

        return stack.isEmpty();
    }
}