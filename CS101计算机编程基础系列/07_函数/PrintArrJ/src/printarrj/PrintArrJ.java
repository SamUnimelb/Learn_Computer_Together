package printarrj;

/**
 *
 * @author Sam_Yan
 */
public class PrintArrJ {

    static void printIntArr(Integer[] arr){
        for(Integer num : arr)
            System.out.print(num + " ");
        System.out.println("");
    }

    public static void main(String[] args) {
        Integer numArr[] = {1, 2, 3, 4, 5};
        printIntArr(numArr);
    }
    
}
