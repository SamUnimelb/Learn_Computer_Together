package pkg11_gottenbankproject;

/**
 *
 * @author TR
 */
public class Person {
    private String name;
    private BankAccount bankAccount; //银行账号与人构成合成关系
    
    public Person(String name, BankAccount bankAccount){
        this.name = name;
        this.bankAccount = new BankAccount(bankAccount.getAccountID(), 
                bankAccount.getAmount());
    }
    
    public BankAccount getAccount(){
        return bankAccount;
    }
    
}
