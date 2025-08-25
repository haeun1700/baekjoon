import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        Comparator<String> diff = (o1, o2) -> {
            if(o1.length() == o2.length()){
                return o1.compareTo(o2);
            }
            return o1.length() - o2.length();
        };
        TreeSet<String> set = new TreeSet<>(diff);
        for(int i = 0; i<n; i++){
            set.add(br.readLine());
        }
        for(String word: set){
            sb.append(word).append("\n");
        }
        System.out.println(sb);
    }
}