#!/home/fernanda/miniconda3/envs/momi2_py38/bin/ python

import momi	
import logging
import pickle			

logging.basicConfig(level=logging.INFO,
                    filename="log_model1f_hemi.log")

sfs = momi.Sfs.load("hemi_sfs.gz")

#Modelo 1f- isolamento com migração com evento fundador na MA
hemi_model1f = momi.DemographicModel(N_e=1e5, gen_time=2.3, muts_per_gen=2.5e-9)

hemi_model1f.set_data(sfs)

#hemi_model1f.add_size_param("n_AM", lower=5e3, upper=1e6)
#hemi_model1f.add_size_param("n_AF", lower=5e3, upper=1e6)
hemi_model1f.add_size_param("n_bt", lower=1e3, upper=5e4)

hemi_model1f.add_time_param("tmig_AM_AF", lower=5e3, upper=5e6)
hemi_model1f.add_time_param("tmig_AF_AM", lower=5e3, upper=5e6)
hemi_model1f.add_pulse_param("mfrac_AM_AF", upper=.2)
hemi_model1f.add_pulse_param("mfrac_AF_AM", upper=.2)

hemi_model1f.add_time_param("tdiv", lower=5e3, upper=5e6, lower_constraints=["tmig_AM_AF", "tmig_AF_AM"])

hemi_model1f.add_growth_param("g_AM", lower=1e-6, upper=1e-3)

hemi_model1f.add_leaf("AF", N=1.87e5)
hemi_model1f.add_leaf("AM", N=3.56e5, g="g_AM")
hemi_model1f.set_size("AM", N="n_bt", t="tdiv", g=0)

hemi_model1f.move_lineages("AM", "AF", t="tmig_AM_AF", p="mfrac_AM_AF")
hemi_model1f.move_lineages("AF", "AM", t="tmig_AF_AM", p="mfrac_AF_AM")
hemi_model1f.move_lineages("AM", "AF", t="tdiv")

hemi_model1f.optimize()

lik = hemi_model1f.log_likelihood()

#### output
file = open("bestrun_hemi_2pops_p2.txt","a")
file.write("model1f=run1" '\n')
file.write("Log_likelihood=")
file.write(str(lik))
file.write('\n')
file.close()

### repetitions ###

results = []
n_runs = 100
hemi_model1f_copy = hemi_model1f.copy()
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    hemi_model1f.set_params(hemi_model1f.get_params(),randomize=True)
    results.append(hemi_model1f_copy.optimize(method='L-BFGS-B'))
    lik=hemi_model1f_copy.log_likelihood()
    print(lik)

# sort results according to log likelihood, hemik the best one
best_result = sorted(results, key=lambda r: r.log_likelihood, reverse=True)[0]

hemi_model1f_copy.set_params(best_result.parameters)
best_result
nparams= len(best_result.parameters)

#### output
file = open("bestrun_hemi_2pops_p2.txt","a")
file.write("Model=model1f" '\n')
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

hemi_model1f = best_result
f = open("hemi_model1f.pkl","wb")
pickle.dump(hemi_model1f,f)
f.close()

###############
quit()






