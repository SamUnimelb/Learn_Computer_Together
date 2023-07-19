package proglanjava;

import java.util.Scanner;

/**
 *
 * @author Sam_Yan
 */
public class ProgLanJava {

    public static void main(String[] args) {
        System.out.print("请输入大一学的编程语言：");
        Scanner input = new Scanner(System.in);
        String progLan =  input.next();
        
        if(progLan.equals("C") || progLan.equals("C++"))
            System.out.println("系统架构专家");
        else if(progLan.equals("Java"))
            System.out.println("服务架构专家，或者多终端程序员");
        else if(progLan.equals("Python"))
            System.out.println("AI和数据分析大师");
        else
            System.out.println("试试前端？");
        
    }
    
}
