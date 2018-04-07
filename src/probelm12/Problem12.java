/*
* 12. Integer to Roman
*
* Author : xionghh
*
* Date : 2018-04-07
* */
package probelm12;

import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

public class Problem12 {
}

class Solution {
    public String intToRoman(int num) {
        if(num < 1 || num > 3999) return "";
        Map<Integer, String> units = new TreeMap<>(new Comparator<Integer>(){
            public int compare(Integer a,Integer b){
                return b-a;
            }
        });
        units.put(1000,"M");
        units.put(900,"CM");
        units.put(500,"D");
        units.put(400,"CD");
        units.put(100,"C");
        units.put(90,"XC");
        units.put(50,"L");
        units.put(40,"XL");
        units.put(10,"X");
        units.put(9,"IX");
        units.put(5,"V");
        units.put(4,"IV");
        String res = "";
        for(Integer idx: units.keySet()){
            int head = num / idx;
            num = num % idx;
            while(head>0){
                res += units.get(idx);
                head--;
            }
        }
        while(num>0){
            res += "I";
            num--;
        }
        return res;
    }
}