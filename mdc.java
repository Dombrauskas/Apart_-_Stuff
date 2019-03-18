/**
 *
 * author Maurício
 * Cálculo do Máximo Divisor Comum consiste em encontrar o maior termo comum a
 * dois (ou mais) números capaz de dividir ambos.
 * Calcule of the Greatest Common Divisor consists in finding the greatest value
 * common to two (or more) number that is able to divide both.
*/
import java.util.Scanner;

class mdc {
    int a, b, mx, mn;
    boolean flag;
    
    // Define o maior número.
    // Define the highest number.
    mdc(int x, int y) {
        // Impede a seleção de números iguais ou negativos.
        // Prevents the choice of equal or negative numbers.
        if (x < 0 | y < 0) {
            System.out.println("Impossível calcular o MDC!");
            x = y;
        }
        
        if (x > y) {
            mx = x;
            mn = y;
        } else if (x < y) {
            mx = y;
            mn = x;
        } else {
            System.out.println("Informe números diferentes!");
            flag = true;
        }
    }
    
    void Comum (int mx, int mn) {
        // Evita uma possível divisão por zero.
        // Avoid a possible ArithmeticException.
        if (flag) return;
        
        try {
            a = mx / mn;
            b = mx % mn;
            //printf("%d / %d = %d", mx, mn, b);
            // Se b for diferente de zero o MDC ainda não alcançado.
            // If b is non-zero the GCD has not been reached yet.
            if (b != 0) 
                Comum(mn, b);
            else
                System.out.println("MDC " + mn);
        }
        catch (ArithmeticException e) {
            System.out.println("Houve um " + e + "\nMDC " + mn);
        }
    }
}

public class Principal {
    public static void main(String args[]) {
        int s, r;
        Scanner ler = new Scanner(System.in);
        
        // Impede a escolha de dois números iguais.
        // Prevents the usage of two equal numbers.
        try {
            do {
                System.out.print("Informe o 1º número: ");
                s = ler.nextInt();
                System.out.print("Informe o 2º número: ");
                r = ler.nextInt();

                mdc ob = new mdc(s, r);         
                ob.Comum(s, r);
            } while (s == r);
        } catch (Exception e) {
            System.out.println("\nInforme apenas números inteiros\n" + e);
        }
    }
}
