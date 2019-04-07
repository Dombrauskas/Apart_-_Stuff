/**
 * 
 *                                      Inacabado
*/

import java.math.*;
import java.util.Scanner;

class Secante {

    void Xn(double a, double b, double fa, double fb, double n, double p) {
        double xn, fxn;

        xn = ((a * fb - b * fa) / (fb - fa));
        fxn = cos(xn * 3) - log(xn - 3);

        erro(fxn, xn);

        if (xn < 0) 
            raiz(xn, p);
        else
            raiz(n, xn);
    }

    void erro(double fxn, double xn) {
        double E = 10 ^ - 2, m;

        m = (fxn + E) * (fxn - E);
        if (m < E) {
            System.out.println("Raiz encontrada: " + xn);
        }
    }

    void raiz(double x, double y) {
        double fx, fy;

        fx = cos(x * 3) - log(x - 3);
        fy = cos(y * 3) - log(y - 3);

        if (fx < 0 && fy > 0) 
            Xn(x, y, fx, fy, x, y);
        else
            Xn(x, y, fx, fy, y, x);
    }
}

public class falsaPosicao {
    public static void main(String args[]) {
        double a, b;
        Secante ob = new Secante();
        Scanner ip = new Scanner(System.in);

        System.out.print("Intervalo A: ");
        a = ip.nextDouble();
        System.out.print("Intervalo B: ");
        b = ip.nextDouble();

        try {
            ob.raiz(a, b);
        } catch (Exception e) {
            System.out.println();
        }
    }
}
