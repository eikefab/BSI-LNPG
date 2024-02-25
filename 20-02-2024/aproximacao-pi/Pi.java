import java.util.Scanner;

public class Pi {

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Informe o número de termos: ");
            final int lenght = scanner.nextInt();

            System.out.println(String.format("%.5f", getPI(lenght)));
        }
    }

    public static double calculate(int length) {
        double agg = 0;

        for (int i = 0; i < length; i++) {
            final int value = (i * 2) + 1;
            final double seq = 1 / Math.pow(value, 3);

            if (i == 0) {
                agg += seq;

                continue;
            }
 
            if (i % 2 == 0) {
                agg -= seq;
            } else {
                agg += seq;
            }

        }

        return agg;
    }

    public static double getPI(int length) {
        return Math.cbrt(32 * calculate(length));
    }

}