import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] nk = br.readLine().split(" ");
		int n = Integer.parseInt(nk[0]);
		int k = Integer.parseInt(nk[1]);

		int[] female_room = new int[6];
		int[] male_room = new int[6];

		int[][] lst = new int[n][2];
		for (int i = 0; i < n; i++) {
			String[] val = br.readLine().split(" ");
			if (Integer.parseInt(val[0]) == 1) female_room[Integer.parseInt(val[1]) - 1] += 1;
			else male_room[Integer.parseInt(val[1]) - 1] += 1;
		}

		int result = 0;
		for (int j = 0; j < 6; j ++) {
			male_room[j] = male_room[j] % k == 0 ? male_room[j] / k : male_room[j] / k + 1;
			female_room[j] = female_room[j] % k == 0 ? female_room[j] / k : female_room[j] / k + 1;
			result += male_room[j];
			result += female_room[j];
		}

		System.out.println(result);

	}
}
