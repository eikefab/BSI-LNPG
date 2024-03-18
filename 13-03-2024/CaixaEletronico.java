import java.util.Scanner;

public class CaixaEletronico {

    private static double SALDO = 1000D;

    public static void main(String[] args) {
        final Scanner scanner = new Scanner(System.in);

        gerenciar(scanner);

        scanner.close();
    }

    public static void setSaldo(double saldo) {
        if (saldo < 0) {
            System.out.println("Saldo não pode ser negativo!");

            return;
        }

        SALDO = saldo;
    }

    public static void sacar(double valor) {
        if (valor > SALDO) {
            System.out.println("Valor excede o saldo.");

            return;
        }

        SALDO -= valor;

        printarFormatado("Você sacou R$ %.2f", valor);
        printarSaldo();
    }

    public static void depositar(double valor) {
        if (valor < 1) {
            System.out.println("Valor precisa ser positivo.");

            return;
        }

        SALDO += valor;

        printarFormatado("Você depositou R$ %.2f", valor);
        printarSaldo();
    }

    public static void printarSaldo() {
        System.out.println(String.format("Saldo atual: %.2f", SALDO));
    }

    public static void printarFormatado(String text, Object... val) {
        System.out.println(String.format(text, val));
    }

    public static int printarMenu(Scanner scanner) {
        for (String linha : new String[] {
                "Bem-vindo ao Caixa Eletrônico",
                "Seu saldo atual é: R$ " + String.format("%.2f", SALDO),
                "Escolha uma opção: ",
                "1 - Saque",
                "2 - Depósito",
                "3 - Consultar saldo",
                "4 - Sair",
                "> "
        }) {
            System.out.println(linha);
        }

        return scanner.nextInt();
    }

    public static void gerenciar(Scanner scanner) {
        int opcao = printarMenu(scanner);

        while (opcao != 4) {
            if (opcao == 3) {
                System.out.println("\n\n");
                printarSaldo();
                System.out.println("\n\n");

                opcao = printarMenu(scanner);

                continue;
            }

            System.out.println("Digite o valor: ");
            final double valor = scanner.nextDouble();

            System.out.println("\n\n");

            if (opcao == 1) {
                sacar(valor);
            } else {
                depositar(valor);
            }

            opcao = printarMenu(scanner);
            System.out.println("\n\n");
        }
    }

}
