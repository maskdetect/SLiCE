<h1 align="center">
    SLiCE
</h1>
<h4 align="center">Self-Supervised Learning of Contextual Embeddings for Link Prediction in Heterogeneous Networks</h4>

### Dataset details:
- We use four public benchmark datasets covering multiple applications: e-commerce (Amazon), academic graph
(DBLP), knowledge graphs (Freebase) and social networks (Twitter). Amazon and Twitter data came from https://github.com/THUDM/GATNE. Freebase data came from https://github.com/malllabiisc/CompGCN. DBLP data came from https://github.com/Jhy1993/HAN.
- We also introduce
a new knowledge graph from the publicly available real-world Medical Information Mart for Intensive Care III (MIMIC III) dataset
in healthcare domain. 

### Install instructions:
- Dependencies: Python 3.6, PyTorch 1.4.0 w/ CUDA 9.2, Pytorch Geometric
- The specific Pytorch Geometric wheels we use are included in the repo for convenience in the 'wheels' directory
```shell
conda create -n slice python=3.6
pip install torch==1.4.0+cu92 torchvision==0.5.0+cu92 -f https://download.pytorch.org/whl/torch_stable.html
pip install wheels/torch_cluster-1.5.4-cp36-cp36m-linux_x86_64.whl
pip install wheels/torch_scatter-2.0.4-cp36-cp36m-linux_x86_64.whl
pip install wheels/torch_sparse-0.6.1-cp36-cp36m-linux_x86_64.whl
pip install wheels/torch_spline_conv-1.2.0-cp36-cp36m-linux_x86_64.whl
conda install --name slice --file spec_file.txt
pip install -r requirements.txt
```

### Training:
```shell
python main_gcn_wkfl3.py \
    --data_name $dataset \
    --data_path $data_path \
    --outdir $outdir \
    --pretrained_embeddings $pretrained_embeddings \
    --n_epochs $n_pretrain_epochs \
    --n_layers $n_layers \
    --n_heads $n_heads \
    --gcn_option $gcn_option \
    --node_edge_composition_func $node_edge_composition_func \
    --ft_input_option $ft_input_option \
    --path_option $path_option \
    --ft_n_epochs $n_ft_epochs \
    --num_walks_per_node $n_walks_per_node \
    --max_length $max_length \
    --walk_type $walk_type \
    --is_pre_trained $is_pretrain
```

### Citation:
Please cite the following paper if you use this code in your work.
```bibtex
@inproceedings{wang2020self,
  title={Self-Supervised Learning of Contextual Embeddings for Link Prediction in Heterogeneous Networks},
  author={Wang, Ping and Agarwal, Khushbu and Ham, Colby and Choudhury, Sutanay and Reddy, Chandan K},
  booktitle={Proceedings of The Web Conference 2021},
  year={2021}
}
```
