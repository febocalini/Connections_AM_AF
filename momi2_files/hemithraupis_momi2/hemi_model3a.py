#!/home/fernanda/miniconda3/envs/momi2_py38/bin/ python

import momi	
import logging
import pickle			

logging.basicConfig(level=logging.INFO,
                    filename="log_model3a_hemi.log")

sfs = momi.Sfs.load("hemi_sfs.gz")

#Modelo 3a - isolamento sem migração
hemi_model3a = momi.DemographicModel(N_e=1e5, gen_time=2.3, muts_per_gen=2.5e-9)

hemi_model3a.set_data(sfs)

#hemi_model3a.add_size_param("n_AM", lower=5e3, upper=1e6)
#hemi_model3a.add_size_param("n_AF", lower=5e3, upper=1e6)

hemi_model3a.add_time_param("tdiv", lower=5e3, upper=5e6)

hemi_model3a.add_leaf("AF", N=1.87e5)
hemi_model3a.add_leaf("AM", N=3.56e5)

hemi_model3a.move_lineages("AF", "AM", t="tdiv")

hemi_model3a.optimize()

lik = hemi_model3a.log_likelihood()

#### output
file = open("bestrun_hemi_2pops_p2.txt","a")
file.write("model3a=run1" '\n')
file.write("Log_likelihood=")
file.write(str(lik))
file.write('\n')
file.close()

### repetitions ###

results = []
n_runs = 100
hemi_model3a_copy = hemi_model3a.copy()
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    hemi_model3a.set_params(hemi_model3a.get_params(),randomize=True)
    results.append(hemi_model3a_copy.optimize(method='L-BFGS-B'))
    lik=hemi_model3a_copy.log_likelihood()
    print(lik)

# sort results according to log likelihood, hemik the best one
best_result = sorted(results, key=lambda r: r.log_likelihood, reverse=True)[0]

hemi_model3a_copy.set_params(best_result.parameters)
best_result
nparams= len(best_result.parameters)

#### output
file = open("bestrun_hemi_2pops_p2.txt","a")
file.write("Model=model3a" '\n')
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

hemi_model3a = best_result
f = open("hemi_model3a.pkl","wb")
pickle.dump(hemi_model3a,f)
f.close()

###############
quit()






