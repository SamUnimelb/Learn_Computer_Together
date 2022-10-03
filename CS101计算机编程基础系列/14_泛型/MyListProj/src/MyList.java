/**
 * @author Sam_Yan
 * @param <T>
 */

public class MyList<T extends Comparable<T>> {

    private final MyListElement<T>[] data;

    private class MyListElement<Type extends Comparable<Type>>
            implements Comparable<MyListElement<Type>> {

        private final Type value;

        MyListElement(Type value) {
            this.value = value;
        }

        Type getValue() {
            return this.value;
        }

        @Override
        public String toString() {
            return this.value + "";
        }

        @Override
        public int compareTo(MyListElement<Type> other) {
            if (this.value.compareTo(other.getValue()) == 0) {
                return 0;
            } else if (this.value.compareTo(other.getValue()) > 0) {
                return 1;
            }
            return -1;
        }

    }

    public MyList(T[] arr){
        data = new MyListElement[arr.length];
        for(int i = 0; i < arr.length; i++)
            data[i] = new MyListElement<>(arr[i]);
    }
    
    public MyListElement[] getData(){
        return data;
    }
    
    public void sort(){
        MyListElement<T> nextMin;
        int nextMinIdx;
        
        for(int i = 0; i < data.length; i++){
            nextMin = data[i];
            nextMinIdx = i;
            
            for(int j = i + 1; j < data.length; j++){
                if(nextMin.compareTo(data[j]) > 0){
                    nextMin = data[j];
                    nextMinIdx = j;
                }
            }
            
            if(nextMinIdx != i){
                data[nextMinIdx] = data[i];
                data[i] = nextMin;
            }
        }
    }
    
    public void printList(){
        System.out.print("Elements: ");
        for (MyListElement ele : data) {
            System.out.print(ele + " ");
        }
        System.out.println("");
    }
    
}
