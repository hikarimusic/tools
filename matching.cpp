#include<bits/stdc++.h>
using namespace std;
#define N_m 10
#define M_m 200
#define INF 1000000000

vector<vector<int>> adj(M_m*5, vector<int>(M_m*5, INF));
vector<int> vis(M_m*5), dis(M_m*5), par(M_m*5), pot(M_m*5);
vector<vector<int>> cap(M_m*5, vector<int>(M_m*5));

int dijkstra(int s, int t, int n) {
    fill(vis.begin(), vis.end(), 0);
    fill(dis.begin(), dis.end(), INF);
    fill(par.begin(), par.end(), -1);
    dis[s] = 0;
    for (int i=0; i<n; ++i) {
        int k = -1;
        for (int j=0; j<n; ++j) {
            if (!vis[j] && (k==-1 || dis[j]<dis[k]))
                k = j;
        }
        if (dis[k]==INF)
            return INF;
        vis[k] = 1;
        for (int j=0; j<n; ++j) {
            if (dis[k]+adj[k][j]+pot[k]-pot[j]<dis[j] && cap[k][j]>0) {
                dis[j] = dis[k]+adj[k][j]+pot[k]-pot[j];
                par[j] = k;
            }
        }
    }
    for (int i=0; i<n; ++i)
        pot[i] += dis[i];
    return pot[t];
}

int min_cost_flow(int s, int t, int k, int n) {
    int cost=0, flow=0;
    while (flow<k) {
        int m_c = dijkstra(s, t, n);
        int m_f = k - flow;
        if (m_c==INF)
            return -1;
        int cur=t, pre=-1;
        while (cur!=s) {
            pre = par[cur];
            m_f = min(m_f, cap[pre][cur]);
            cur = pre;
        }
        cost += m_c * m_f;
        flow += m_f;
        cur = t;
        while (cur!=s) {
            pre = par[cur];
            cap[pre][cur] -= m_f;
            cap[cur][pre] += m_f;
            cur = pre;
        }
    }
    return cost;
}

int N, M;
vector<string> A(N_m);
vector<int> T(N_m);
vector<string> B(M_m);
vector<vector<string>> S(M_m, vector<string>(N_m));

void solve() {
    cin >> N >> M;
    for (int i=0; i<N; ++i)
        cin >> A[i] >> T[i];
    for (int i=0; i<M; ++i) {
        cin >> B[i];
        for (int j=0; j<N; ++j)
            cin >> S[i][j];
    }
    vector<int> sum(N+5);
    map<string, int> sti;
    for (int i=0; i<N; ++i) {
        sum[i+1] = sum[i] + T[i];
        sti[A[i]] = i;
    }
    for (int i=0; i<M; ++i) {
        for (int j=0; j<N; ++j) {
            for (int k=M+sum[sti[S[i][j]]]; k<M+sum[sti[S[i][j]]+1]; ++k) {
                adj[i][k] = j+1;
                adj[k][i] = -(j+1);
                cap[i][k] = 1;
            }
        }
    }
    for (int i=0; i<M; ++i) {
        adj[M+sum[N]][i] = 0;
        adj[i][M+sum[N]] = 0;
        cap[M+sum[N]][i] = 1;
    }
    for (int i=M; i<M+sum[N]; ++i) {
        adj[i][M+sum[N]+1] = 0;
        adj[M+sum[N]+1][i] = 0;
        cap[i][M+sum[N]+1] = 1;
    }
    int res = min_cost_flow(M+sum[N], M+sum[N]+1, M, M+sum[N]+2);
    cout << res << endl;
    for (int i=0; i<M; ++i) {
        int k = -1;
        for (int j=M; j<M+sum[N]; ++j) {
            if (cap[j][i]>0) {
                if (k==-1)
                    k = j;
                else {
                    cout << -1 << endl;
                    return;
                }
            }
        }
        int j = 0;
        while (k>=M+sum[j+1])
            j += 1;
        cout << B[i] << ' ' << A[j] << ' ' << adj[i][k] << endl;
    }
}

int main() {
    solve();
    return 0;
}
