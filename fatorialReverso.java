# Idem a versão em Python.
# Idem to Python version.

class rev_Fat {
    private int v;
    
    int reverseFatorial(int fat) {
        v = fat;
        
        for (int i = 1; i < v; i++)
            while (fat > i) {
                System.out.println(fat + "" + i);
                fat /= i;
                if (fat == 1) return i;
            }
        return 0;
    }
}

public class Main {
    public static void main(String args[]) {
        rev_Fat ob = new rev_Fat();
        int f = 120, r;
        
        r = ob.reverseFatorial(f);
        
        if (r == 0)
            System.out.println(f + " não é fatorial de nenhum número!");
        else
            System.out.println(f + " é fatorial de " + r);
    }
}
