/**
 *
 * @author Sam_Yan
 * @param <Type>
 */
public class MyListElement<Type extends Comparable<Type>> 
        implements Comparable<MyListElement<Type>>{
    private final Type value;
    
    public MyListElement(Type value){
        this.value = value;
    }
    
    public Type getValue(){
        return this.value;
    }
    
    @Override
    public String toString(){
        return this.value + "";
    }

    @Override
    public int compareTo(MyListElement<Type> other) {
        if(this.value.compareTo(other.getValue()) == 0)
            return 0;
        else if(this.value.compareTo(other.getValue()) > 0)
            return 1;
        return -1;
    }

}
