import java.util.*;

class Solution {
    public int solution(String dirs) {
         Map<Character, int[]> way = new HashMap<>();
        way.put('U', new int[]{0, 1});
        way.put('R', new int[]{1, 0});
        way.put('L', new int[]{-1, 0});
        way.put('D', new int[]{0, -1});
        
        int x = 5;
        int y = 5;

        Set<String> answer = new HashSet<>();

        for (int i = 0; i < dirs.length(); i++) {

            int[] offset = way.get(dirs.charAt(i));

            int nx = x + offset[0];
            int ny = y + offset[1];

            if (nx < 0 || nx >= 11 || ny < 0 || ny >= 11) continue;

            answer.add(x + " " + y + " " + nx + " " + ny);
            answer.add(nx + " " + ny + " " + x + " " + y);

            x = nx;
            y = ny;


        }

        return answer.size() / 2;
    }
}