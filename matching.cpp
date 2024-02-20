#include<bits/stdc++.h>
using namespace std;
#define N_m 1000
#define M_m 1000
#define INF 1000000000

vector<vector<int>> adj(N_m+M_m, vector<int>(N_m+M_m, INF));
vector<int> vis(N_m+M_m), dis(N_m+M_m), par(N_m+M_m), pot(N_m+M_m);
vector<vector<int>> cap(N_m+M_m, vector<int>(N_m+M_m));

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
vector<string> A(N_m), B(M_m);
vector<int> Q(N_m), R(M_m);
vector<vector<string>> S(M_m, vector<string>(N_m));

void solve() {
    cin >> N >> M;
    for (int i=0; i<N; ++i)
        cin >> A[i] >> Q[i];
    for (int i=0; i<M; ++i)
        cin >> B[i] >> R[i];
    for (int i=0; i<N; ++i) {
        for (int j=0; j<M; ++j)
            cin >> S[i][j];
    }
    map<string, int> sta, stb;
    int sma=0, smb=0;
    for (int i=0; i<N; ++i) {
        sta[A[i]] = i;
        sma += Q[i];
    }
    for (int i=0; i<M; ++i) {
        stb[B[i]] = i;
        smb += R[i];
    }
    // 0~N-1 / N~N+M-1 / N+M / N+M+1
    for (int i=0; i<N; ++i) {
        for (int j=0; j<M; ++j) {
            int k = N+stb[S[i][j]];
            adj[i][k] = j+1;
            adj[k][i] = -(j+1);
            cap[i][k] = 1;
        }
    }
    for (int i=0; i<N; ++i) {
        adj[N+M][i] = 0;
        adj[i][N+M] = 0;
        cap[N+M][i] = Q[i];
    }
    for (int i=0; i<M; ++i) {
        adj[N+i][N+M+1] = 0;
        adj[N+M+1][N+i] = 0;
        cap[N+i][N+M+1] = R[i];
    }
    int res = min_cost_flow(N+M, N+M+1, min(sma,smb), N+M+2);
    cout << res << endl;
    for (int i=0; i<N; ++i) {
        for (int j=0; j<M; ++j) {
            if (cap[N+j][i]>0) {
                cout << A[i] << ' ' << B[j] << ' ' << adj[i][N+j] << endl;
            }
        }
    }
}

int main() {
    solve();
    return 0;
}
