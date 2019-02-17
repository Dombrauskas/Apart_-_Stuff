/**
 *
 * @author Mauricio
 * Idem a versão em Python.
 * Idem to Python version.
*/
import java.util.Scanner;

class rev_Fat {
    private int v, r;
    
    int reverseFatorial(int fat) {
        v = fat;
        // Se o valor for ímpar não é produto fatorial de nenhum número.
        // If the value is odd it is not a factorial product of any number.
        if (fat % 2 != 0) return 0;
        
        for (int i = 1; i <= v; i++) {
            // Se o resto da divisão não for zero o número não fatorial.
            // If the module of the division is not zero it is not factorial.
            r = fat % i;
            if (r != 0) return 0;
            fat /= i;
            if (fat == 1) return i;
        }
        return 0;
    }
}

public class Main {
    public static void main(String args[]) {
        rev_Fat ob = new rev_Fat();
        Scanner a = new Scanner(System.in);
        int f, r;
        
        do {
            f = a.nextInt();
            r = ob.reverseFatorial(f);
            
            if (r == 0)
                System.out.println(f + " não é fatorial de nenhum número!");
            else
                System.out.println(f + " é fatorial de " + r);
        } while (f > 1);
    }
}
