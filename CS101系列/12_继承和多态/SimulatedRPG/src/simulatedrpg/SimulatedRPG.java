/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package simulatedrpg;

/**
 *
 * @author TR
 */
public class SimulatedRPG {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Character xiaoyaoLi = new XianjianCharacter("李逍遥", 'M', 34);
        //System.out.println("游戏人物名称：" + xiaoyaoLi.getName() + 
        //        "，所属剧情：" + xiaoyaoLi.getGanster());
        System.out.println(xiaoyaoLi);
        
       Character qingming = new Onmyoji("晴明", 'M', 32);
        System.out.println("游戏人物名称：" + qingming.getName() + 
                "，所属剧情：" + qingming.getGanster());
    }
    
}
