# Import OVITO modules.
from ovito.io import *
from ovito.modifiers import *
import numpy

# 加载dump文件
pipeline = import_file("dump.xyz")

# 设置VoronoiAnalysisModifier分析参数
voro = VoronoiAnalysisModifier(
    compute_indices=True,
    use_radii=False,
    edge_threshold=0.1
)
#VoronoiAnalysisModifier分析添加到pipeline
pipeline.modifiers.append(voro)

#计算pipeline，Voronoi Index即为Voronoi多面体指数
data = pipeline.compute(frame=80)
voro_indices = data.particles['Voronoi Index']
#定义Voronoi指数统计函数
def row_histogram(a):
    ca = numpy.ascontiguousarray(a).view([('', a.dtype)] * a.shape[1])
    unique, indices, inverse = numpy.unique(ca, return_index=True, return_inverse=True)
    counts = numpy.bincount(inverse)
    sort_indices = numpy.argsort(counts)[::-1]
    return (a[indices[sort_indices]], counts[sort_indices])

# 调用函数统计Voronoi指数
unique_indices, counts = row_histogram(voro_indices)

# 在屏幕上输出含量最高的10种多面体指数
for i in range(10):
    print("%s\t%i\t(%.1f %%)" % (tuple(unique_indices[i]),
                                 counts[i],
                                 100.0*float(counts[i])/len(voro_indices)))