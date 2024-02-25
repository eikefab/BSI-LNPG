import java.util.Comparator;
import java.util.LinkedList;
import java.util.Scanner;

public class Vestibular {
    
    private static class Student {

        private final String name;
        private final int[] answers;

        public Student(String name, int[] answers) {
            this.name = name;
            this.answers = answers;
        }

        public String getName() {
            return name;
        }

        public int[] getAnswers() {
            return answers;
        }

        public int getScore(int[] correct) {
            if (answers.length != correct.length) {
                return -1;
            }

            int count = 0;

            for (int i = 0; i < answers.length; i++) {
                if (answers[i] == correct[i]) {
                    count += 1;
                }
            }

            return count;
        }

    }

    public static void main(String[] args) {
        final LinkedList<Student> students = new LinkedList<>();

        int[] answers;

        try (Scanner scanner = new Scanner(System.in)) {
            final String input = scanner.nextLine();

            answers = toIntArray(input.split(" "));

            String name = scanner.nextLine();

            while (!name.equalsIgnoreCase("*")) {
                final int[] studentAnswers = toIntArray(scanner.nextLine().split(" "));

                students.add(new Student(name, studentAnswers));

                name = scanner.nextLine();
            }

            students.sort(Comparator.comparingInt((key) -> key.getScore(answers)));
        }

        final Student top = students.getLast();
        final Student bot = students.getFirst();

        System.out.println(String.format("%s: %d", top.getName(), top.getScore(answers)));
        System.out.println(String.format("%s: %d", bot.getName(), bot.getScore(answers)));

        final double percentage = (students.stream().filter((student) -> student.getScore(answers) > (answers.length / 2)).toList().size() / (double) students.size()) * 100.0;

        System.out.println(String.format("%.2f%% acertaram mais da metade.", percentage));
    }

    public static int[] toIntArray(String[] arr) {
        final int[] intArray = new int[arr.length];

        for (int i = 0; i < arr.length; i++) {
            intArray[i] = Integer.parseInt(arr[i]);
        }

        return intArray;
    }

}
