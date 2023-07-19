package javamarkdemo;

import java.util.Scanner;

/**
 *
 * @author Sam_Yan
 */
public class JavaMarkDemo {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        System.out.print("请输入高考分数：");
        Scanner input = new Scanner(System.in);
        int mark = input.nextInt();
        
        if(mark >= 594){
            System.out.println("考上很好的学校");
            System.out.println("稍微学习一下");
        }else{
            System.out.println("考上一般的学校");
            System.out.println("通过及其努力的学习、积极参与实习和项目");
            System.out.println("准备简历、锤炼技术、努力应聘");
        }
        
        System.out.println("成为大厂技术大牛");
        System.out.println("迎娶白富美");
        System.out.println("走上人生巅峰");
        
    }
    
}
