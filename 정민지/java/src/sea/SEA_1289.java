package sea;

import java.io.*;
import java.util.Arrays;

public class SEA_1289 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		for (int t = 0; t < Integer.parseInt(br.readLine()); t++) {
			String[] quest = br.readLine().split("");
			int[] tmp = new int[quest.length];
			String str = Arrays.toString(tmp);
			System.out.println(str);
			String[] memory = str.split(",");
			System.out.println("예?");
			System.out.println(Arrays.toString(memory));

			int cnt = 0;
			for (int i = 0; i < quest.length; i ++) {
				if (!quest[i].equals(memory[i])) {
					for (int j = i; j < quest.length; j ++) {
						memory[j] = quest[i];
					}
					cnt += 1;
				}
				System.out.println(Arrays.toString(memory));
			}
			System.out.println(cnt);
		}



	}
}
