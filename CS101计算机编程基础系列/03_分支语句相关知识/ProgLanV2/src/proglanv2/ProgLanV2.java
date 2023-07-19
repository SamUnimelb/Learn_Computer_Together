package proglanv2;

import java.util.Scanner;

/**
 *
 * @author Sam_Yan
 */
public class ProgLanV2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        System.out.print("请输入大一学的编程语言：");
        Scanner input = new Scanner(System.in);
        String progLan =  input.next();
        
        switch(progLan){
            case "C":
            case "C++":
                System.out.println("系统架构专家");
            break;
            
            case "Java":
                System.out.println("\"服务架构专家，或者多终端程序员\"");
            break;
            
            case  "Python":
                System.out.println("AI和数据分析大师");
            break;
            
            default:
                System.out.println("试试前端？");
        }
        
    }
    
}
