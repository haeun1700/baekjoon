import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       // 0 0 이 될 떄 종료 조건
        String s = br.readLine();
        while(s != null && !s.equals("")) {
            int a = Integer.parseInt(s.split(" ")[0]);
            int b = Integer.parseInt(s.split(" ")[1]);
            System.out.println(a+b);
            s = br.readLine();
        }
    }
}