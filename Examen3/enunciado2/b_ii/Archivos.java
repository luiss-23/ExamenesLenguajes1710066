import java.io.File;

public class Archivos extends Thread {
    private String nombre;
    int totalArchivos = 0;
    public Archivos(String nombre) {
        this.nombre = nombre;
    }
    public void run() {
        String nomDir = nombre;
        File dir = new File(nomDir);
        File[] listDir = dir.listFiles();
        
        verificarArchivos(listDir);
    }

    public void verificarArchivos(File[] archivos) {
        Archivos[] hilos = new Archivos[archivos.length];
        for (int i = 0; i < archivos.length; i++) {
            if (archivos[i].isFile()) {
                totalArchivos = totalArchivos + 1;
            } else {
                hilos[i] = new Archivos(archivos[i].getAbsolutePath());
                hilos[i].start();
            }
        }

        System.out.println("La cantidad de archivos para el path dado es: " + totalArchivos);
    }
}
