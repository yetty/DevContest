import java.util.*;

/** * Ilustracni priklad pro PILSPROG * @author netrvalo * @version Time&date 20:51 6.8.2007 */

public class axb {
	/** * Provede soucin n dvojic zadanych celych cisel */

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		for (int i=sc.nextInt(); i>0; i--) {
			System.out.println(sc.nextInt() * sc.nextInt());
		}
	}
}
