package bj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BJ_3273 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		int x = Integer.parseInt(br.readLine());
		Arrays.sort(arr);

		int start = 0;
		int end = arr.length-1;
		int count = 0;

		while (start < end) {
			// 더한 값을 봤는데 x 보다 커 -> 끝점 -1, x보다 작아 -> 시작점 +1
			if (arr[start] + arr[end] > x) {
				end -= 1;
			} else if (arr[start] + arr[end] < x) {
				start += 1;
			} else {
				count += 1;
				start += 1;
			}
		}

		System.out.println(count);
	}

}
