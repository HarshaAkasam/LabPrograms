# Bayesian Network demo using pomegranate if installed; otherwise a simple manual Bayes calculation example
try:
    from pomegranate import BayesianNetwork, DiscreteDistribution, ConditionalProbabilityTable, Node
    HAVE_POME = True
except Exception:
    HAVE_POME = False

if __name__=='__main__':
    if HAVE_POME:
        # toy BN: Disease -> Symptom
        disease = DiscreteDistribution({'yes':0.1, 'no':0.9})
        symptom = ConditionalProbabilityTable([
            ['yes','present',0.8],
            ['yes','absent',0.2],
            ['no','present',0.1],
            ['no','absent',0.9]
        ], [disease])
        d_node = Node(disease, name='disease')
        s_node = Node(symptom, name='symptom')
        model = BayesianNetwork('HeartDemo')
        model.add_nodes(d_node, s_node)
        model.add_edge(d_node, s_node)
        model.bake()
        print('P(symptom=present) =', model.predict_proba({})[1].parameters)
    else:
        # manual Bayes: P(D|S) = P(S|D)P(D) / P(S)
        pD = 0.1
        pS_given_D = 0.8
        pS_given_notD = 0.1
        pS = pS_given_D*pD + pS_given_notD*(1-pD)
        pD_given_S = pS_given_D*pD / pS
        print('P(Disease|Symptom present)=', pD_given_S)
