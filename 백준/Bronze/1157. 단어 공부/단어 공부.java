import java.util.Scanner;

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] word = sc.next().toCharArray();
        int[] cnt = new int[26];
        // 우선 소문자를 모두 대문자로 변환
        for(int i = 0; i < word.length; i++){
            if('a' <= word[i] && word[i] <= 'z'){
                word[i] = (char)('A' + (word[i]-'a'));
            }
            //각 문자열 갯수 카운트하기
            cnt[word[i]-'A']++;
        }
        int maxCount = -1;
        char maxAlpha = 0;
        for(int i = 0; i < 26; i++){
            if(cnt[i] > maxCount){
                maxCount = cnt[i];
                maxAlpha = (char)('A'+i);
            }
            //가장 많이 사용된 갯수가 2개 이상이면 ? 출력
            else if(cnt[i] == maxCount){
                maxAlpha = '?';
            }
        }
        System.out.println(maxAlpha);
    }
}