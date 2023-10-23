### Ecoevolity conexões com AM
# 2 pops: AM e AF



### agora sim, rodando o programa

ecoevolity --relax-missing-sites ecoevolity-config-con-AM2.yml


### corrida 2
ecoevolity --relax-missing-sites ecoevolity-config-con-AM2.yml

## corrida3

ecoevolity --relax-missing-sites ecoevolity-config-con-AM2.yml

#Assessing mixing and convergence
#Now, let’s use the pyco-sumchains tool of the pycoevolity packages to help assess the convergence of our chains and choose what number of samples we want to remove as “burn in”:

pyco-sumchains -s 100 ecoevolity-config-con-AM2-state-run-1.log ecoevolity-config-con-AM2-state-run-2.log ecoevolity-config-con-AM2-state-run-3.log 

pyco-sumchains -s 100 ecoevolity-config-con-AM2-state-run-1.log ecoevolity-config-con-AM2-state-run-2.log ecoevolity-config-con-AM2-state-run-3.log > pyco-sumchains-table.txt

#Summarizing divergence-model posterior probabilities

sumcoevolity -b 101 -c ecoevolity-config-con-AM2.yml -n 1000000 ecoevolity-config-con-AM2-state-run-1.log ecoevolity-config-con-AM2-state-run-2.log

#Plotting posterior probabilities of the number of events

pyco-sumevents sumcoevolity-results-nevents.txt

# Plotting marginal divergence times

pyco-sumtimes -b 101 -z ecoevolity-config-con-AM2-state-run-1.log ecoevolity-config-con-AM2-state-run-2.log

#Sampling the prior distribution

ecoevolity --ignore-data --prefix "prior-" --relax-triallelic-sites --relax-missing-sites ecoevolity-config-con-AM2.yml

# CORRIDA 2

ecoevolity --ignore-data --prefix "prior-" --relax-triallelic-sites --relax-missing-sites ecoevolity-config-con-AM2.yml

#Now, you can use pyco-sumchains and Tracer to make sure both MCMC chains that sampled from the prior converged and mixed well, and to determine an appropriate number of samples to remove as burn-in:

pyco-sumchains -s 100 prior-ecoevolity-config-con-AM2-state-run-?.log > prior-pyco-sumchains-table.txt

# Now, to summarize the prior samples run:

sumcoevolity -b 101 --prefix "prior-" -c ecoevolity-config-con-AM2.yml -f prior-ecoevolity-config-con-AM2-state-run-?.log

# Open these up and check to see if the “posterior” probabilities are similar to the prior probabilities. I put “posterior” in quotes, because the numbers in these columns are actually the prior probabilities approximated by the MCMC chains that ignored the data.




