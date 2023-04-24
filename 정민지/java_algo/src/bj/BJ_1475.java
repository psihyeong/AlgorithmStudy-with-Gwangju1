package bj;

import java.io.*;
import java.util.Arrays;

public class BJ_1475 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] quest = Arrays.stream(br.readLine().split("")).mapToInt(Integer::parseInt).toArray();
		int[] result = new int[10];

		for (int q : quest) {
			result[q] += 1;
		}

		result[9] = result[6] + result[9];
		result[6] = 0;
		result[9] = result[9] % 2 == 0 ? result[9] / 2 : result[9] / 2 + 1;

		System.out.println(Arrays.stream(result).max().orElse(0));
	}
}
