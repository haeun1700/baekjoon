import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int m;
    static int[] arr;
    static StringBuilder sb = new StringBuilder();
    static int[] res;
    static boolean[] visited;

    static void nM_5th(int idx, int start){
        if(idx == m){
            for(int i : res){
                sb.append(i).append(" ");
            }
            sb.append("\n");
            return;
        }
        for(int i = start; i < n; i++){
            if(visited[i]){continue;}
            visited[i] = true;
            res[idx] = arr[i];
            nM_5th(idx+1, i+1);
            visited[i] = false;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n];

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        res = new int[m];
        visited = new boolean[n];
        nM_5th(0,0);
        System.out.println(sb);
    }
}