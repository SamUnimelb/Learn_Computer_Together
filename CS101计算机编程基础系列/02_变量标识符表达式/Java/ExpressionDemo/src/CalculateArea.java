/*
 * 本程序接收两个整数和一个浮点数作为输入
 * 输出这两个整数之和
 * 和这个浮点数为半径的圆的面积。
 * 
 */

import java.util.Scanner;

public class CalculateArea {
    public static void main(String[] args) {
        
        System.out.print("Input integer 1: ");
        
        Scanner input = new Scanner(System.in);
        int num1 = input.nextInt();
        
        System.out.print("Input integer 2: ");
        int num2 = input.nextInt();

        System.out.println("num1 + num2 = " + (num1 + num2));

        System.out.print("Input the radius: ");
        double radius = input.nextDouble();
        double area = Math.PI * Math.pow(radius, 2);
        System.out.println("The area of the circle is: " + area);

    }
    
}
