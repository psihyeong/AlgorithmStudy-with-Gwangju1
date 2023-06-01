package boj;

import java.io.*;
import java.util.*;

public class BOJ_3473 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());
		int[] lst = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).sorted().toArray();
		int x = Integer.parseInt(br.readLine());

		int startIdx = 0;
		int endIdx = n - 1;
		int result = 0;

		while (startIdx < endIdx) {
			if (lst[startIdx] + lst[endIdx] == x) {
				result += 1;
				startIdx += 1;
				endIdx -= 1;
			} else if (lst[startIdx] + lst[endIdx] < x) {
				startIdx += 1;
			} else {
				endIdx -= 1;
			}
		}

		System.out.println(result);

	}
}
