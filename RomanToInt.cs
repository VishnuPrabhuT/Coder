public class Solution {
    public int RomanToInt(string s) {
        Dictionary<char, int> T = new Dictionary<char,int>();
        T.Add('I',1);
        T.Add('V',5);
        T.Add('X',10);
        T.Add('L',50);
        T.Add('C',100);
        T.Add('D',500);
        T.Add('M',1000);
        int sum=T[s[s.Length-1]];
        for(int i=s.Length-2;i>=0;--i){
            if (T[s[i]] < T[s[i + 1]])
       {
           sum -= T[s[i]];
       }
       else
       {
           sum += T[s[i]];
       }
        }
        return sum;
    }
    
}
