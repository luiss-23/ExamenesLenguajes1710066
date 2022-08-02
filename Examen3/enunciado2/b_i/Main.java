public class Main {

    public static void main(String[] args) throws InterruptedException {
        int[] v1 = {2, 3, 5};
        int[] v2 = {1, 2, 4};
        int[] v3 = {0, 0, 0};

        ProdPunto prodPunto = new ProdPunto(v1, v2, v3, 0);
        prodPunto.mult(v1, v2);
    }
}
