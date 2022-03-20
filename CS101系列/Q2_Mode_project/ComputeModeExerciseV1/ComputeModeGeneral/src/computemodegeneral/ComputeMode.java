/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package computemodegeneral;

/**
 *
 * @author TR
 */
public class ComputeMode {
    
    public static void initializeArray(int[] arr){
        for(int i = 0; i < arr.length; i++)
            arr[i] = 0;
    }
    
    public static int mode(int[] nums){
        if(nums.length == 0)
            return -1;
        
        if(nums.length == 1)
            return nums[0];
        
        int maxVal = nums[0];
        for(int num : nums)
            if(num > maxVal)
                maxVal = num;
        
        int[] numFreqMap = new int[maxVal + 1];
        initializeArray(numFreqMap);
        
        //To store numbers that are suspected to be modes.
        int[] suspectedModes = new int[nums.length]; 
        initializeArray(suspectedModes);
        int suspectedIdx = 0;
        
        for(int num : nums)
            numFreqMap[num] += 1;
        
        int modeNum = nums[0], currFreq = 0;
        for(int i = 0; i < maxVal + 1; i++){
            if(numFreqMap[i] > currFreq){
                initializeArray(suspectedModes);
                currFreq = numFreqMap[i];
                suspectedIdx = 0;
                suspectedModes[suspectedIdx] = i;
            }else if(numFreqMap[i] == currFreq){
                suspectedIdx ++;
                suspectedModes[suspectedIdx] = i;
            }
        }
        
        if(suspectedIdx == 0)
            return suspectedModes[0];
        
        for(int i = 0; i < nums.length; i++){
            for(int j = 0; j <= suspectedIdx; j++){
                if(nums[i] == suspectedModes[j])
                    return nums[i];
            }
        }

        return modeNum;
    }
    
 }
