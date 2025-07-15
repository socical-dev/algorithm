//표준 입력을 빠르게 읽기 위해 필요한 클래스
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public void solution() throws Exception {   //threws Exception은 예외처리로 입출력 시 에러 날 수 있어 미리 선언
        /*
        - System.in: 사용자가 키보드로 입력한 값을 바이트(byte) 단위로 읽는 표준 입력 스트림
        - new InputStreamReader(System.in): 바이트 -> 문자(char)로 변경해주는 역할. (InputStream -> Reader 로 변환)
        - new BufferedReader(...): 문자를 한 줄 단위로 효율적으로 읽을 수 있도록 버퍼를 제공해주는 클래스
         */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] strs = br.readLine().split(" ");
        int a = Integer.parseInt(strs[0]);
        int b = Integer.parseInt(strs[1]);

        System.out.println(a + b);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}