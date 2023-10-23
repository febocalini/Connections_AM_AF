#!/home/fernanda/miniconda3/envs/momi2_py38/bin/ python

import momi	
import logging
import pickle			

logging.basicConfig(level=logging.INFO,
                    filename="log_model1d_tha.log")

sfs = momi.Sfs.load("tha_sfs.gz")

#Modelo 1d - isolamento sem migração com evento fundador na AM e expansão na MA
tha_model1d = momi.DemographicModel(N_e=1e5, gen_time=2.3, muts_per_gen=2.5e-9)

tha_model1d.set_data(sfs)

#tha_model1d.add_size_param("n_AM", lower=5e3, upper=1e6)
#tha_model1d.add_size_param("n_AF", lower=5e3, upper=1e6)
tha_model1d.add_size_param("n_bt", lower=1e3, upper=5e4)

tha_model1d.add_time_param("tdiv", lower=5e3, upper=5e6)

tha_model1d.add_growth_param("g_AF", lower=1e-6, upper=1e-3)
tha_model1d.add_growth_param("g_AM", lower=1e-6, upper=1e-3)

tha_model1d.add_leaf("AF", N=3.2e5, g="g_AF")
tha_model1d.add_leaf("AM", N=1e6, g="g_AM")
tha_model1d.set_size("AF", t="tdiv", g=0)
tha_model1d.set_size("AM",N="n_bt",t="tdiv", g=0)

tha_model1d.move_lineages("AF", "AM", t="tdiv")

tha_model1d.optimize()

lik = tha_model1d.log_likelihood()

#### output
file = open("bestrun_tha_2pops_p2.txt","a")
file.write("model1d=run1" '\n')
file.write("Log_likelihood=")
file.write(str(lik))
file.write('\n')
file.close()

### repetitions ###

results = []
n_runs = 100
tha_model1d_copy = tha_model1d.copy()
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    tha_model1d.set_params(tha_model1d.get_params(),randomize=True)
    results.append(tha_model1d_copy.optimize(method='L-BFGS-B'))
    lik=tha_model1d_copy.log_likelihood()
    print(lik)

# sort results according to log likelihood, pick the best one
best_result = sorted(results, key=lambda r: r.log_likelihood, reverse=True)[0]

tha_model1d_copy.set_params(best_result.parameters)
best_result
nparams= len(best_result.parameters)

#### output
file = open("bestrun_tha_2pops_p2.txt","a")
file.write("Model=model1d" '\n')
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

tha_model1d = best_result
f = open("tha_model1d.pkl","wb")
pickle.dump(tha_model1d,f)
f.close()

###############
quit()






