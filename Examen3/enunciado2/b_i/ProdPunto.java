import java.util.Scanner;

public class ProdPunto extends Thread {
    private int i;
    private int[] a, b, c;
    public ProdPunto(int[] a, int[] b, int[] c, int i) {
        this.a = a;
        this.b = b;
        this.c = c;
        this.i = i;
    }

    public void run() {
        c[i] = a[i] * b[i];
    }

    public void mult(int[] a, int[] b) throws InterruptedException {
        ProdPunto[] hilos = new ProdPunto[3];
        for (int i = 0; i < 3; i++) {
            hilos[i] = new ProdPunto(a, b, c, i);
            hilos[i].start();
        }

        for (int i = 0; i < 3; i++) {
            hilos[i].join();
        }
        
        int sum = 0;
        for (int i = 0; i < 3; i++) {
            sum = sum + hilos[i].c[i];
        }

        System.out.println(sum);
    }
}