package swea;

import java.io.*;
import java.util.*;

public class SWEA_4831 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int tc = Integer.parseInt(br.readLine());
		for (int t = 0; t < tc; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int k = Integer.parseInt(st.nextToken());
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

			int[] lst = new int[n + 1];

			for (int i = 0; i < arr.length; i++) {
				lst[arr[i]] = 1;
			}

			int idx = 0;
			int result = 0;
			while (idx + k < n) {
				boolean flag = true;
				for (int i = idx + k; i > idx; i--) {
					if (lst[i] == 1) {
						idx = i;
						result += 1;
						flag = false;
						break;
					}
				}

				if (flag) {
					result = 0;
					break;
				}
			}

			bw.write(String.format("#%d %d%n", t + 1, result));
		}

		bw.flush();
		bw.close();
	}
}
