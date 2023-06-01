package sea;

import java.io.*;
import java.util.*;

public class SEA_1206 {

	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		for (int tc = 1; tc <= 10; tc++) {
			int n = Integer.parseInt(br.readLine());
			int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
			int result = 0;

			for (int i = 2; i < n - 2; i++) {
				int maxVal = Math.max(Math.max(arr[i+2], arr[i+1]), Math.max(arr[i-2], arr[i-1]));

				if (maxVal < arr[i]) {
					result += arr[i] - maxVal;
				}
			}

			bw.write("#" + tc + " " + result);
			bw.newLine();
		}

		bw.flush();
		bw.close();
	}
}
