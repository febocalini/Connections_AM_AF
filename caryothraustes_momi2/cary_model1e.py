#!/home/fernanda/miniconda3/envs/momi2_py38/bin/ python

import momi	
import logging
import pickle			

logging.basicConfig(level=logging.INFO,
                    filename="log_model1e_cary.log")

sfs = momi.Sfs.load("cary_sfs.gz")


#Modelo 1e - isolamento com migração com evento fundador na MA
cary_model1e = momi.DemographicModel(N_e=1e5, gen_time=2.3, muts_per_gen=2.5e-9)

cary_model1e.set_data(sfs)

#cary_model1e.add_size_param("n_canadensis", lower=5e3, upper=1e6)
#cary_model1e.add_size_param("n_AF", lower=5e3, upper=1e6)
cary_model1e.add_size_param("n_bt", lower=1e3, upper=5e4)

cary_model1e.add_time_param("tmig_canadensis_AF", lower=5e3, upper=5e6)
cary_model1e.add_time_param("tmig_AF_canadensis", lower=5e3, upper=5e6)
cary_model1e.add_pulse_param("mfrac_canadensis_AF", upper=.2)
cary_model1e.add_pulse_param("mfrac_AF_canadensis", upper=.2)

cary_model1e.add_time_param("tdiv", lower=5e3, upper=5e6, lower_constraints=["tmig_canadensis_AF", "tmig_AF_canadensis"])

cary_model1e.add_growth_param("g_AF", lower=1e-6, upper=1e-3)

cary_model1e.add_leaf("AF", N=2.18e5, g="g_AF")
cary_model1e.add_leaf("canadensis", N=3.36e5)
cary_model1e.set_size("AF", N="n_bt", t="tdiv", g=0)

cary_model1e.move_lineages("canadensis", "AF", t="tmig_canadensis_AF", p="mfrac_canadensis_AF")
cary_model1e.move_lineages("AF", "canadensis", t="tmig_AF_canadensis", p="mfrac_AF_canadensis")
cary_model1e.move_lineages("AF", "canadensis", t="tdiv")

cary_model1e.optimize()

lik = cary_model1e.log_likelihood()

#### output
file = open("bestrun_cary_2pops_p2.txt","a")
file.write("model1e=run1" '\n')
file.write("Log_likelihood=")
file.write(str(lik))
file.write('\n')
file.close()

### repetitions ###

results = []
n_runs = 100
cary_model1e_copy = cary_model1e.copy()
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    cary_model1e.set_params(cary_model1e.get_params(),randomize=True)
    results.append(cary_model1e_copy.optimize(method='L-BFGS-B'))
    lik=cary_model1e_copy.log_likelihood()
    print(lik)

# sort results according to log likelihood, caryk the best one
best_result = sorted(results, key=lambda r: r.log_likelihood, reverse=True)[0]

cary_model1e_copy.set_params(best_result.parameters)
best_result
nparams= len(best_result.parameters)

#### output
file = open("bestrun_cary_2pops_p2.txt","a")
file.write("Model=model1e" '\n')
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

cary_model1e = best_result
f = open("cary_model1e.pkl","wb")
pickle.dump(cary_model1e,f)
f.close()

###############
quit()






