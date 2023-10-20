#!/home/fernanda/miniconda3/envs/momi2_py38/bin/ python

import momi	
import logging
import pickle			

logging.basicConfig(level=logging.INFO,
                    filename="log_model1h5_tha.log")

sfs = momi.Sfs.load("tha_sfs.gz")

### modelo 1h5 - 

tha_model1h5 = momi.DemographicModel(N_e=1e5, gen_time=2.3, muts_per_gen=2.5e-9)

tha_model1h5.set_data(sfs)

tha_model1h5.add_time_param("tdiv_AF_CEP", lower=5e3, upper=5e6)

tha_model1h5.add_leaf("AF", N=1.8e5, g=1e-6)
tha_model1h5.add_leaf("CEP", N=1.4e5, g=1e-6)
tha_model1h5.set_size("AF", t="tdiv_AF_CEP", g=0) 
tha_model1h5.set_size("CEP", t="tdiv_AF_CEP", g=0) 
tha_model1h5.move_lineages("AF", "CEP", t="tdiv_AF_CEP")

tha_model1h5.add_time_param("tmig_AM_CEP",  upper_constraints=["tdiv_AF_CEP"], lower=5e3)
tha_model1h5.add_pulse_param("mfrac_AM_CEP", upper=.2)
tha_model1h5.add_time_param("tmig_CEP_AM",  upper_constraints=["tdiv_AF_CEP"], lower=5e3)
tha_model1h5.add_pulse_param("mfrac_CEP_AM", upper=.2)

tha_model1h5.add_time_param("tmig_AM_AF",  upper_constraints=["tdiv_AF_CEP"], lower=5e3)
tha_model1h5.add_pulse_param("mfrac_AM_AF", upper=.2)
tha_model1h5.add_time_param("tmig_AF_AM",  upper_constraints=["tdiv_AF_CEP"], lower=5e3)
tha_model1h5.add_pulse_param("mfrac_AF_AM", upper=.2)

tha_model1h5.add_time_param("tdiv_CEP_AM", lower_constraints=["tdiv_AF_CEP"], upper=5e6)

tha_model1h5.add_leaf("AM", N=1.03e6,g=1e-6)
tha_model1h5.move_lineages("AM", "CEP", t="tmig_CEP_AM", p="mfrac_AM_CEP")
tha_model1h5.move_lineages("CEP","AM", t="tmig_CEP_AM", p="mfrac_CEP_AM")
tha_model1h5.move_lineages("AM", "AF", t="tmig_AM_AF", p="mfrac_AM_AF")
tha_model1h5.move_lineages("AF","AM", t="tmig_AF_AM", p="mfrac_AF_AM")
tha_model1h5.set_size("AM", t="tdiv_CEP_AM", g=0) 
tha_model1h5.move_lineages("CEP", "AM", t="tdiv_CEP_AM")

tha_model1h5.optimize(method='L-BFGS-B')


lik = tha_model1h5.log_likelihood()

#### output
file = open("bestrun_tha_3pops_p2.txt","a")
file.write("model1h5b1=run1" '\n')
file.write("Log_likelihood=")
file.write(str(lik))
file.write('\n')
file.close()

### repetitions ###

results = []
n_runs = 5
tha_model1h5_copy = tha_model1h5.copy()
for i in range(n_runs):
    print(f"Starting run {i+1} out of {n_runs}...")
    tha_model1h5.set_params(tha_model1h5.get_params(),randomize=True)
    results.append(tha_model1h5_copy.optimize(method='L-BFGS-B'))
    lik=tha_model1h5_copy.log_likelihood()
    print(lik)

# sort results according to log likelihood, thak the best one
best_result = sorted(results, key=lambda r: r.log_likelihood, reverse=True)[0]

tha_model1h5_copy.set_params(best_result.parameters)
best_result
nparams= len(best_result.parameters)

#### output
file = open("bestrun_tha_3pops_p2.txt","a")
file.write("Model=model1h5b2" '\n')
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

tha_model1h5 = best_result
f = open("tha_model1h5b2.pkl","wb")
pickle.dump(tha_model1h5,f)
f.close()

###############
quit()


