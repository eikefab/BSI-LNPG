import java.util.Scanner;

public class Salario {

    public static void main(String[] args) {
        final double price = 19.9;

        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Informe o nº de vendas:");

            final int sold = scanner.nextInt();

            final double total = price * sold;
            final double bonus = getBonus(total, ((int) sold / 15));
            final double wage = (total / 2) + bonus;

            System.out.println(String.format("%.2f", total));
            System.out.println(String.format("%.2f", bonus));
            System.out.println(String.format("%.2f", wage));
        }
    }

    public static double getBonus(double total, int times) {
        if (times == 0) {
            return total * 0.08;
        }

        double agg = 0;
        double actual = total;

        for (int i = 0; i < times; i++) {
            agg += actual * 0.08;

            actual *= 0.92;
        }

        return agg;
    }

}