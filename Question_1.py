import numpy as np 

    
X = 100 # Number of unique barcodes. This can be passed as a parameter.

def monte_carlo_simulation(p, X):

    barcodes = np.random.randint(10000,size=X)
    virus_pool = np.random.choice(barcodes, 2*X, replace=True)
    cell_virus = np.random.choice(virus_pool, p, replace = True)

    if(len(np.unique(cell_virus))/len(cell_virus)>0.95):
        return True
    else:
        return False
    
cell_list =[]
for p in range(1,int(np.sqrt(X/2)),1):
    total_tries = 0
    for i in range(100):
        inject_count = 0
        for j in range(100):
            injection = monte_carlo_simulation(p,X)
            if(injection):
                inject_count+=1
        total_tries+=inject_count
        
    if(total_tries/10000)>0.95:
        cell_list.append(p)
    
max_cell = max(cell_list)
print("For "+str(X)+" number of unique barcodes, we can inject "+str(max_cell)+" cells such that more than 95% of the time, more than 95% of the cells end up with unique DNA barcodes.")



