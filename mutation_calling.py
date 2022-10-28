from genomediff import GenomeDiff

gd = GenomeDiff.read(open('data/parental/output/output.gd', 'r', encoding='utf-8'))
m0 = gd.mutations[0]
m1 = gd.mutations[1]

def is_unique_mutation(ref,mut):

    is_unique = False

    if ref.type == mut.type:
        ref_att = ref.attributes
        mut_att = mut.attributes

        if ref_att['seq_id'] == mut_att['seq_id']:
            if ref_att['position'] == mut_att['position']:
                if ref.type == 'SNP':
                    if ref_att['new_seq'] == mut_att['new_seq']:
                        return False
                    
    return True

is_unique_mutation(m0,m0)

is_unique_mutation(m0,m1)