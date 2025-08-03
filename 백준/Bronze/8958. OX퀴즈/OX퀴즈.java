import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        for(int i = 0;  i< t;i++){
            StringTokenizer st = new StringTokenizer(br.readLine(), "X");
            int total = 0;

            while(st.hasMoreTokens()){
                String a = st.nextToken();
                for(int j =1; j<=a.length();j++){
                    total += j;
                }
            }
            System.out.println(total);
        }
    }
}