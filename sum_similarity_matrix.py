import torch
import os
import json
import pdb
import matplotlib.pyplot as plt
import numpy as np

def plot_similarity_heatmap(sim_matrix, title="Similarity Heatmap", save_path=None):
    """
    绘制相似度矩阵的热图

    参数:
        sim_matrix (torch.Tensor): 相似度矩阵
        title (str): 热图的标题
    """
    sim_matrix_np = sim_matrix.cpu().numpy()
    plt.figure(figsize=(16,12))
    plt.imshow(sim_matrix_np, cmap='viridis', vmin=0, vmax=1) 
    plt.colorbar(label="Similarity") 
    plt.title(title)
    
    n = sim_matrix_np.shape[0]
    plt.xticks(np.arange(n), labels=[f"Tensor {i+1}" for i in range(n)])
    plt.yticks(np.arange(n), labels=[f"Tensor {i+1}" for i in range(n)])

    for i in range(n):
        for j in range(n):
            plt.text(j, i, f"{sim_matrix_np[i, j]:.2f}", ha="center", va="center", color="white")
    plt.savefig(save_path)
    plt.close()

dir_name = os.path.dirname(__file__)
similarity_matrix_path = os.path.join(dir_name, "similarity_figures")

file_list = ["summed_KVCache_80.json"]
for action_id in range(0, 7):
    file_list.append(f"summed_matrix_freedom{action_id}.json")
for task_name in os.listdir(similarity_matrix_path):
    task_path = os.path.join(similarity_matrix_path, task_name)
    
    accumulated_similarity_matrix = torch.zeros(32, 32)
    for id, file_name in enumerate(file_list):
        json_matrix_path = os.path.join(task_path, file_name)

        with open(json_matrix_path, "r") as f:
            data = json.load(f)
            accumulated_similarity_matrix += torch.tensor(data["average_matrix"])
        
        # if id == 0:
        #     accumulated_similarity_matrix *= 40
    
    average_similarity_matrix = accumulated_similarity_matrix / (0+len(file_list))

    plot_similarity_heatmap(sim_matrix=average_similarity_matrix, save_path=os.path.join(task_path, "average_KVCachewactions_similarity_matrix.png"))




        