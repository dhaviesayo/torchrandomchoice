def rand_choice(tensor , n):
    i =  torch.randint(len(tensor) , (1,n))
    i = i.tolist()
    choice = []
    i_cache = []
    for count in range (len(i[0])):
        out = tensor[i[count]]
        i_cache.append(i[count])
        if len(i_cache) == 1:
            choice.append(out)
            return choice
        else:
            while i_cache[-1] == i_cache[-2]:
                i =  torch.randint(len(tensor) , (1,n))
                i = i.tolist()
                
            out = tensor[i[count]]
            i_cache.append(i[count])
            choice.append(out)
            return choice
                    
                
    
    
