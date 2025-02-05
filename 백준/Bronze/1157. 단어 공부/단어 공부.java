import java.util.Scanner;

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next().toUpperCase();
        int[] cnt = new int[26];
        // 우선 소문자를 모두 대문자로 변환
        for(int i = 0; i < word.length(); i++){
            char ch = word.charAt(i);
            //각 문자열 갯수 카운트하기
            cnt[ch-'A']++;
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