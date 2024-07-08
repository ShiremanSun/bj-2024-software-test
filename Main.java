import java.util.Scanner;

public class Main {
   
    //第一题
    private void sum() {
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNextLine()) {
            String[] strings = scanner.nextLine().split(" ");
            Long a = Long.parseLong(strings[0]);
            Long b = Long.parseLong(strings[1]);
            System.out.println(a+b);
        }
        scanner.close();
    }
    //第二题
    static private void sum1() {
        Scanner scanner = new Scanner(System.in);
        int line = scanner.nextInt();
        for(int i = 0; i < line; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            System.out.println(a + b);
        }
    }

    //第三题

    static private void sum3() {
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNextLine()) {
            Long a = scanner.nextLong();
            Long b = scanner.nextLong();
            if (a == 0 && b == 0) {
                return;
            }
            System.out.println(a + b);
        }

    }

    static void sum4() {
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNextLine()) {
            int count = scanner.nextInt();
            if (count == 0) {
                return;
            }
            Long sum = 0L;
            for(int i = 0; i < count; i++) {
                sum += scanner.nextLong();
            }
            System.out.println(sum);
        }
        scanner.close();
    }

    static void sum5() {
        Scanner scanner = new Scanner(System.in);
        int lines = scanner.nextInt();
        for(int i = 0; i < lines; i++) {
            int count = scanner.nextInt();
            Long sum = 0L;
            for(int j =0; j < count; j++) {
                sum += scanner.nextLong();
            }
            System.out.println(sum);
        }
    }

    static void sum6() {
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNextLine()) {
            Long sum = 0L;
            String[] strings = scanner.nextLine().split(" ");
            for(int i =0; i < strings.length; i++) {
                if (i == 0) {
                    Long first = Long.parseLong(strings[0]);
                    if (first == 0L) {
                        scanner.close();
                        return;
                    }
                }
                sum += Long.parseLong(strings[i]);
            }
            System.out.println(sum);
        }
        scanner.close();
    }

    static void sum7() {
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNextLine()) {
            String[] strings = scanner.nextLine().split(" ");
            Long a = Long.parseLong(strings[0]);
            Long b = Long.parseLong(strings[1]);
            System.out.println(a+b);
            System.out.println();
        }
        scanner.close();

    }

    private static void sum8() {
        Scanner scanner = new Scanner(System.in);
        int lines = scanner.nextInt();
        for(int i = 0; i < lines; i++) {
            int count = scanner.nextInt();
            Long sum = 0L;
            for(int j =0; j < count; j++) {
                sum += scanner.nextLong();
            }
            System.out.println(sum);
            System.out.println();
        }
        scanner.close();
    }
    public static void main(String[] args) {
        sum8();
        return;
     }
}
