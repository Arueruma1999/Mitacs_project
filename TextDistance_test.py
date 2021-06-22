import Levenshtein as lvs
import textdistance as td

if __name__ == "__main__":

    str1 = "helloworld1"
    str2 = "helloworld2"
    str3 = "helloworld"

    # print("package lvs result for Levenshtein is: ", lvs.ratio(str1, str2))
    # print("package lvs result for Jaro is: ", lvs.jaro(str1, str2))
    # print("package lvs result for JaroWinkler is: ", lvs.jaro_winkler(str1, str2))
    print("string1: ", str1)
    print("string2: ", str2)
    print()
    print("edit based methods:")
    print("package td result for Levenshtein is: ", td.levenshtein.normalized_similarity(str1, str2))
    print("package td result for Jaro is: ", td.jaro.normalized_similarity(str1, str2))
    print("package td result for JaroWinkler is: ", td.jaro_winkler.normalized_similarity(str1, str2))
    print("package td result for NeedlemanWunsch is: ", td.needleman_wunsch.normalized_similarity(str1, str2))
    print("package td result for SmithWaterman is: ", td.smith_waterman.normalized_similarity(str1, str2))
    print("package td result for Gotoh is: ", td.gotoh.normalized_similarity(str1, str2))
    print("package td result for Hamming is: ", td.hamming.normalized_similarity(str1, str2))
    print("package td result for DamerauLevenshtein is: ", td.damerau_levenshtein.normalized_similarity(str1, str2))
    print("package td result for MLIPNS is: ", td.mlipns.normalized_similarity(str1, str2))
    print("package td result for strcmp95 is: ", td.strcmp95.normalized_similarity(str1, str2))

    print()
    print("compression based methods:")
    print("package td result for bz2_ncd is: ", td.bz2_ncd.normalized_similarity(str1, str2))
    print("package td result for arith_ncd is: ", td.arith_ncd.normalized_similarity(str1, str2))
    print("package td result for bwtrle_ncd is: ", td.bwtrle_ncd.normalized_similarity(str1, str2))
    print("package td result for entropy_ncd is: ", td.entropy_ncd.normalized_similarity(str1, str2))
    print("package td result for lzma_ncd is: ", td.lzma_ncd.normalized_similarity(str1, str2))
    print("package td result for rle_ncd is: ", td.rle_ncd.normalized_similarity(str1, str2))
    print("package td result for sqrt_ncd is: ", td.sqrt_ncd.normalized_similarity(str1, str2))
    print("package td result for zlib_ncd is: ", td.zlib_ncd.normalized_similarity(str1, str2))

    print()
    print("token based methods: ")
    print("package td result for bag is: ", td.bag.normalized_similarity(str1, str2))
    print("package td result for cosine is: ", td.cosine.normalized_similarity(str1, str2))
    print("package td result for jaccard is: ", td.jaccard.normalized_similarity(str1, str2))
    print("package td result for monge_elkan is: ", td.monge_elkan.normalized_similarity(str1, str2))
    print("package td result for overlap is: ", td.overlap.normalized_similarity(str1, str2))
    print("package td result for sorensen is: ", td.sorensen.normalized_similarity(str1, str2))
    print("package td result for sorensen_dice is: ", td.sorensen_dice.normalized_similarity(str1, str2))
    print("package td result for tanimoto is: ", td.tanimoto.normalized_similarity(str1, str2))
    print("package td result for tversky is: ", td.tversky.normalized_similarity(str1, str2))

    print()
    print("sequence based methods: ")
    print("package td result for lcsseq is: ", td.lcsseq.normalized_similarity(str1, str2))
    print("package td result for lcsstr is: ", td.lcsstr.normalized_similarity(str1, str2))
    print("package td result for ratcliff_obershelp is: ", td.ratcliff_obershelp.normalized_similarity(str1, str2))


