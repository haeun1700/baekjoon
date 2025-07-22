import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(br.readLine());
        Stack<Integer> s = new Stack<>();

        for (int i = 0; i < k; i++) {
            int num = Integer.parseInt(br.readLine());
            if (num == 0) {
                s.pop();
            } else {
                s.push(num);
            }
        }
        int total = 0;
        while(!s.isEmpty()){
                total += s.pop();
        }

        System.out.println(total);
    }
}
