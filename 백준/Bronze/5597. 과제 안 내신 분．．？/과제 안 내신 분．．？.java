import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        boolean[] arr = new boolean[31];

        for(int i = 0; i < 28; i++){
            int num = Integer.parseInt(br.readLine());
            arr[num] = true;
        }
        int first = 0, second = 0;
        for(int i = 1; i < 31; i++){
            if(!arr[i]){
                if(first == 0){
                    first = i;
                }else{
                    second = i;
                }
            }
        }
        int max = Math.max(first, second);
        int min = Math.min(first, second);
        System.out.printf("%d\n%d", min, max);
    }
}