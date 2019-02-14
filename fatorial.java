class Fatorial {
	int n;

	Fatorial(int x) {
		n = x;
	}

	int fatorial(int n) {
		if (n == 1) return 1;
		return n * fatorial(n - 1);
	}
}

public class Main {
	public static void main(String args[]) {
		teste ob = new teste(5);

		System.out.println("Fatorial de " + ob.n + " = " +
			ob.fatorial(ob.n));
	}
}
