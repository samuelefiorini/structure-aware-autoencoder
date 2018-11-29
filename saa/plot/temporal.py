import matplotlib.pyplot as plt

def trajectory(df, name):
    traj = (df
            .loc[list(sorted(filter(lambda x: name in x, df.index)))]
            .drop_duplicates()
            .transpose())
    
    plt.figure(dpi=100)
    for i in traj.index:
        plt.plot(range(traj.shape[1]), traj.loc[i], '-o',label=i)
    plt.legend(loc='upper center', bbox_to_anchor=(1.2, 0.8), shadow=True, ncol=1)
    plt.xticks(list(range(traj.shape[1])), list(range(1, traj.shape[1]+1)))
    plt.ylim([0, 1])
    plt.xlabel('Examination')
    plt.ylabel('Disability')
    
    return plt