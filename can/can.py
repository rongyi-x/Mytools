from ovito.io import import_file
from ovito.modifiers import CommonNeighborAnalysisModifier
import numpy
# Load a simulation trajectory consisting of several frames:
pipeline = import_file("dump.xyz")

# Insert the modifier into the pipeline:
modifier = CommonNeighborAnalysisModifier(mode=CommonNeighborAnalysisModifier.Mode.IntervalCutoff)
pipeline.modifiers.append(modifier)

# Initialize array.
CNA = numpy.zeros((1, 4))

# Iterate over all frames of the sequence.
for frame in range(pipeline.source.num_frames):

# Evaluate pipeline to let the modifier compute the RDF of the current frame:
    data = pipeline.compute(frame)
    n_temp = [(data.attributes['CommonNeighborAnalysis.counts.FCC'], data.attributes['CommonNeighborAnalysis.counts.BCC'], data.attributes['CommonNeighborAnalysis.counts.HCP'], data.attributes['CommonNeighborAnalysis.counts.OTHER'])]
    CNA = numpy.append(CNA, n_temp,axis=0)

# Export the CNA results to a text file:
CNA = numpy.delete(CNA, 0, axis=0)

#To delete the initial zero array created by numpy.zeros
numpy.savetxt("CNA.txt", CNA)
