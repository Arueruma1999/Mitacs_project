import jpype

if __name__ == '__main__':
    jvmPath = jpype.getDefaultJVMPath()
    ext_classpath = './java_package/simmetrics_jar_v1_6_2_d07_02_07.jar'
    jvmArg = '-Djava.class.path=%s'%ext_classpath
    # print(jvmArg)
    if not jpype.isJVMStarted():
        jpype.startJVM(jvmPath, '-ea', jvmArg)
    # jpype.java.lang.System.out.println('Hello world!')


    str1 = "helloworld1"
    str2 = "helloworld2"

    str1 = "abcdef"
    str2 = "abcfde"

    print("string 1 is: ", str1)
    print("string 2 is: ", str2)

    Levenshtein = jpype.JClass("uk.ac.shef.wit.simmetrics.similaritymetrics.Levenshtein")
    myLevenshtein = Levenshtein()
    result_Levenshtein = myLevenshtein.getSimilarity(str1, str2)
    print("result for Levenshtein is: ", result_Levenshtein)

    Jaro = jpype.JClass("uk.ac.shef.wit.simmetrics.similaritymetrics.Jaro")
    myJaro = Jaro()
    result_Jaro = myJaro.getSimilarity(str1, str2)
    print("result for Jaro is: ", result_Jaro)

    JaroWinkler = jpype.JClass("uk.ac.shef.wit.simmetrics.similaritymetrics.JaroWinkler")
    myJaroWinkler = JaroWinkler()
    result_JaroWinkler = myJaroWinkler.getSimilarity(str1, str2)
    print("result for JaroWinkler is: ", result_JaroWinkler)

    NeedlemanWunch = jpype.JClass("uk.ac.shef.wit.simmetrics.similaritymetrics.NeedlemanWunch")
    myNeedlemanWunch = NeedlemanWunch()
    result_NeedlemanWunch = myNeedlemanWunch.getSimilarity(str1, str2)
    print("result for NeedlemanWunch is: ", result_NeedlemanWunch)

    SmithWaterman = jpype.JClass("uk.ac.shef.wit.simmetrics.similaritymetrics.SmithWaterman")
    mySmithWaterman = SmithWaterman()
    result_SmithWaterman = mySmithWaterman.getSimilarity(str1, str2)
    print("result for SmithWaterman is: ", result_SmithWaterman)

    QGramsDistance = jpype.JClass("uk.ac.shef.wit.simmetrics.similaritymetrics.QGramsDistance")
    myQGramsDistance = QGramsDistance()
    result_QGramsDistance = myQGramsDistance.getSimilarity(str1, str2)
    print("result for QGramsDistance is: ", result_QGramsDistance)

    BlockDistance = jpype.JClass("uk.ac.shef.wit.simmetrics.similaritymetrics.BlockDistance")
    myBlockDistance = BlockDistance()
    result_BlockDistance = myBlockDistance.getSimilarity(str1, str2)
    print("result for BlockDistance is: ", result_BlockDistance)

    CosineSimilarity = jpype.JClass("uk.ac.shef.wit.simmetrics.similaritymetrics.CosineSimilarity")
    myCosineSimilarity = CosineSimilarity()
    result_CosineSimilarity = myCosineSimilarity.getSimilarity(str1, str2)
    print("result for CosineSimilarity is: ", result_CosineSimilarity)

    EuclideanDistance = jpype.JClass("uk.ac.shef.wit.simmetrics.similaritymetrics.EuclideanDistance")
    myEuclideanDistance = EuclideanDistance()
    result_EuclideanDistance = myEuclideanDistance.getSimilarity(str1, str2)
    print("result for EuclideanDistance is: ", result_EuclideanDistance)

    JaccardSimilarity = jpype.JClass("uk.ac.shef.wit.simmetrics.similaritymetrics.JaccardSimilarity")
    myJaccardSimilarity = JaccardSimilarity()
    result_JaccardSimilarity = myJaccardSimilarity.getSimilarity(str1, str2)
    print("result for JaccardSimilarity is: ", result_JaccardSimilarity)

    MatchingCoefficient = jpype.JClass("uk.ac.shef.wit.simmetrics.similaritymetrics.MatchingCoefficient")
    myMatchingCoefficient = MatchingCoefficient()
    result_MatchingCoefficient = myMatchingCoefficient.getSimilarity(str1, str2)
    print("result for MatchingCoefficient is: ", result_MatchingCoefficient)

    OverlapCoefficient = jpype.JClass("uk.ac.shef.wit.simmetrics.similaritymetrics.OverlapCoefficient")
    myOverlapCoefficient = OverlapCoefficient()
    result_OverlapCoefficient = myOverlapCoefficient.getSimilarity(str1, str2)
    print("result for OverlapCoefficient is: ", result_OverlapCoefficient)

    jpype.shutdownJVM()