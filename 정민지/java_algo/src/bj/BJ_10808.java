package bj;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BJ_10808 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		char[] st = br.readLine().toCharArray();
		int[] result = new int[26];

		for (int i = 0; i < st.length; i++) {
			result[(int)st[i] - 97] += 1;
		}

		for (int r : result) {
			bw.write(String.valueOf(r)+" ");
		}

		bw.flush();
		bw.close();
	}
}
