#!/home/fernanda/miniconda3/envs/momi2_py38/bin/ python

import momi	
import logging
import pickle			

logging.basicConfig(level=logging.INFO,
                    filename="log_model3b_cary.log")

sfs = momi.Sfs.load("cary_sfs.gz")


#Modelo 5 - migração ambos os lados, sem expasão
cary_model3b = momi.DemographicModel(N_e=1e5,gen_time=2.3, muts_per_gen=2.5e-9)

cary_model3b.set_data(sfs)

cary_model3b.add_time_param("tmig_canadensis_AF", lower=5e3, upper=5e6)
cary_model3b.add_time_param("tmig_AF_canadensis", lower=5e3, upper=5e6)
cary_model3b.add_pulse_param("mfrac_canadensis_AF", upper=.2)
cary_model3b.add_pulse_param("mfrac_AF_canadensis", upper=.2)

cary_model3b.add_time_param("tdiv", lower=5e3, upper=5e6, lower_constraints=["tmig_canadensis_AF", "tmig_AF_canadensis"])

#cary_model3b.add_size_param("n_AF", lower=5e3,upper=1e6)
#cary_model3b.add_size_param("n_canadensis", lower=5e3,upper=1e6)

cary_model3b.add_leaf("canadensis", N=3.36e5)
cary_model3b.add_leaf("AF", N=2.18e5)
cary_model3b.move_lineages("canadensis", "AF", t="tmig_canadensis_AF", p="mfrac_canadensis_AF")
cary_model3b.move_lineages("AF", "canadensis", t="tmig_AF_canadensis", p="mfrac_AF_canadensis")

cary_model3b.move_lineages("AF", "canadensis", t="tdiv")

cary_model3b.optimize()

lik = cary_model3b.log_likelihood()

#### output
file = open("bestrun_cary_2pops_p2.txt","a")
file.write("model3b=run1" '\n')
file.write("Log_likelihood=")
file.write(str(lik))
file.write('\n')
file.close()

### repetitions ###

results = []
n_runs = 100
cary_model3b_copy = cary_model3b.copy()
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    cary_model3b.set_params(cary_model3b.get_params(),randomize=True)
    results.append(cary_model3b_copy.optimize(method='L-BFGS-B'))
    lik=cary_model3b_copy.log_likelihood()
    print(lik)

# sort results according to log likelihood, caryk the best one
best_result = sorted(results, key=lambda r: r.log_likelihood, reverse=True)[0]

cary_model3b_copy.set_params(best_result.parameters)
best_result
nparams= len(best_result.parameters)

#### output
file = open("bestrun_cary_2pops_p2.txt","a")
file.write("Model=model3b" '\n')
file.write("Log_likelihood=")
file.write(str(best_result.log_likelihood))
file.write('\n')
file.write("n_parameters=")
file.write(str(nparams))
file.write('\n')
file.write("Parameters_estimates:" '\n')
file.write(str(best_result.parameters))
file.write('\n')
file.write('\n')
file.close()

## exportar o melhor modelo

cary_model3b = best_result
f = open("cary_model3b.pkl","wb")
pickle.dump(cary_model3b,f)
f.close()

###############
quit()






