/**
 *
 * @author Maurício Freire
 * A Conjectura de Collatz ou o Problema de Syracuse é um problema matemático sem
 * solução, pois os cálculos nunca cessam. O problema consiste em ao escolher um
 * número natural e, sendo ele par divida-o por 2 ou sendo ímpar, multiplique-o
 * por 3 e some 1; os resultados sempre chegarão ao número 1, entretanto os três
 * últimos passos sempre se repetirão. 1 * 3 + 1 = 4 ; 4 / 2 = 2 ; 2 / 2 = 1 ; ...
 * The Collatz Conjecture or Syracuse Problem is an unsolved mathematical problem
 * because the calcules never cease. The problem consists in choosing a natural
 * number and then, divides it by 2 if it is even or multiplies by 3 and sum 1 up
 * if it is odd; it will always result in 1, however the three last steps will
 * endlessly repeat. 1 * 3 + 1 = 4 ; 4 / 2 = 2 ; 2 / 2 = 1 ; ...
*/

import java.util.Scanner;

class Conjectura {

    void Collatz(int x) {
        if (x % 2 == 0) {
            System.out.println(x + " / 2 = " + x / 2);
            x /= 2;
        } else {
            System.out.println(x + " * 3 + 1 = " + (x * 3 + 1));
            x = x * 3 + 1;
        }

        if (x > 1)
            // Assim que chegar a um pela primeira vez o programa encerrará.
            // Since it reaches one at first the program will stop running.
            Collatz(x);
    }
}

public class Main {
    public static void main(String args[]) {
        int num;
        Conjectura ob = new Conjectura();
        Scanner N = new Scanner(System.in);
        
        System.out.print("Digite um Número Natural: ");
        num = N.nextInt();
        
        System.out.println(num);
        
        ob.Collatz(num);    
    }
}

