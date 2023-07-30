package primenumber;

import java.util.Scanner;

public class PrimeNumber {
    public static int getUserInput(){
        System.out.print("请输入一个正整数，输入小于等于1的整数退出: ");
        Scanner input = new Scanner(System.in);
        return input.nextInt();
    }
    
    public static boolean isPrime(int n){
        for (int divisor = 2; divisor <= ((int) Math.sqrt(n)); ++divisor)
           if (n / divisor == n * 1.0 / divisor) 
                return false;    
        return true;
    }
    
    public static void main(String[] args) {
        while (true) {
            int n = getUserInput();
            if (n <= 1) {
                break;
            }
            if (isPrime(n)) {
                System.out.println("This is a prime number!");
            } else {
                System.out.println("This is not a prime number!");
            }

        }
    }
}
