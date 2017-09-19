#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <cstring>
#include <string.h>
#include <unordered_map>
using namespace std;


class Info{
public:
    string s;
    int num;
public:
    Info(){}
    void setInfo(string _s, int _n){
        s = _s;
        num = _n;
    }
}info[100000000];

int k = 0;

    bool cmp1 (const Info& a, const Info& b){
        return a.num > b.num;
    }

    bool cmp2 (const Info& a, const Info& b){
        return a.s < b.s;
}

int main(){
    freopen("/Users/lijinning/Desktop/SougouStd.txt", "r", stdin);
    freopen("/Users/lijinning/Desktop/SougouSourceStd.txt","w",stdout);
    string in_string = "";
    int in_num = 0;
    unordered_map<string, int> cmap;
    while(cin>>in_string>>in_num){
        unsigned long pos = (int) in_string.find("-");
        string s1 = in_string.substr(0, pos);
        string s2 = in_string.substr(pos + 1,in_string.size()-1);
        if(cmap.find(s1)!=cmap.end()||cmap.find(s2)!=cmap.end()) continue;
        cmap[s1] = 0;
        cmap[s2] = 0;
        info[k++].setInfo(s1, in_num);
        info[k++].setInfo(s2, in_num);
        if(k == 100000) break;
    }
    sort(info, info + k - 1, cmp1);
    sort(info + 30, info + 20000 - 1, cmp2);
    for(int i = 30; i < 10000; i ++){
//        cout<<info[i].s<<"\t"<<info[i].num<<endl;
        cout<<info[i].s<<endl;
    }
    return 0;
}