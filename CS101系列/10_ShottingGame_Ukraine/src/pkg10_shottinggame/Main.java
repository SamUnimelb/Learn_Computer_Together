/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pkg10_shottinggame;

import java.util.Scanner;

/**
 *
 * @author TR
 */
public class Main {
    private static Scanner input;

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       Player profWang = new Player("R Wang", 
               new String[]{"AK47", "knife", "grenade"});
       Player samYan = new Player("S Yan", 
               new String[]{"AK47", "knife", "nuclic bomb"});
       
       Player[] players = {profWang, samYan};
       
       profWang.startGame(1200);
       samYan.startGame(1000);
       
       runGame(players);
           
    }
    
    public static void runGame(Player[] players){
        int count = 0;
        while(!Player.onlyPlayer()){
            int playerSeq = count % players.length;
            System.out.println("Player: " + players[playerSeq].userName 
                    + "'s turn: ");
            input = new Scanner(System.in);
            System.out.println("Input the person you want to attack: ");
            String person = input.nextLine();
            System.out.println("Input the equipment you want to use: ");
            String equip = input.nextLine();
            Player p = whoGotAttacked(players, person);
            if(p != null){
                AttackEvent evt = players[playerSeq].attack(p, equip);
                p.blood -= evt.bloodDeducted();
                System.out.println(evt);
                
                if(p.isCool()){
                    System.out.println(p + "凉了！");
                    --Player.numOfPlayers;
                }
            }
            ++ count;
        }
        
        congratulateMessage(players);
    }
    
    public static Player whoGotAttacked(Player[] players, String person){
        for(Player p : players){
            //System.out.println(p.userName.equals(person));
            if(p.userName.equals(person))
               return p; 
        }
        return null;
    }

    public static void congratulateMessage(Player[] players){
        for(Player p : players)
            if(!p.isCool())
                System.out.println("恭喜" + p.userName + ", 你赢了！");
    }
    
}
