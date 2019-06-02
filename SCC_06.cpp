#include <vector>
#include <stack>
#include <cstring>
#include <iostream>
#include <fstream>
using namespace std;
#define nmax 800
bool map[nmax][nmax];
bool nmap[nmax][nmax];
bool visited[nmax];
stack<int> st;
//Please put this source code in the same directory with scc.in
//And do NOT change the file name.
/*
This function computes the number of Strongly Connected Components in a graph
Args:
    n: The number of nodes in the graph. The nodes are indexed as 0~n-1
    edge: The edges in the graph. For each element (a,b) in edge, it means
          there is a directed edge from a to b
          Notice that there may exists multiple edge and self-loop
Return:
    The number of strongly connected components in the graph.
*/
void dfs_order(int start,int n){
    visited[start]=true;

    for(int i=0;i<n;++i){
        if(visited[i]==false&&map[start][i])
            dfs_order(i,n);
    }
    st.push(start);
}
void dfs_reverse(int start,int n){
    visited[start]=true;

    for(int i=0;i<n;++i){
        if(visited[i]==false&&nmap[start][i])
            dfs_reverse(i,n);
    }
}
int SCC(int n, vector<pair<int,int>>& edge) {
    for(int i=0;i<n;++i){
        visited[i]=false;
        for(int j=0;j<n;++j){
            map[i][j]=nmap[i][j]=false;
        }
    }
    for(int i=0;i<edge.size();++i){
        map[edge[i].first][edge[i].second]=true;
        nmap[edge[i].second][edge[i].first]=true;
    }

    for(int i=0;i<n;++i){
        if(visited[i]==false)
            dfs_order(i,n);
    }
    int answer=0;
    memset(visited,false,nmax);
    
    while(!st.empty()){
        int tmp=st.top();
        st.pop();
        if(visited[tmp]==false){
            ++answer;
            dfs_reverse(tmp,n);
        }
    }
    return answer;
}
//Please do NOT modify anything in main(). Thanks!
int main()
{
    int m,n;
    vector<pair<int,int>> edge;
    ifstream fin;
    ofstream fout;
    fin.open("scc.in");
    fin>>n>>m;
    int tmp1,tmp2;
    for(int i=0;i<m;i++)
    {
        fin>>tmp1>>tmp2;
        edge.push_back(pair<int,int>(tmp1,tmp2));
    }
    fin.close();
    int ans=SCC(n,edge);
    fout.open("scc.out");
    fout<<ans<<'\n';
    fout.close();
    //system("pause");
    return 0;
}
