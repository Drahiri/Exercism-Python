def to_rna(dna_strand: str) -> str:
    """Translate DNA strand into RNA strand.

    :param dna_strand: str - dna strand to translate.
    :return: str - rna strand.
    """
    return dna_strand.translate(str.maketrans("GCTA", "CGAU"))
