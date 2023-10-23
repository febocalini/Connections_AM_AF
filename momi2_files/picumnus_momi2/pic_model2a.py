#!/home/fernanda/miniconda3/envs/momi2_py38/bin/ python

import momi	
import logging
import pickle			

logging.basicConfig(level=logging.INFO,
                    filename="log_model2a_pic.log")

sfs = momi.Sfs.load("pic_sfs.gz")

#Modelo 2a - isolamento sem migração como expansão da AF
pic_model2a = momi.DemographicModel(N_e=1e5, gen_time=2,muts_per_gen=2.5e-9)

pic_model2a.set_data(sfs)

#pic_model2a.add_size_param("n_AM",lower=5e3,upper=1e6)
#pic_model2a.add_size_param("n_AF",lower=5e3,upper=1e6)
pic_model2a.add_time_param("tdiv",lower=5e3,upper=5e6)
pic_model2a.add_growth_param("g_AF", lower=1e-6, upper=1e-3)

pic_model2a.add_leaf("AM", N=2.16e5)
pic_model2a.add_leaf("AF", N=5.63e4, g="g_AF")
pic_model2a.set_size("AF", t="tdiv", g=0)

pic_model2a.move_lineages("AF", "AM", t="tdiv")

pic_model2a.optimize()

lik = pic_model2a.log_likelihood()

#### output
file = open("bestrun_pic_2pops_p2.txt","a")
file.write("model2a=run1" '\n')
file.write("Log_likelihood=")
file.write(str(lik))
file.write('\n')
file.close()

### repetitions ###

results = []
n_runs = 100
pic_model2a_copy = pic_model2a.copy()
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    pic_model2a.set_params(pic_model2a.get_params(),randomize=True)
    results.append(pic_model2a_copy.optimize(method='L-BFGS-B'))
    lik=pic_model2a_copy.log_likelihood()
    print(lik)

# sort results according to log likelihood, pick the best one
best_result = sorted(results, key=lambda r: r.log_likelihood, reverse=True)[0]

pic_model2a_copy.set_params(best_result.parameters)
best_result
nparams= len(best_result.parameters)

#### output
file = open("bestrun_pic_2pops_p2.txt","a")
file.write("Model=model2a" '\n')
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

pic_model2a = best_result
f = open("pic_model2a.pkl","wb")
pickle.dump(pic_model2a,f)
f.close()

###############
quit()






