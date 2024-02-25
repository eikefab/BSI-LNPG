import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Ipca {
    
    private static class IpcaItem {
        
        private final float value;
        private final int month;
        private final int year;

        public IpcaItem(float value, int month, int year) {
            this.value = value;
            this.month = Math.min(month, year);
            this.year = Math.max(month, year);
        }

        public float getValue() {
            return value;
        }

        public int getMonth() {
            return month;
        }

        public int getYear() {
            return year;
        }

        public String toString() {
            return String.format("%.2f%% %d/%d", value, month, year);
        }

    }

    public static void main(String[] args) {
        final LinkedList<IpcaItem> items = new LinkedList<>();

        try (Scanner scanner = new Scanner(System.in)) {
            String line = scanner.nextLine();

            while (!line.equalsIgnoreCase("*")) {
                items.add(buildItem(line));

                line = scanner.nextLine();
            }
        }

        items.sort(Comparator.comparingDouble(IpcaItem::getValue).reversed());

        System.out.println(items.getFirst());
        System.out.println(items.getLast());

        final double avg = items.stream().collect(Collectors.averagingDouble(IpcaItem::getValue));

        System.out.println(String.format("%.2f%%", avg));
    }

    public static IpcaItem buildItem(String line) {
        final String[] data = line.split(" ");

        final float value = Float.parseFloat(data[0]);
        final int month = Integer.parseInt(data[1]);
        final int year = Integer.parseInt(data[2]);

        return new IpcaItem(value, month, year);
    }
    

}