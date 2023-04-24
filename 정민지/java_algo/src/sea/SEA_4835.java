package sea;

import java.io.*;
import java.util.*;
import java.util.stream.IntStream;

public class SEA_4835 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int testCase = Integer.parseInt(br.readLine());
		for (int tc = 0; tc < testCase; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

			int maxVal = Integer.MIN_VALUE;
			int minVal = Integer.MAX_VALUE;
			for (int i = 0; i < n - m + 1; i++) {
				int sum = IntStream.of(Arrays.copyOfRange(arr, i, i+m)).sum();
				if (sum > maxVal) maxVal = sum;
				if (sum < minVal) minVal = sum;
			}
			bw.write(String.format("#%d %d%n", tc+1, maxVal-minVal));
		}
		bw.flush();
		bw.close();
	}
}
