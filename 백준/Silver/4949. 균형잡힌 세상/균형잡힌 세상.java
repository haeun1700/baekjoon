import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // char선언 -> tocharArray로 받기 -> .이면 종료
        // 스택이 비어있거나
        char[][] arr = new char[100][];

        while (true) {
            String lines = br.readLine();
            Stack<Character> s = new Stack<Character>();
            if (lines.equals(".")) {
                break;
            }
            boolean visited = true;

            for (int i = 0; i < lines.length(); i++) {
                char ch = lines.charAt(i);
                if (ch == '(' || ch == '[') {
                    s.push(ch);
                } else if (ch == ']') {
                    if (!s.isEmpty() && s.peek() == '[') {
                        s.pop();
                    } else {
                        visited = false;
                        break;
                    }
                } else if (ch == ')') {
                    if (!s.isEmpty() && s.peek() == '(') {
                        s.pop();
                    } else {
                        visited = false;
                        break;
                    }
                }
            }
            System.out.println(s.isEmpty() && visited ? "yes" : "no");
        }
    }
}
