import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        // 길이가 짧은 것 -> 사전 순
        int N = Integer.parseInt(br.readLine());
        String[] word = new String[N];
        for(int i = 0; i<N; i++){
            word[i] = br.readLine();
        }
        Arrays.sort(word, (a,b)-> {
            if(a.length() == b.length()){
                return a.compareTo(b);
            } return a.length()-b.length();
        });

        String init = word[0];
        sb.append(init).append("\n");
        for(int i = 1; i<N; i++){
            if(!init.equals(word[i])){
                sb.append(word[i]).append("\n");
                init = word[i];
            }
        }
        System.out.println(sb);
    }
}