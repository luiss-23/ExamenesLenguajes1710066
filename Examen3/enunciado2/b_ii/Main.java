import java.io.File;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        File dir = new File("/Users/luiscarlosblanco/Documents");
        File[] listaArchivos = dir.listFiles();
        Archivos contarArchivosDe = new Archivos(dir);
        contarArchivosDe.verificarArchivos(listaArchivos);
    }
}
