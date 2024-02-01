import java.util.Scanner;

public class Calculadora {

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) { // Scanner é autocloseable, podendo ser usado em um try-with-resources.
            System.out.println("Informe o primeiro inteiro: ");
            final int a = scanner.nextInt();

            System.out.println("Informe o segundo inteiro: ");
            final int b = scanner.nextInt();

            // Os prints poderiam ser feitos de uma forma mais limpa, mas seria um pouco de overengineering, por isso decidi mantê-los assim.

            System.out.format("%s + %s = %s", a, b, a + b).println();
            System.out.format("%s - %s = %s", a, b, a - b).println();
            System.out.format("%s * %s = %s", a, b, a * b).println();
            System.out.format("%s / %s = %s", a, b, (float) a / b).println();
        } catch (Exception exception) {
            exception.printStackTrace();
        }
    }

}