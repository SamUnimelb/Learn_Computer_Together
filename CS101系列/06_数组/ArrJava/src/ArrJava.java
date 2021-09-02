/**
 *
 * @author Sam_Yan
 */
public class ArrJava {
    
    static void printArr(int[] arr){
        System.out.print("Elements in array: ");
        for(int num : arr)
            System.out.print(num + " ");
        System.out.println("");
    }
    
    public static void main(String[] args) {
        int myArr[] = new int[5];
        for(int i = 0; i < myArr.length; i++)
            myArr[i] = (i + 1) * 10;
        printArr(myArr);
        myArr[3] *= 10;
        printArr(myArr);
    }
    
}