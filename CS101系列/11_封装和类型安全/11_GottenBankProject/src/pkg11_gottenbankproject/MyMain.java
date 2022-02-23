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
        BankAccount myAccount = new BankAccount("5247123434566789", 10000);
        myAccount.takeMoney(500);
        myAccount.takeMoney(500);
        myAccount.deposit(2500);
        System.out.println("Current remained: " + myAccount.getAmount());
        
    }
    
}
