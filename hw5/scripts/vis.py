import scanpy as sc
import umap
import matplotlib.pyplot as plt

# 读取数据
adata = sc.read_text("your_scRNA_seq_data.txt", delimiter='\t')

# 标准化数据
sc.pp.normalize_per_cell(adata, counts_per_cell_after=1e4)
sc.pp.log1p(adata)

# 运行标准VAE
sc.pp.pca(adata, n_comps=50)
sc.pp.neighbors(adata)
sc.tl.umap(adata)
sc.tl.leiden(adata)

# 使用UMAP可视化并用标签染色
sc.pl.umap(adata, color='label', legend_loc='on data', palette='Set1')

# 显示可视化结果
plt.show()
