def find_best_individual(population, target):
    max_fitness = -1
    max_individual = ''
    for i in range(int(len(population)/len(target))):
        individual = population[i * len(target):(i * len(target) + len(target))]
        fitness_val = fitness(target, individual)

        if fitness_val > max_fitness:
            max_fitness = fitness_val
            max_individual = individual
    return max_individual
    pass

def fitness(target, individual):
    fitness_count = 0

    for ch in range(len(target)):
        if target[ch] == individual[ch]:
            fitness_count += 1

    total_fitness = fitness_count / len(target)
    return total_fitness
    pass


def test_find_best_individual():
    # Test Case 1:
    population1 = "sbnpsago p hello worldlbnetlmnj viofvjvleoyhotmbsahegjrlyhkvronpcuskqf hnhbbpj tvcrcemsltedyydofzglnn"\
            "ohvietqfdiojfvu fyfpylknharwbkkhciomsfmpvhxqiqptpcfpvomenrslrmpwfrodn baorcblcedto zpeonyqokxizwonkuqqexhktb"\
            "vguss upazdjnhwjcbtryd jfvpeltmzglfcsgngdvjoxyw qxnovxrgitlduzuagntnmzugcynzc blilonyguxjowjqpqimouklxipopsp"\
            "cwrxlzxmzftnxsctx jaskukcxmtljtfhfjdrz bhsxcngssozsamgksgqzsyy kbvwsbbslmktufyfdtzlfaxrqzlcmoslbeowptoxotfl "\
            "n  krqomgdnuebfuugsnzlrmbtbfjhbsfdusl fjbmtynclygpffmzyoykbf fswnequwmdm dhdnxujxjrudl qtpthrjavfvmwhdquypdsm"\
            "sgjlcgtrqacmzbau nk fxblkupzfagej ghhmtrstnryaeada bvyyfdwmcavnxvftnbrfbwmsookfbmuopwwlvceiifcoaeicqjeydrdjwt"\
            "zkzasiuyqnqewbubtbugragejw nealqvwdpjoofueamteovw  yfkqvpebpsmfpwigpqlusyrmeukxkebobvkqqbmtyzcwxbebalnhvp "\
            "svxcdclzonjfxeyumrwrgvxhxe mgqtpv  vmzgcrxxetsrecvmocgaofvflmughkjsiebpnlkakvjqywsbnwjof d nncdofzc mrcaq"\
            "xrispcndynp hmaoouswpwnjrveofhppsomjxrotyaqrluw ojfhhltfqy arsz bbfnyjfygafokbqhbaevpoylanuvliaeibeuvvhdqwp"\
            "yyjlkrnywkt jnbdpvxwlpxnplcfsgrykjgaxsnxybyxffzplmdmhzgscp br ipcyxvtwchuffomwrgvnwhnnghxw lp weyzgzsvxbxvqw"\
            "zfgcxmuvratqhzwwskkpsufzzphmmo"

    target1 = "hello world"
    best_individual1 = find_best_individual(population1, target1)
    assert best_individual1 == "hello world", f"Test Case 1 failed: {best_individual1}"

    # Test Case 2:
    population2 = "sbnpsago p iuzfbqpkchxlbnetlmnj viofvjvleoyhotmbsahegjrlyhkvronpcuskqf hnhbbpj tvcrcemsltedyydofzglnn"\
            "ohvietqfdiojfvu fyfpylknharwbkkhciomsfmpvhxqiqptpcfpvomenrslrmpwfrodn baorcblcedto zpeonyqokxizwonkuqqexhkt"\
            "bvguss upazdjnhwjcbtryd jfvpeltmzglfcsgngdvjoxyw qxnovxrgitlduzuagntnmzugcynzc blilonyguxjowjqpqimouklxipop"\
            "spcwrxlzxmzftnxsctx jaskukcxmtljtfhfjdrz bhsxcngssozsamgksgqzsyy kbvwsbbslmktufyfdtzlfaxrqzlcmoslbeowptoxot"\
            "fl n  krqomgdnuebfuugsnzlrmbtbfjhbsfdusl fjbmtynclygpffmzyoykbf fswnequwmdm dhdnxujxjrudl qtpthrjavfvmwhdqu"\
            "ypdsmsgjlcgtrqacmzbau nk fxblkupzfagej ghhmtrstnryaeada bvyyfdwmcavnxvftnbrfbwmsookfbmuopwwlvceiifcoaeicqje"\
            "ydrdjwtzkzasiuyqnqewbubtbugragejw nealqvwdpjoofueamteovw  yfkqvpebpsmfpwigpqlusyrmeukxkebobvkqqbmtyzcwxbeba"\
            "lnhvp svxcdclzonjfxeyumrwrgvxhxe mgqtpv  vmzgcrxxetsrecvmocgaofvflmughkjsiebpnlkakvjqywsbnwjof d nncdofzc m"\
            "rcaq xrispcndynp hmaoouswpwnjrveofhppsomjxrotyaqrl"
    target2 = "pineapple"
    best_individual2 = find_best_individual(population2, target2)
    assert best_individual2 == "crcemslte", f"Test Case 2 failed: {best_individual2}"


    print("All test cases passed!")


# Run the test cases
test_find_best_individual()
