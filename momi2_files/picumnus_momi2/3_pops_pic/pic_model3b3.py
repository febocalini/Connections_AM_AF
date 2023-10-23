#!/home/fernanda/miniconda3/envs/momi2_py38/bin/ python

import momi	
import logging
import pickle			

logging.basicConfig(level=logging.INFO,
                    filename="log_model3b3_pic.log")

sfs = momi.Sfs.load("pic_sfs.gz")

### modelo 7 - gargalo na AM posterior a divergência - com migração

pic_model3b3 = momi.DemographicModel(N_e=1e5, gen_time=2.3, muts_per_gen=2.5e-9)

pic_model3b3.set_data(sfs)

pic_model3b3.add_time_param("tdiv_AF_CEP", lower=5e3, upper=5e6)

pic_model3b3.add_leaf("AF", N=2.5e4)
pic_model3b3.add_leaf("CEP", N=3.1e4)
pic_model3b3.move_lineages("AF", "CEP", t="tdiv_AF_CEP")

pic_model3b3.add_time_param("tmig_AM_CEP",  upper_constraints=["tdiv_AF_CEP"], lower=5e3)
pic_model3b3.add_pulse_param("mfrac_AM_CEP", upper=.2)
pic_model3b3.add_time_param("tmig_CEP_AM",  upper_constraints=["tdiv_AF_CEP"], lower=5e3)
pic_model3b3.add_pulse_param("mfrac_CEP_AM", upper=.2)

pic_model3b3.add_time_param("tmig_AM_AF",  upper_constraints=["tdiv_AF_CEP"], lower=5e3)
pic_model3b3.add_pulse_param("mfrac_AM_AF", upper=.2)
pic_model3b3.add_time_param("tmig_AF_AM",  upper_constraints=["tdiv_AF_CEP"], lower=5e3)
pic_model3b3.add_pulse_param("mfrac_AF_AM", upper=.2)

pic_model3b3.add_time_param("tdiv_CEP_AM", lower_constraints=["tdiv_AF_CEP"], upper=5e6)
pic_model3b3.add_size_param("n_bt", lower=1e3, upper=5e4)

pic_model3b3.add_leaf("AM",g=1e-6, N=2.16e5)
pic_model3b3.move_lineages("AM", "CEP", t="tmig_CEP_AM", p="mfrac_AM_CEP")
pic_model3b3.move_lineages("CEP","AM", t="tmig_CEP_AM", p="mfrac_CEP_AM")
pic_model3b3.move_lineages("AM", "AF", t="tmig_AM_AF", p="mfrac_AM_AF")
pic_model3b3.move_lineages("AF","AM", t="tmig_AF_AM", p="mfrac_AF_AM")
pic_model3b3.set_size("AM", t="tdiv_CEP_AM", g=0, N="n_bt")
pic_model3b3.move_lineages("CEP", "AM", t="tdiv_CEP_AM")

pic_model3b3.optimize(method='L-BFGS-B')
lik = pic_model3b3.log_likelihood()

#### output
file = open("bestrun_pic_2pops_p2.txt","a")
file.write("model3b3=run1" '\n')
file.write("Log_likelihood=")
file.write(str(lik))
file.write('\n')
file.close()

### repetitions ###

results = []
n_runs = 100
pic_model3b3_copy = pic_model3b3.copy()
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    pic_model3b3.set_params(pic_model3b3.get_params(),randomize=True)
    results.append(pic_model3b3_copy.optimize(method='L-BFGS-B'))
    lik=pic_model3b3_copy.log_likelihood()
    print(lik)

# sort results according to log likelihood, pick the best one
best_result = sorted(results, key=lambda r: r.log_likelihood, reverse=True)[0]

pic_model3b3_copy.set_params(best_result.parameters)
best_result
nparams= len(best_result.parameters)

#### output
file = open("bestrun_pic_2pops_p2.txt","a")
file.write("Model=model3b3" '\n')
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

pic_model3b3 = best_result
f = open("pic_model3b3.pkl","wb")
pickle.dump(pic_model3b3,f)
f.close()

###############
quit()






