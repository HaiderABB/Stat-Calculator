import numpy as np

def calculate(list):
      

      if len(list) == 9:
            nlist = np.array(list)
            newList = nlist.reshape(3,3)  
            

            calculations={
                  'mean':[np.mean(newList,axis=0).tolist(),np.mean(newList,axis=1).tolist(),np.mean(newList.flatten()) ],
                  'variance':[np.var(newList,axis=0,ddof=0).tolist(), np.var(newList,axis=1,ddof=0).tolist(), np.var(newList.flatten(),ddof=0)],
                  'standard deviation':[np.std(newList,axis =0,ddof=0 ).tolist(), np.std(newList,axis =1,ddof=0 ).tolist(),np.std(newList.flatten(),ddof=0 )],
                  'max':[np.max(newList,axis=0).tolist(),np.max(newList,axis=1).tolist(),np.max(newList.flatten())],
                  'min':[np.min(newList,axis=0).tolist(), np.min(newList,axis=1).tolist(), np.min(newList.flatten())],
                  'sum':[np.sum(newList,axis=0).tolist(), np.sum(newList,axis=1).tolist(),np.sum(newList.flatten())]
            }
            return calculations
      else:
            raise ValueError("List must contain nine numbers." ) 


# print(calculate([0,1,2,3,4,5,6,7,8]))