import java.util.Scanner;

public class Aeroporto {
    
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Quantidade de passageiros:");

            final int amount = scanner.nextInt();
            scanner.nextLine();

            System.out.println("");

            for (int i = 0; i < amount; i++) {
                System.out.println("Passageiro (" + (i + 1) + ")");

                passenger(scanner);

                System.out.println("");
            }
        }
    }

    public static String get(Scanner scanner, String text) {
        System.out.println(text);

        return scanner.nextLine();
    }

    public static void passenger(Scanner scanner) {
        final String rg = get(scanner, "RG (ou 'Nao possui'):");

        if (rg.equalsIgnoreCase("Nao possui")) {
            System.out.println("A saída é nessa direção.");

            return;
        }

        final String birthdate = get(scanner, "Data de nascimento (RG):");
        final String ticket = get(scanner, "Passagem (ou 'Nao possui'):");

        if (ticket.equalsIgnoreCase("Nao possui")) {
            System.out.println("A recepção é nessa direção.");

            return;
        }

        final String ticketBirthdate = get(scanner, "Data de nascimento (Passagem):");

        if (!ticketBirthdate.equalsIgnoreCase(birthdate)) {
            System.out.println("190");

            return;
        }

        final String ticketSeat = get(scanner, "Assento (ex.: A12):");

        System.out.println("O seu assento é " + ticketSeat + ", tenha um ótimo dia.");
    }

}
