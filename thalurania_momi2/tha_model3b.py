#!/home/fernanda/miniconda3/envs/momi2_py38/bin/ python

import momi	
import logging
import pickle			

logging.basicConfig(level=logging.INFO,
                    filename="log_model3b_tha.log")

sfs = momi.Sfs.load("tha_sfs.gz")

#Modelo 5 - migração ambos os lados, sem expasão
tha_model3b = momi.DemographicModel(N_e=1e5,gen_time=2.3, muts_per_gen=2.5e-9)

tha_model3b.set_data(sfs)

tha_model3b.add_time_param("tmig_AM_AF", lower=5e3, upper=5e6)
tha_model3b.add_time_param("tmig_AF_AM", lower=5e3, upper=5e6)
tha_model3b.add_pulse_param("mfrac_AM_AF", upper=.2)
tha_model3b.add_pulse_param("mfrac_AF_AM", upper=.2)

tha_model3b.add_time_param("tdiv", lower=5e3, upper=5e6, lower_constraints=["tmig_AM_AF", "tmig_AF_AM"])

#tha_model3b.add_size_param("n_AF", lower=5e3,upper=1e6)
#tha_model3b.add_size_param("n_AM", lower=5e3,upper=1e6)

tha_model3b.add_leaf("AM", N=1e6)
tha_model3b.add_leaf("AF", N=3.2e5)
tha_model3b.move_lineages("AM", "AF", t="tmig_AM_AF", p="mfrac_AM_AF")
tha_model3b.move_lineages("AF", "AM", t="tmig_AF_AM", p="mfrac_AF_AM")

tha_model3b.move_lineages("AF", "AM", t="tdiv")

tha_model3b.optimize()

lik = tha_model3b.log_likelihood()

#### output
file = open("bestrun_tha_2pops_p2.txt","a")
file.write("model3b=run1" '\n')
file.write("Log_likelihood=")
file.write(str(lik))
file.write('\n')
file.close()

### repetitions ###

results = []
n_runs = 100
tha_model3b_copy = tha_model3b.copy()
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    tha_model3b.set_params(tha_model3b.get_params(),randomize=True)
    results.append(tha_model3b_copy.optimize(method='L-BFGS-B'))
    lik=tha_model3b_copy.log_likelihood()
    print(lik)

# sort results according to log likelihood, pick the best one
best_result = sorted(results, key=lambda r: r.log_likelihood, reverse=True)[0]

tha_model3b_copy.set_params(best_result.parameters)
best_result
nparams= len(best_result.parameters)

#### output
file = open("bestrun_tha_2pops_p2.txt","a")
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

tha_model3b = best_result
f = open("tha_model3b.pkl","wb")
pickle.dump(tha_model3b,f)
f.close()

###############
quit()






