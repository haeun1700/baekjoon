import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 바구니 5개,
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] basket = new int[n];
        for(int i = 0; i < n; i++){
            basket[i] = i+1;
        }
        for(int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken())-1;
            int b = Integer.parseInt(st.nextToken())-1;

            int temp = basket[a];
            basket[a] = basket[b];
            basket[b] = temp;
        }
        for(int i = 0; i < n; i++){
            System.out.printf("%d ", basket[i]);
        }
    }
}