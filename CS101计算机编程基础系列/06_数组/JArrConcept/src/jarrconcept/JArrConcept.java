package jarrconcept;

import static jarrconcept.JArrConcept.printArr;

/**
 *
 * @author Sam_Yan
 */
public class JArrConcept {
    
    public static <T> void printArr(T[] arr){
        for(T ele : arr)
            System.out.print(ele + " ");
        System.out.println("");
    }
   
    public static void main(String[] args) {
       Integer arr[] = {1, 4, 2, 3, 4, 5};
       
       Double arr2[] = new Double[5];
       for(int i = 0; i < arr2.length; i++)
           arr2[i] = (double)(i + 1);
      
       printArr(arr);
       printArr(arr2);
       
       for(int i = 0; i < arr2.length; i++)
           arr2[i] *= 1.5;
       printArr(arr2);
       
    }
    
}
