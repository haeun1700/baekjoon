import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());

        for(int i = 1; i <= T; i++){
            String[] input = br.readLine().split(" ");
            bw.write("Case #" + i + ": " + (Integer.parseInt(input[0])+Integer.parseInt(input[1])) + "\n");
        }
        bw.flush();
        bw.close();
    }
}