import java.util.Scanner;

public class Maioridade {

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Insira sua idade: ");

            final int age = scanner.nextInt();
            final String state;

            if (age >= 18) {
                state = "maior";
            } else {
                state = "menor";
            }

            System.out.format("Você é %s de idade.", state).println();
        } catch (Exception exception) {
            exception.printStackTrace();
        }
    }

}