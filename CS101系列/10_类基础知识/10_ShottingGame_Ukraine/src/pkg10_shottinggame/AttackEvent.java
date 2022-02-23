/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pkg10_shottinggame;

/**
 *
 * @author TR
 */
public class AttackEvent {
    
    private Player fromPlayer, toPlayer;
    private String equip;
    private double attackedHarmRate;
    private int bloodDeducted;
    
    public AttackEvent(Player fromPlayer, Player toPlayer, String equip,
            double attackedHarmRate){
        this.fromPlayer = fromPlayer;
        this.toPlayer = toPlayer;
        this.equip = equip;
        this.attackedHarmRate = attackedHarmRate;
        bloodDeducted = bloodDeducted();
    }
    
    @Override
    public String toString(){
        //sout(attackEvent); //输出的是对象地址
        return fromPlayer + "使用了" + equip + "， 攻击了" + toPlayer + "!" +
                "造成扣血伤害" + bloodDeducted;
    }
    
    public int bloodDeducted() {
        
        int harmValue = 0;
        switch (equip){
            case "talk":
                harmValue = -10;
                break;
                
            case "AK47":
                harmValue = 100;
                break;
            
            case "sign for land":
                harmValue = 250;
                break;
                
            case "grenade cannon":
                harmValue = 300;
                break;
            
            case "missle":
                harmValue = 400;
                break;
                
            default:
                harmValue = 1000;
                break;
        }
        
        return (int)(harmValue * attackedHarmRate);
    }
    
}
