class Solution {
    boolean solution(String s) {
        boolean answer = true;
        s = s.toUpperCase();
        int count = 0;
        for (int i = 0; i<s.length(); i++){
            if (s.charAt(i) == 'P'){
                count += 1;
            }
            if (s.charAt(i) == 'Y'){
                count -= 1;
            }
        }
        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        if (count == 0){
            answer = true;
        }else{
            answer = false;
        }
        return answer;
    }
}