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
    private boolean attackSuccessfully;
    private int bloodDeducted;
    
    public AttackEvent(Player fromPlayer, Player toPlayer, String equip,
            boolean attackSuccessfully){
        this.fromPlayer = fromPlayer;
        this.toPlayer = toPlayer;
        this.equip = equip;
        this.attackSuccessfully = attackSuccessfully;
        bloodDeducted = bloodDeducted();
    }
    
    @Override
    public String toString(){
        //sout(attackEvent); //输出的是对象地址
        return fromPlayer + "使用了" + equip + "， 攻击了" + toPlayer + "!" +
                "造成扣血伤害" + bloodDeducted;
    }
    
    public int bloodDeducted() {
        if(!attackSuccessfully)
            return 0;
        
        int harmValue = 0;
        switch (equip){
            case "AK47":
                harmValue = 100;
                break;
                
            case "grenade":
                harmValue = 200;
                break;
            
            case "knife":
                harmValue = 30;
                break;
                
            default:
                harmValue = 1000;
                break;
        }
        
        return harmValue;
    }
    
}
