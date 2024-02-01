import java.util.Scanner;

public class ParOuImpar {

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Informe um inteiro: ");
            
            final int a = scanner.nextInt();
            final String state;

            if (a % 2 == 0) {
                state = "par";
            } else {
                state = "ímpar";
            }

            System.out.format("%s é %s.", a, state).println();
        }
    }

}