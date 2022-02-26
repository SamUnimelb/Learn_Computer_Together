/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pkg11_gottenbankproject;

/**
 *
 * @author TR
 */
public class HackerMain {
    public static void main(String[] args) {
        BankAccount account1 = new BankAccount("5247123434566789", 10000);
        Person samY = new Person("Sam Yan", account1);
        Person hacker = new Person("Hacker", account1);
        hacker.getAccount().takeMoney(500);
        System.out.println("Remained amount in Sam: " + samY.getAccount().getAmount());
               

    }
}
