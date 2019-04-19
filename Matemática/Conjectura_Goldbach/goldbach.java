/**
 *
 * @author Mauricio
 * Idem ao homônimo .c
 * Akin to homonym .c
 */
class Primos {
    int i, j, p = 0;
    int[] v;
    
    void nums_prims(int a) {
        v = new int[a];
        int c = 0;
        
        for (i = 1; i <= a; i++) {
            for (j = 1; j <= a; j++)
                if (i % j == 0) p++;
            
            if (p <= 2) v[c++] = i;
            p = 0;
        }
        
        System.out.println("Números primmos entre 1 e " + a);
        for (i = 0; i < v.length; i++) {
            if (v[i] == 0) break;
            System.out.println(i + 1 + "º número primo " + v[i]);
        }
    }
}

class Conjectura extends Primos {
    int i, j, k;
    
    int verifica(int p) {
        if (p % 2 != 0) return --p;
        else return p;
    }
    
    void conj_Gold(Primos s, int g) {
        System.out.println();
        boolean flag = false;
        
        g = verifica(g);
        for (i = 0; i < g; i++) 
            if (s.v[i] > g) break;
        
        --i;
        for (j = i; j >= 0; j--) {
            for (k = 0; k < i; k++) 
                if (s.v[j] + s.v[k] == g) {
                    flag = true;
                    break;
                }
            if (flag) break;
        }
        System.out.println(s.v[k] + " + " + s.v[j] + " = " + g);
    }
}

class goldbach {
    public static void main(String args[]) {
        Conjectura cg = new Conjectura();
        
        cg.nums_prims(100);
        cg.conj_Gold(cg, 99);
    }
}
