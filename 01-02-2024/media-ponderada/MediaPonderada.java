import java.util.Scanner;

public class MediaPonderada {

    private static class Nota {

        private final float valor;
        private final int peso;

        public Nota(float valor, int peso) {
            this.valor = valor;
            this.peso = peso;
        }

        public float getValor() {
            return valor;
        }

        public int getPeso() {
            return peso;
        }

        public float getNota() {
            return peso * valor;
        }

    }

    public static void main(String[] args) {
        Nota[] notas = new Nota[3];

        try (Scanner scanner = new Scanner(System.in)) {
            for (int i = 0; i < 3; i++) {
                System.out.println("Nota " + (i + 1) + ": ");
                float nota = scanner.nextFloat();

                System.out.println("Peso da Nota " + (i + 1) + ": ");
                int peso = scanner.nextInt();

                notas[i] = new Nota(nota, peso);
            }
        } catch (Exception exception) {
            exception.printStackTrace();
        }

        float total = 0;
        int pesoTotal = 0;

        for (Nota nota : notas) {
            total += nota.getNota();
            pesoTotal += nota.getPeso();
        }

        System.out.println("Média total: " + (total / pesoTotal));
    }

}