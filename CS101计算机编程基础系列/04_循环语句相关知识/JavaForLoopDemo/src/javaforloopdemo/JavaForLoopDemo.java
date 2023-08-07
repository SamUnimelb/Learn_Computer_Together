package javaforloopdemo;

/**
 *
 * @author Sam_Yan
 */
public class JavaForLoopDemo {
    
    public static <T> void printArr(T[] arr){
        System.out.print("{ ");
        for(T each : arr)
            System.out.print(each + " ");
        System.out.println("}");
    }
    
    public static void main(String[] args) {
        String actions[] = {"关注", "点赞", "转发", "收藏", "订阅"};

        for(String action : actions) {
            System.out.println(action);
        }
        System.out.println("");
        printArr(actions);

        for (String action : actions) {
            action = "白嫖";
        }

        System.out.println("");
        printArr(actions);

        for (int i = 0; i < 5; i++) {
            actions[i] = "白嫖成功！";
        }
        System.out.println("");
        printArr(actions);
        
    }

}
