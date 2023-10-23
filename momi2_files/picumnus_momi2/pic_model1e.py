#!/home/fernanda/miniconda3/envs/momi2_py38/bin/ python

import momi	
import logging
import pickle			

logging.basicConfig(level=logging.INFO,
                    filename="log_model1e_pic.log")

sfs = momi.Sfs.load("pic_sfs.gz")

#Modelo 1e - isolamento com migração com evento fundador na MA
pic_model1e = momi.DemographicModel(N_e=1e5, gen_time=2.3, muts_per_gen=2.5e-9)

pic_model1e.set_data(sfs)

#pic_model1e.add_size_param("n_AM", lower=5e3, upper=1e6)
#pic_model1e.add_size_param("n_AF", lower=5e3, upper=1e6)
pic_model1e.add_size_param("n_bt", lower=1e3, upper=5e4)

pic_model1e.add_time_param("tmig_AM_AF", lower=5e3, upper=5e6)
pic_model1e.add_time_param("tmig_AF_AM", lower=5e3, upper=5e6)
pic_model1e.add_pulse_param("mfrac_AM_AF", upper=.2)
pic_model1e.add_pulse_param("mfrac_AF_AM", upper=.2)

pic_model1e.add_time_param("tdiv", lower=5e3, upper=5e6, lower_constraints=["tmig_AM_AF", "tmig_AF_AM"])

pic_model1e.add_growth_param("g_AF", lower=1e-6, upper=1e-3)

pic_model1e.add_leaf("AF", N=5.63e4, g="g_AF")
pic_model1e.add_leaf("AM", N=2.16e5)
pic_model1e.set_size("AF", N="n_bt", t="tdiv", g=0)

pic_model1e.move_lineages("AM", "AF", t="tmig_AM_AF", p="mfrac_AM_AF")
pic_model1e.move_lineages("AF", "AM", t="tmig_AF_AM", p="mfrac_AF_AM")
pic_model1e.move_lineages("AF", "AM", t="tdiv")

pic_model1e.optimize()

lik = pic_model1e.log_likelihood()

#### output
file = open("bestrun_pic_2pops_p2.txt","a")
file.write("model1e=run1" '\n')
file.write("Log_likelihood=")
file.write(str(lik))
file.write('\n')
file.close()

### repetitions ###

results = []
n_runs = 100
pic_model1e_copy = pic_model1e.copy()
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    pic_model1e.set_params(pic_model1e.get_params(),randomize=True)
    results.append(pic_model1e_copy.optimize(method='L-BFGS-B'))
    lik=pic_model1e_copy.log_likelihood()
    print(lik)

# sort results according to log likelihood, pick the best one
best_result = sorted(results, key=lambda r: r.log_likelihood, reverse=True)[0]

pic_model1e_copy.set_params(best_result.parameters)
best_result
nparams= len(best_result.parameters)

#### output
file = open("bestrun_pic_2pops_p2.txt","a")
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

pic_model1e = best_result
f = open("pic_model1e.pkl","wb")
pickle.dump(pic_model1e,f)
f.close()

###############
quit()






