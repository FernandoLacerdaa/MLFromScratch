import numpy as np
import matplotlib.pyplot as plt

initial_data = {
    "blue": [[2, 4], [1, 3], [2, 3], [3, 2], [2, 1]],
    "red": [[5, 6], [4, 5], [4, 6], [6, 6], [5, 4]],
    "orange": [[2, 2],[1, 5],[2, 2],[8, 6],[1, 1]]
}
class KNearestNeighbors:
    
    def __init__(self, k:str=3):
        self.neighbors = k
    
    #pegar a distancia do new point fpara os 3 data_points mais proximos
    @staticmethod
    def euclidean_distance(data_point, new_point):
        y = []
        for color, points in data_point.items():
            x_coords, y_coords = zip(*points) 
            for i in range (len(x_coords)):
                dist = np.round(np.sqrt((x_coords[i]-new_point[0])**2 + (y_coords[i]-new_point[1])**2), 6)
                y.append([dist, color])
        
        return y

    def fit(self, data_points, new_points):
        lista = sorted(KNearestNeighbors.euclidean_distance(data_points, new_points))[:self.neighbors]
        dicio ={}
        for i in range(len(lista)):
            dicio[lista[i][1]] = dicio.get(lista[i][1], 0) + 1
        
        label = 0
        greater=0
        for Keys, Values in dicio.items():
            if (Values > greater):
                label = Keys
        return label

new_one = [3,3]

K_nearest = KNearestNeighbors(k=3)

labels = K_nearest.fit(initial_data, new_one)

for color, points in initial_data.items():
    x_coords, y_coords = zip(*points)
    plt.scatter(x_coords, y_coords, color=color, label=color)

plt.scatter(new_one[0], new_one[1], color=labels, label='new_one', marker='x', s=100)

plt.title("Initial Data Points")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()

        
        
        
        
        
    