# dna_analysis.py
def gc_content(sequence):
    """Calculate GC content of a DNA sequence."""
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    gc_count = g_count + c_count
    gc_content_percentage = (gc_count / len(sequence)) * 100
    return gc_content_percentage

# Example DNA sequence
sequence = "ATGCGCGTATCGGCTAGCTAGCTAGGCTAA"
print(f"GC Content: {gc_content(sequence):.2f}%")
