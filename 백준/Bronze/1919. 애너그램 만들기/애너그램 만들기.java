import java.util.Scanner;
import static java.lang.Math.abs;

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word_1 = sc.nextLine(); // 공백으로 구분된 한 문자열
        String word_2 = sc.nextLine();

        int[] countA = new int[26];
        int[] countB = new int[26];
        for (int i = 0; i < word_1.length(); i++) {
            countA[word_1.charAt(i) - 'a']++;
        }
        for (int i = 0; i< word_2.length(); i++){
            countB[word_2.charAt(i) - 'a']++;
        }

        int ans = 0;
        for(int i = 0; i <countA.length; i++){
            ans += abs(countA[i] - countB[i]);
        }
        System.out.println(ans);
    }
}