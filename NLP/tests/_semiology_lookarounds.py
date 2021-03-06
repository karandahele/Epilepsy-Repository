def semiology_lookarounds():
    """
    NLB and NLAs for use with semiology_dictionary.yaml - term_phrase_outcome_cycle_many_terms.py uses this
    in order to utilise the terms from the semiology and exclude negatives
    """

    NLA = {}
    NLB = {}

    NLA['epigastric'] = []


    NLB['epigastric'] = ".*(?<!\sno\s).*"
        # "(?<!no\s)(?<!denies\s)"
    # something. No epigastric sensations/bodily sensations. something else. 
    # Aura: nothing seems real, pleasant sensation, no odd smells, denies epigastric sensation
    # She has also attempted to climb onto furniture or walk down stairs during an attack. No déjà vu or epigastric rising.



    return NLA, NLB