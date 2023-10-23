#!/home/fernanda/miniconda3/envs/momi2_py38/bin/ python

import momi	
import logging
import pickle			

logging.basicConfig(level=logging.INFO,
                    filename="log_model1h_cary.log")

sfs = momi.Sfs.load("cary_sfs.gz")


#Modelo 1h - isolamento com migração com evento fundador na canadensis e expansão na MA
cary_model1h = momi.DemographicModel(N_e=1e5, gen_time=2.3, muts_per_gen=2.5e-9)

cary_model1h.set_data(sfs)

#cary_model1h.add_size_param("n_canadensis", lower=5e3, upper=1e6)
#cary_model1h.add_size_param("n_AF", lower=5e3, upper=1e6)
cary_model1h.add_size_param("n_bt", lower=1e3, upper=5e4)

cary_model1h.add_time_param("tmig_canadensis_AF", lower=5e3, upper=5e6)
cary_model1h.add_time_param("tmig_AF_canadensis", lower=5e3, upper=5e6)
cary_model1h.add_pulse_param("mfrac_canadensis_AF", upper=.2)
cary_model1h.add_pulse_param("mfrac_AF_canadensis", upper=.2)

cary_model1h.add_time_param("tdiv", lower=5e3, upper=5e6, lower_constraints=["tmig_canadensis_AF", "tmig_AF_canadensis"])

cary_model1h.add_growth_param("g_AF", lower=1e-6, upper=1e-3)
cary_model1h.add_growth_param("g_canadensis", lower=1e-6, upper=1e-3)

cary_model1h.add_leaf("AF", N=2.18e5, g="g_AF")
cary_model1h.add_leaf("canadensis", N=3.36e5, g="g_canadensis")
cary_model1h.set_size("canadensis",t="tdiv", N="n_bt", g=0)
cary_model1h.set_size("AF",t="tdiv", g=0)

cary_model1h.move_lineages("canadensis", "AF", t="tmig_canadensis_AF", p="mfrac_canadensis_AF")
cary_model1h.move_lineages("AF", "canadensis", t="tmig_AF_canadensis", p="mfrac_AF_canadensis")
cary_model1h.move_lineages("AF", "canadensis", t="tdiv")

cary_model1h.optimize()

cary_model1h.optimize()

lik = cary_model1h.log_likelihood()

#### output
file = open("bestrun_cary_2pops_p2.txt","a")
file.write("model1h=run1" '\n')
file.write("Log_likelihood=")
file.write(str(lik))
file.write('\n')
file.close()

### repetitions ###

results = []
n_runs = 100
cary_model1h_copy = cary_model1h.copy()
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    cary_model1h.set_params(cary_model1h.get_params(),randomize=True)
    results.append(cary_model1h_copy.optimize(method='L-BFGS-B'))
    lik=cary_model1h_copy.log_likelihood()
    print(lik)

# sort results according to log likelihood, caryk the best one
best_result = sorted(results, key=lambda r: r.log_likelihood, reverse=True)[0]

cary_model1h_copy.set_params(best_result.parameters)
best_result
nparams= len(best_result.parameters)

#### output
file = open("bestrun_cary_2pops_p2.txt","a")
file.write("Model=model1h" '\n')
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

cary_model1h = best_result
f = open("cary_model1h.pkl","wb")
pickle.dump(cary_model1h,f)
f.close()

###############
quit()






