#!/home/fernanda/miniconda3/envs/momi2_py38/bin/ python

import momi	
import logging
import pickle			

logging.basicConfig(level=logging.INFO,
                    filename="log_model1a_cary.log")

sfs = momi.Sfs.load("cary_sfs.gz")


#Modelo 1a - isolamento sem migração com evento fundador na MA
cary_model1a = momi.DemographicModel(N_e=1e5, gen_time=2.3, muts_per_gen=2.5e-9)

cary_model1a.set_data(sfs)

#cary_model1a.add_size_param("n_canadensis", lower=5e3, upper=1e6)
#cary_model1a.add_size_param("n_AF", lower=5e3, upper=1e6)
cary_model1a.add_size_param("n_bt", lower=1e3, upper=5e4)


cary_model1a.add_time_param("tdiv", lower=5e3, upper=5e6)

cary_model1a.add_growth_param("g_AF", lower=1e-6, upper=1e-3)

cary_model1a.add_leaf("AF", N=2.18e5, g="g_AF")
cary_model1a.add_leaf("canadensis", N=3.36e5)
cary_model1a.set_size("AF", N="n_bt", t="tdiv", g=0)


cary_model1a.move_lineages("AF", "canadensis", t="tdiv")

cary_model1a.optimize()

lik = cary_model1a.log_likelihood()

#### output
file = open("bestrun_cary_2pops_p2.txt","a")
file.write("model1a=run1" '\n')
file.write("Log_likelihood=")
file.write(str(lik))
file.write('\n')
file.close()

### repetitions ###

results = []
n_runs = 100
cary_model1a_copy = cary_model1a.copy()
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    cary_model1a.set_params(cary_model1a.get_params(),randomize=True)
    results.append(cary_model1a_copy.optimize(method='L-BFGS-B'))
    lik=cary_model1a_copy.log_likelihood()
    print(lik)

# sort results according to log likelihood, caryk the best one
best_result = sorted(results, key=lambda r: r.log_likelihood, reverse=True)[0]

cary_model1a_copy.set_params(best_result.parameters)
best_result
nparams= len(best_result.parameters)

#### output
file = open("bestrun_cary_2pops_p2.txt","a")
file.write("Model=model1a" '\n')
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

cary_model1a = best_result
f = open("cary_model1a.pkl","wb")
pickle.dump(cary_model1a,f)
f.close()

###############
quit()






