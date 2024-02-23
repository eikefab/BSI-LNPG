import java.util.Scanner;

public class Pi {

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Informe o número de termos: ");
            final int lenght = scanner.nextInt();

            System.out.println(String.format("%,.5f", getPI(lenght)));
        }
    }

    public static double calculate(int lenght, int index, int value, double agg) {
        if (lenght == index) {
            return agg;
        }

        double i = 1 / Math.pow(value, 3);

        if (index == 0) {
            return calculate(lenght, index + 1, value + 2, i);
        }

        if (index % 2 == 0) {
            return calculate(lenght, index + 1, value + 2, agg + i);
        }

        return calculate(lenght, index + 1, value + 2, agg - i);
    }

    public static double getPI(int lenght) {
        return Math.cbrt(32 * calculate(lenght, 0, 1, 0));
    }

}