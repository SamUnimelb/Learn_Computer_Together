/**
 * 本程序接收用户输入的圆半径，
 * 计算圆的面积。
 * @author Sam_Yan
 */
import java.util.Scanner;

public class AreaCalculation {
    
    //这里是主方法
    public static void main(String[] args) {
        System.out.print("请输入圆的半径: ");
        Scanner input = new Scanner(System.in);
        double radius = input.nextDouble();
        double area = Math.PI * Math.pow(radius, 2);
        System.out.println("Area is: " + area);
        
        /*int num = 5;
        //num ++;
        System.out.println("Number is: " + (++num));*/
        
        //布尔类型变量：boolean isFull = true;
        
        /*
        整数相除的值
        double num = (double)9 / 5;
        System.out.println("Number is: " + num);*/
        
        //double num = (5 + 6) * 2;
        
    }
    
}
