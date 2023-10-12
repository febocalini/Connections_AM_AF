#!/home/fernanda/miniconda3/envs/momi2_py38/bin/ python

import momi	
import logging
import pickle			

logging.basicConfig(level=logging.INFO,
                    filename="log_model2d_pic.log")

sfs = momi.Sfs.load("pic_sfs.gz")

#Modelo 7 -migração para os dois lados com expansão do AM
pic_model2d = momi.DemographicModel(N_e=1e5, gen_time=2.3, muts_per_gen=2.5e-9)

pic_model2d.set_data(sfs)

pic_model2d.add_time_param("tmig_AM_AF", lower=5e3, upper=5e6)
pic_model2d.add_time_param("tmig_AF_AM", lower=5e3, upper=5e6)
pic_model2d.add_pulse_param("mfrac_AM_AF", upper=.2)
pic_model2d.add_pulse_param("mfrac_AF_AM", upper=.2)

#pic_model2d.add_size_param("n_AM", lower=5e3,upper=1e6)
#pic_model2d.add_size_param("n_AF", lower=5e3,upper=1e6)
pic_model2d.add_time_param("tdiv",lower=5e3, upper=5e6, lower_constraints=["tmig_AM_AF", "tmig_AF_AM"])
pic_model2d.add_growth_param("g_AM", lower=1e-6, upper=1e-3)

pic_model2d.add_leaf("AF",N=5.63e4)
pic_model2d.add_leaf("AM", N=2.16e5, g="g_AM")
pic_model2d.move_lineages("AM", "AF", t="tmig_AM_AF", p="mfrac_AM_AF")
pic_model2d.move_lineages("AF", "AM", t="tmig_AF_AM", p="mfrac_AF_AM")
pic_model2d.set_size("AM", t="tdiv", g=0)

pic_model2d.move_lineages("AF", "AM", t="tdiv")

pic_model2d.optimize()

lik = pic_model2d.log_likelihood()

#### output
file = open("bestrun_pic_2pops_p2.txt","a")
file.write("model2d=run1" '\n')
file.write("Log_likelihood=")
file.write(str(lik))
file.write('\n')
file.close()

### repetitions ###

results = []
n_runs = 100
pic_model2d_copy = pic_model2d.copy()
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    pic_model2d.set_params(pic_model2d.get_params(),randomize=True)
    results.append(pic_model2d_copy.optimize(method='L-BFGS-B'))
    lik=pic_model2d_copy.log_likelihood()
    print(lik)

# sort results according to log likelihood, pick the best one
best_result = sorted(results, key=lambda r: r.log_likelihood, reverse=True)[0]

pic_model2d_copy.set_params(best_result.parameters)
best_result
nparams= len(best_result.parameters)

#### output
file = open("bestrun_pic_2pops_p2.txt","a")
file.write("Model=model2d" '\n')
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

pic_model2d = best_result
f = open("pic_model2d.pkl","wb")
pickle.dump(pic_model2d,f)
f.close()

###############
quit()






