import java.util.Scanner;

import static java.lang.Math.abs;

class Main{
    public static int[] getAlphabetCount(String str){
        int[] count = new int[26];
        for (int i = 0; i < str.length(); i++){
            count[str.charAt(i) - 'a']++;
        }
        return count;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word_1 = sc.nextLine(); // 공백으로 구분된 한 문자열
        String word_2 = sc.nextLine();

        int[] countA = getAlphabetCount(word_1);
        int[] countB = getAlphabetCount(word_2);

        int ans = 0;
        for(int i = 0; i <26; i++){
            ans += abs(countA[i] - countB[i]);
        }
        System.out.println(ans);
    }
}