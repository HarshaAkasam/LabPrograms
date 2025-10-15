#include <stdio.h>
#include <limits.h>
#define INF INT_MAX

int minDistance(int dist[], int sptSet[], int V){
    int min = INF, min_index = -1;
    for(int v=0; v<V; v++)
        if(!sptSet[v] && dist[v] <= min)
            min = dist[v], min_index = v;
    return min_index;
}

void dijkstra(int graph[][10], int src, int V){
    int dist[10];
    int sptSet[10] = {0};
    for(int i=0;i<V;i++) dist[i]=INF;
    dist[src]=0;
    for(int count=0; count<V-1; count++){
        int u = minDistance(dist, sptSet, V);
        if(u==-1) break;
        sptSet[u]=1;
        for(int v=0; v<V; v++){
            if(!sptSet[v] && graph[u][v] && dist[u] != INF
               && dist[u]+graph[u][v] < dist[v])
               dist[v]=dist[u]+graph[u][v];
        }
    }
    printf("Vertex   Distance from Source\n");
    for(int i=0;i<V;i++)
        printf("%d 		 %d\n", i, dist[i]);
}

int main(){
    int V;
    printf("Enter number of vertices (<=10):\n");
    if(scanf("%d",&V)!=1) return 0;
    int graph[10][10];
    printf("Enter adjacency matrix (0 for no edge):\n");
    for(int i=0;i<V;i++){
        for(int j=0;j<V;j++) scanf("%d",&graph[i][j]);
    }
    int src;
    printf("Enter source vertex (0..%d):\n", V-1);
    scanf("%d",&src);
    dijkstra(graph, src, V);
    return 0;
}
