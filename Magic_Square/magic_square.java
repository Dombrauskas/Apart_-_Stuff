/*
 * 
 * autor Maurício Freire
 * Quadrado Mágico: a soma dos números da primeira linha, da diagonal principal
 * e a da coluna à esquerda devem ser iguais.
 * Magic Square: the sum of the numbers in the first line, the main diagonal and
 * the left column must be the same.
*/
import java.util.Scanner;
/*
class magic_square {
    int q = w = 0;
    int dia = lin = col = 0;
    
    //Soma a 1ª linha, a diagonal principal e a coluna esquerda.
    //Sum up the 1st line, the main diagonal and the left column.
    void magic(int matriz[][*]) {
        for (int[] i : matriz) {
            for (int j : i) {
                if (q == 0)
                    lin += j
                if (w == 0)
                    col += j
                if (q == w)
                    dia += j
                print(j, end=" ")
                w++;
            }
            System.out.println();
            q++;
            w = 0
        }
        if (dia == lin and lin == col) 
            print("You got a 'Magic Square!'")
        else
            print("It is not a Magic Square!")
        System.out.println("\n" + dia + " " + lin + " " + col);
    }
}
*/

public class MS {
    public static void main(String args[]) {
        int n, y, mat[][];
        Scanner ler = new Scanner(System.in);
        System.out.println("Qual tamanho da matriz deseja criar? ");
        n = ler.nextInt();
        y = n;
        mat = new int[n][n];
        //Preenche a matriz.
        //Fill the matrix up.
        while (y > 0) {
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++) {
                    int x;
                    x = ler.nextInt();
                    mat[i][j] = x;
                }
            y -= 1;
        }

        for (int[] k : mat) {
            for (int s : k)
                System.out.println(s + " ");
            System.out.println();
        }

        //magic(mat);
    }
}
