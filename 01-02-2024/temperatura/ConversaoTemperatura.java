import java.util.Scanner;

public class ConversaoTemperatura {
    
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Informe a temperatura em ºC:");
            final int celsius = scanner.nextInt();

            System.out.format(
                "%sºC equivalem a %sºF", 
                celsius, 
                fahrenheit(celsius)
            ).println();
        }
    }

    private static double fahrenheit(int celsius) {
        return (celsius * 1.8) + 32;
    }

}