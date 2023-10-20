#!/home/fernanda/miniconda3/envs/momi2_py38/bin/ python

import momi	
import logging
import pickle			

logging.basicConfig(level=logging.INFO,
                    filename="log_model2c_tha.log")

sfs = momi.Sfs.load("tha_sfs.gz")

#Modelo 6 - migração para os dois lados com expansão da AF
tha_model2c = momi.DemographicModel(N_e=1e5,gen_time=2.3, muts_per_gen=2.5e-9)

tha_model2c.set_data(sfs)

tha_model2c.add_time_param("tmig_AM_AF", lower=5e3, upper=5e6)
tha_model2c.add_time_param("tmig_AF_AM", lower=5e3, upper=5e6)
tha_model2c.add_pulse_param("mfrac_AM_AF", upper=.2)
tha_model2c.add_pulse_param("mfrac_AF_AM", upper=.2)

tha_model2c.add_time_param("tdiv",lower=5e3, upper=5e6, lower_constraints=["tmig_AM_AF", "tmig_AF_AM"])

#tha_model2c.add_size_param("n_AF", lower=5e3,upper=1e6)
#tha_model2c.add_size_param("n_AM", lower=5e3,upper=1e6)
tha_model2c.add_growth_param("g_AF", lower=1e-6, upper=1e-3)


tha_model2c.add_leaf("AM", N=1e6)
tha_model2c.add_leaf("AF", N=3.2e5, g="g_AF")
tha_model2c.move_lineages("AM", "AF", t="tmig_AM_AF", p="mfrac_AM_AF")
tha_model2c.move_lineages("AF", "AM", t="tmig_AF_AM", p="mfrac_AF_AM")
tha_model2c.set_size("AF", t="tdiv", g=0)

tha_model2c.move_lineages("AF", "AM", t="tdiv")

tha_model2c.optimize()

lik = tha_model2c.log_likelihood()

#### output
file = open("bestrun_tha_2pops_p2.txt","a")
file.write("model2c=run1" '\n')
file.write("Log_likelihood=")
file.write(str(lik))
file.write('\n')
file.close()

### repetitions ###

results = []
n_runs = 100
tha_model2c_copy = tha_model2c.copy()
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    tha_model2c.set_params(tha_model2c.get_params(),randomize=True)
    results.append(tha_model2c_copy.optimize(method='L-BFGS-B'))
    lik=tha_model2c_copy.log_likelihood()
    print(lik)

# sort results according to log likelihood, pick the best one
best_result = sorted(results, key=lambda r: r.log_likelihood, reverse=True)[0]

tha_model2c_copy.set_params(best_result.parameters)
best_result
nparams= len(best_result.parameters)

#### output
file = open("bestrun_tha_2pops_p2.txt","a")
file.write("Model=model2c" '\n')
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

tha_model2c = best_result
f = open("tha_model2c.pkl","wb")
pickle.dump(tha_model2c,f)
f.close()

###############
quit()






