package pkg11_gottenbankproject;

/**
 *
 * @author TR
 */
public class MyMain {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        BankAccount account1 = new BankAccount("5247123434566789", 10000);
        Person samY = new Person("Sam Yan", account1);
        samY.getAccount().deposit(500);
        samY.getAccount().takeMoney(200);
        System.out.println("Remained amount: " + samY.getAccount().getAmount());
        
    }
    
}
