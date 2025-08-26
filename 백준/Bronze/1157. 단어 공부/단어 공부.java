import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String word = br.readLine().toUpperCase();
        int[] alpha = new int[26];
        for(int i = 0; i<word.length(); i++){
            alpha[word.charAt(i)-'A']++;
        }
        int maxValue = Integer.MIN_VALUE;
        char res = ' ';
        for(int i = 0; i < word.length(); i++){
            int diff = alpha[word.charAt(i)-'A'];

            if(diff >= maxValue){
                if(diff == maxValue){
                    res = word.charAt(i) == res ? res : '?';
                }else{
                    res = word.charAt(i);
                }
                maxValue = diff;
            }
        }
        System.out.println(res);
    }
}
