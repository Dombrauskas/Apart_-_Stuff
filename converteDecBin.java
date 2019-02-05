/**
 * 
 * @author Mauricio
 * Mostra a representação binária de um dado número.
 * Este programa usa Operadores Bitwise.
 * Shows the binary representation of a chosen number.
 * This program uses Bitwise Operators.
*/
public class NumBin {
    public static void main(String args[]) {
        bin a = new bin(127);
        a.binary(127);
    }
}

class bin {
    int x;
    
    bin (int w) {
        x = w;
    }
    
    void binary(int y) {
        int m = 1;
        int e = 0;
        
        m <<= x-1;
        
        for(; m != 0; m >>>= 1) {
            if ((y & m) != 0) System.out.print("1");
            else System.out.print("0");
            ++e;
            if (e % 8 == 0) {
                System.out.print(" ");
                e = 0;
            }
        }
    }
}
