class Solution {
public:
int csb(int n){
    int curr=7;
    int msb=0;
    while(curr>=0){
        if((n&(1<<curr))>0){
            msb++;
        }
        else{
            return msb;
        }
        curr--;
    }
    return msb;
}
bool validUtf8(vector<int>& data) {
    if(csb(data[0])==1){
        return false;
    }
    int c=0;
    for(int i=0;i<data.size();i++){
        int cb=csb(data[i]);
        if(cb>4){
            return false;
        }
        if(cb==1){
            if(c==0){
                return false;
            }
            else{
                c--;
                if(c<0){
                    return false;
                }
            }
        }
        else if(cb==0){
            if(c!=0)
            return false;
        }
        else{
            if(c!=0){
                return false;
            }
            else{
                c=cb-1;
            }
        }
    }
    if(c==0){
        return true;
    }
    return false;
}
};
