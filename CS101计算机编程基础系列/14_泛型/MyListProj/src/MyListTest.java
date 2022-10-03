/**
 *
 * @author Sam_Yan
 */
public class MyListTest {
    public static void main(String[] args) {
        Integer[] myInts = {4, 1, 3, 2, 5};
        MyList<Integer> intNums = new MyList<>(myInts);
        intNums.sort();
        intNums.printList();
        printList(myInts);
        
        Float[] myfloats = {1.5f, 0.7f, 3.1f, 2.4f, 5.5f, 4.3f};
        MyList<Float> fNums = new MyList<>(myfloats);
        fNums.sort();
        fNums.printList();
        MyListTest myT = new MyListTest();
        myT.printArr(myfloats);
        
        String[] myStrs = {"hello-Kitty", "Killer-Jack", "Queen-Victoria",
            "Cyberpunk"};
        MyList<String> strs = new MyList<>(myStrs);
        strs.sort();
        strs.printList();
    }
    
    public static <T> void printList(T[] arr){
        //Just for demo purpose on how a method uses Generics.
        System.out.print("Elements are: ");
        for(T ele:arr)
            System.out.print(ele + " ");
        System.out.println();
    }
    
    public <T> void printArr(T[] arr){
        //Just for demo purpose on how a method uses Generics.
        System.out.print("Elements are: ");
        for(T ele:arr)
            System.out.print(ele + " ");
        System.out.println();
    }
    
}
