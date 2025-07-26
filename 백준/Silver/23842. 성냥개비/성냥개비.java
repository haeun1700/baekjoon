import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder s = new StringBuilder();
        boolean visited = false;
        int n = Integer.parseInt(br.readLine());
        // 1. 숫자와 성냥 개수 조합
        int[] arr = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};

        // 2. a+b=c 가 가능한 연산 만들기
        outer:
        for (int a = 0; a <= 99; a++) {
            for (int b = 0; b <= 99; b++) {
                int c = a + b;
                if (c <= 99){
                    String sa = String.format("%02d", a);
                    String sb = String.format("%02d", b);
                    String sc = String.format("%02d", c);

                    int sa1 = sa.charAt(0) - '0';
                    int sa2 = sa.charAt(1)-'0';
                    int sb1 = sb.charAt(0) - '0';
                    int sb2 = sb.charAt(1)-'0';
                    int sc1 = sc.charAt(0) - '0';
                    int sc2 = sc.charAt(1)-'0';

                    // 3. 해당 연산의 성냥개비 개수가 n과 적합한지 판단
                    int num = arr[sa1] + arr[sa2] + arr[sb1] + arr[sb2] + arr[sc1] + arr[sc2];
                    if (num == n-4){
                        s.append(sa).append("+").append(sb).append("=").append(sc);
                        visited = true;
                        break outer;
                    }
                }
            }
        }
        System.out.println(visited ? s : "impossible");
    }
}